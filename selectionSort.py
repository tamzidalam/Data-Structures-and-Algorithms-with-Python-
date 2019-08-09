


def selectionSort(a):

    position = len(a)-1

    index = 0

    while position != 0 :

        index=0

        while index != position:

            if(a[index] > a[position]) :

                temp = a[index]

                a[index] = a[position]

                a[position]= temp

            index = index+1

        position = position - 1

    print(a)






if __name__=="__main__" :

    a = [5,21,12,3,4,65,32,9,0]


    selectionSort(a)






