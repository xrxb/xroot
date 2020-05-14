y = 0
yy = 0
x = 709
x = x - 1
abc = "abcdefghijklmnopqrstuvwxyz"
result=[]
def count():
     global x, y, yy, abc, result
     if x > (len(abc)-1):
          x = x - len(abc)
          y = y + 1
          if y > len(abc):
               y = y - len(abc)
               yy = yy + 1
               count()
          count()
     result.append(x)
     result.append(y)
     result.append(yy)
     return result
     
result=count()
x=result[0]
y=result[1]
yy=result[2]

if (yy == 0)&(y == 0):
     print(abc[x])
elif (yy == 0)&(y > 0):
     y = y - 1
     print(abc[y]+abc[x])
else:
     yy = yy - 1
     y = y - 1
     print(abc[yy]+abc[y]+abc[x])

