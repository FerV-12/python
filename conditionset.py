age=15
# > < >= <= == !=
if age>=60:
  print('Senior')
elif age>=18:
  print('Adult')
else:
  print('Minor')
  
  
  #Logical Operators
theNumber = 21
if theNumber>=0 and theNumber>=10:
  print('The perfect number')
    
#ternary operation numbType = 'value_if_true' if condition value else 'value_if_false'
numbType = 'Negative' if age < 0 else 'Even' if age%2==0 else 'Odd'
print(numbType)
#()? 'sadasd':'weaweae'

#Looping statements
isAlive=True
lives=3
while  isAlive and lives>0:
  if lives != 0:
      print("you're still in the Game!")
  else:
    print('Game Over')
    isAlive=False
  lives-=1
  
#for(i=0:1<=10:i++)
#for counting range('min,'max','increment')
for x in range (1,11,3):
  print(x)
  
  myname='Ferjhon'
  for x in myname:
    print(x)
    
shoppingList=['Toothpaste','Brush','Soap']
shoppingList2=[{'id':100, 'name':'soap'},{'id':200, 'name':'snack'},{'id':300, 'name':'plate'}]
for item in shoppingList2:
  print(item['name'])