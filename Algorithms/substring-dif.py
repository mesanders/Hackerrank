import sys

def longest_range_min_sum(P, Q, posP, posQ, slice_size, max_sum):
    longest = 0
    i = 0
    running_sum = 0
    while i + longest < slice_size:
        if P[posP + i + longest] != Q[posQ + i + longest]:
            running_sum += 1
        if running_sum > max_sum:
            if P[posP + i] != Q[posQ + i]:
                running_sum -= 1
            i += 1
        else:
            longest += 1
    return longest

def compare_miss_matches(data):
    max_mismatches, P,Q = data.pop(0).split()
    max_mismatches = int(max_mismatches)
    m = n = len(P)
    longest = 0
    for i in xrange(m + n + 1):
        if i > n:
            slice_size = m - (i - n)
        else:
            slice_size = min(i, m)
        if slice_size == 0:
            continue
        end1 = max(m, m - i)
        
        if i > n:
            end1 = m - (i - n)
            
        posP = end1 - slice_size
        end2 = min(i, n)
        posQ = end2 - slice_size
        longest_in_sub = longest_range_min_sum(P, Q, posP, posQ, slice_size, max_mismatches)
        longest = max(longest, longest_in_sub)
    return longest

if __name__ == "__main__":
    data = sys.stdin.readlines()
    num_cases = int(data.pop(0))
    for ignore in xrange(num_cases):
        print compare_miss_matches(data)
