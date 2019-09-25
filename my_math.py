from sympy import *
from sympy.abc import*
def fourier(func): # 
    get = fourier_transform(func,x,k,noconds=True)
    pprint(get)
def normolize_volume_integrate(func):
    if ('N*' in str(func)):
        func = func.replace('N','')
    elif ('n*' in str(func)):
        func = func.replace('n','')
    return 'N = ('+ str(volume_integrate('('+func+')**2')) +')**-0.5'
def matrix_dot_func(func):
    ans = Matrix(eval(func[0]))
    for i  in func[1:]:
        ans *=  Matrix(eval(i))
    pprint(ans)
    return ans
def volume_integrate(func):
    try:
        if ('y' in str(func)):
            dv = '*sin(x)'
            func = func + dv
            pprint(func)
            func = str(integrate(str(func),(y,2*pi,0)))
            pprint(func)
            func = str(integrate(func,(x,pi,0)))
        if ('r' in str(func)):
            dv = '*r**2'
            func = func + dv
            func = str(integrate(str(func),(r,oo,0)))
        pprint((str(func)))
        func = str(func)
        if ('Piecewise' in func):
            a_func = func.split(',')
            func = a_func[0].replace('Piecewise(','')
            func = func +')'
    except Exception as e:
        print(e)
        return '...自己算'
    return str(func)
def integrate_(func,up=None,down = None):
    try:
        x = Symbol('x')
        if ('^' in func):
            func = func.replace('^','**')
        get = integrate(func,(x,up,down))
        init_printing()
        pprint(func)
        pprint(get)
        return str(get)
    except:
        return '無法計算'
def diffff(func,time=1):
    try:
        x = Symbol('x')
        if ('^' in func):
            func = func.replace('^','**')
        get = diff(func,x,time)
        init_printing()
        pprint(func)
        pprint(get)
        return str(get)
    except:
        return '無法計算'
if __name__ =='__main__':
    #fn = 'sin(x)*cos(x)/(x**2)'
    
    #print(diffff(fn))
    #print(normolize_volume_integrate('(cos(x)*cos(2*y))'))
    #fourier(sech(x))
##    matrix_dot_func( [
##                              "[[  1.1333   ,   4],\
##                                [  0.005,   0.9]]",
##                              "[[  0.4375,  9.375 ],\
##                                  [  -0.0775,   0.625]]",
##                      ] )
    integrate_("(i/x - i*c)**-1")











