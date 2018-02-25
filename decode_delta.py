def decode_delta(inputs):
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
        if(n == 0):
            split_result.append('0')
            inputs = inputs[1: ]
            continue
        k_dd = n
        k_dr = int(inputs[n + 1 : n + n + 1], 2)
        k_d = k_dr - 1 + math.pow(2, k_dd)
        one_number = inputs[: 2 * n + int(k_d) + 1]
        inputs = inputs[2 * n + 1 + int(k_d): ]
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
        k_dd = n
        k_dr = int(code[n + 1 : n + n + 1], 2)
        k_r = int(code[2 * n + 1 :], 2)
        k_d = k_dr - 1 + math.pow(2, k_dd)
        part_1 = math.pow(2, k_d)
        part_2 = k_r
        result.append(int(part_1 + part_2))

    return result
