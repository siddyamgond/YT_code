import random

a = random.randint(1,100)
b = int(input("Enter number"))
count=0

while True:
  if a>b:
    print("Enter greater number")
    b = int(input("Enter number"))
    count=count+1
  elif a<b:
     print("Enter greater number")
     b = int(input("Enter number"))
     count=count+1
  else:
    break;

print("You guess correct number in ",count," attempts ")

