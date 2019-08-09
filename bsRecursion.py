

def binarySearch(a,key,low,high):

    if low > high:

        return False

    else:

        mid=int((low+high)/2)

        if(key == a[mid]):

            return True

        elif (key < a[mid]):

            high=mid-1

            return binarySearch(a,key,low,high)

        elif (key > a[mid]):

            low = mid + 1

            return binarySearch(a, key, low, high)


if __name__=="__main__" :

    a = [4, 65, 100, 250, 322]

    low=0

    high=len(a)-1

    key = input("Enter the number you want to search :\n")

    status = binarySearch(a, int(key),low,high)

    print(status)

