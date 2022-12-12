
#3. Numeriai, eilutės, sąraša

#Papildykite sistemą tokiais duomenimis: pažymiai, vidurkiai, dalykų kreditai

from classes.Student import Student
from classes.Group import Group
from classes.Lesson import Lesson
from classes.Marks import Marks
from classes.Averages import Averages

lessons = []
marks = []
students = []
averagesz = []

g1 = Group("PI20A")
g2 = Group("PI20B")
g3 = Group("PI20C")

students.append(Student("Justas", 25, g3))
students.append(Student("Jonas", 19, g3))
students.append(Student("Kotryna", 22, g2))


lessons.append(Lesson("Python", 6, []))
lessons.append(Lesson("Veido Atpazinimas", 3, []))
lessons.append(Lesson("Inzinerija", 6, []))

for student in students:
  for lesson in lessons:
    lesson.add_student(student)

print(*lessons, sep="\n\r")


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

print ("Vidurkiai:")

for i in range(len(students)):
  averagesz.append(Averages(students[i], []))
  for mark in marks:
    if(mark.student == students[i]):
      averagesz[i].marks.append(mark)
      
print(*averagesz)