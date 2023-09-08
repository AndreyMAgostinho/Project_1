game_over = False
red_score = 0
blue_score = 0
while game_over == False:
  answer = input("Did someone make a point?")
  if answer == 'yes':
    input("which team scored the goal, red team or blue team?")
    if answer == 'blue':
      blue_score = blue_score + 1

    else:
      red_score = red_score + 1

  else:
    game_over == False

  answer_2 = float(input("Enter the time for the game:"))
  if answer_2 >= 60:
    game_over = True

  else: 
    game_over = False