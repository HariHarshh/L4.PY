print(" Enter Marks Obtained in 4 Subjects: ")
Maths = int(input("Maths  :")) 
English = int(input("English  :"))
Science = int(input("Science   :"))
Hindi = int(input("Hindi  :"))

sum = Maths+English+Science+Hindi
print("sum of math, english, science and hindi = ", sum)

perc =(sum/400)*100

print("Percentage = ", perc)