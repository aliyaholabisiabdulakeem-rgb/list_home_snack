# 1
students = [("Alice", 78), ("Bob", 45), ("Charlie", 90), ("Diana", 62), ("Kent", 30)]
#   a
print("=====1A=====")
for names, scores in students:
    print(names, scores)
#   b
print("=====1B=====")
for names, scores in students:
    if scores > 60:
        print(names, scores)
print("=====1C=====")   
pass_count = 0 
for names, scores in students:
    if scores >= 50:
        pass_count += 1
print("Pass count = ", pass_count)
    
#  2
print()
products = [("Laptop", 1200), ("Mouse", 25), ("Keyboard", 45), ("Monitor", 300), ("USB cable", 10)]
#  a
print("=====2A=====")   
def cost_more_than_100(products):
    items, price = products
    return price > 100
print(list(filter(cost_more_than_100, products)))
#  b
print("=====2B=====")   
total = 0
for items, price in products:
    total += price
print("Total = " , total)
#  c
print("=====2C=====")   
for items, price in products:
    print("products:" , items , "-" , "price:" , price)

#   3
print()
points = [(2,3), (-1,4), (5,-6), (0,7), (-3,-2)]
#  a
print("=====3A=====")   
def positive_value(points):
   return points[0] > 0 and points[1] > 0
print(list(filter(positive_value, points)))
#  b
print("=====3B=====")   
for x,y in points:
    print(x, y)
#  c
print("=====3C=====")   
points = [(2,3), (-1,4), (5,-6), (0,7), (-3,-2)]
new_list_of_points = []
for x, y in points:
    if x > 0 and y > 0:
        new_list_of_points.append((x, y))
print(new_list_of_points)

#  4
print()
employees = [("John", "IT", 50000), ("Jane", "HR", 45000), ("Mike", "IT", 60000), ("Sara", "Finance", 70000)]
#  a
print("======4A=====")
for name, department, salary in employees:
    print(name, department, salary)

#  b
print("======4B=====")
def it_department(employees):
    name, department, salary = employees
    return department == "IT"
print(list(filter(it_department, employees)))

#  c
print("======4C=====")
for names,department,salary in employees:
    if salary > 55000:
        print(names, salary)
