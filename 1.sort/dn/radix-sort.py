def radixSort(array):
    
    # 배열의 최대값을 찾는다.
    maximum = max(array)

    #자리수별로 counting sort 실행
    exp = 1
    while maximum / exp > 0:
        countingSort(array, exp)
        exp *= 10

# Counting Sort 구현        
def countingSort(array, exp):
    n = len(array)    
    output = [0] * n       
    count = [0] * 10
         
    for i in range(0, n):        
        index = int(array[i] / exp)
        count[index % 10] += 1
 
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    i = n - 1
    while i >= 0:
        index = int(array[i] / exp)
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
        
    i = 0
    for i in range(0, len(array)):
        array[i] = output[i]