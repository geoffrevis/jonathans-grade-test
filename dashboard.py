import gradeCentral
import authentication
import os

def mainMenu():
  print('''-- Main Menu -- 
[ 1 ] - Grade Central
[ 2 ] - Exit''')
  selection = input("Select an Option: ")
  if(selection == '1'):
    clearScreen()
    gradeCentral.main()
    clearScreen()
    mainMenu()
  elif(selection == '2'):
    return
  else:
    clearScreen()
    print ("You must select an option!")
    mainMenu()
    
#this literally just clears the screen.  May break on your computer depending on OS
def clearScreen():
  os.system('cls' if os.name=='nt' else 'clear')
  
def main():    
    # Require user to login or signup
    clearScreen()
    while(not authentication.currentUser):
      if(authentication.authenticate()):
        clearScreen()
        print('Welcome,', authentication.currentUser)
    mainMenu()

if __name__ == "__main__":
    main()