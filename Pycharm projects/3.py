obj= {
    'name' : 'Student 1',
    'id' : '18BD2333',
}


name= obj.get('name')

for el in name:
     if el in ['d','u']:
         continue
     print(el)