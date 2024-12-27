print("Welcome")
name = input('May I ask for your name? ')
print(f'It is a preasure meeting you, {name}!')
age = input('How old are you, that is if you do not mind me asking?')
print(f'WOW your {age} years old, thats amazing!')
print(f'How can I help you today?')

def display_menu():
  print("1. Placeholder") 
  print("2. Placeholder")    
  print("3. Placeholder")  
  print("4. Exit\n")  



def user_selection():
    while True:
        display_menu()
        user_choice = input("Please select an option (1-4): ")
        if user_choice == "4":
            print("If that is all I will take my leave, Goodbye!")
            break



display_menu()
user_selection()


