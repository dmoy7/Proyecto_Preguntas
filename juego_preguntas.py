import random


#INSTRUCCIONES DE EJECUCIÓN: 
#1. Se deberá ejecutar el siguiente código en consola e importar el modulo random
#2. Se deberá elegir el número de la ronda como se solicita en consola.
#3. Se debe elegir la opción (A, B, C ó D) en letra mayúscula cuando la consola lo solicite y presionar enter.

categoria1=int(input("Presione 1 para comenzar con la primera ronda de preguntas: "))
if categoria1 == 1:
    list1 = ["Pregunta 1", "Pregunta 2","Pregunta 3", "Pregunta 4", "Pregunta 5" ]
    a=random.choice(list1)
    print("La pregunta seleccionada para la primera ronda es: ", a)
    if a=="Pregunta 1":
        respuesta1=input("Elija la opción correcta para la Pregunta 1:\n¿Que jugador ganó el mundial del 2002?\n A. Ronaldo\n B. Messi\n C. Pele\n D. Maradona\n ")
        if respuesta1 == 'A':
            puntaje=2
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()        
    elif a=="Pregunta 2":
        respuesta2=input("Elija la opción correcta para la Pregunta 2:\n¿Cuál es el simbolo químico del Oro?\n A. Or\n B. Au\n C. Al\n D. Dm\n")
        if respuesta2 == 'B':
            puntaje=2
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    elif a=="Pregunta 3":
        respuesta3=input("Elija la opción correcta para la Pregunta 3:\n¿Cuál es la capital de Magdalena?\n A. Medellín\n B. Barranquilla\n C. Santa Marta\n D. Bogotá\n")
        if respuesta3 == 'C':
            puntaje=2
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    elif a=="Pregunta 4":
        respuesta4=input("Elija la opción correcta para la Pregunta 4:\n¿De qué se alimentan los Koalas?\n A. Carne\n B. Leche\n C. Bambú\n D. Eucalípto\n")
        if respuesta4 == 'D':
            puntaje=2
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    else:
        respuesta4=input("Elija la opción correcta para la Pregunta 5:\n¿Cuál fue la primera película de Walt Disney?\n A. Blancanieves y los siete enanitos\n B. Mickey Muse\n C. Caperucita Roja\n D. La Bella Durmiente\n")
        if respuesta4 == 'A':
            puntaje=2
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
else:
    print('Gracias por participar se lleva un puntaje de 0')
    quit() 

categoria2=int(input("Felicidades!!!!. Puedes presionar 2 para seguir con la segunda ronda o presionar 0 para retirarte con el acumulado: "))
if categoria2 == 2:
    list2 = ["Pregunta 1", "Pregunta 2","Pregunta 3", "Pregunta 4", "Pregunta 5" ]
    b=random.choice(list2)
    print("La pregunta seleccionada para la segunda ronda es: ", b)
    if b=="Pregunta 1":
        respuesta1=input("Elija la opción correcta para la Pregunta 1:\n¿Cuál es el río más largo del mundo?\n A. El Rio Nilo\n B. El Rio Amazonas\n C. El Rio Negro\n D. El Rio Muerto\n")
        if respuesta1 == 'A':
            puntaje=4
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    elif b=="Pregunta 2":
        respuesta2=input("Elija la opción correcta para la Pregunta 2:\n¿Quién escribió La Odisea?\n A. Miguel de Cervantes\n B. Homero\n C. Aristoteles\n D. Platon\n ")
        if respuesta2 == 'B':
            puntaje=4
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()     
    elif b=="Pregunta 3":
        respuesta3=input("Elija la opción correcta para la Pregunta 3:\n¿Quién pintó La última cena?\n A. Piccaso\n B. Alejandro Magno\n C. Leonardo Da Vinci\n D. Sócrates\n ")
        if respuesta3 == 'C':
            puntaje=4
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    elif b=="Pregunta 4":
        respuesta4=input("Elija la opción correcta para la Pregunta 4:\n¿Cuál es el océano más grande?\n A. Atlántico\n B. Meditarreneo\n C. índico\n D. Pacífico\n ")
        if respuesta4 == 'D':
            puntaje=4
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    else:
        respuesta5=input("Elija la opción correcta para la Pregunta 5:\n¿En qué año comenzó la II Guerra Mundial?\n A. 1939\n B. 1938\n C. 1945\n D. 1980\n")
        if respuesta5 == 'A':
            puntaje=4
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
else:
    print ("Gracias por participar y se lleva un puntaje de 2")
    quit() 

