import numpy as np

# pub input example
# pubInputSample1 = 'A 1 2 2'
# pubInputSample2 = 'A 2 4 4'
# pubInputSample3 = 'b 1 2 2'
# pubInputSamples = [pubInputSample1, pubInputSample2, pubInputSample3]

# create defailts
A = np.array([[1, 1], [2, 2]])
b = np.array([1, 1])


def string2array(pubInputString):
    sel_matrix = pubInputString[0]  # select matrix to manipulate
    row = int(pubInputString[2])
    element1 = int(pubInputString[4])
    element2 = int(pubInputString[6])
    print(sel_matrix, row, element1, element2)

    return sel_matrix, row, element1, element2


def solver(sel_matrix, row, element1, element2):
    global A, b

    # manipulate matrices
    if sel_matrix == 'A':
        A[row-1, :] = np.array([element1, element2])
    elif sel_matrix == 'b':
        b = np.array([element1, element2])

    print('A: ', A)
    print('b: ', b)

    x = np.matmul(A, b.T)

    return x


def returntoPub(x):
    xString = f'x {x[0]} {x[1]}'
    return xString


def processInput(sample):
    sel_matrix, row, element1, element2 = string2array(sample)
    x = solver(sel_matrix, row, element1, element2)
    xString = returntoPub(x)
    return xString


# i = 1
# # perform local test
# for sample in pubInputSamples:
#     print(f'case {i}: ')
#     sel_matrix, row, element1, element2 = string2array(sample)
#     x = solver(sel_matrix, row, element1, element2)
#     xString = returntoPub(x)
#     print('x: ', x)
#     print('xString: ', xString)
#     print('-----------')
#     i += 1
