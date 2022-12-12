class Averages:
  def __init__(self, student, marks) -> None:
    self.student = student
    self.marks = marks
    
  def __repr__(self) -> str:
    lessonss = []
    mesg = f"{self.student} averages: \r\n"
    for mark in self.marks:
      if mark.lesson not in lessonss:
        lessonss.append(mark.lesson)
    
    avg = []
    for lesson in lessonss:
      suma = 0.0
      counter = 0
      mesg += "Lesson " + lesson.name + " average - "
      for mark in self.marks:
        if(mark.lesson == lesson):
          suma += mark.mark
          counter += 1
      final = suma/counter
      avg.append(final)
      mesg+=str(final) + "\r\n"
    
    mesg +="Ovr. avg. : "
    averageFinal = 0.0
    for kk in avg:
      averageFinal += kk
      
    mesg +=str(averageFinal /len(avg)) + "\r\n"
    return mesg
      