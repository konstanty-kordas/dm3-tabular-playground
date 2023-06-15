require("fitdistrplus")
set.seed(10)
n <- 25
size <- 1000
prob <- .5
y_rnbinom <- rnbinom(100000, size = 100, prob = 0.5)          # Draw N nbinomially distributed values
plot(y_dnbinom)                                          # Plot dnbinom values
df <- read.csv("./data.csv")
data <- df$f_07
plot(table(data))
