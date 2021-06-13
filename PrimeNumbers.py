def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:                
                print(i,"times",num//i,"is",num)
                return False
                break

        else:
            return True
       
    else:
        return False

print(is_prime(12))