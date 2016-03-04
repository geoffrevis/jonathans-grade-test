import gradeCentral


admins = {'Jonathan': '122091'}
'''while True:
    login = input('Username: ')
    passw = input('Password: ')
    admins[login] = passw'''


def signUp():
    newAdmin = input('New Username: ')
    newPass = input('New Password: ')
    if newAdmin in admins:
        print(
            'It appears that username is taken, please try a something else.')
    else:
        print('Adding new username...')
        admins[newAdmin] = newPass
        print('Congratulations, hello ', newAdmin)
        print('What would you like to do today?')

        # print(admins)


def logIn():
    adminName = input('Username: ')
    adminPass = input('Password: ')
    if adminName in admins:  # if their username is in admin
        # if the user in admins password = the password given
        if admins[adminName] == adminPass:
            print('Welcome,', adminName)
            while True:  # while this is true, run grade central
                gradeCentral.main()


def main():    
    # Require user to login or signup
    action = input('Login [ 1 ] or Sign Up [ 2 ]')
    if action == '1':  # if they choose login request username and password
        while True:
            logIn()
    else:
        signUp()

main()