#Dia de diccionarios jeje#

personal_data = {'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }}
"""
personal_data['salary'] = 20000
personal_data['skills'].append('Java')

print(len(personal_data))
print(personal_data['skills'])
print(personal_data['address']['zipcode'])
print(personal_data.get('address'))
print(personal_data.get('salary'))

personal_data['skills'].remove('Java')
print(personal_data['skills'])

personal_data.pop('skills')
"""

#exercises#

dog = dict()
empty_dog = {}
dog['name']= 'david'
dog['color']= 'brown'
dog['breed']= 'santos'
dog['legs']= 4
dog['age']= 23

student ={'first':'david',
          'last':'santos',
          'gender':'male',
          'age':45,
          'marital':'alone',
          'status':'well',
          'address':{'street':'CarlosMarx'}
          }

print(dog)
print(student['address'])
print(len(student))
print(student.values())


