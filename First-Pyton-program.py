print('|---------------------------------|')
print("|Welcome to my chariter generator |")
print('|---------------------------------|')

race_list = [Orc,Human,Elf]

gender = input('Please Pick your gender ')

if gender == "male" or "female":
   race = input('Please pick a Race'+ str(race_list))
   print  
else:
    print('Sorry there are only 2 genders')


