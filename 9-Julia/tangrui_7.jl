#=
2024-06-22
借鉴  唐睿代码  中 TangRui_2.mlx
=#

using LinearAlgebra
using StaticArrays
using Random

function myloop(;L = 100,theta = 10, alpha = 0.3, b = 1.2, K = 1, T = 10^3, H = 10)
    #Random.seed!(0)
    
    M=@SMatrix [1 0; b  0]

    strmtx = rand(0:1,L,L)
    paymtx = zeros(L,L)
    strselct = zeros(L,L)
    payselct =zeros(L,L)

    A_mtx =  zeros(L,L) #初始化压力矩阵A  
    A_self =  zeros(L,L)  #内心-伦理
    A_peer =  zeros(L,L)   #经济利润

    Fc = zeros(T+1)  #合作比例。有两个参数T+1, 1，则为 T+1 * 1 的列向量
    overstress = zeros(T+1)
    Fc[1] = sum(strmtx)/L^2

    for t = 1:T
        #4个邻居的策略
        strneigh = circshift(strmtx, 1) + circshift(strmtx, -1) + circshift(strmtx, (0, 1)) + circshift(strmtx, (0, -1))
        A_self +=  (strneigh .< 2.5)

        for i = 1:L
            for j = 1:L
                paymtx[i,j] =(@views [strmtx[i,j] 1-strmtx[i,j]] * M * [strneigh[i,j]; 4-strneigh[i,j]])[1]
            end
        end

          
        payave = (circshift(paymtx, 1)+circshift(paymtx, -1)+circshift(paymtx, (0, 1))+circshift(paymtx, (0, -1)))./4
       
        A_peer += (paymtx .< payave)

        A_mtx = (1-alpha).*A_self + alpha.*A_peer
        Agap = max.(theta .- A_mtx, 0)
        P1=exp.(-Agap)
 
        #randmtx = @SMatrix rand(1:4,L,L)   #每个个体选择一个邻居
        x = ((1,0), (-1,0), (0,1), (0,-1))

        for i =1:L
            for j = 1:L
                nei=rand(1:4,1)[1]
                i0=mod(i+x[nei][1]-1, L) +1
                j0=mod(j+x[nei][2]-1, L) +1
                strselct[i,j] = @views strmtx[i0, j0]
                payselct[i,j] = @views paymtx[i0, j0]
            end
        end
        K_A = Agap * K./theta
        P2 = 1 ./ (1 .+ exp.((paymtx .-payselct)./K_A))
        P2[isnan.(P2)] .= 0.5

        P1P2selectmtx = (P1.*P2 .> rand(L,L))

        strmtx[P1P2selectmtx.==1] .= strselct[P1P2selectmtx.==1]

        A_peer[P1P2selectmtx.==1] .= 0
        A_self[P1P2selectmtx.==1] .= 0
        Fc[t+1] =sum(strmtx)/L^2
        overstress[t+1]= sum(A_mtx .>= (theta+H)) /L^2
    end
    return Fc, overstress
end

t1=time_ns()
Fcor, overst = myloop(T = 10^2)
t2=time_ns()

println("Time is ", (t2-t1)/10^9)
