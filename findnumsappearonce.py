def find_num_appear_once():
    a = [1, 3, 4, 3, 4, 2]
    
    res = a[0]
    for i in range(1, len(a)):
        res = res ^ a[i]
     
    count = 0
    while(res % 2 != 1):
        res = res >> 1
        count += 1

    n1 = n2 = 0
    for i in range(len(a)):
        if ((a[i] >> count) & 1):
            n1 ^= a[i]
        else:
            n2 ^= a[i]
    print n1 
    print n2
find_num_appear_once()
