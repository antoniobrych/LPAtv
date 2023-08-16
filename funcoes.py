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

def generate_random_array(max_range,size):
    return npr.randint(max_range,size=size)
a5_1d = generate_random_array(5,(1,5))
a6_1d = generate_random_array(5,(1,5))

def detect_intersection(arr_a1_1d,arr_a2_1d):
    arr_intersect_1d = np.intersect1d(arr_a1_1d,arr_a2_1d)
    return arr_intersect_1d

def print_array_element(array):
    print(f"Common elements:")
    for i in range(len(array)):
        print("   ",array[i])

def print_intersection(arr_intersect_1d):
    if len(arr_intersect_1d)>0:
        print("Intersection")
        print_array_element(arr_intersect_1d)
        arr_index_intersec1 = np.where(arr_a1_1d in arr_intersect_1d)
        print("Index at Array 1:",end="")
        print_array_element(arr_index_intersec1)
        arr_index_intersec2 = np.where(arr_a2_1d in arr_intersect_1d)
        print("Index at Array 1:",end="")
        print_array_element(arr_index_intersec2)
    else:
        print("No elements at intersection")

#5
def stack_1d_array(arr_a1_1d,arr_a2_1d):
    arr_stacked = np.hstack((arr_a1_1d,arr_a2_1d))
    return arr_stacked
def mode(df):
    df_local = df.flatten()
    df_local = np.sort(df_local)
    unique, counts = np.unique(df_local, return_counts=True)
    most_freq_index = np.where(counts==np.max(counts))
    print(f"Mode is: {unique[most_freq_index][0]}, {np.max(counts)} occurences")

def stats_print(df):
    #print stats from data
    df_local = df.flatten("C")
    print("-*-"*10)
    print("Mean: ",np.average(df_local))
    print("Median: ", np.median(df_local))
    print("Std Dev: ",np.std(df_local))
    print("Max Value: ", np.max(df_local))
    print("Min Value: ", np.min(df_local))
    mode(df)
    print("-*-"*10)

def parity_check(arr_1d):
    arr_1d[]