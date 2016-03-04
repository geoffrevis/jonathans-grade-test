from statistics import mean as m
import os

studentDict = {'Jonathan': [100, 93, 92, 95], 'Kelly': [100, 100, 100, 95]}

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

#this literally just clears the screen.  May break on your computer depending on OS
def clearScreen():
  os.system('cls' if os.name=='nt' else 'clear')

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
    
def mainMenu():
    print(''' -- Grade Central -- 
    Main Menu:
    [ 1 ] - Add Student(s)
    [ 2 ] - Enter New Grade(s)
    [ 3 ] - Average Grade(s)
    [ 4 ] - Remove Student(s)
    [ 5 ] - Exit Grade Central
    [ 6 ] - Add User
    [ 7 ] - Remove User
    [ 8 ] - Exit to Main Menu
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
    elif action == '8':
        return True
    else:
        clearScreen();
        print('No valid choice was given, please, try again')
    mainMenu()


def main():
  clearScreen();
  mainMenu()
    
        
        
#__name__ is a special python variable that is set by the interpreter for each file
#if the file is being run directly __name__ == "__main__"
#otherwise it is __name__ == the name of the file ("gradeCentral") in this case
#this code is to prevent main() from executing when this file is imported.
if __name__ == "__main__":
    main()