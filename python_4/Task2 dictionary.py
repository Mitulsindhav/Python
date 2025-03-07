d1={"a":5,"b":6,"c":7}
d2={"a":10,"c":20,"d":30}
d3={}

#d3={"a":[5,10],"b":6, "c":[7,20],"d":30}
#sum=0


for i in d1,d2:
    sum=sum+d1[i]

print("sum :",sum)




for key in set(list(d1.keys()) + list(d2.keys())):
    try:
        d3.setdefault(key,[]).append(d1[key])        
    except KeyError:
        pass

    try:
        d3.setdefault(key,[]).append(d2[key])          
    except KeyError:
        pass

print(d3)
