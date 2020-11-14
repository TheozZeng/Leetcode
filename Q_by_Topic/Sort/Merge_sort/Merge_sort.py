def merge_2_list(L,R):
    i = j = k = 0
    arr = [None]*(len(L)+len(R))
    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    return arr

def merge_sort(arr):
    if(len(arr) == 0):
        return []
    elif(len(arr) == 1):
        return arr
    else:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        print(L,"|",R)
        L = merge_sort(L)
        R = merge_sort(R)
        return merge_2_list(L,R)

arr = [2,3,7,4,9,10]
print(merge_sort(arr))
