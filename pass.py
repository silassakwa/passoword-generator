import random 
lc=["a","d","e","f"]
up=["A","B","C","D","E","F"]
num=["1","2","3","4","5"]
sc=["!","@","#","$","%"]
password=random.choice(lc)+random.choice(up)+random.choice(num)+random.choice(sc)
password=password+password+password
print(password)
