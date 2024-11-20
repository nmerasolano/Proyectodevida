import time
import pyttsx3
# Proyecto de Vida - Datos personales
engine = pyttsx3.init()
engine.say("ingrese su nombre")
engine.runAndWait()
# Función para capturar los datos personales
def proyecto_de_vida():
    nombre = input("Ingresa tu nombre: ")
    engine.say("ingrese su grado")
    engine.runAndWait()
    grado = input("Ingresa tu grado: ")
    engine.say("ingrese su edad")
    engine.runAndWait()
    edad = input("Ingresa tu edad: ")
    engine.say("ingrese su fecha de nacimiento")
    engine.runAndWait()
    fecha_nacimiento = input("Ingresa tu fecha de nacimiento (DD/MM/AAAA): ")
    # Mostrar Proyecto de Vida
    print("\n--- Proyecto de Vida ---")
    print(f"Nombre: {nombre}")
    print(f"Grado: {grado}")
    print(f"Edad: {edad} años")
    print(f"Fecha de Nacimiento: {fecha_nacimiento}")
    
# Ejecutar la función
proyecto_de_vida()

def mostrar_dedicatoria():
    dedicatoria = [
        "Para ti, que siempre me has apoyado.",
        "Gracias por estar a mi lado en cada paso del camino.",
        "Esta dedicatoria es solo un pequeño gesto de todo lo que significas para mí.",
        "Con cariño y gratitud, siempre."
    ]
    
    for linea in dedicatoria:
        print(linea)
        time.sleep(2)  # Pausa de 2 segundos entre cada línea
mostrar_dedicatoria()
def mostrar_dedicatoria():
    dedicatoria = [
        "Para ti, que siempre me has apoyado.",
        "Gracias por estar a mi lado en cada paso del camino.",
        "Esta dedicatoria es solo un pequeño gesto de todo lo que significas para mí.",
        "Con cariño y gratitud, siempre."
    ]
    
    # Inicializar el motor de texto a voz
    engine = pyttsx3.init()
    
    for linea in dedicatoria:
        print(linea)
        #engine.say({nombre})
        engine.runAndWait()
 
        engine.say(linea)  # Leer en voz alta
        engine.runAndWait()
        time.sleep(2)  # Pausa de 2 segundos entre cada línea
    
 #   engine.stop()

mostrar_dedicatoria()

def mostrar_contenido():
    contenido = ["MI AUTOBIOGRAFIA",
                    "QUIEN SOY",
                    "COMO SOY",
                    "MIS EXPERIENCIAS ",
                    "MIS LOGROS",
                    "FODA PERSONAL",
                    "FORTALEZAS",
                    "OPORTUNIDADES",
                    "DEBILIDADES",
                    "AMENAZAS",
                    "MIS METAS",
                    "MIS SUENOS Y ANHELOS",
                    "LO QUE QUIERO SER Y HACER EN EL FUTURO ",
                    "MISION",
                    "VISION",
                    "PLAN DE VIDA",
                    "AREA FAMILIAR",
                    "AREA ACADEMICA",
                    "ACCIONES",
                    "AREA FAMILIAR",
                    "AREA ACADEMICA",
                    "CONCLUSION"]

    # Inicializar el motor de texto a voz
    #engine = pyttsx3.init()
    
    for linea1 in contenido:
        print(linea1)
        #engine.say({nombre})
        engine.runAndWait()
 
        engine.say(linea1)  # Leer en voz alta
        engine.runAndWait()
        time.sleep(2)  # Pausa de 2 segundos entre cada línea

mostrar_contenido()
engine = pyttsx3.init()

def insertar_contenido():
    engine.say("desués de hacer un autoanálisis describa quién es usted")
    engine.runAndWait()
    quien = input("desués de hacer un autoanálisis describa quién es usted? ")
    engine.say("describa su apariencia física y valores espirituales: ")
    engine.runAndWait()
    como_soy= input("describa su apariencia física y valores espirituales: ")
    engine.say("describa las vivencias más bonitas de su vida: ")
    engine.runAndWait()
    experiencias = input("describa las vivencias más bonitas de su vida: ")
    engine.say("ingrese sus logros obtenidos")
    engine.runAndWait()
    logros= input("ingrese sus logros obtenidos ")
    engine.say("ingrese sus fortalezas")
    engine.runAndWait()
    fortalezas= input("ingrese sus fortalezas ")
    
    
    # Mostrar Proyecto de Vida
    print("\n--- Proyecto de Vida ---")
    print(f"Quien soy: {quien}")
    print(f"Como soy: {como_soy}")
    print(f"Experiencias: {experiencias}")
    print(f"logros: {logros}")
    print(f"fortalezas: {fortalezas}")

    insertar_contenido()
    engine.stop()