library(ggplot2)

data = read.table("output.csv", sep="\t",header=TRUE)

data$mi_distance = data$mi_distance/max(data$mi_distance)

quartz()

plot = ggplot(data, aes(x=position, group=1))
plot = plot + geom_line(aes(y=mi_distance, color="red"))
plot = plot + geom_line(aes(y=jensen_shannon_distance, color="blue"))
print(plot)
