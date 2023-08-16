import numpy as np
import numpy.random as npr
#1
def gerar_array1_1D():
    a1 = np.arange(0,10)
    a2 = np.arange(0,10)
    a3 = a1 + a2
    return a3
a3 = gerar_array1_1D()

#2
def gerar_array2_2D(a3):
    a3_2D = a3.reshape(2,5)
    a3_2D = a3_2D.astype(float)
    a3_2D = a3_2D.transpose()
    return a3_2D
a3_2D = gerar_array2_2D(a3)

#3
def gerar_array3_2D(a3_2D):
    a4_2D = npr.randint(10, size=(2,5))
    a4_2D = a4_2D@a3_2D
    return a4_2D
a4_2D = gerar_array3_2D(a3_2D)

#4