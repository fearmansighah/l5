from processData import processInput
import numpy as np
import time

A = np.array([[1, 1], [2, 2]])
b = np.array([1, 1])

# pub input example
pubInputSample1 = 'A 1 2 2'
pubInputSample2 = 'A 2 4 4'
pubInputSample3 = 'b 1 2 2'
pubInputSamples = [pubInputSample1, pubInputSample2, pubInputSample3]

i = 1
# # perform local test
for sample in pubInputSamples:
    print(f'case {i}: ')
    xString = processInput(sample)
    print('xString: ', xString)
    print('-----------')
    i += 1

with open('readings.txt', 'r') as file:
    line = file.readline()
    while line:
        # do something with line
        print(line.strip())
        time.sleep(2)
        line = file.readline()
