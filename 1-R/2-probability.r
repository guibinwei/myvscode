b=1000
k <- seq(0, b, by = 10)
y = rep(1,b/10 + 1)

#n=100
#k0 <- seq(0, n, by = 10)
#y0=dbinom(k0, n, 0.5)

plot(k, y,type = "l")
#lines(k0, y0,type = "l")