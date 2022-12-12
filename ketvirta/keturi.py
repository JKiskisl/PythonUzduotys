
#Darbas su failais

#Patobulinkite sistemą taip, 
# kad vienus duomenis paimtų iš failiuko, 
# o kitus duomenis išsaugotu į failiuką.


from classes.Averages import Averages
from classes.Group import Group
from classes.Lesson import Lesson
from classes.Marks import Marks
from classes.Student import Student
import re


lessons = []
marks = []
students = []
averagesz = []

studPath = "C:\\Users\\smics\\Desktop\\PythonUzd_Justas_Kiskis_PI20C\\inputStudents.txt"

read_stud = open(studPath).read().splitlines()
for line in read_stud:
  student = line.split('\t')
  students.append(Student(student[0], student[1]))
  
lessPath = "C:\\Users\\smics\\Desktop\\PythonUzd_Justas_Kiskis_PI20C\\inpurtLessons.txt"
  
read_lesson = open(lessPath)
for l in read_lesson:
  lesson = l.split('\t')
  lessons.append(Lesson(lesson[0], lesson[1], []))  


for student in students:
  for lesson in lessons:
    lesson.add_student(student)

print(*lessons, sep="\n")


marks.append(Marks(lessons[0].get_student(0), lessons[0], 8))
marks.append(Marks(lessons[1].get_student(0), lessons[1], 7))
marks.append(Marks(lessons[0].get_student(0), lessons[0], 8))
marks.append(Marks(lessons[1].get_student(0), lessons[1], 10))

marks.append(Marks(lessons[0].get_student(1), lessons[0], 9))
marks.append(Marks(lessons[1].get_student(1), lessons[1], 7))
marks.append(Marks(lessons[0].get_student(1), lessons[0], 5))
marks.append(Marks(lessons[1].get_student(1), lessons[1], 9))

marks.append(Marks(lessons[0].get_student(2), lessons[0], 10))
marks.append(Marks(lessons[1].get_student(2), lessons[1], 7))
marks.append(Marks(lessons[0].get_student(2), lessons[0], 10))
marks.append(Marks(lessons[1].get_student(2), lessons[1], 10))

print("Pazymiai:")

print(*marks, sep="\n")


writePath = "C:\\Users\\smics\\Desktop\\PythonUzd_Justas_Kiskis_PI20C\\output.txt"

for i in range(len(students)):
  averagesz.append(Averages(students[i], []))
  for mark in marks:
    if(mark.student == students[i]):
      averagesz[i].marks.append(mark)
with open(writePath, 'w') as f:
  for i in averagesz:
    f.write(f"{i}\n")
