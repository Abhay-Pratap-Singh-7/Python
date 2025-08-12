# Declare a dictionary { key : value }
student = {
    'name' : 'ABHAY PRATAP SINGH',
    'age' : 20,
    'branch' : 'CSE'
}
print(student)

# to access value of a certain key
print(student['name'])

# to get value and dont want keyerror : error when certain key is not found 
print(student.get('phone' , 'Not Found'))

# add or update 
student.update({ 'name' : 'SURYA PRATAP SINGH', 'age' : 22, 'phone' : 9696806511}) 
print(student)

# delete a key and value; can also use pop method
del student['branch']
print(student)

# to all keys
print(student.keys())

# to see all values
print(student.values())

# to all items
print(student.items())

# to print key
for key in student:
    print(key)

# to print kay and values both
for key, values in student.items():
    print(key, values)