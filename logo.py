def find_duplicate_with_index(string='samsung'):
    for x in range(len(string)):
        for y in range(x + 1, len(string)):
            if string[x] == string[y]:
                print(string[x], x, y)
            
    

find_duplicate_with_index()