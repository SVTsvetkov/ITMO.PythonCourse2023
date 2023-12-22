#Работа со строками
#string1 = "This is a string."
#string2 = " This is another string."
#print(string1+string2)
#print(len(string1))
#print(string2.title())
#print(string2.upper())

#d = "qwerty"
#print(d)
#ch = d[2]
#print(ch+'  '+'d[2]')
#chm = d[1:3]
#print(chm+'  '+'d[1:3]')
#a=d[1:]
#print(a+'  '+'d[1:]')
#b=d[:3]
#print(b+'  '+'d[:3]')
#c=d[:]
#print(c+'  '+'d[:]')
#k=d[1:5:2]
#print(k+'  '+'d[1:5:2]')

#Работа с числами
#x=10
#y=2
#print(x/y)
#print(x%y)
#print(x**y)
#param = "string" + str(15)
#print(param)

#n1 = input("Enter the first number: ")
#n2 = input("Enter the second number: ")
#n3 = float(n1) + float(n2)
#print(n1 + " plus " + n2 + " = ", n3)

#a = 1/3
#print("{:7.3f}".format(a))
#a = 2/3
#b = 2/9
#print("{:7.3f} {:7.3f}".format(a, b))
#print("{:10.3e} {:10.3e}".format(a, b))

#n1 = input("Enter the first number: ")
#n2 = input("Enter the second number: ")
#n3 = float(n1) + float(n2)
#print(n1 + " plus " + n2 + " = ", "{:7.3f}".format(n3))

#Списки
#list1 = [82,8,23,97,92,44,17,39,11,12]
#print(list1)
#help(dir(list))
#help(list1.insert)
#a=333
#b=444
#list1[0]=a
#list1[1]=b
#print(list1)
#list1.append(111)
#print(list1)
#list1.insert(0, 222)
#print(list1)
#list1.remove(0)
#print(list1)
#a=len(list1)-1
#print(a)
#list1.pop(a)
#print(list1)

#list1.sort(reverse=True)
#print(list1)

#list2 = [3,5,6,2,33,6,11]
#lis = sorted(list2)
#lis.sort(reverse=True)
#print(list2)
#print(lis)

#Кортежи
#seq = (2,8,23,97,92,44,17,39,11,12)
#print(seq)
#print(seq.count(8))
#print(seq.index(44))
#listseq = list(seq)
#type(listseq)
#print(listseq)
#lis1 = sorted(listseq)
#lis1.sort(reverse=True)
#print(listseq)
#print(lis1)

#Словари
#D={'food': 'Apple', 'quantity': 4,'Color': 'Red'}
#print(D['food'])
#D['quantity']+=10
#print(D['quantity'])

#dp = {}
#dp['name']='Ivan'
#dp['age']=18
#print(dp)

#Вложенность хранения данных
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},'job': ['dev', 'mgr'],'age': 25}
print(rec['name'])
print(rec['name']['firstname'])
print(rec['job'])
rec['job'].append('janitor')
print(rec['job'])
#input()