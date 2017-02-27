class student:
	def __init__(self, name):
		self.name = name
		self.attend = 0
		self.grades = []
		print("hi my name is {0}".format(self.name))


	def addGrade(self, grade):
		self.grades.append(grade)
	def attendday(self):
		self.attend += 1
	def getAvg(self):

		return sum(self.grades)/ len(self.grades)


student1 = student("mike")

for X in range(1,11):
	student1.attendday()


student1.addGrade(9)
student1.addGrade(8)
student1.addGrade(7)
student1.addGrade(7)
student1.addGrade(7)

print (student1.grades)
print (student1.getAvg())
