from abc import ABCMeta, abstractmethod
'''
Using Book abstract base class Book so that the derived classes fiction, regular and novel classes are forced to use the method calculate_rent().
'''

class Book:
	__metaclass__ = ABCMeta

	@abstractmethod
	def calculate_rent(self): 
		raise NotImplementedError()

'''
Creating separate classes for all the book category so that if there is a change in the price in future then there will be a change at one place
'''
#fiction class
class fiction(Book):
	def __init__(self,title,days):
		self.days = days
		self.rent = 3
		self.first_two_day_charge = 1
	def calculate_rent(self):
		if int(self.days)<3:
			return self.first_two_day_charge*self.days
		else:
			return float(self.first_two_day_charge)*2 + float(int(self.days)-2)*float(self.rent)
			
# regular class
class regular(Book):
	def __init__(self,title,days):
		self.days = days
		self.rent = 1.5
		self.first_two_day_charge = 1
	def calculate_rent(self):
		if int(self.days)<3:
			return float(self.first_two_day_charge)*float(self.days)
		else:
			return float(self.first_two_day_charge)*2 + float(int(self.days)-2)*float(self.rent)
			
# novel class			
class novel(Book):
	def __init__(self,title,days):
		self.days = days
		self.rent = 1.5
		self.first_two_day_charge = 4.5
	def calculate_rent(self):
		if int(self.days)<3:
			return float(self.first_two_day_charge)*float(self.days)
		else:
			return float(self.first_two_day_charge)*2 + float(int(self.days)-2)*float(self.rent)
			
def main():
	# Reading txt file as input
	file = open(r"C:\\Users\\GOD\\Desktop\\story3.txt")
	input_list = file.readlines()
	total = 0
	for each in input_list:
		title,days,category = each.split(",")
		category = category.replace("\n","")
		if category == 'fiction':
			f = fiction(title,days)
			print ("Price for {} is ".format(title),f.calculate_rent())
			total += f.calculate_rent()
		
		if category == 'regular':
			r = regular(title,days)
			print ("Price for {} is ".format(title),r.calculate_rent())
			total += r.calculate_rent()

		if category == 'novel':
			n = novel(title,days)
			print ("Price for {} is ".format(title),n.calculate_rent())
			total += n.calculate_rent()
	# Total of all the inputs
	print ("Total rent of all books is {}".format(total))
if __name__ == "__main__":
    main()
