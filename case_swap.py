def swap_case(s):
    temp = ""
    for i in s:
        if i.isupper():
            temp+=i.lower()
        elif i.islower():
            temp+=i.upper()
        else:
            temp+=i
    return temp


if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2"'
    result = swap_case(s)
    print(result)