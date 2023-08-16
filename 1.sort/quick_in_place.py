import random


def quick(arr):
    def sort(first, last):
        if first >= last:
            return

        pivot = arr[first]
        left = first + 1
        right = last
        
        while left <= right:
            while left <= last and pivot > arr[first]:
                left += 1
            
            while pivot < arr[right]:
                right -= 1
            
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right += 1
        
        arr[first], arr[right] = arr[right], arr[first]
    
        sort(first, right - 1)
        sort(left, last)

    return sort(0, len(arr))

array = [random.randint(0, 10) for _ in range(20)]
print(array)
print(quick(array))