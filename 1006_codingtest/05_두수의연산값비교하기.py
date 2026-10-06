def solution(a, b):
    a_b = int(str(a) + str(b))

    if a_b >= 2 * a * b:
        return a_b
    else:
        return 2 * a * b
