# array = []
# student_num = int(input("How many students took the test?: "))

# while student_num > 0:
#     score = [n for n in input("Enter the student name and grade separated by a space").split(" ")]
#     array.append(score)
#     student_num -= 1
    
    
#     def get_top_scores(input_list):
#         max = 0
#         top_students = []
#     for student in (input_list):
#         name = student[0]
#         score = int(student[1])
        
#     if score > max :
#         max = score
#         top_students = [name]
#     elif score == max:
#         top_students.append(name)

# return top_students, max


# names = {
#     "Robert" : "30",
#     "Alice" : "90",
#     "Charlie" : "50",
#     "Amanda" : "20",
#     "Ariel" : "40",
# }
# print(names)


# top_students, highest_score = get_top_scores(array)

        


array = []
student_num = int(input("How many students took the test?: "))

while student_num > 0:
    score = [n for n in input("Enter the student name and grade separated by a space: ").split(" ")]
    array.append(score)
    student_num -= 1
	
	
def get_top_scores(array):
    max = 0
    top_students = []
    
    for student in array:
        name = student[0]
        score = int(student[1])
        
        if score > max :
            max = score
            top_students = [name]

        elif score == max:
            top_students.append(name)
    return top_students




top_students = get_top_scores(array)
print(top_students)