class Marks:
  def __init__(self, student, lesson, mark) -> None:
    self.student = student
    self.lesson = lesson
    self.mark = mark
  
  def __repr__(self) -> str:
    return f"{self.student}, {self.lesson.name}, mark - {self.mark}"
  