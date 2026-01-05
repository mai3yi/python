entries = []
print ("___________________________________")
print ("Welcome to the User Log System.")
print ("___________________________________")
# criteria: Create a menu system that acts like a small database of user input that is searchable.
print ("Please select an option from the menu below:")
print ("1. Add Entry")
print ("2. Search Entries")
print ("3. View All Entries")
print ("4. Exit")
print ("___________________________________")
print ("Please type the number corresponding to your choice:")
print ("___________________________________")

while True:
        print ("___________________________________")
        print ("Re-select an option from the menu below:")
        print ("1. Add Entry")
        print ("2. Search Entries")
        print ("3. View All Entries")
        print ("4. Exit")
        print ("___________________________________")
        print ("Please type the number corresponding to your choice:")
        print ("___________________________________")
        user_input = input()
        if user_input == "1":
                lines = []
                print ("___________________________________")
                print ("You have selected Add Entry.")
                print ("Please enter your entry below.")
                print (" Type //done to save. Type //back to go back to the main menu.")
                print ("___________________________________")
                while True:
                        user_input = input()
                        disallow = user_input.strip()
                        
                        if user_input == "//done":      
                                if lines == []:
                                        print ("___________________________________")
                                        print ("You must type at least one character.")
                                        print ("___________________________________")
                                        continue
                                else:
                                        full_entry = "\n".join(lines)
                                        entries.append(full_entry)
                                        print ("___________________________________")
                                        print ("Entry saved.")
                                        print ("___________________________________")
                                        break
                        elif user_input == "//back":
                                break
                        
                        elif  disallow == "":
                                print ("___________________________________")
                                print ("You must type at least one character.")
                                print ("___________________________________")
                                continue
                        else:
                                lines.append(user_input)
           
                   
        elif user_input == "2":
                print ("___________________________________")
                print ("You have selected Search Entries.")
                print ("___________________________________")
                
                if entries == []:
                                print ("___________________________________")
                                print ("Nothing to search.")
                                print ("___________________________________")
                                continue
                else:
                        print ("___________________________________")
                        print ("Type a term to search.")
                        print("Case sensitivity matters. Type //done to leave.")
                        print ("___________________________________")
                        while True: 
                                user_input = input()
                                disallow = user_input.strip()
                                found = [] 
                                
                                if user_input == "//done":
                                        break
                                
                                elif disallow == "":
                                        print ("___________________________________")
                                        print ("You must type at least one character.")
                                        print ("___________________________________")
                                        continue
                                        #display search results w the result from user input
                                        
                                for entry in entries:
                                        if user_input in entry:
                                                found.append(entry)
                                if found == []:
                                        print ("___________________________________")
                                        print ("No matches found. Try again.")
                                        print ("___________________________________")
                                        continue
                                else:
                                        for match in found:
                                                print (match)
                                                continue
                                
        elif user_input == "3":
                print ("___________________________________")
                print ("You have selected View All Entries.")
                print ("___________________________________")
                
                if entries == []:
                        print ("___________________________________")
                        print ("Nothing here.")
                        print ("___________________________________")
                        
                else:
                        for entry in entries:
                                print (entry)
                        
        elif user_input == "4":
                print ("___________________________________")
                print ("Exiting program. Bye!")
                print ("___________________________________")
                break
        else:
                print ("___________________________________")
                print("Invalid Input. Try again.")
                print ("___________________________________")