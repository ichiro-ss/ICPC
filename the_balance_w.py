while True:
    data = ""
    while True:
        s = str(input())
        data = data + s
        if data[-1] == '.':
            break

    if data[0] == '.':
        break
    l_small = 0
    l_big = 0
    flag = True
    is_small = []
    for c in data:
        if c == '(':
            l_small += 1
            is_small.append(True)
        if c == '[':
            l_big += 1
            is_small.append(False)
        if c == ')':
            l_small -= 1
            if len(is_small) > 0 and not is_small.pop(-1):
                flag = False
                break
        if c == ']':
            l_big -= 1
            if len(is_small) > 0 and is_small.pop(-1):
                flag = False
                break
        if l_small < 0 or l_big < 0:
            flag = False
            break
    if flag:
        if not l_small and not l_big:
            print("yes")
        else:
            print("no")
    else:
        print("no")


# be careful of to index out of range