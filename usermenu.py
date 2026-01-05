entries = []

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

while True:
        print ("Re-select an option from the menu below:")
        print ("1. Add Entry")
        print ("2. Search Entries")
        print ("3. View All Entries")
        print ("4. Exit")
        print ("-----------------------------------")
        print ("Please type the number corresponding to your choice:")
        print ("-----------------------------------")
        user_input = input()
        if user_input == "1":
                lines = []
                print ("You have selected Add Entry.")
                print ("Please enter your entry below.")
                print (" Type //done to save. Type //back to go back to the main menu.")
                while True:
                        user_input = input()
                        disallow = user_input.strip()
                        
                        if user_input == "//done":      
                                if lines == []:
                                        print ("You must type at least one character.")
                                        continue
                                else:
                                        full_entry = "\n".join(lines)
                                        entries.append(full_entry)
                                        print ("Entry saved.")
                                        break
                        elif user_input == "//back":
                                break
                        
                        elif  disallow == "":
                                print ("You must type at least one character.")
                                continue
                        else:
                                lines.append(user_input)
           
                   
        elif user_input == "2":
                print ("You have selected Search Entries.")
                
                if entries == []:
                                print ("Nothing to search.")
                                continue
                else:
                        print ("Type a term to search.")
                        print("Case sensitivity matters. Type //done to leave.")
                        while True: 
                                user_input = input()
                                disallow = user_input.strip()
                                found = [] 
                                
                                if user_input == "//done":
                                        break
                                
                                elif disallow == "":
                                        print ("You must type at least one character.")
                                        continue
                                        #display search results w the result from user input
                                        
                                for entry in entries:
                                        if user_input in entry:
                                                found.append(entry)
                                if found == []:
                                        print ("No matches found. Try again.")
                                        continue
                                else:
                                        for match in found:
                                                print (match)
                                                continue
                                
                                        
                                
        elif user_input == "3":
                print ("You have selected View All Entries.")
                #code for viewing entries here
        elif user_input == "4":
                print ("Exiting program. Bye!")
                break
        else:
                print("Invalid Input. Try again.")