class user:
	name = ""
	age = 0
	gender = ''
	def __init__(self, name, age, gender):
		self.name = name 
		self.age = age
		self.gender = gender
		
	def printInfo(self):
		print('Name: ' + self.name)
		print('Age: ' + self.age)
		print('Gender: ' + self.gender)
		
	




def main():

	print('Welcome user!\n')
	name = input('What is your name?')
	age = input('What is your age?')
	gender = input('What is your gender?')
	
	usr = user(name, age, gender)
	
	usr.printInfo()
	

	
if __name__ == "__main__":
	main()