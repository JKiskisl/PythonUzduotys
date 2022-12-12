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
    
    match (averageFinal/len(avg)):
        case number if number < 5:
            self.student.spec = "Skola"
        case number if 5 <= number <= 6:
            self.student.spec = "Saitynai"
        case number if 6 <= number <= 8:
            self.student.spec = "Duomenu baze"
        case number if 8 <= number <= 10:
            self.student.spec = "AI"

    mesg += "Specilizacija: " + self.student.spec + "\n"
    
    return mesg
      