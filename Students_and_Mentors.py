def avg_rate_course(sl, course):
   sum_grades=0
   k=0
   for stud in sl:
       for course_self,grade in stud.grades.items():
           if course == course_self:
              for el_grade in  grade:
                sum_grades+= el_grade
                k+=1
   return sum_grades/k


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_grade(self):
        sum_grades=0
        k=0
        for course,grade in self.grades.items():
            for el_grade in  grade:
                sum_grades+= el_grade
                k+=1
        return sum_grades/k

    def __str__(self):
        res = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' \
         f'Средняя оценка за домашние задания: {self.average_grade()}\n' \
         f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
         f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self,other):
        if not isinstance(other,Student):
            print ('Не студент')
            return
        return self.average_grade()>other.average_grade()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname):
       super().__init__(name, surname)

    def __str__(self):
        res= f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n'
        return res
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def average_grade(self):
        sum_grades=0
        k=0
        for course,grade in self.grades.items():
            for el_grade in  grade:
                sum_grades+= el_grade
                k+=1
        return sum_grades/k

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}\n'
        return res
    def __lt__(self,other):
        if not isinstance(other,Lecturer):
            print ('Не лектор')
            return
        return self.average_grade()>other.average_grade()

best_student = Student('Lana', 'Antonova', 'female')
best_student.courses_in_progress += ['Python']
best_student.finished_courses=['Введение в программирование']

bad_gay = Student('Alex', 'Rost', 'male')
bad_gay.courses_in_progress += ['GIT']

Doctor_lector=Lecturer('Ivan','Petrovich')
Doctor_lector.courses_attached +=['Python']
Doctor_lector.courses_attached += ['GIT']

Doctorka_lector=Lecturer('Svetlana','Ivanovna')
Doctorka_lector.courses_attached +=['Python']
Doctorka_lector.courses_attached += ['GIT']

best_student.rate_lector(Doctor_lector,'Python',2)
best_student.rate_lector(Doctor_lector,'Python',7)
bad_gay.rate_lector(Doctor_lector,'GIT',5)
bad_gay.rate_lector(Doctor_lector,'GIT',8)

best_student.rate_lector(Doctorka_lector,'Python',9)
best_student.rate_lector(Doctorka_lector,'Python',8)
bad_gay.rate_lector(Doctorka_lector,'GIT',10)
bad_gay.rate_lector(Doctorka_lector,'GIT',8)

Reviewer1 = Reviewer('Some', 'Buddy')
Reviewer1.courses_attached += ['Python']
Reviewer1.courses_attached += ['GIT']
Reviewer1.courses_attached += ['API']

Reviewer1.rate_hw(best_student, 'Python', 10)
Reviewer1.rate_hw(best_student, 'Python', 8)
Reviewer1.rate_hw(bad_gay, 'GIT', 7)
Reviewer1.rate_hw(bad_gay, 'GIT', 2)
Reviewer1.rate_hw(bad_gay, 'GIT', 1)


print(Reviewer1.__str__())
print(Doctor_lector.__str__())
print(Doctorka_lector.__str__())
print(best_student.__str__())
print(bad_gay.__str__())
print(f'Студент {best_student.surname} лучше {bad_gay.surname}' if best_student.__lt__(bad_gay)==True else  f'Студент {bad_gay.surname} лучше {best_student.surname}')
print(f'Лектор {Doctor_lector.surname} лучше {Doctorka_lector.surname}\n' if Doctor_lector.__lt__(Doctorka_lector)==True else  f'Лектор {Doctorka_lector.surname} лучше {Doctor_lector.surname}\n')

#print(bad_gay.grades)
#print(best_student.grades)
sl_student = [bad_gay, best_student]
print( f'Средняя оценка студентов по курсу GIT {round(avg_rate_course(sl_student,"GIT"),2)}')
print( f'Средняя оценка студентов по курсу Python {round(avg_rate_course(sl_student,"Python"),2)}\n')

#print(Doctor_lector.grades)
#print(Doctorka_lector.grades)
sl_lector = [Doctor_lector, Doctorka_lector]
print( f'Средняя оценка лекторов по курсу GIT {round(avg_rate_course(sl_lector,"GIT"),2)}')
print( f'Средняя оценка лекторов по курсу Python {round(avg_rate_course(sl_lector,"Python"),2)}\n')






