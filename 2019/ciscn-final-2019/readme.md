## fix规则

防御失败：可能由于防御包过大或非正常防御包，无法解压等原因，不会扣分。 
文件解压超时：可能是防御包非标准tar.gz格式或者文件过多，过大等原因，不会扣分。 
CHECK检测失败：服务未能在规定时间内返回正常信息导致检测失败，不会扣分。 
EXP利用成功：执行防御包中的update.sh后防御失败，漏洞未修补，不会扣分。 
服务异常：执行防御包中的update.sh后导致服务不可用，会进行扣分，直到再次检测后服务正常。 防御成功：恭喜你。。