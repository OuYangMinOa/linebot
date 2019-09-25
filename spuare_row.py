global arrays,used,m,ans,temp
def square_sums_row(N):
    global arrays,used,m,ans,temp
    used = []
    ans = []
    arrays = [x+1 for x in range(N)][::-1]
    m = len(arrays)
    temp = 0
    for i in range(m):
        used =[i]
        ans = [arrays[i]]
        dfs(i)
        if (temp):
            break
    if (not temp):
        return False
    else:
        return ans
def dfs(last):
    global arrays,used,m,ans,temp
    if (len(ans) == m):
        temp = 1
        return
    this = arrays[last]
    for i in range(m):
        jj = arrays[i]
        if (i in used):
            continue
        elif ( test(this+ jj) ):
            used.append(i)
            ans.append(jj)
            dfs(i)
            if (temp ==0):
                used.remove(i)
                ans.remove(jj)
def test(x):
    if (x**0.5 == int(x**0.5)):
        return True
    return False
if __name__=="__main__":
    print(square_sums_row(16))
