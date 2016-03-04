admins = {'Jonathan': '122091'}
currentUser = None

def addUser():
    newAdmin = input('New Username: ')
    newPass = input('New Password: ')
    if newAdmin in admins:
        print(
            'It appears that username is taken, please try something else.')
        addUser()
    else:
        print('Adding new username...')
        admins[newAdmin] = newPass
        

def addMultipleUsers():
  number = input("How many users do you want to enter: ")
  number = int(number)
  x = 0
  while(x < number):
    addUser()
    x += 1
    
def addMultipleOneInput():
  users = input("Enter users following the convention: Username1,Password1|Username2,Password2")
  #Username1,Password1|Username2,Password2
  users_arr = users.split('|')
  #["Username1,Password1", "Username2,Password2"]
  for user in users_arr:
    #"Username1,Password1"
    user_arr = user.split(',')
    #["Usernam1","Password1"]
    admins[user_arr[0]] = user_arr[1]
  
def printUsers():
  for kv in admins.items():
    print(kv)
  
def removeUser():
    nameToremove = input('What user do you want to remove? Username: ')
    if nameToremove in admins:
        print('Removing user...')
        del admins[nameToremove]
        print('Can we help you with anything else?')
        main()
    else:
        print('User does not exist.')
        removeUser()
    print(admins)

def authenticate():
  inpt1 = input('Log In [ 1 ] Add a User [ 2 ] Add Multiple Users [ 3 ] Add Multiple Users on one line [ 4 ] show users [ 5 ]: ')
  if(inpt1) == '1':
    if logIn():
      return True
  elif(inpt1 == '2'):
    if addUser():
      return True
  elif(inpt1 == '3'):
    addMultipleUsers()
    authenticate()
  elif(inpt1 == '4'):
    addMultipleOneInput()
    authenticate()
  elif(inpt1 == '5'):
    printUsers()
    authenticate()
    
            
def logIn():
    login = input('Username: ')
    passw = input('Password: ')

    if login in admins:
        if admins[login] == passw:
            global currentUser
            currentUser = login
            return True
        else:
            print('Invalid password.')
            return False
    else:
        print('That Username does not exist please')
        return False