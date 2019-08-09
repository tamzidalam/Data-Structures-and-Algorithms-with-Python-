


def mergeSort(a):

    i=len(a)


    if i==1:
        return

    else:

        mid = len(a) // 2

        l = a[:mid]
        r = a[mid:]

        mergeSort(l)
        mergeSort(r)
        mergeElements(a,l,r)

def mergeElements(a,l,r):


    i=0
    j=0
    k=0

    while i<len(l) and j<len(r):

        if(l[i]<=r[j]):

            a[k]=l[i]

            i=i+1


        else:

            a[k]=r[j]
            j=j+1

        k = k + 1



    while(i<len(l)):

        a[k]=l[i]
        i = i + 1
        k = k + 1

    while (j < len(r)):

        a[k] = r[j]
        j = j + 1
        k = k + 1





if __name__=="__main__" :

    a=[0,5,64,2,9,8]


    mergeSort(a)

    print(a)


