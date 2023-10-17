
def quick(arr):
    def sort(start, end):
        if start >= end:
            return
        
        pivot = arr[start]
        left = start + 1
        right = end

        while left <= right:
            while left <= end and pivot > arr[left]:
                left += 1
            
            while pivot < arr[right]:
                right -= 1
            
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
        arr[start], arr[right] = arr[right], arr[start]

        sort(start, right - 1)
        sort(left, end)

    return sort(0, len(arr) - 1)
