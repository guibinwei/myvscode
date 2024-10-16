#=
2024-06-22
借鉴  唐睿代码  中 TangRui_2.mlx
=#

using LinearAlgebra
using Random

function myloop(;L = 100,theta = 10, alpha = 0.3, b = 1.2, K = 1, T = 10^2, H = 10)
    #Random.seed!(0)
    
    M=zeros(L,L,4)

    M[:,:,1] .=1
    M[:,:,3] .= b

    Strmtx = rand(0:1,L,L)

    A_mtx = zeros(L,L) #初始化压力矩阵A  
    A_peer = zeros(L,L)
    A_self = zeros(L,L)

    Fc = zeros(T+1,1)  #合作比例。有两个参数T+1, 1，则为 T+1 * 1 的列向量
    Fc[1] = sum(Strmtx)/L^2
    overstress = zeros(T+1,1)

    str1=zeros(L,L,4)  #自己
    str2=zeros(L,L,4)   #邻居


    for t = 1:T
        #4个邻居的策略
        Strnei= Array{Int64}(undef,L,L,4)
        Strnei[:,:,1]= circshift(Strmtx, 1)
        Strnei[:,:,2]= circshift(Strmtx, -1)  #下面的邻居
        Strnei[:,:,3]= circshift(Strmtx, (0, 1))  #右移一列-左边的邻居
        Strnei[:,:,4]= circshift(Strmtx, (0, -1))  #右边的邻居
        Strneighbor = dropdims(sum(Strnei,dims=3), dims=3)

        str1[:,:,1]=Strmtx
        str1[:,:,2]=Strmtx
        str1[:,:,3] = 1 .- Strmtx
        str1[:,:,4] = 1 .- Strmtx

        str2[:,:,1] = Strneighbor
        str2[:,:,2] = 4 .- Strneighbor
        str2[:,:,3] = Strneighbor
        str2[:,:,4] = 4 .- Strneighbor    

        payoffmtx = dropdims(sum(str1.*M.*str2,dims=3), dims=3)./4
        
        paynei= Array{Float64}(undef,L,L,4)
        paynei[:,:,1]= circshift(payoffmtx, 1)  #行的变动-上下的邻居，首先是下移一行，即上面的邻居
        paynei[:,:,1]= circshift(payoffmtx, -1)  #下面的邻居
        paynei[:,:,1]= circshift(payoffmtx, (0, 1))  #右移一列-左边的邻居
        paynei[:,:,1]= circshift(payoffmtx, (0, -1))  #右边的邻居

        payoff_average = dropdims(sum(paynei,dims=3), dims=3)
      
        A_peer += (payoffmtx .< payoff_average)

        A_mtx = (1-alpha).*A_self + alpha.*A_peer
        Agap = max.(theta .- A_mtx, zeros(L))
        P1=exp.(-Agap)
        payoffsample = zeros(L,L,4)
        Strsample = zeros(L,L,4)   #注意此处本来有off，但是下面4个层都没有off，乃取消

        randmtx = rand(1:4,L,L)   #每个个体选择那个邻居
        payoffsampleselct =zeros(L,L)
        Strsampleselct =zeros(L,L)
        for i =1:L
            for j = 1:L
                payoffsampleselct[i,j] = paynei[i,j,randmtx[i,j]]
                Strsampleselct[i,j] = Strnei[i,j,randmtx[i,j]]
            end
        end
        K_A = Agap * K./theta
        P2 = 1 ./ (1 .+ exp.((payoffmtx .-payoffsampleselct)./K_A))
        P2[isnan.(P2)] .= 0.5

        P1P2selectmtx = (P1.*P2 .> rand(L,L))

        Strmtx[P1P2selectmtx.==1] .= Strsampleselct[P1P2selectmtx.==1]

        A_peer[P1P2selectmtx.==1] .= 0
        A_self[P1P2selectmtx.==1] .= 0
        Fc[t+1] =sum(Strmtx)/L^2
        overstress[t+1]= sum(A_mtx .>= (theta+H)) /L^2
    end
    return Fc, overstress
end

t1=time_ns()
Fcor, overst = myloop(T = 10^5)
t2=time_ns()

println("Time is ", (t2-t1)/10^9)
