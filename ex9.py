# You are developing a program for a teacher to grade their students' exams. The program should prompt the teacher to enter the number of questions on the exam, the number of questions the student answered correctly, and the number of points each question is worth. The program should then calculate the student's grade as a percentage, and print out a message indicating whether the student passed or failed the exam.

#Get the number of questions on the exam
no_ques = int(input("Enter the total number of questions: "))
print('Total number of questions:', no_ques,'\n')

#Get the number of questions answered correctly
no_ques_correct = int(input("Enter the number of questions answered correctly: "))
print('Number of questions answered correctly:', no_ques_correct,'\n')

#Get the number of points each question is worth
points_per_ques = int(input("Enter the number of points each question is worth: "))
print('Each question is worth:', points_per_ques, 'points','\n')

#Calculate the student's grade as a percentage
student_grade = (no_ques_correct / no_ques) * 100

#Print out a message indicating whether the student passed or failed the exam
if(student_grade >= 50):
    print("The student has PASSED the exam with a grade of", student_grade, "%")
else:
    print("The student has FAILED the exam with a grade of", student_grade, "%")