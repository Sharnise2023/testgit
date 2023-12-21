car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

bike = 'BMX'
print("Is bike == 'BMX'? I predict True.")
print(bike == 'BMX')

print("\nIs bike == 'trek'? I predict False.")
print(bike == 'trek')

pie = 'apple'
print("Is pie == 'apple'? I predict True.")
print(pie == 'apple')

print("\nIs pie == 'cherry'? I predict False.")
print(pie == 'cherry')

cake = 'chocolate'
print("Is cake == chocolate? I predict True.")
print(cake == 'chocolate')

print("\nIs cake == 'strawberry'? I predict False.")
print(cake == 'strawberry')
car = 'Mercedes'
car.lower() == 'mercedes' 


alien_color = 'green'
if 'green' in alien_color:
    print("player won 5 points.")
    
alien_color = 'green'
if 'green' in alien_color:
    print("print player is correct.")
    if 'blue' in alien_color:
        print("player is loss.")

alien_color = 'green'
if 'green' in alien_color:
    print("player won 5 points for shooting the alien.")
alien_color = 'blue'
if 'green' in alien_color:
    print("player just earrned 5 points for shooting the alien.")
else:
    print("\nplayer just earned 1 points.")
    



alien_color = 'yellow'
if 'green' in alien_color:
    print("player earned 5 points.")
elif alien_color == 'yellow':
    print("player earned 10 points.")
else:
    print("player earned 15 points")



alien_color = 'red'
if 'green' in alien_color:
    print("player earned 5 points.")
elif alien_color == 'yellow':
    print("player earned 10 points.")
else:
    print("player earned 15 points.")




alien_color = 'green'
if 'green' in alien_color:
    print("player earned 5 points.")
elif alien_color == 'yellow':
    print("player earned 10 points")
else:
    print("player earned 15 points.")

age = 64
if age < 2:
    print("The person is an baby.")
elif age < 4:
    print("The person is an toddler.")
elif age < 13:
    print("The person is an kid.")
elif age < 20:
    print("The person is an teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

favorite_fruits = ['watermelon', 'canalope', 'honeydew']
if 'watermelon' in favorite_fruits:
    print("I really love watermelon!")
if 'canalope' in favorite_fruits:
    print("I really love canalope!")
if 'honeydew' in favorite_fruits:
    print("I really love honeydew!")
if 'peaches' in favorite_fruits:
    print("I really love peaches!")
if 'strawberries' in favorite_fruits:
    print("I really love strawberries!")

user_names= ['eric', 'alice', 'bob', 'admin', 'charlie', 'david']
for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin, would you like to see a status reort?")
    else:
        print(f"Hello {user_name}, thank you for logging in again.")