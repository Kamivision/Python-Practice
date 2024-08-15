#ask for user input
print("Welcome to Minecraft Madlibs! To get your funny story enter a word following each prompt below...")

#create variables to fill the blanks & save user input to corrisponding variables
verb1 = input("verb: ")
verb2= input("verb: ")
furniture_type = input("type of furniture: ")
food_type1 = input("type of food: ")
animal_plural = input("type of animal (plural): ")
food_type2 = input("type of food: ")
plural_noun_thing1 = input("plural noun - thing: ")
verb3 = input("verb: ")
noun_thing = input("noun - thing: ")
plural_noun_thing2 = input("plural noun - thing: ")

#create a paragraph with blanks
madlib = f"Welcome to Minecraft, a game where you can {verb1} , {verb2} and build {furniture_type} for days! Build a farm and grow {food_type1} , spawn {animal_plural}  from eggs and collect {food_type2} from chickens! You can also hunt for wild {plural_noun_thing1} and go fishing. {verb3} in creative mode or see how long you last in survival {noun_thing}. Watch out for Creepers and other bizarre {plural_noun_thing2} in survival mode!"

#output completed paragraph with user input
print(madlib)
