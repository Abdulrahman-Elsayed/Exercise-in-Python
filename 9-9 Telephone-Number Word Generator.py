def m(n):
    w = ''
    l = list()
    dict = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'], 5: ['J', 'K', 'L'],
           6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}
    def s(n, w, l):
        if len(str(n)) == 1:
            for i in range(len(dict[n])):
                l.append(w + dict[n][i])
        else: 
            str_n = str(n)
            dict_key = int(str_n[0])
            str_n = str_n[1:]
            n = int(str_n)
            for i in range(len(dict[dict_key])):
                w_next = w + dict[dict_key][i]
                s(n, w_next, l)            
    s(n, w, l)
    return l

print(m(782))
