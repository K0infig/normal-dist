import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

 
dice_result = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)


mean = sum(dice_result)/len(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

std_deviation = statistics.stdev(dice_result)
print("The mean value is : " + str(mean))
print("The meadian value is : " + str(median))
print("The mode value is : " + str(mode))
print("The standard deviation is : " +str(std_deviation))

first_standard_dev_start, first_standard_dev_end = mean-std_deviation, mean+std_deviation
second_standard_dev_start, second_standard_dev_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_standard_dev_start, third_standard_dev_end = mean-(3*std_deviation), mean+(3*std_deviation)


listOfFirstDev = [result for result in dice_result if result> first_standard_dev_start and result<first_standard_dev_end]
listOfSecondDev = [result for result in dice_result if result> second_standard_dev_start and result<second_standard_dev_end]
listOfThirdDev = [result for result in dice_result if result> third_standard_dev_start and result<third_standard_dev_end]

print(len(listOfFirstDev)*100/len(dice_result))
print(len(listOfSecondDev)*100/len(dice_result))
print(len(listOfThirdDev)*100/len(dice_result))
fig = ff.create_distplot([dice_result], ["Result"], show_hist =False)
fig.add_trace(go.Scatter(x=[mean, mean], y =[0,0.17], mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[first_standard_dev_start,first_standard_dev_start], y =[0,0.17], mode="lines", name="1st standard deviation start"))
fig.add_trace(go.Scatter(x=[first_standard_dev_end,first_standard_dev_end], y =[0,0.17], mode="lines", name="1st standard deviation end"))

fig.add_trace(go.Scatter(x=[second_standard_dev_start,second_standard_dev_start], y =[0,0.17], mode="lines", name="2nd standard deviation start"))
fig.add_trace(go.Scatter(x=[second_standard_dev_end,second_standard_dev_end], y =[0,0.17], mode="lines", name="2nd standard deviation end"))

fig.add_trace(go.Scatter(x=[third_standard_dev_start,third_standard_dev_start], y =[0,0.17], mode="lines", name="3rd standard deviation start"))
fig.add_trace(go.Scatter(x=[third_standard_dev_end,third_standard_dev_end], y =[0,0.17], mode="lines", name="3rd standard deviation end"))
fig.show()
