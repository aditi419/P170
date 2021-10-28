from tkinter import *
root = Tk()
root.title('P170')
root.geometry('500x500')

percentage_grade_3_label = Label()
percentage_grade_5_label = Label()
percentage_grade_10_label = Label()


class Grade3:
    def __init__(self, language_arts, mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics

        def percentage(self):
            total_marks = self.language_arts+mathematics
            total_marks_with_100 = total_marks*100
            grade_3_percentage = total_marks/200
            percentage_grade_3_label = grade_3_percentage


class Grade5:
    def __init__(self, language_arts, mathematics, social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies

        def percentage(self):
            total_marks = self.language_arts+mathematics+social_studies
            total_marks_with_100 = total_marks*100
            grade_3_percentage = total_marks/300
            percentage_grade_5_label = grade_5_percentage

class Grade10:
    def __init__(self,language_arts,mathematics,social_studies,foreign_language):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        
        def percentage(self):
            total_marks = self.language_arts+mathematics+social_studies+foreign_language
            total_marks_with_100 = total_marks*100
            grade_3_percentage = total_marks/400
            percentage_grade_5_label = grade_5_percentage
            
object_grade_3 = Grade3(40,50)
btn = Button(root,text='Grade 3',command=object_grade_3.percentage())
btn.pack()
percentage_grade_3_label.pack()

object_grade_5 = Grade5(40,50,90)
btn2 = Button(root,text='Grade 5',command=object_grade_5.percentage)
btn2.pack()
percentage_grade_5_label.pack()

object_grade_10 = Grade10(40,50,90,80)
btn = Button(root,text='Grade 10',command=object_grade_10.percentage)
btn.pack()
percentage_grade_10_label.pack()
            
mainloop()
