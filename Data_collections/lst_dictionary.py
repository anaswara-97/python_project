employees = [
    {"e_id": 1000, "e_name": "ram", "salary": 25000, "department": "testing", "exp": 1},
    {"e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1},
    {"e_id": 1002, "e_name": "raj", "salary": 20000, "department": "mrkt", "exp": 1},
    {"e_id": 1003, "e_name": "nikil", "salary": 26000, "department": "developer", "exp": 1},
    {"e_id": 1004, "e_name": "nivi", "salary": 28000, "department": "developer", "exp": 2},
]
#print employee name only
# for employee in employees:
#      print(employee["e_name"])

# using map function
e_name=list(map(lambda employee:employee["e_name"],employees))
print(e_name)
print("-----------------")

#print employee name in uppercase
# for employee in employees:
#     print(employee["e_name"].upper())
e_name=list(map(lambda emp:emp["e_name"].upper(),employees))
print(e_name)
print("-----------------")

#print employee name where department is developer
# for employee in employees:
#     if employee["department"]=="developer":
#         print("developer : ",employee["e_name"])

developer=list(filter(lambda dep:dep["department"]=="developer",employees))
print(developer)

# names of emploees where department is developer
deve_name=list(map(lambda developer:developer["e_name"],developer))
print(deve_name)
print("-----------------")

#print total salary of employees
tot=0
for employee in employees:
    tot=tot+employee["salary"]
print("total : ",tot)

salary=list(map(lambda salary:salary["salary"],employees))
print(salary)

# sum of all salaries
print(sum(salary))

# display maximum salary amount
salary=max(list(map(lambda salary:salary["salary"],employees)))
print("maximum salary : ",salary)

# display minimum salary amount
salary=min(list(map(lambda salary:salary["salary"],employees)))
print("minimum salary : ",salary)
print("-----------------")

#print employee name only