def my_name() :
    print("My name is shahd")
my_name()

def my_meal(food ,drink) :
    print( f"I like to eat {food} and while drinking {drink}")
my_meal("pasta" ,"juice")

def cube(number):
  return number**3

result = cube(3)
print(result)

def by_three(num):
 if num%3==0:
    return cube(num)
 else:
    return False
 



print(by_three(9))