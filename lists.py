data = [120,23,12,123,546,67] 
fruits = ["banana", "papaya","orange"]
print("original list:",data)
print("original list:",fruits)
fruits.append("pea")
print("after append:",fruits)

data.append("245")
print("after append:",data)

data.extend([245,328,190,])
print("after extend:",data)

fruits.extend(["cajou","pumpkin", "lemon",])
print("after extend:",fruits)
if 200 in data:
   idx = data.index(200)
   print("index of 200:",idx)

data.sort()
print("after sort:",data)

data.reverse()
print("after reverse:",data)    