# list datastructure, its ordered and changeable
cars = ["Mercedes", "Nissan", "Toyota", "Range"]
cars[1] = "Subaru"
cars.append("Mitsubishi")
cars.insert(2, "Bmw")
cars.pop(0)
cars.sort()
cars.reverse()
cars.copy()
print(cars)
# this is a tuple,ordered, its unchangeable
fruits = ("Mangoes", "Oranges", "Pineapple", "Avocado", "Oranges")
x = fruits.count("Oranges")

print(fruits)
for x in fruits:
    print(x)

# sets datastructure
countries = {"Kenya", "Uganda", "Tanzania", "Burundi", "Ethopia"}
print(countries)

# dictionaries
matunda={
"amount":40,
"jina":"Ndizi",
"rangi":"Yellow",
"name":"Banana"
}
matunda["size"]="Large"
matunda.pop("amount")
print(matunda)