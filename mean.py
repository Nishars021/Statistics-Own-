import statistics

data = [10,20,30,40]

#Normal way to find out mean
mean = sum(data)/len(data)
print(mean)

#Using package
mean = statistics.mean(data)
print(mean)