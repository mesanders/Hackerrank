#!/usr/bin/py
# Head ends here
def lonelyinteger(a):
    answer = 0
    mapping = {}
    for x in a:
        if x not in mapping:
            mapping[x] = 0
        else:
            mapping[x] = 1
    
    for y in mapping:
        if mapping[y] == 0:
            answer = y
        
    return answer

# Tail starts here
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
    