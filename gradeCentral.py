from statistics import mean as m

admins = {'Jonathan': '122091'}
'''while True:
    login = input('Username: ')
    passw = input('Password: ')
    admins[login] = passw'''


studentDict = {'Jonathan': [100, 93, 92, 95], 'Kelly': [100, 100, 100, 95]}
'''while True:
    nameToenter = input('Student Name: ')
    gradeToenter = input('Grade: ')
    studentDict[nameToenter] = gradeToenter'''


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


def addStudent():
    nameToenter = input('Student Name: ')
    if nameToenter in studentDict:
        print('That student already exists.')
        action = input('Would you like to add a grade for that student? Yes [ 1 ] No [ 2 ] ')
        if action == 'Yes' or 'YES' or 'yes':
            gradeToenter = input('Grade: ', [])
            print('Adding grade...')
            studentDict[nameToenter].append(int(gradeToenter))
            print(studentDict)
        else:
            print('Can we help you with anything else?')
            main()
    else:
        print('Adding student to directory...')
        studentDict[nameToenter] = []
        print(studentDict)
        action = input(
            'Would you like to add a grade for that student? Yes [ 1 ] No [ 2 ] ')
        if action == '1':
            gradeToenter = input('Grade: ')
            if nameToenter in studentDict:
                print('Adding grade to', nameToenter)
                studentDict[nameToenter].append(int(gradeToenter))
                print('Can we help you with anything else?')
                main()
        else:
            print('Can we help you with anything else?')
            main()


def enterGrades():
    nameToenter = input('Student: ')
    gradeToenter = input('Grade: ')
    if nameToenter in studentDict:
        print('Adding grade...')
        studentDict[nameToenter].append(int(gradeToenter))
    else:
        print('Student does not exist.')
        action = input(
          'Would you like to add as a student? Yes [ 1 ] No [ 2 ] ')
        if action == '1':
          addStudent()

    print(studentDict)
    print('Can we help you with anything else?')
    main()


def removeStudent():
    nameToremove = input('What student do you want to remove?: ')
    if nameToremove in studentDict:
        print('Removing student...')
        del studentDict[nameToremove]
    else:
        print('Student does not exist.')
        removeStudent()
    print(studentDict)
    print('Can we help you with anything else?')
    main()


def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
    print(eachStudent, 'has an average grade of: ', avgGrade)


def main():
    print('''
    Welcome to Grade Central
    [ 1 ] - Add Student(s)
    [ 2 ] - Enter New Grade(s)
    [ 3 ] - Average Grade(s)
    [ 4 ] - Remove Student(s)
    [ 5 ] - Exit Grade Central
    [ 6 ] - Add User
    [ 7 ] - Remove User
    ''')
    action = input('What do you want to do today? ')
    if action == '1':
        addStudent()
    elif action == '2':
        enterGrades()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        removeStudent()
    elif action == '5':
        exit()
    elif action == '6':
        addUser()
    elif action == '7':
        removeUser()
    else:
        print('No valid choice was given, please, try again')


login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome,', login)
        main()
    else:
        print('Invalid password, program will detonate in 10 seconds.')
else:
    print('That Username does not exist please, try again.')
    action = input('Would you like to add a new user? Yes[1] No[2] ')
    if action == '1':
        addUser()
    else:
        print("Sorry to see you go.")
