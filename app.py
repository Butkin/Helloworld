print("Hello world")

age = 46
print(age)

price = 19.98
first_name = "Piotr"
is_online = False


"/--------------------------------/"


"ankieta do przyjecia  wiek imie "


#first = float(input("Podaj pierwsza wartość: "))
#second = float(input("Podaj drugą wartość: "))
#sum = first + second
#print ("Sum: " + str(sum))


course = "Python for Beginners"
print (course.upper())
print (course.find('for'))
print (course.replace('x','4'))
print ('Python' in course)

print( 10 +3)
print (10 * 3)
print (10 - 7)
print (10/3)
print (10//3)
print(10%3)
print(10**3)


x = 3
x = x +3
print (x)
y = 4
print (y)
y +=4
print (y)
y -=4
print (y)
y *=4
print (y)
y /=4
print (y)

z = 10 + 3* 2
print (z)

a = (10+3)* 2
print (a)

# weight  k)g or L  Weight in Kg is

weight = float(input("Tell me your weight: "))
meter = input("Tell me id this value in (K)g or (L)bs?: ")
if meter == "k" :
    weight *= 2.20462262
    print("Weight in Lbs:" + str(weight))
elif meter == "l":
    weight /= 2.20462262
    print("Weight in Kg: " + str(weight))
else:
    print("Enter again correct values: weight and k or l")

i = 1
while i <= 10:
    print(i * "@" )
    i = i +1

