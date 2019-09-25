def make_rsa_(n):
    out = [2]
    for i in range(3,n,2):
        if (check(i)):
            out.append(i)
    return out
def check(num):
    if (num%2==0):
        return False
    for i in range(3,int(num**0.5),2):
        if (num%i==0):
            return False
    return True
lib = make_rsa_(500)
# 生成 小於 10000以所有的質數
import random
def RSA(num ):
    print("對",num,"加密\n")
    p  = int(random.choices(lib)[0])
    q = int(random.choices(lib)[0])
    while p==q:
        q = random.choices(lib)
    # 找到兩個大質數 p,q
    r = (p-1)*(q-1)
    e = random.randint(2,r)
    flag = check(r,e)
    while not flag:
        e = random.randint(2,r)
        flag = check(r,e)
    # 找到一個e 跟 r 互質
    # 找到一個d
    # ed - 1 = r的倍數
    for ti in range(1,r):
        if ((e*ti-1)%r ==0):
            d =ti
            break
    N = p*q
    print("公鑰: N=",N,", e =",e)#,"私鑰: N=",N,", d=",d)
    this_ =  num**e
    for i in range(0,(this_+1)):
        if ( (this_- i) %N == 0):
            c = i
            break
    print("加密後文本:",c)
    decrption(N,d,c)
def decrption(N,d,c):
    f = c**d
    print("\n私鑰",d,"慾解密:",c)
    for i in range(0,c**d+1):
        if ((f-i) %N == 0):
            print("解密後文本:",i)
            break
def check(n_1,n_2):
    for i in range(min(n_1,n_2),1,-1):
        if (n_1%i ==0 and n_2%i ==0):
            return False
    return True
for i in range(20):
    RSA(random.randint(10,50))
    print("="*100)
