# The program keeps score in a game.
# Date: 06/16/2021
# Author: Pragat Wagle

def point():
   """ Return the player who wins a point """
   player = input("\nWho wins a point, player A or B? ")
  
   if player.upper() == 'A':
       return 'A';
   elif player.upper() == 'B':
       return 'B';
   else:
       print("\nInvalid Player!!! \n");
       return 'E';

def game():
   """ Plays the game """
   # Initialize scores to 0
   A = 0
   B=  0
  
   # Iterate till user is found
   while True:
      
       # Calling point function
       player = point()
      
       # Assigning points
       if player == 'A':
           A += 1
       elif player == 'B':
           B += 1
      
       # Printing the scores of both players
       print("A Score " + str(A))  
       print("B Score " + str(B))  
          
       # Checking for winner
       if A >= 3 and (A-B) >= 2:
           return 'A'
       elif B >= 3 and (B-A) >= 2:
           return 'B'
       elif A>=7 and A >= B:
           return 'A'
       elif B>=7 and B >= A:
           return 'B'      
      
def main():
   """ Main function """
   print("\nThe program keeps score in a game.\n")
  
   # Calling game function
   winner = game()
  
   # Printing results
   print("\n\n The winner is player " + str(winner) + " !")
  
  
# Calling main function
main()
















