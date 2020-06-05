y = 0
yy = 0
x = ""
abc = "abcdefghijklmnopqrstuvwxyz"
result=[]
def name(x):
     global result
     #x = input("Give a number to convert at ID columns of Excel: ")
     x = int(x) - 1
     count(x)
     x=result[0]
     y=result[1]
     yy=result[2]

     if (yy == 0)&(y == 0):
          #print(abc[x])
          result = abc[x]
          #print(result)
     elif (yy == 0)&(y > 0):
          y = y - 1
          #print(abc[y]+abc[x])
          result = (abc[y]+abc[x])
          #print(result)
     else:
          yy = yy - 1
          y = y - 1
          #print(abc[yy]+abc[y]+abc[x])
          result = (abc[yy]+abc[y]+abc[x])
          #print(result)
     return result

def count(x):
     global y, yy, abc, result
     if x > (len(abc)-1):
          x = x - len(abc)
          y = y + 1
          if y > len(abc):
               y = y - len(abc)
               yy = yy + 1
               count(x)
          count(x)
     result.append(x)
     result.append(y)
     result.append(yy)
     return result
     
#result=name(x)


