library(ggplot2)

toy_model_data = read.table("roc_data/toy_model_roc.tsv", sep="\t",header=TRUE)
tia1_tia_data = read.table("roc_data/small_prob_tia1.tsv", sep="\t",header=TRUE)
tia1_4tia_data = read.table("roc_data/small_prob_4TIA1.tsv", sep="\t",header=TRUE)
tia1_comp_tia_data = read.table("roc_data/comp_prob_tia1.tsv", sep="\t",header=TRUE)
tia1_comp_4tia_data = read.table("roc_data/comp_prob_4tia1.tsv", sep="\t",header=TRUE)
u1_complete_data = read.table("roc_data/u1_complete_roc.tsv", sep="\t",header=TRUE)
u1_2_8_data = read.table("roc_data/u1_2_8_roc.tsv", sep="\t",header=TRUE)
u1_3_7_data = read.table("roc_data/u1_3_7_roc.tsv", sep="\t",header=TRUE)

random_model_data = data.frame(tpr=c(0.0, 1.0), fpr=c(0.0, 1.0))

quartz()

plot = ggplot(toy_model_data, aes(x=fpr, y=tpr))

plot = plot + geom_line(aes(color="Toy model"))

plot = plot + geom_line(data=u1_3_7_data, aes(color="U1 3-7"))
plot = plot + geom_line(data=u1_2_8_data, aes(color="U1 2-8"))
plot = plot + geom_line(data=u1_complete_data, aes(color="U1 complete"))

plot = plot + geom_line(data=tia1_tia_data, aes(color="TIA1 simple - U1 2-8"))
plot = plot + geom_line(data=tia1_4tia_data, aes(color="TIA1 4x - U1 2-8"))
plot = plot + geom_line(data=tia1_comp_tia_data, aes(color="TIA1 simple - U1 complete"))
plot = plot + geom_line(data=tia1_comp_4tia_data, aes(color="TIA1 4x - U1 complete"))

plot = plot + geom_line(data=random_model_data, size=0.75, linetype="dotdash", color="black")

plot = plot + scale_color_manual(name = "HMMs",
                                 values = c(
                                            "Toy model" = "#00FF00",
                                            "U1 3-7" = "#0000FF",
                                            "U1 2-8" = "#00FFFF",
                                            "U1 complete" = "#0099CC",
                                            "TIA1 simple - U1 2-8" = "#FF0000",
                                            "TIA1 4x - U1 2-8" = "#FF9900",
                                            "TIA1 simple - U1 complete" = "#663300",
                                            "TIA1 4x - U1 complete" = "#003366"
                                            )
                                 ) + theme(legend.position="right")
plot = plot + xlab("FPR") + ylab("TPR") + labs(title = "ROC Curve")

print(plot)

quartz()

plot = ggplot(toy_model_data, aes(x=tpr, y=ppv))

plot = plot + geom_line(aes(color="Toy model"))

plot = plot + geom_line(data=u1_3_7_data, aes(color="U1 3-7"))
plot = plot + geom_line(data=u1_2_8_data, aes(color="U1 2-8"))
plot = plot + geom_line(data=u1_complete_data, aes(color="U1 complete"))

plot = plot + geom_line(data=tia1_tia_data, aes(color="TIA1 simple - U1 2-8"))
plot = plot + geom_line(data=tia1_4tia_data, aes(color="TIA1 4x - U1 2-8"))
plot = plot + geom_line(data=tia1_comp_tia_data, aes(color="TIA1 simple - U1 complete"))
plot = plot + geom_line(data=tia1_comp_4tia_data, aes(color="TIA1 4x - U1 complete"))

plot = plot + scale_color_manual(name = "HMMs",
                                 values = c(
                                            "Toy model" = "#00FF00",
                                            "U1 3-7" = "#0000FF",
                                            "U1 2-8" = "#00FFFF",
                                            "U1 complete" = "#0099CC",
                                            "TIA1 simple - U1 2-8" = "#FF0000",
                                            "TIA1 4x - U1 2-8" = "#FF9900",
                                            "TIA1 simple - U1 complete" = "#663300",
                                            "TIA1 4x - U1 complete" = "#003366"
                                            )
                                 ) + theme(legend.position="right")

plot = plot + xlab("TPR") + ylab("Precision") + labs(title = "Precision Curve")

print(plot)

