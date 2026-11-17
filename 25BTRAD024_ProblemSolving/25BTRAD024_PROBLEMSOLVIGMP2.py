# Student Grading Automation

def calculate_grade(score):
&quot;&quot;&quot;Convert a numeric score (0-100) into a letter grade.&quot;&quot;&quot;
if score &gt;= 90:
return &quot;A&quot;
elif score &gt;= 80:
return &quot;B&quot;
elif score &gt;= 70:
return &quot;C&quot;
elif score &gt;= 60:
return &quot;D&quot;
else:
return &quot;F&quot;

def process_students(students):
&quot;&quot;&quot;
students: a dictionary like {&quot;Name&quot;: score, ...}
Prints each student&#39;s grade and returns a summary.
&quot;&quot;&quot;
results = {}

for name, score in students.items():
grade = calculate_grade(score)
results[name] = grade
print(f&quot;{name}: Score = {score}, Grade = {grade}&quot;)

return results

def class_average(students):
&quot;&quot;&quot;Calculate the average score of the class.&quot;&quot;&quot;
total = sum(students.values())
count = len(students)
return total / count

# ----- Main program -----

# Sample data: replace with your actual student scores
students = {
&quot;Aarav&quot;: 92,
&quot;Diya&quot;: 76,
&quot;Kabir&quot;: 58,
&quot;Meera&quot;: 84,
&quot;Rohan&quot;: 67
}

print(&quot;----- Grading Report -----&quot;)
results = process_students(students)

avg = class_average(students)
print(f&quot;\nClass Average: {avg:.2f}&quot;)

# Count how many students got each grade
grade_counts = {}
for grade in results.values():

grade_counts[grade] = grade_counts.get(grade, 0) + 1

print(&quot;\nGrade Distribution:&quot;)
for grade, count in sorted(grade_counts.items()):
print(f&quot;{grade}: {count} student(s)&quot;)