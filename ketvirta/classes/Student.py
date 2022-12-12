class Student:
  def __init__(self, name, lastname) -> None:
    self.name = name
    self.lastname = lastname
    
  def __repr__(self) -> str:
    return f"{self.name} {self.lastname}"

