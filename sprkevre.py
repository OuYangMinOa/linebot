def find_value(x,y):
    half = max(abs(x),abs(y))
    n = 1+2*half
    t = (n)**2-1
    if ((x,y) == (half,-1*half)):
        return t
    if (half == x or half==abs(x)):
        if (x>0):
            return t - (n-1)**2 + 1 - 1 + half + y
        else:
            return t - n + 2 - half + y 
    else:
        if (y>0):
            return t - (n-1)**2 + 1+ 3*half -1 + x
        else:
            return t  - half + x
        
while 1:
    x,y = eval(input("x:")),eval(input('y:'))
    print(find_value(x,y))
