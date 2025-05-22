student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91]

max_score=0

for score in student_scores:
    if score>max_score:
        max_score=score
        print( score)
print(max_score)
min_score=200
for score in student_scores:
    if score<min_score:
        min_score=score
        print(score)
print(min_score)
marks=[8,65,89,86,55,91,64,89]
max_marks=0
min_marks=100
for i in marks:
    if max_marks<i:
        max_marks=i
    if min_marks>i:
        min_marks=i
print(max_marks)
print(min_marks)