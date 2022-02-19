
from utils import intInput, userSelect, readFile, readFileIntoDict, appendFileDict, writeFile, appendFile

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
    output = readFileIntoDict(userDB)
    usernameList = readFileIntoDict(userDB, ['username'])
    print(f'output2 {usernameList}')
    
    if output:
        userData['username'] = input("Enter your username: ")
        # nameTaken = True
        while userData['username'] in usernameList:
            # first column = row[0] = username.
            userData['username'] = input("Username is taken, please enter another a username: ")
            # nameTaken = False
                
        userData['waterRate'] = intInput("Please enter your water unit price: ")
        userData['elecRate'] = intInput("Please enter your electricity unit price: ")
        print('heree', userData)

    appendFileDict(userDB, [userData])

# ======= New user flow =======

# ======= Existing user flow =======
    
elif opts[selected] == exists:
    username = input("Enter your username: ")
    output = readFileIntoDict(userDB)

    if output:
        nameNotFound = True
        while nameNotFound:
            for row in output:
                # first column = row[0] = username.
                if userData['username'] == row['username']:
                    nameNotFound = False
                    break
            username = input("Username not found, please try again: ")

    # for row in output:
    #     # first column = row[0] = username.
    #     if username == row[0]:
    #         username = input("Username does not exist, please try again: ")

# ======= Existing user flow =======

else:
    exit()

print(f'Welcome {userData["username"]}')
print('End of program')




