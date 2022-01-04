import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd 

df = pd.read_csv("data.csv")
readingScore=df["reading score"].to_list()

mean= st.mean(readingScore)
median= st.median(readingScore)
mode= st.mode(readingScore)
std= st.stdev(readingScore)

first_stdev_start, first_stdev_end = mean-std, mean+std
second_stdev_start, second_stdev_end = mean-(2*std), mean+(2*std)
third_stdev_start, third_stdev_end = mean-(3*std), mean+(3*std)

print("mean of the data is- ",mean, "; median of the data is- ",median,"; mode of the data is- ",mode, "; standard deviation of the data is- ",std)


data_1stdev = [result for result in readingScore if result > first_stdev_start and result < first_stdev_end]
data_2stdev = [result for result in readingScore if result > second_stdev_start and result < second_stdev_end]
data_3stdev = [result for result in readingScore if result > third_stdev_start and result < third_stdev_end]

print(len(data_1stdev)*100/len(readingScore), "% of data lies within first standard deviation")
print(len(data_2stdev)*100/len(readingScore), "% of data lies within second standard deviation")
print(len(data_3stdev)*100/len(readingScore), "% of data lies within third standard deviation")

fig= ff.create_distplot([readingScore],["reading score"], show_hist= False)

fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.21], mode = "lines", name="MEAN"))
fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.21], mode = "lines", name="stdev1 start"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.21], mode = "lines", name="stdev1 end"))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.21], mode = "lines", name="stdev2 start"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.21], mode = "lines", name="stdev2 end"))
fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0, 0.21], mode = "lines", name="stdev3 start"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.21], mode = "lines", name="stdev3 end"))


fig.show()

