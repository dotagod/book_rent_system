# Book class with objects days and number_of_books
class Book:
	def __init__(self,days,number_of_books):
		self.days = days
		self.number_of_books = number_of_books

	def calculate_rent(self):
		return int(self.days)*int(self.number_of_books)

def main():
	# Reading txt file as input
	file = open(r"C:\\Users\\GOD\\Desktop\\story1.txt")
	input_list = file.readlines()
	total = 0
	for each in input_list:
		days,number_of_books = each.split(",")
		b = Book(days,number_of_books)
		print (b.calculate_rent())
		total += b.calculate_rent()

	print ("Total rent of book is {}".format(total))
if __name__ == "__main__":
    main()
