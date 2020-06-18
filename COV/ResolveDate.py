def resolvedate(x):
    #x = '232333/44/2000'
    primerabarra = x.find('/')
    segundabarra = x.find('/',(x.find('/')+1),len(x))
    x1 = x[0:primerabarra]
    x2 = x[(primerabarra+1):segundabarra]
    x3 = x[(segundabarra+1):(len(x))]
    x = x2+'/'+x1+'/2020'
    #print(x)
    return x
