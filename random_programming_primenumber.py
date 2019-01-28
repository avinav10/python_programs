##prime number---- 2,3,5,7,11 number is divisible by itself

def prime_number(number):

    store=[]

    for i in range(2,number+1):

        isPrime = True

        for num in range(2,i):
            if (i%num)==0:
                isPrime = False

        if isPrime:
            store.append(i)
    return store

print(prime_number(100))


def func(string):
 print(string)

func("hello world")



# def find_prime(number):
#
#     if number==1:
#         return False
#
#     for i in range(2,number):
#         if number%i==0:
#             return False
#     return True
#
#
# for i in range(1,100):
#     print(i,find_prime(i))




