def Logarithmic_merge(index, cut_off, buffer_size): 

    L = [[] for _ in range(cut_off)]
    cur = 0
    index = index[: cut_off]
    while index:
        z0 = []
        
        for i in range(cur, len(index)):

            z0.append(index[i])
            if(len(z0) == buffer_size):
                break
        cur = i + 1
            
                
    
        if(len(z0) == buffer_size):
            min_ = cut_off
            for i in reversed(range(cut_off)):
                if(len(L[i]) == 0):
                    if i < min_:
                        min_ = i
                        
            for i in range(0, min_):
                L[min_] += L[i]
                L[i] = []
                
            L[min_] += z0
        else:
            S = [z0] + L
            m = 0
            for i in reversed(range(len(S))):
                if len(S[i]) != 0:
                    m = i
                    break

            S = S[ :m + 1]
            R = []
            for s in S:
                s = sorted(s)
                R.append(s)
            return R
            break
