name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

new_dict = {}

for key, val in zip(name, favorite_animal):
    new_dict[key] = val    

print new_dict
