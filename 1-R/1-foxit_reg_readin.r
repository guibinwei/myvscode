library(tidyverse)
#严重警告：foxit版本号 需要随着 阅读器的版本而改变
version1 <- "9.0"   #需要根据foxit版本修改
version2 <- paste("Foxit Reader", version1)
mkey <- file.path("SOFTWARE", "Foxit Software", version2, "Preferences",
"History", "LastSession", fsep = "\\")
#添加 基础条目 HCU 
a1 <- readRegistry(mkey, "HCU", maxdepth  =  3)
a1[[1]] <- NULL  #删除Active项-活动页面
a2 <- map(a1,3)  #提取 filename项  #list可以，chr-字符串也可以。所以就不简化了
a3 <- str_replace_all(a2, "\\\\", "/")   #轻量输出-不需要超链接
a4 <- str_replace(a3, "(.*)", "[\\1](<file://\\1>)")   #在obsidian中为链接增加 <>
n <- length(a4)
a5 <- paste0("【", 1:n, "】 ", a4)    #在markdown中[]有特殊含义，乃修改为 【】
a5b = paste0(1:n, "-", a3)
stamp = format(Sys.time(), "%Y-%m-%d-%H_%M")
fn0 <- "D:/idm8/foxit_reg_auto"   #filename
fnb <- "D:/idm8/foxit_reg_auto_lite"
fn = paste0(fn0,".txt")
# fn2 = paste0(fn0,"-",stamp,".txt")
fnb2 = paste0(fnb,"-",stamp,".txt")
# 本来添加日期，但是为了便于思源/obsidian 打开txt文件，乃固定文件名称
write.table(a5, fn, row.names  =  FALSE, col.names  = FALSE, quote  =  FALSE)
# write.table(a5, fn2, row.names  =  FALSE, col.names  = FALSE, quote  =  FALSE)
write.table(a5b, fnb2, row.names  =  FALSE, col.names  = FALSE, quote  =  FALSE)
