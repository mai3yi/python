
print ("Welcome to the User Log System.")
# criteria: Create a menu system that acts like a small database of user input that is searchable.
print ("Please select an option from the menu below:")
print ("1. Add Entry")
print ("2. Search Entries")
print ("3. View All Entries")
print ("4. Exit")
print ("-----------------------------------")
print ("Please type the number corresponding to your choice:")
print ("-----------------------------------")

user_input = input()
if user_input == "1":
        print ("You have selected Add Entry.")
        #code for adding an entry here
elif user_input == "2":
        print ("You have selected Search Entries.")
        #code for searching entries here
elif user_input == "3":
        print ("You have selected View All Entries.")
        #code for viewing entries here
elif user_input == "4":
        print ("Exiting program. Bye!")
else:
    print("Invalid Input. Try again.")