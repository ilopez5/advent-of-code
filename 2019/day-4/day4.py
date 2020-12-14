def hack(start, end):
    ctr = 0
    for num in range(start, end+1):
        a, b, c, d, e, f = grab_digits(num)
        if check_incr(a,b,c,d,e,f) and check_dup(a,b,c,d,e,f):
            ctr += 1
    return ctr

def hack_two(start, end):
    ctr = 0
    for num in range(start, end + 1):
        a, b, c, d, e, f = grab_digits(num)
        if check_dup_alt(a,b,c,d,e,f) and check_incr(a,b,c,d,e,f):
            ctr += 1
    return ctr

def check_dup(a,b,c,d,e,f):
    lst = [a,b,c,d,e,f]
    for i in range(5):
        if lst[i] in lst[i+1:]:
            return True
    return False

def check_dup_alt(a,b,c,d,e,f):
    lst, dups, checked = [a,b,c,d,e,f], [], []
    
    for digit in lst:
        if lst.count(digit) > 1 and digit not in checked:
            dups.append((digit, lst.count(digit)))
        checked.append(digit)                                           # checked should match lst after loop
    
    for tup in dups:
        if tup[1] == 2:
            return True
    return False

def check_incr(a,b,c,d,e,f):
    if a <= b <= c <= d <= e <= f:
        return True
    else:
        return False

def grab_digits(num):
    f = ((num % 10))
    e = ((num % 100) - f) // 10
    d = ((num % 1000) - e) // 100
    c = ((num % 10000) - d) // 1000
    b = ((num % 100000) - c) // 10000
    a = ((num % 1000000) - b) // 100000
    return a,b,c,d,e,f

if __name__ == "__main__":
    print(hack(382345, 843167))
    print(hack_two(382345, 843167))