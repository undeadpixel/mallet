library(ggplot2)

toy_model_data = read.table("roc_data/toy_model_roc.tsv", sep="\t",header=TRUE)
tia1_postint_data = read.table("roc_data/tia1_postint_u1_comp_4tia1_roc.tsv", sep="\t",header=TRUE)
tia1_intron_data = read.table("roc_data/small_prob_4TIA1.tsv", sep="\t",header=TRUE)
tia1_complete_data = read.table("roc_data/u1_comp_4tia1.tsv", sep="\t",header=TRUE)
u1_complete_data = read.table("roc_data/u1_complete_roc.tsv", sep="\t",header=TRUE)
u1_2_8_data = read.table("roc_data/u1_2_8_roc.tsv", sep="\t",header=TRUE)
u1_3_7_data = read.table("roc_data/u1_3_7_roc.tsv", sep="\t",header=TRUE)

quartz()

plot = ggplot(toy_model_data, aes(x=fpr, y=tpr))
plot = plot + geom_line(aes(color="Toy model"))
plot = plot + geom_line(data=u1_3_7_data, aes(color="U1 3-7"))
plot = plot + geom_line(data=u1_2_8_data, aes(color="U1 2-8"))
plot = plot + geom_line(data=u1_complete_data, aes(color="U1 complete"))
plot = plot + geom_line(data=tia1_intron_data, aes(color="TIA1 simple"))
plot = plot + geom_line(data=tia1_postint_data, aes(color="TIA1 with post-int"))
plot = plot + geom_line(data=tia1_complete_data, aes(color="U1 complete & TIA1"))

plot = plot + scale_color_manual(name = "HMMs",
                                 values = c(
                                            "Toy model" = "#00FF00",
                                            "U1 3-7" = "#0000FF",
                                            "U1 2-8" = "#00FFFF",
                                            "U1 complete" = "#0099CC",
                                            "TIA1 simple" = "#FF0000",
                                            "TIA1 with post-int" = "#FF9900",
                                            "U1 complete & TIA1" = "#663300"
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
plot = plot + geom_line(data=tia1_intron_data, aes(color="TIA1 simple"))
plot = plot + geom_line(data=tia1_postint_data, aes(color="TIA1 with post-int"))
plot = plot + geom_line(data=tia1_complete_data, aes(color="U1 complete & TIA1"))

plot = plot + scale_color_manual(name = "HMMs",
                                 values = c(
                                            "Toy model" = "#00FF00",
                                            "U1 3-7" = "#0000FF",
                                            "U1 2-8" = "#00FFFF",
                                            "U1 complete" = "#0099CC",
                                            "TIA1 simple" = "#FF0000",
                                            "TIA1 with post-int" = "#FF9900",
                                            "U1 complete & TIA1" = "#663300"
                                            )
                                 ) + theme(legend.position="right")
plot = plot + xlab("TPR") + ylab("Precision") + labs(title = "Precision Curve")

print(plot)

