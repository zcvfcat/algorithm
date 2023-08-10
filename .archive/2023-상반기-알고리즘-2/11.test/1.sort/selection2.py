def selection(array):
    for i in range(len(array)):
        select = i

        for j in range(len(array)):
            if array[select] > select[j]:
                select = j
        
        array[i], array[select] = array[select], array[i]
    
