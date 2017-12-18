'''
@author J.D. Mazz
This program calculates a checksum using XOR
'''
def checksum(start, length):
    count = length
    skips = 0
    pos = start
    checksum = 0
    while count > 0:
        pos += skips
        checksum ^= xor_range(pos,pos+count-1)
        pos += count-1
        skips += 1
        count -= 1
    return checksum

def get_pattern(e):
    # O(1)
    table = [e, 1, e+1, 0]
    return table[e % 4]

def xor_range(start, end):
    # O(1)
    return get_pattern(end) ^ get_pattern(start-1)

def test():
    print(checksum(0, 3)) # 2
    print(checksum(17, 4)) # should be 14
    print(checksum(0, 10000))
