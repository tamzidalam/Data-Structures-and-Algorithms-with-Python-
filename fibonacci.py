

def fib(a):

    if a == 0 :

        return 0

    if a == 1 :

        return 1

    else :

        return fib(a-1) + fib (a-2)








if __name__=="__main__":


  num=int(input())

  for i in range(num+1):

      fibonacci=fib(i)

      print(fibonacci)








