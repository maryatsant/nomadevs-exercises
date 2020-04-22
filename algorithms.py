## find minimun in an array A

A = [4, 10, 40, -5, 100, -43]

def find_minimum(A):
    if len(A) == 0:             
        return None
    minimum = A[0]              
    for i in range(1, len(A)):  
        if A[i] < minimum:      
            minimum = A[i]       
    return minimum

print('Minimum of', A, 'is', find_minimum(A))


## find average in an array

A = [30, 20, 10, 40]

def average(A):
    if len(A) == 0:             
        return None
    sum = 0
    for i in range(0, len(A)):
        sum = sum + A[i]
    average = sum / len(A)
    return average

print('Average of all the elements of the array is', average(A))

## calculate median

def bubblesort(A):
    for i in reversed(range(1, len(A))):
        for j in range(0, i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp    

A = [60, 61, 50, 62]

bubblesort(A)
print('After:', A)

def calcualte_median(A):
    
    if len(A) % 2 == 0:
        return (A[int(len(A) / 2)] + A[int(len(A) / 2 - 1)]) / 2
    else:
        return A[int(len(A) / 2)]

print(calcualte_median(A))

B = [60, 61, 50, 62, 5]
bubblesort(B)
print('After:', B)

print(calcualte_median(B))


## Implement the function is_there_sum(A, target) which return True if there exists two elements
## in A whose sum is exactly target or False otherwise

A = [30, 20, 10, 40]

target = int(input())

def is_there_sum(A, target):
    if len(A) == 0:       
        return None
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if A[j] + A[i] == target:
                return True
            
    return False

print(is_there_sum(A, target))


## function rotate(A, count)  which rotates the  array A  by count  elements


A =[1, 2, 3, 4, 5, 6, 7]
count = int(input())

def rotate(A, count):
    for i in (range(0, count)):
        first = A[0]
    for i in range(0, len(A)-1):
        A[i] = A[i+1]
        A[len(A)-1] = first
print(rotate(A, count))


## symmetrical

def is_symmetrical(A):
    if if len(A) == 0:             
        return None
    for i in range(len(A) / 2):
        if A[i] != A[len(A) -1 -i]:
            return False
        return True

A =[10, 20, 20, 10]
isA = is_symmetrical(A)
print(isA)



