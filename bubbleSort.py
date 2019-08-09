
def bubbleSort(a):



    for i in range(len(a)):

        for j in range(i):

            if(a[i] <=a [j]):

                temp =a[i]

                a[i] = a[j]

                a[j] = temp



    print(a)






if __name__=="__main__" :

    a = [5,21,12,3,4,65,32,9,0]


    bubbleSort(a)

