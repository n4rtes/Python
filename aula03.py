'''
a = ' curso '
b = 'python'
c = a+b
print(c)
print(len(a))
print(c.count('o'))
print(c.lower())
print(c.upper())
print(c.title())
print(c.split())
print(c.replace(b, 'Java Script'))
print(c.find('n'))
print(c.strip(a))
print(c.replace(b, 'Java Sript ') + c.strip())

str = 'curso de python'

print(str[6:8])  # de 
print(str[0])    # c
print(str[2:5])  # rso 
print(str[8:])   # python
print(str * 2 )
print(str + ' show')

Exercício:

str = 'python e a linguagem do backend'

print(len(str))
print(str.count('n'))
print(str.title())
print(str.split())
print(str.find('linguagem'))
print(str.strip())


str = 'python e a linguagem do backend'

print(str[0:6])
print(str.find('b'))
print(str[24:])
print(str.find('b'), str[24:])
print(str.find('m'))
print(str[0:20])

# Exercício 

L = [3, [5, 6, 1], 'Python', (0, 2)]

print(L, 'Lista proposta')

L[0] = 33 
L[1] = [3, 2, 1]
L[3] = 1, 3

print(L, f'... O indice da lista "L[0]" agora eh igual a 33 ')
print(L, f'... O indice da lista "L[1] agora eh [5,6,1]')
print(L, f'... O indice da lista "L[3]" agora eh (1,3) ')


# Exercício pág.23
L = [1,'A',"A", 3, 3, 4, 5]

L.extend([6, 10])
print(L)

print(L.count(3))

L.pop(0)
print(L)

L.remove('A')
print(L)

L.remove('A')
print(L)


# Exercício pág. 24

lista = [1,'Python',"HTML",3,4,5]

print(len(lista))

lista.append(3)
print(lista)

lista.extend([10,20])
print(lista)

print(lista.count(3), 'eh a quantidade que o numero 3 da lista aparece')

lista.remove('HTML')
print(lista, 'removendo o objeto "HTML')

lista.remove(1)
print(lista, 'removendo o objeto "1" da lista')

lista.insert(0, 1)
print(lista)

'''

#Exercícios pág. 29

L = [1,'python',(100,200),10,10,['Id',101,'RG',321123], 'Salvador']
print(L)

L[0] = 2
print(L)

print(L[5][0:2])
