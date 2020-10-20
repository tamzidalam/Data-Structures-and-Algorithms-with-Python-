

def binarySearch(array,t):

    high=len(array)

    low=0


    while low<high:


        mid=low+((high-low)//2)


        if array[mid]==t:
            return mid

        if array[mid]<t:
            low=mid+1


        else:
            high = mid - 1


    return -1






if __name__=="__main__" :

    sorted_array=[0,5,13,19,22,41,55,68,72,81,98]

    print(binarySearch(sorted_array,19))