# create list of users
known_users = ['John', 'Paul', 'George', 'Ringo']

while True:
    print('Hi my name is Travis')
    name = input('what is your name?  ').strip().capitalize()

    if name in known_users:
        print('Hello  ' + (name))
        remove = input('Would you like to be removed from system? y/n?  ').lower()

        if remove =='y':
            known_users.remove(name)
        elif remove == 'n':
            print("no problem I didn't want you to leave anyway")

    else:
        print('hmm I dont think I have met you yet{}').format(name))
        add_me = input('would you like to be added to the system (y/n)?: '),strip().lower()
        if add_me == 'y':
            known_users.append(name)
        elif add_me == 'n':
            print('no worries, see you around!')