# main.py

# H E Y L I S T E N 
# If you're using Windows, this doesn't need any changes. If you're using Linux, change
# 'cls' in os.system('cls') in mainmenu() to os.system('ls')
# H E Y L I S T E N 

import os # Used to clear the screen. 
# Setting up files to be read. They're .txt because OBS defaults to that in the open selector
# but it doesn't really matter.
with open('p1name.txt','w') as f:
    f.write('Player 1')
with open('p2name.txt','w') as f:
    f.write('Player 2')
with open('p1wins.txt','w') as f:
    f.write('0')
with open('p2wins.txt','w') as f:
    f.write('0')
p1name = 'Player 1' # Temporary placeholders for the player names so they aren't submitted
p2name = 'Player 2' # before you press Submit Names, to queue up next matches.

def rename(pos):
    if pos == 'p1':
        return input('Enter a name for Player 1: ')
    else:
        return input('Enter a name for Player 2: ')
        

def mainmenu():
    os.system('cls') # Note this only works in windows. Change 'cls' to 'ls' if you're using Linux
    global p1name
    global p2name
    side = ''
    choice = ''
    print('''
Main Menu:
    
    [1] Player 1 Name
    [2] Player 2 Name 
    [3] Submit Names/Reset Scores
    [4] Add win...
    [5] Fix...
    [6] More...
    [0] Quit''')
    choice = input('Choose an option: ')
    if choice == '1':
        p1name = rename('p1')
        mainmenu()
    elif choice == '2':
        p2name = rename('p2')
        mainmenu()
    elif choice == '3':
        with open('p1name.txt','w') as f:
            f.write(p1name)
        with open('p2name.txt','w') as f:
            f.write(p2name)
        with open('p1wins.txt','w') as f:
            f.write('0')
        with open('p2wins.txt','w') as f:
            f.write('0')
        mainmenu()
    elif choice == '4':
        win = ''
        print('''
Which side?
    [1] Player 1
    [2] Player 2
    [0] Back''')
        side = input('Choose an option: ')
        if side == '1':
            with open('p1wins.txt','r') as f:
                win = f.read()
                win = int(win) + 1
            with open('p1wins.txt','w') as g:
                g.write(str(win))
        elif side == '2':
        
            with open('p2wins.txt','r') as f:
                win = f.read()
                win = int(win) + 1
            with open('p2wins.txt','w') as g:
                g.write(str(win))
        elif side == '0':
            mainmenu()
        else:
            print('Invalid selection!')
            input('Press Enter to return to main menu!')
        mainmenu()
    elif choice == '5':
        print('''
Fix Menu:

    [1] Swap Players/Wins
    [2] Fix Player 1 Name
    [3] Fix Player 2 Name
    [4] Fix Player 1 Wins
    [5] Fix Player 2 Wins
    [0] Back''')
        choice = input('Choose an option: ')
        if choice == '1':
            with open('p1name.txt','r+') as f:
                p2name = f.read()
                with open('p2name.txt','r+') as g:
                    p1name = g.read()
                    g.seek(0)
                    g.write(p2name)
                    g.truncate()
                f.seek(0)
                f.write(p1name)
                f.truncate()
            with open('p1wins.txt','r+') as f:
                p2wins = f.read()
                with open('p2wins.txt','r+') as g:
                    p1wins = g.read()
                    g.seek(0)
                    g.write(p2wins)
                    g.truncate()
                f.seek(0)
                f.write(p1wins)
                f.truncate()
        elif choice == '2':
            p1name = rename('p1')
            with open('p1name.txt','w') as f:
                f.write(p1name)
        elif choice == '3':
            p2name = rename('p2')
            with open('p2name.txt','w') as f:
                f.write(p2name)
        elif choice == '4':
            win = input('How many wins?: ')
            with open('p1wins.txt','w') as f:
                f.write(win)
        elif choice == '5':
            win = input('How many wins?: ')
            with open('p2wins.txt','w') as f:
                f.write(win)
        elif choice == '0':
            pass
        else:
            print('Invalid selection!')
            input('Press Enter to return to main menu!')
        mainmenu()
    elif choice == '6':
        print('''
More Menu:

    [1] Readme/About
    [0] Back''')
        choice = input('Choose an option: ')
        if choice == '1':
            print('''
Hi! I'm Travis Williams (or @ShrimpyNobashi) and this is a script project
that I tried to make as easy to use as possible. It creates 4 text files in
the same folder that you put it in that you can point your streaming suite
at with Text (then, in Text, select "choose from file"), then arrange them
yourself (lazy asshole) to set up your stream layout. I'd say center-align
the wins, left-align Player 1, then right-align Player 2 and it SHOULD work.

If you find any errors, feel free to tweet at me! I appreciate you!''')
            input('Press Enter to return to main menu!')
        elif choice == '0':
            pass
        else:
            print('Invalid selection!')
            input('Press Enter to return to main menu!')
        mainmenu()
    elif choice == '0':
        pass
    else:
        print('Invalid selection!')
        input('Press Enter to return to main menu!')
        mainmenu()
mainmenu()