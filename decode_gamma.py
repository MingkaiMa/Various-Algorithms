def decode_gamma(inputs):
    import math
    split_result = []
    result = []
    while(len(inputs) != 0):
        n = 0
        for s in inputs:
            if s == '1':
                n += 1
                continue
            else:
                break
        one_number = inputs[: 2 * n + 1]
        inputs = inputs[2 * n + 1: ]
        split_result.append(one_number)

    for code in split_result:
        if code == '0':
            result.append(1)
            continue
        n = 0
        for s in code:
            if s == '1':
                n += 1
            else:
                break
        code = code[n + 1: ]

        part_1 = math.pow(2, n)
        part_2 = int(code, 2)
        result.append(int(part_1 + part_2))

    return result
