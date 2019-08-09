

def binarySearch(a,key):

    low=0


    high=len(a)-1

    mid=0

    i=0

    while low<=high :

        mid = int((low + high) / 2)


        if(key == a[mid]):

            return True

        elif(key < a[mid]):

            high=mid-1

        else:

            low=mid+1

    return False







if __name__=="__main__" :

    a=[4,65,100,250,322]

    key=input("Enter the number you want to search :\n")


    status=binarySearch(a,int(key))

    print(status)


