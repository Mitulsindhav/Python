def fun(max):
    cnt = 1
    while cnt <=max:
        if cnt%2==0:
            yield cnt
        cnt+=1

ctr = fun(10)
for n in ctr:
        print(n)


 

   
