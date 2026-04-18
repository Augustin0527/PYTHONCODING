class Student:
   def __init__(self,sid,name,grade,marks):
       self.sid = sid
       self.name = name
       self.grade = grade
       self.marks = marks
   def average(self):
       return sum(self.marks)/ len(self.marks)
   def highest_marks(self):
       return max (self.marks) 
   def lowest_marks(self): 
       return min(self.marks)  
   def result(self):
       return "pass" if self.average() >= 50 else "fail"
   def performance(self):
       avg = self.average() 
       if avg >= 90:
           return "excellent"
       elif avg >= 75:
           return "good"
       elif avg >= 50:
           return "average"
       else:
           return "poor"
   def display(self):
       print("_" , self.sid) 
       print("name:" , self.name) 
       print("grade:" , self.grade) 
       print("marks:" , self.marks) 
       print("average:",round (self.average(),2))     
       print("highest:", self.highest_marks())
       print("lowest:", self.lowest_marks())
       print("result:", self.result())
       print("performance:", self.performance())


students = [
    Student(8994,"john pork",5,[23,99,68,80,57,67 ]), 
    Student(8995,"cinella zelenski",5,[23,10,68,80,57,67 ]),    
    ]
for s in students:
    s.display()            