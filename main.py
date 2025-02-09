student_data = {'id1':
{'name':['sara'],
'class': ['v'],
'subject_intergration':['english, maths, Science']
 },
'id2':
{'name':['david'],
'class': ['v'],
'subject_intergration':['english, maths, Science']},
'id3' :
{'name':['sara'],
'class': ['v'],
'subject_intergration':['english, maths, Science']},
'id4':
{'name':['surya'],
'class': ['v'],
'subject_intergration':['english, maths, Science']},
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)