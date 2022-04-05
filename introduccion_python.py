
import cmath

def new_message(message):
    print(message, '(s/n): ')
    again = input()
    if again == 's':
        return True
    elif again == 'n':
        return False
    else:
        print("**Error**")
        return new_message(message)

def ejercicios():
    print('-----> Ejercicios de practica, introduccion a python laboratorio #1 de conmutación <-----')
    case = int(input('Digite el ejercicio el cual quiere ejecutar: '))
    
    if case == 1:
        a = float(input('Digite el valor de a: '))
        b = float(input('Digite el valor de b: '))
        c = float(input('Digite el valor de c: '))
        d = (b**2) - (4*a*c)
        sol1 = (-b-cmath.sqrt(d))/(2*a)
        sol2 = (-b+cmath.sqrt(d))/(2*a)
        print('Las soluciones son {0} y {1}'.format(sol1,sol2))
        
    
    elif case == 2:
        str = 'w3big'
        print(str)
        print(str[0:-1])
        print(str[0])
        print(str[2:5])
        print(str[2:])
        print(str * 2)
        print(str + "TEST")
    
    elif case == 3 :
        list = [ 'abcd', 786 , 2.23, 'w3big', 70.2 ]
        tinylist = [123, 'w3big']
        print (list)
        print (list[1:3])
        print (list[2:])
        print (tinylist * 2)
        print (list + tinylist)

    elif case == 4: 
        name= input('entre nombre de archivo')
        handle = open(name, 'r')
        counts= dict()
        for line in handle:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word, 0) + 1
        bigcount = None
        bigword = None
        for word, count in list(counts.items()):
            if bigcount is None or count > bigcount:
                bigword = word
                bigcount = count
        print(bigword, bigcount)

    elif case == 5:
        age = int(input("entre la edad de su perro: "))
        print("")
        if age < 0:
            print("errado")
        elif age == 1:
            print("es un cachorro")
        elif age == 2:
            print("es un adulto")
        elif age > 2:
            human = 22 + (age -2)*5
            print("la edad de su perro es: ", human)
        input('presione tecla para terminar')

    elif case == 6: 
        n = 100
        sum = 0
        counter = 1
        while counter <= n:
            sum = sum + counter
            counter += 1
        print("la suma de los %d primeros números es: %d" % (n,sum))

    elif case == 7:
        sites = ["Baidu", "Google","w3big","Taobao"]
        for site in sites:
            if site == "w3big":
                print("w3big")
                break
        print("otro site " + site)

    elif case == 8:
        a = ['Google', 'Baidu', 'w3big', 'Taobao', 'QQ']
        for i in range(len(a)):
            print(i, a[i])

    elif case == 9:
        def area(width, height):
            return width * height
        def print_welcome(name):
            print("Welcome", name)
        print_welcome("w3big")
        w = 4
        h = 5
        print("width =", w, " height =", h, " area =", area(w, h))

    elif case == 10:
        def min(a, b):
            if a < b:
                return a
            else:
                return b
        def max(a, b):
            if a > b:
                return a
            else:
                return b
        print('El máximo de 3 y -10 es', max(3,-10))
        print('El minimo entre 5 y 7 es', min(5, 7))

    else: print('*********************INCORRECTO, Valide el ejercicio que quiere ejecutar!*********************')

    if new_message('¿Desea realizar otra operación?'):
        print()
        ejercicios()
    else:
        print('¡Gracias por Utilizar esta Aplicación!')
            
ejercicios()

