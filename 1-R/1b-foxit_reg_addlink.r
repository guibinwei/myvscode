library(tidyverse)
#对原来没有超链接的foxit记录，重新读入，添加记录

fn <- "D:/idm8/foxit_reg_auto.txt-old.txt"   #filename   #读入之前没有添加超链接的foxit记录
# 本来添加日期，但是为了便于思源打开txt文件，乃固定文件名称
a1 <- read.table(file = fn, sep = "\t")
a2 <- unlist(a1)
a3 <- unname(a2)
a3b <- str_replace(a3, "\\[.*\\] ", "")   #去掉前面的方括号序号
a4 <- str_replace(a3, "(.*)", "[\\1](file://\\1)")  #添加超链接
n <- length(a4)
a5 <- paste0("[", 1:n, "] ", a4)   #重新添加序号
fn <- "D:/idm8/foxit_reg_auto.txt"   #filename
# 本来添加日期，但是为了便于思源打开txt文件，乃固定文件名称
write.table(a5, fn, row.names  =  FALSE, col.names  = FALSE, quote  =  FALSE)