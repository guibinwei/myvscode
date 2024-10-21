using Agents
#using Random: Xoshiro # access the RNG object
using Statistics: mean
using WAV

t1 = time()


@agent struct SchellingAgent(GridAgent{2}) 
    #mood::Bool # whether the agent is happy in its position
    #group::Int # The group of the agent, determines mood as it interacts with neighbors
    A_self::Int   #伦理
    A_peer::Int   #收益
    #A_mtx::Float64  #压力
    revenue::Float64  #收益
    #revenue_nb_av::Float64  #邻居的平均收益
    #P1::Float64   #第一层概率
    #P2::Float64   #第二层概率
    #Pmix::Float64  #概率相乘
    strate::Int   #1-合作 0-背叛
    overstress::Int  #过度压力
end

function schelling_step_1!(agent, model)
    # Here we access a model-level property `min_to_be_happy`.
    # This will have an assigned value once we create the model.
    A = [1 0; model.temp 0] 
    #以下是针对当前单个代理的指令
    payoff =0
    a=[agent.strate, 1-agent.strate]
    PA=transpose(a) * A
    # For each neighbor, get group and compare to current agent's group
    # and increment `count_neighbors_same_group` as appropriately.
    # Here `nearby_agents` (with default arguments) will provide an iterator
    # over the nearby agents one grid cell away, which are at most 8.
    for neighbor in nearby_agents(agent, model)
        b=[neighbor.strate, 1-neighbor.strate]
        pay0 = PA * b
        payoff += PA * b
    end
    agent.revenue=payoff
    return
end
function schelling_step_2!(agent, model)
    # Here we access a model-level property `min_to_be_happy`.
    # This will have an assigned value once we create the model.
    minbetray = model.min_betray
    alpha = model.alpha
    theta = model.theta
    lamda = model.lamda
    Kmax = model.Kmax
    #以下是针对当前单个代理的指令
    count_betray = 0
    revenue_nb = 0
    # For each neighbor, get group and compare to current agent's group
    # and increment `count_neighbors_same_group` as appropriately.
    # Here `nearby_agents` (with default arguments) will provide an iterator
    # over the nearby agents one grid cell away, which are at most 8.
    for neighbor in nearby_agents(agent, model)
        if neighbor.strate==0
            count_betray += 1
        end
        revenue_nb += neighbor.revenue
    end
    #nearby_number = length(nearby_agents(agent, model))
    nearby_number = 4
    revenue_nb_av=revenue_nb/nearby_number
    bet2= (count_betray>=2)
    pe2=(agent.revenue <= revenue_nb_av)
    #更新压力矩阵A
    agent.A_self += (count_betray>=2)
    agent.A_peer += (agent.revenue <= revenue_nb_av) #计算朋辈压力
    A_mtx = (1-alpha) * agent.A_self + alpha * agent.A_peer #更新压力矩阵A
    #迭代&策略更新
    A_gap=maximum([theta-A_mtx,0])
    P1 = exp(-A_gap)  #计算概率P1
    ragent = random_agent(model)
    K_A = Kmax*A_gap/theta 
    drevenue= agent.revenue -ragent.revenue
    P2 = 1 / (1+ exp(drevenue/K_A))
    isnan(P2) && (P2= 0) #处理NaN值赋0  #0/0先赋值为0，然后赋值为0.5
    Pmix=P1*P2
    if Pmix > rand() 
        agent.strate = ragent.strate
        agent.A_peer = 0 #清空改变策略的Ap
        agent.A_self = 0 #清空改变策略的As
    end
    #Fc(t+1) = sum(sum(Strmtx))/L^2  #在最后提取数据时计算
    agent.overstress = (A_mtx >= (theta+lamda))
    return
end

function complex_model_step!(model)
    # tip: these schedulers should be defined as properties of the model
    for agent in allagents(model)
        schelling_step_1!(agent, model)
        schelling_step_2!(agent, model)
    end
    return
end

function wealth_model_2D(;L=100, betray=2, temp = 1.2, alpha =  0.3, theta = 20, Kmax = 1, lamda = 10)     
    size = (L, L)
    space = GridSpaceSingle(size; periodic = true, metric = :manhattan) #1000个代理
    properties = Dict(:min_betray => betray, :temp => temp,
    :alpha => alpha, :theta => theta, :lamda => lamda, :Kmax => Kmax)
    model = StandardABM(SchellingAgent, space; 
    properties, model_step! = complex_model_step!)  #定义模型，包含 空间 代理 进化规则 属性 调度程序（调度者）

    for n in 1:L^2
        add_agent_single!(model; revenue=0, A_self=0, A_peer=0, strate = rand(0:1), overstress=0)
    end
    return model  
end

schelling = wealth_model_2D()

N = 10^4
#adata = [(:strate, mean), (:overstress, mean)]
adata = [:strate, :revenue, :A_peer, :A_self, :overstress]
#data, _ = run!(schelling, N; adata)
data, _ = run!(schelling, N; adata, when=0.1*N)
#data, _ = ensemblerun!(schelling, N; adata, parallel = true, when=0.1*N)
#data[(end-20):end, :]
t2 = time()
println(round((t2-t1)/60; digits=2))
wavplay("d:/jianguo/myvscode/Julia/data/stage_clear.wav")