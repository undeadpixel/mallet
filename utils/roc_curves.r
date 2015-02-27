library(ggplot2)

toy_model_data = read.table("roc_data/toy_model_roc.tsv", sep="\t",header=TRUE)
tia1_postint_data = read.table("roc_data/tia1_postint_u1_comp_4tia1_roc.tsv", sep="\t",header=TRUE)
u1_complete_data = read.table("roc_data/u1_complete_roc.tsv", sep="\t",header=TRUE)
u1_2_8_data = read.table("roc_data/u1_2_8_roc.tsv", sep="\t",header=TRUE)
u1_3_7_data = read.table("roc_data/u1_3_7_roc.tsv", sep="\t",header=TRUE)

quartz()

plot = ggplot(toy_model_data, aes(x=fpr, y=tpr))
plot = plot + geom_line(color="red")
plot = plot + geom_line(data=tia1_postint_data, color="blue")
plot = plot + geom_line(data=u1_complete_data, color="green")
plot = plot + geom_line(data=u1_2_8_data, color="orange")
plot = plot + geom_line(data=u1_3_7_data, color="yellow")

print(plot)

quartz()

plot = ggplot(toy_model_data, aes(x=tpr, y=ppv))
plot = plot + geom_line(color="red")
plot = plot + geom_line(data=tia1_postint_data, color="blue")
plot = plot + geom_line(data=u1_complete_data, color="green")
plot = plot + geom_line(data=u1_2_8_data, color="orange")
plot = plot + geom_line(data=u1_3_7_data, color="yellow")

print(plot)
