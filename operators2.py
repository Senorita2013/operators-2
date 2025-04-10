a=23
b=24
c=22

if a > b and a > c:
    print("a is bigger")
elif b > a and b > c:
    print("b is bigger")
else:
    print("c is bigger")

#!=
p= 10
q= 12
r= 12

print(p!=q)
print(p!=r)
print(q!=r)

t=int(input("Enter a number"))
if t%2 != 0:
    print("t is an odd number")

#BMI
w=float(input("Enter the weight"))
h=float(input("Enter the height"))

BMI= w / (h/100)**2

print(BMI)

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 34.9:
    print("You are severly overweight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are severly obese") 