"""
Vamos a continuar con las cositas de sintaxis que se pueden olvidar    
"""

lst =list()
lst2 =[]

fruits = ['banana','sandia','uva','manzana','pera']

"""
for i in fruits:
    print(f'fruits: {i}')
"""

it1,it2,*it=fruits

print(type(it1),it2,it)

last= len(fruits)-1
print(fruits[last])

print(fruits[last]=='lima')


fruits[last]='meme'
print(fruits[last])

fruits.append('sexo')
last= len(fruits)-1
print(fruits[last])

print(fruits)
fruits.pop(len(fruits)-1)
print(fruits)

a=fruits+['mango','sexeee']
print(a)

fruits.extend(['a','b'])
print(fruits)

#exercises 5
