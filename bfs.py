import sys
global path,temp
def pour(A,B,a,b):
  left = b-B
  if (left > A):
    return 0,B+A
  else:
    return A-left,b
def chech(a,b,ans):
  if (ans >b and ans > a):
    return False
  small = 0
  for i in range(1,min(a,b)+1):
    if (a%i ==0 and b%i ==0):
      small = i
  if (ans % small==0):
    return True
  else:
    return False
def bfs(a,b,ans):
  global path,temp,ans_for_all
  this = []
  this_path = []
  if (len(str(path)) > 2**28):
    return False
  for i in path[-1]:
    A,B = i[0],i[1]
    #fill A b
    if (A!= a):
      this.append([a,B])
      this_path.append(i)
    if (B!= b):
      this.append([A,b])
      this_path.append(i)
    #empty A B
    if (A!= 0):
      this.append([0,B])
      this_path.append(i)
    if (B!= 0):
      this.append([A,0])
      this_path.append(i)
    #pour
    if (B!=b and A!=0):
      t,r = pour(A,B,a,b)
      this_path.append(i)
      this.append([t,r])
    if(A!=a and B!=0):
      t,r = pour(B,A,b,a)
      this_path.append(i)
      this.append([r,t])
  path.append(this)
  for i in this:
      if (ans in i):
        ans_for_all.append(i)
        temp =1
        return this_path[this.index(i)]
  get = bfs(a,b,ans)
  if not get:
    return False
  ans_for_all.append(get)
  return this_path[this.index(get)]
def start(out):
  global path,temp,ans_for_all
  path =[]
  ans_for_all=[]
  temp = 0
  if (chech(out[0],out[1],out[2]) ):
    if (out[1] != out[2] and out[0]!=out[2]):
      path.append( [[0,out[1]],[out[0],0]] )
      get = bfs(out[0],out[1],out[2])
      if not get:
        print("超出記憶體")
        return False,'N'
      ans_for_all.append(get)
    else:
      print('1')
    path = []
    print("次數  ",out[0],out[1])
    out_ans = "次數   {} {}".format(out[0],out[1])
    for i,j in enumerate(ans_for_all[::-1]):
      print("第{:2.0f}次".format(i),j[0],j[1])
      out_ans = out_ans + "\n第{:2.0f}次 {} {}".format(i,j[0],j[1])
    return True,out_ans
  else:
    print("沒有辦法")
    return False,[]
if __name__ =="__main__":
  while 1:
    get =input().split(' ')
    out=[]
    for i in get:
      out.append(eval(i))
    start(out)
