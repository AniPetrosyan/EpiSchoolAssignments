def fizzBuzz(n):

    while n in range(1, 1000):
        if(n % 3 == 0):
            print("Fizz")
        elif(n % 5 == 0):
            print("Buzz")
        if(n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz")
        else:
            print(n)
        n +=1

fizzBuzz(1)