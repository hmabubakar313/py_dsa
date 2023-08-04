def fact(num):
    if num < 0:
        print('no fact')
    elif num == 0:
        return 1
    elif num > 0:
        result = 1
        while num > 0:
            result *= num
            num -= 1
        return result


print(fact(5))