import random
import names

print('|---------------------------------|')
print("|Welcome to my chariter generator |")
print('|---------------------------------|')

valid_genders = ["male", "female"]
gender = None
race_list = ['Orc','Human','Elf']

def ask_gender() -> str:
  return str(input("Enter your Gender: ")).lower()

gender = ask_gender()
while gender not in valid_genders:
  print("Unknown gender, try again")
  gender = ask_gender()

print(f"You have chosen {gender}")
 
names.get_full_name()
print(' Hello '+ names.get_full_name(gender))

