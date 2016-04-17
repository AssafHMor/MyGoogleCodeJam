

def sort_vectors(vector1, vector2):
    """
    returns vector1 as sorted list and vector2 as reverse sorted lis
    :param vector1: unsorted first list of numbers
    :param vector2: unsorted second list of numbers
    :return: returns the two sorted lists
    """
    vector1.sort()
    vector2.sort(reverse=True)
    return vector1, vector2


def multiply_vectors(n, vector):
    """
    returns the sum of two points in vector
    :param n:
    :param vector:
    :return:
    """
    ans = 0
    for i in range(0, n):
        ans += int(vector[0][i] * vector[1][i])
    return ans


file = open("A-large-practice.in", 'r')
T = int(file.readline())
target = open("output.txt", 'w')
for i in range(0, T):
    n = int(file.readline())
    v1 = file.readline()
    v1 = [int(k) for k in v1.split(' ')]
    v2 = file.readline()
    v2 = [int(k) for k in v2.split(' ')]
    target.write("Case #%d: %d" %(i+1, multiply_vectors(n, sort_vectors(v1, v2))))

file.close()
target.close()
