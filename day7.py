# bubble
arr = [1, 5, 1, 2, 4, 6]

def bubleSort(arr):
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
    return arr

print(bubleSort(arr))

# selection
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
  
print(selection_sort([4,2,5, 12, 21, 54, 65,4]))


# insertion 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        while arr[i - 1] > arr[i] and i > 0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    return arr
 
print(insertion_sort([4, 5, 6, 1, 0, -6, 5, 12]))

# merge
def sort(array1, array2):
    print("Array1: ", array1)
    print("Array2: ", array2)
    print("==================")
    result = []
    i,j = 0,0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i+=1
        else:
            result.append(array2[j])
            j+=1

    while j < len(array2):
        result.append(array2[j])
        j+=1

    while i < len(array1):
        result.append(array1[i])
        i+=1


    return result

  
def devide(data):

    if len(data)<2:
        return data
    else:
        middle = len(data)//2
        array1 = devide(data[0:middle])
        array2 = devide(data[middle:])
        return sort(array1, array2)
      
data = [8,5,2,7,6,4,9,1,3]      
print(devide(data)) 
