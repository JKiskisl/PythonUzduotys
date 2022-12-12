class Student:
  def __init__(self, name, age, grupe) -> None:
    self.name = name
    self.age = age
    self.grupe = grupe
    self.spec=""
    
  def __repr__(self) -> str:
    return f"Student name - {self.name}, age - {self.age}, group - {self.grupe}"

