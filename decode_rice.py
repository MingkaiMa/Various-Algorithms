def decode_rice(inputs, b):
    import math
    result = []
    split_result = []
    while(len(inputs) != 0):
        n = 0
        for s in inputs:
            if s == '1':
                n += 1
                continue
            else:
                break
        one_number = inputs[: n + int(math.log(b, 2)) + 1]
        split_result.append(one_number)
        inputs = inputs[n + int(math.log(b, 2)) + 1: ]

    for code in split_result:
        n = 0
        for s in code:
            if s == '1':
                n += 1
                continue
            else:
                break
        r = int(code[n + 1: ], 2)
        result.append(int(n * b + r))

    return result
