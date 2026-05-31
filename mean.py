import statistics

#Normal way to find out mean
data = [10,20,30,40]
mean = sum(data)/len(data)
print(mean)

#Using package
mean = statistics.mean(data)
print(mean)