
from utils import intInput, userSelect, getByID, readFile, readFileIntoDict, appendFileDict, writeFile, appendFile, getByIDAsDict

userDB = 'username_db.csv'

new = 'New'
exists = 'Existing'
leave = 'Exit'

opts = [new, exists, leave]
userData = {'username': '', 'waterRate': 0, 'elecRate': 0}

# ======= Select new or existing user =======

selected = userSelect(opts)
print(f'Selected: {selected}) {opts[selected]}')

# ======= Select new or existing user =======


# ======= New user flow =======

if opts[selected] == new:
    # output = readFileIntoDict(userDB)
    usernameList = readFileIntoDict(userDB, ['username'])
    print(f'list of users: {usernameList}')
    
    if usernameList:
        userData['username'] = input("Enter your username: ")
        while userData['username'] in usernameList:
            userData['username'] = input("Username is taken, please enter another a username: ")

        userData['waterRate'] = intInput("Please enter your water unit price: ")
        userData['elecRate'] = intInput("Please enter your electricity unit price: ")

    print('heree', userData)
    
    appendFileDict(userDB, [userData])

# ======= New user flow =======

# ======= Existing user flow =======
    
elif opts[selected] == exists:
    
    usernameList = readFileIntoDict(userDB, ['username'])

    if usernameList:
        userData['username'] = input("Enter your username: ")
        while userData['username'] not in usernameList:
            userData['username'] = input("Username not found, please enter another a username: ")
    else:
        print('no users in database, please create user first')
    
    output = getByIDAsDict(userDB, userData['username'])

# ======= Existing user flow =======

else:
    exit()

if userData['username'] != '':
    print(f'Welcome {userData["username"]}')
    print(f'Info: {output}')

print('End of program')




