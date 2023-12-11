numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

count = 0
while count <= 10:
    print(count)
    count += 1


for number in numbers:
    print(number)

count = 10
while count >= 0:
    print(count)
    count -= 1

# nested loops to iterate 7 times. 
# The outer loop iterates 7 times,
#  and the inner loop iterates 7 times for each iteration of the outer loop. Inside the inner loop, the code prints a # character
#  expected output 

#######
#######
#######
#######
#######
#######
#######

for i in range(7):
    for j in range(7):
        print(' #', end='')
    print()


# iterate throuh all numbers and multiple each by it self
for number in numbers:
    print(f"{number} x {number} = {number * number}")



tools = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
# Print all items in tools
for tool in tools:
    print(tool)

# print only even numbers from the range 0 - 100
for i in range(100):
    if i % 2 == 0:
        print(i)    

# print only odd numbers from the range 0 - 100
for i in range(100):
    if i % 2 != 0:
        print(i)    


total = 0

for i in range(100):
    total += i
print('the sum of all number is ', total)


total_odd = 0
total_even = 0

for i in range(100):
    if i % 2 == 0:
        total_even += i
    else:
        total_odd += i

    

print(f'The sum of all evens is {total_even}. and the sum of all odds is {total_odd}')    


fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for fruit in reversed(fruits):
  reversed_fruits.append(fruit)

print(reversed_fruits)