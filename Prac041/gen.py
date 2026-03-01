from datetime import datetime 
print(datetime.now())

#objects for datetime.now()
x = datetime.now()
ans=x.replace(microseconds=0)






from datetime import datetime
x=datetime.now().strtime("%B")




from datetime import datetime, timedelta
a=datetime.now()
b=timedelts(days=5)
print(a-b)





a=datetime(2025,1,1,1,1)

b=datetime(2025,2,2,2,2)

print((a-b).total_seconds())





import json 
name="filen.json"
with open (name,"r") as file:
    flobal var
    var=load(name)
print(var)







import json
