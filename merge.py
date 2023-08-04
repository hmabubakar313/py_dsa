def merge_the_tools(string, k):
    # print(string, k)
    for i in range(0, len(string), k):
        # print(i)
        s = string[i:i+k]
        print(''.join(sorted(set(s))), end='\n')

    

if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)