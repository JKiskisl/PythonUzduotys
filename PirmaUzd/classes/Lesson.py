class Lesson:
  def __init__(self, name, credit, student) -> None:
    self.name = name
    self.credit = credit
    self.student = student
    
  def add_student(self, student):
    self.student.append(student)
    
  def get_student(self,ind):
    return self.student[ind]
  
  def __repr__(self) -> str:
    return f"Name - {self.name}, credit - {self.credit}, students - {self.student}"