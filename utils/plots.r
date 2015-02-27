library(ggplot2)

plot_real_false_metric = function (metric_name, metric_text) {
  quartz()

  plot = ggplot(real_data, aes_string(x="positions", y=metric_name, group=1))
  plot = plot + geom_bar(data = false_data, stat = "identity", fill="#FF0000", alpha=0.8)
  plot = plot + geom_bar(fill="#00FF00", stat = "identity", alpha=0.8)

  plot = plot + xlab("Positions") + ylab(metric_text) + theme_bw()

  print(plot)
}

plot_context_metric = function (metric_name, metric_text) {
  quartz()

  plot = ggplot(context_data, aes_string(x="positions", y=metric_name, group=1))
  plot = plot + geom_bar(fill="#00FF00", stat = "identity", alpha=0.8)

  plot = plot + xlab("Positions") + ylab(metric_text) + theme_bw()

  print(plot)
}

real_data = read.table("real_stats.tsv", sep="\t",header=TRUE)
false_data = read.table("false_stats.tsv", sep="\t",header=TRUE)
context_data = read.table("context_stats.tsv", sep="\t",header=TRUE)


plot_real_false_metric("jensen_shannon", "Jensen-Shannon Distance")
plot_real_false_metric("mutual_information_distance", "Mutual information distance")
plot_real_false_metric("mutual_information_ratio", "Mutual information ratio")

plot_context_metric("jensen_shannon", "Jensen-Shannon Distance")
plot_context_metric("mutual_information_distance", "Mutual information distance")
plot_context_metric("mutual_information_ratio", "Mutual information ratio")

