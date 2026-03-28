student = {
    "name":"merwan",
    "age":10,
    "grade":"5",
    "city": "longeuil"
}
print("original dictionary")
print(student)
print("name:",student["name"])
print("age using get():", student.get("age"))
student["school"] = "greenfield park"
print("after adding new field")
print(student)
student["age"]= 11
print("after updating age")
print(student)
removed = student.pop("city")
print("removed city",removed)
print("after pop():",student)
print("keys:",student.keys())
print("values:",student.values())
print("items:",student.items())
student.update({"grade":"6"})
print("after updating grade",student)