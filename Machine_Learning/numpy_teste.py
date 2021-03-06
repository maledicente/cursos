import numpy as np

data = [15, 16, 18, 19, 22, 24, 29, 30, 34]

print("\nmean:", np.mean(data))
print("median:", np.median(data))
print("50th percentile (median):", np.percentile(data, 50))
print("25th percentile:", np.percentile(data, 25))
print("75th percentile:", np.percentile(data, 75))
print("standard deviation: {:.2f}".format(np.std(data)))
print("variance: {:.2f}".format(np.var(data)))
