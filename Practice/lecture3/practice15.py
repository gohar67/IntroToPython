dict1 = {'key1':123,'key2':[12,23,33],'key3':'hello'}
x = str(input('write a key:'))
y = str(input('write a vale:'))
dict1.update( { x : y } )
print(dict1)