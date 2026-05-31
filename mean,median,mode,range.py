import statistics

data = [10,22,30,44,50]

#Mean
mean = sum(data)/len(data)
print("Mean  : ",mean)

#Median
median = statistics.median(data)
print("Median : ",median)

#Mode
mode = statistics.mode(data)
print("Mode : ",mode)

#Range
range = max(data) - min(data)
print("Range : ",range)