def get_test_input():
    num_of_inputs = int(input())
    tests = []
    for i in range(num_of_inputs):
        tests.append(input())
    return tests

def get_output(testCase):
    if len(testCase) % 2 != 0:
        return -1
    
    half = len(testCase) // 2
    a, b = testCase[:half], testCase[half:]

    maps = {}
    for i in b:
        if i not in maps:
            maps[i] = 1
        else:
            maps[i] += 1
    for i in a:
        if (i in maps) and (maps[i] > 0):
            half -=  1
            maps[i] -= 1
    
    return half

if __name__ == "__main__":
    for testCase in get_test_input():
        print(get_output(testCase))