from math import sqrt
age = 12
height = 7.1
a = 2
b = 3
complex_num = a + b * 1j

b = input("Enter Base: ")
h = input("Enter height: ")
print("The Area of the Triangle is: ", (0.5 * int(b) * int(h)))


a = int(input("Enter Side a: "))
b = int(input("Enter Side b: "))
c = int(input("Enter Side c: "))

print("The Perimeter of the triangle is: ", (a + b + c))

w = input("Enter width: ")
l = input("Enter lenght: ")
print("The Area of the Rectangle is: ", (int(w) * int(l)))

print("The perimeter of the Rectangle is: ", (2 * (int(w) + int(l))))


# Slope
m = 2
print("SLope: ", m)

# If y = 0
# X-Intercept
b = 1
print("X-Intercept: ", b)

# If X = 0
# Y-Intercept
c = -2
print("Y-Intercept: ", c)


x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope
m2 = (y2 - y1) / (x2 - x1)

# Euclidean distance
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Slope:", m)
print("Distance:", distance)


if m == m2:
    print("Slope are equal")
else:
    print("Slope are different.")


x_values = [1, 2, 3, 4, 5, 7, 8, 9]

for x in x_values:
    y = x**2 + 6*x + 9
    print(f"when x ={x}, y = {y}")


python_length = len("python")
dragon_length = len("dragon")

print(f"Length of 'python': {python_length}")
print(f"Length of 'dragon': {dragon_length}")

# Falsy comparison
if python_length != dragon_length:
    print("Lengths are different.")


"on" in "python" and "on" in "dragon"


sentence = "I hope this course is not full of jargon"
"jargon" in sentence


text = "python"
length = len(text)

float_length = float(length)
string_length = str(float_length)

print(f"Length of 'python': {length}")
print(f"Float length: {float_length}")
print(f"String length: {string_length}")


number = 20

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number } is not even")


floor_division = 7 // 3
converted_value = int(2.7)

print(f"Floor division: {floor_division}")
print(f"Converted value: {converted_value}")


if floor_division == converted_value:
    print("They are equal.")
else:
    print("They are different.")


type("10") == type(10)


type("9.8") == type(10)


hr = int(input("Enter hours: "))

rate_per_hr = float(input("Enter rate per hour: "))


weekly_pay = hr * rate_per_hr
print(f"Your weekly earning is : {weekly_pay}")


num_of_years = int(input("Enter number of years you have live: "))
seconds_lived = num_of_years * 365 * 24 * 60 * 60

print(f"You have lived for {seconds_lived} seconds")


for i in range(1, 6):
    line = ""
    for j in range(1, 6):
        power = (j - 1) * (i - 1)
        value = 1 ** power
        line += f"{value:<4}"
    print(line)
