pizzas = ['cheese', 'bbq', 'pepperoni']
for pizza in pizzas:
    print(pizza)

pizzas = ['cheese', 'bbq', 'pepperoni']
for pizza in pizzas:
    print ("I love to eat " + pizza.title() + " pizza" + ".")
print ("I really enjoy eating different types of pizza.")
print ("I like to eat pzza mostly during movie nights.")
print ("My favorite pizza was the one we would eat for school lunch")
print ("I really love pizza!")

animals = ['dog', 'cat', 'pig']
for animal in animals:
    print(animal)
animals = ['dog', 'cat', 'pig']
for animal in animals:
    print ("A " + animal.title() + " makes a great pet" + "!")
print ("All three of these animals walk on four legs.")
print ("All of them will make a great pet!")

pizzas = ['cheese', 'bbq', 'pepperoni']
friend_pizzas = pizzas[:]
pizzas.append('vegetable')
friend_pizzas.append('chicken')
print("My favorite pizzas are:")
for pizza in pizzas[0:4]:
    print(pizza.title())
print("My friend favorite pizzas are:")
for pizza in friend_pizzas[0:4]:
    print(pizza.title())
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
for food in my_foods:
    print(food)
friends_food = ['pizza', 'carot cake', 'falafel','jello']
for food in friends_food:
    print(food)
menus = ('shrimp', 'lobster', 'oysters', 'red snappa', 'grab')
for menu in menus:
    print(menu)

menus = ('shrimp', 'lobster', 'oysters', 'red snappa', 'grab')
print("original menus:")
for menu in menus:
    print(menu)
menus = ('shrimp', 'lobster', 'oysters', 'salad', 'chicken')
print("\nModified menus:")
for menu in menus:
    print(menu)
    