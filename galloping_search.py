def gallop_to(a, val):

    before_dic = {}
    length = len(a.get_list())
    count = 0



    bound = a.cur
    while True:
        current_value = a.peek(bound)
        count += 1
        if current_value == None:
            break
        if current_value <= val:
            temp = (bound + 1) * 2 - 1
            before_dic[temp] = bound
            bound = temp
            a.next(temp)

        else:
            break

    res_key = binary_search(a, val, before_dic[bound], min(bound, length - 1))

    a.cur = res_key
    return count

def binary_search(lst, k, lower, upper):
    low = lower
    height = upper


    while low <= height:
        mid = (low + height) // 2
        if lst.peek(mid) < k:

            low = mid + 1
        elif lst.peek(mid) > k:
            height = mid - 1
        else:

            return mid

    return low
