
#=
print("Hi, Julia!")
rem(10,3)
div(10,3)


for i in 1:3
    for j in 1:3
        print("i=", i, " j=", j, "\n")
    end
end

for i in 1:3, j in 1:3
    print("i=", i, " j=", j, "\n")
end

for i ∈ 1:3, j ∈ 1:3
    print("i=", i, " j=", j, "\n")
end

x=0
for k in 1:100000
    term = (1/k)^2
    x = x + term
    if (abs(term) < 1e-10) break end
end


x=0
iter = 0
term=1
while ( abs(term) > 0.3) && (iter < 100000)
    iter = iter + 1
    print("iter=", iter, "\n")
    term = 1/iter
    x = x + term
end
=#

# prompt to input
println("What's your name? 提示: 先空格+回车 再 回答+回车...")

# Calling rdeadline() function
name = readline()

#println("The name is ", name) 
println("The name is $name, 谢谢") 
#=

print("101")
function sum_zeta(s,nterms)
    x = 0
    for n in 1:nterms
        x = x + (1/n)^s
    end
    return x
end
sum_zeta(2,100000)

print("102")

sum_zeta(s,nterms) = sum(1/n^s for n=1:nterms)
sum_zeta(2,100000)

print("103")

function circle(r)
    area = π * r^2
    circumference = 2π * r
    return area, circumference
end

a, c = circle(1.5)

shape = circle(1)     # returns (7.0685834705770345, 2.356194490192345)
shape[1]                # 7.0685834705770345
shape[2]                # 2.356194490192345
a, c = shape            # destructures the tuple as in the original

=#