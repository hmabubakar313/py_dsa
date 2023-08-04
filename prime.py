def prime(num):
    x = [i for i in range(2, num) if num%1 == 0 & num%num == 0]
    print(x)
    

prime(10)