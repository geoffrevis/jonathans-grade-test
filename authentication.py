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
        global currentUser
        currentUser = newAdmin
        print('Hello ', newAdmin)
        print('What would you like to do today?')
        main()
        # print(admins)


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
  inpt1 = input('Log In [ 1 ] Add a User [ 2 ]: ')
  if(inpt1) == '1':
    if logIn():
      return True
  elif(inpt1 == '2'):
    if addUser():
      return True
    
            
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