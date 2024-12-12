'''
"appddddz", 可以消除多少个pdd？ 首先变成"apddz" 然后是 "az"。 给出最优算法
"adddpddz" -> "adddz"
"ppdddd" -> "pdd" -> ""
'''

def str_elimination(s):
    stack = []
    count_d=0 #count of successive d. if count_d==2, then we can remove the last 3 elements from stack
    for c in s:
        stack.append(c)
        if c == 'd':
            count_d+=1
            if count_d==2: #remove the last 3 elements from stack
                count_d=0 #reset count_d regardless of whether we remove the last 3 elements or not
                while len(stack)>=3 and stack[-1] == 'd' and stack[-2] == 'd' and stack[-3] == 'p':
                    stack.pop()
                    stack.pop()
                    stack.pop()
        else:
            count_d=0 #reset count_d if c is not 'd'
    return ''.join(stack)

print("appddddz ->",str_elimination("appddddz"))  # az
print("adddpddz ->",str_elimination("adddpddz"))  # adddz
print("ppdddd ->",str_elimination("ppdddd"))  # ""