import curses
import sys
from subprocess import call 
import msvcrt

    

gameRunning = True

	
# import sleep to show output for some time period 
from time import sleep 
  
# define clear function 
def clear(): 
    # check and make call for specific operating system 
    _ = call('clear' if os.name =='posix' else 'cls') 

def printMenu():
	# main menu screen that will be printed every game loop
	print('||=~~~~~~~The Heroes of Earth~~~~~~~~=||')
	print('||=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||=1)Start New Game~~~~~~~~~~~~~~~~~~=||')
	print('||=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||=2)Load Game~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||=3)Help~~~~~~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||=4)Quit Game~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~=||')
	print('||====================================||')



def checkInputs():
	return True


import time
def main():
	stdscr = curses.initscr()
	curses.beep()
	printMenu()
	print ("press SPACE to enter the serial number")

	while not msvcrt.kbhit() or msvcrt.getch() != " ":
		# do something else
		print (".")
		time.sleep(0.1)

# clear the keyboard buffer
	while msvcrt.kbhit():
		keypress = msvcrt.getch()
		if keypress == chr(34):
			sys.exit()
	
		

	
if __name__ == "__main__":
	main()