categoria3=int(input("Felicidades!!!!. Puedes presionar 3 para seguir con la tercera ronda o presionar 0 para retirarte con el acumulado: "))
if categoria3 == 3:
    list3 = ["Pregunta 1", "Pregunta 2","Pregunta 3", "Pregunta 4", "Pregunta 5" ]
    c=random.choice(list3)
    print("La pregunta seleccionada para la tercera ronda es: ", c)
    if c=="Pregunta 1":
        respuesta1=input("Elija la opción correcta para la Pregunta 1:\n¿Cual es país más poblado de la Tierra?\n A. China\n B. Colombia\n C. EEUU\n D. España\n")
        if respuesta1 == 'A':
            puntaje=8
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    elif c=="Pregunta 2":
        respuesta2=input("Elija la opción correcta para la Pregunta 2:\n¿Cuál es la capital de Suecia?\n A. Estambul\n B. Estocolmo\n C. Moscu\n D. Madrid\n")
        if respuesta2 == 'B':
            puntaje=8
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()     
    elif c=="Pregunta 3":
        respuesta3=input("Elija la opción correcta para la Pregunta 3:\n¿Cómo se llama el animal terrestre más rápido del mundo?\n A. Leopardo\n B. Tigre\n C. Guepardo\n D. León\n")
        if respuesta3 == 'C':
            puntaje=8
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    elif c=="Pregunta 4":
        respuesta4=input("Elija la opción correcta para la Pregunta 4:\n¿En qué país se encuentra el famoso monumento Taj Mahal?\n A. China\n B. Perú\n C. Japón\n D. India\n")
        if respuesta4 == 'D':
            puntaje=8
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    else:
        respuesta5=input("Elija la opción correcta para la Pregunta 5:\n¿Cuántas lenguas cooficiales existen en España?\n A. 4\n B. 3\n C. 5\n D. 2\n")
        if respuesta5 == 'A':
            puntaje=8
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
else:
    print ("Gracias por participar y se lleva un puntaje de 4")
    quit()

categoria4=int(input("Felicidades!!!!. Puedes presionar 4 para seguir con la cuarta ronda o presionar 0 para retirarte con el acumulado: "))
if categoria4 == 4:
    list4 = ["Pregunta 1", "Pregunta 2","Pregunta 3", "Pregunta 4", "Pregunta 5" ]
    d=random.choice(list3)
    print("La pregunta seleccionada para la cuarta ronda es: ", d)
    if d=="Pregunta 1":
        respuesta1=input("Elija la opción correcta para la Pregunta 1:\n¿Cuál es el lago más profundo del mundo?\n A. Lago Baikal\n B. Lago Tanganica\n C. Lago Vostok\n D. Lago Malawi\n")
        if respuesta1 == 'A':
            puntaje=16
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    elif d=="Pregunta 2":
        respuesta2=input("Elija la opción correcta para la Pregunta 2:\n¿Cómo se llama la estación espacial rusa?\n A. MAR\n B. MIR\n C. NUN\n D. TON\n")
        if respuesta2 == 'B':
            puntaje=16
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()     
    elif d=="Pregunta 3":
        respuesta3=input("Elija la opción correcta para la Pregunta 3:\n¿Cuál fue el primer metal que empleó el hombre?\n A. Orol\n B. Platino\n C. Cobre\n D. Broncei\n")
        if respuesta3 == 'C':
            puntaje=16
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    elif d=="Pregunta 4":
        respuesta4=input("Elija la opción correcta para la Pregunta 4:\n¿En qué lugar del cuerpo se produce la insulina?\n A. Corazón\n B. Hígado\n C. Riñón\n D. Páncreas\n")
        if respuesta4 == 'D':
            puntaje=16
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    else:
        respuesta5=input("Elija la opción correcta para la Pregunta 5:\n¿Cuál es la capital de Irán?\n A. Teherán\n B. Bangkok\n C. Moscu\n D. Estambul\n")
        if respuesta5 == 'A':
            puntaje=16
            print ("La respuesta es correcta y su puntaje es:", puntaje)
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
else:
    print ("Gracias por participar y se lleva un puntaje de 8")
    quit()

