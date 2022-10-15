from person import Person
player1 = Person()
while player1.health_status >= 1 and player1.mood >= 1 and player1.capital >= 1:
 command = input('видите действие: ')
 if command == 'work':
   player1.work()
 if command == 'wolk':
   player1.wolk()
 if command == 'go to the doctor':
   player1.go_to_the_doctor()
 print(player1)
if player1.health_status <= 0:
  print('вы имволид')
if player1.mood <= 0:
  print('вы вaвли в депресию')
if player1.capital <= 0:
  print('вы банкрот')