categoria5=int(input("Felicidades!!!!. Puedes presionar 5 para seguir con la quinta y última ronda o presionar 0 para retirarte con el acumulado: "))
if categoria5 == 5:
    list5 = ["Pregunta 1", "Pregunta 2","Pregunta 3", "Pregunta 4", "Pregunta 5" ]
    e=random.choice(list3)
    print("La pregunta seleccionada para la quinta ronda es: ", e)
    if e=="Pregunta 1":
        respuesta1=input("Elija la opción correcta para la Pregunta 1:\n¿Quién es el autor de el Quijote?\n A. Miguel de Cervantes\n B. Homero\n C. Socrates\n D. Aristoteles\n")
        if respuesta1 == 'A':
            puntaje=50
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
            print ("FELICIDADES, USTED HA GANADO EL CONCURSO!!!!!!!!!!")
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    elif e=="Pregunta 2":
        respuesta2=input("Elija la opción correcta para la Pregunta 2:\n¿Dónde se encuentra la Basílica: La Sagrada Familia?\n A. Madrid\n B. Barcelona\n C. Estambul\n D. Valencia\n")
        if respuesta2 == 'B':
            puntaje=50
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
            print ("FELICIDADES, USTED HA GANADO EL CONCURSO!!!!!!!!!!")
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()     
    elif e=="Pregunta 3":
        respuesta3=input("Elija la opción correcta para la Pregunta 3:\n¿Qué es una hemeroteca?\n A. Comida\n B. Colección de monumentos\n C. Colección de revistas\n D. Una discoteca\n")
        if respuesta3 == 'C':
            puntaje=50
            print ("La respuesta es correcta y su puntaje total es:", puntaje)
            print ("FELICIDADES, USTED HA GANADO EL CONCURSO!!!!!!!!!!")
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    elif e=="Pregunta 4":
        respuesta4=input("Elija la opción correcta para la Pregunta 4:\n¿En qué año se aprobó la actual Constitución española?\n A. 2005\n B. 1975\n C. 1955\n D. 1978\n")
        if respuesta4 == 'D':
            puntaje=50
            print ("La respuesta es correcta y su puntaje es:", puntaje)
            print ("FELICIDADES, USTED HA GANADO EL CONCURSO!!!!!!!!!!")
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
    else:
        respuesta5=input("Elija la opción correcta para la Pregunta 5:\n¿Cuál es el aeropuerto más transitado del mundo?\n A. Aerpuerto de Guangzhou\n B. Aeropuerto de Atlanta\n C. Aeropuerto de Estambul\n D. Aeropuerto de Madrid\n")
        if respuesta5 == 'A':
            puntaje=50
            print ("La respuesta es correcta y su puntaje es:", puntaje)
            print ("FELICIDADES, USTED HA GANADO EL CONCURSO!!!!!!!!!!")
        else:
            print ("La respuesta es incorrecta, gracias por participar")
            quit()
else:
    print ("Gracias por participar y se lleva un puntaje de 16")
    

