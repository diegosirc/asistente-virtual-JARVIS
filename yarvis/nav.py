import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

def speak(text):
    # Sintetizar y reproducir el texto
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    # Inicializar el reconocimiento de voz
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustar para el ruido ambiente
        audio = recognizer.listen(source)

    try:
        # Reconocer el texto hablado
        query = recognizer.recognize_google(audio, language='es-ES')
        print("Usuario:", query)
        return query.lower()  # Convertir a minúsculas para facilitar la comparación
    except sr.UnknownValueError:
        # En caso de no entender la consulta, esperar a la próxima orden
        return ""
    except sr.RequestError:
        speak("Lo siento, señor Navarro, estoy teniendo problemas para conectarme al servicio de reconocimiento de voz.")
        return ""

def is_url(text):
    # Verificar si el texto parece ser una URL
    return "http://" in text or "https://" in text

# Saludo inicial
speak("Hola señor Navarro")

# Esperar comando del usuario
while True:
    # Escuchar y reconocer el comando del usuario
    command = recognize_speech()

    # Procesar el comando indicado
    #if "jarvis" in command:
    if "hola jarvis" in command:
            speak("Hola Señor Navarro. ¿En qué puedo ayudarlo?")
    elif "jarvis abre una página web" in command:
            speak("¿Qué página web quieres abrir, señor?")
            website = recognize_speech()
            if is_url(website):
                webbrowser.open(website)
                speak("OK, Señor Navarro. Aquí tiene la página abierta.")
            else:
                speak("Lo siento, Señor Navarro. No parece ser una URL válida.")
    elif "jarvis abre youtube" in command:
            speak("¿Qué vídeo desea reproducir en YouTube?")
            song_query = recognize_speech()
            youtube_url = "https://www.youtube.com/results?search_query=" + "+".join(song_query.split())
            webbrowser.open(youtube_url)
            speak("OK, Señor Navarro. Aquí tiene los resultados de su búsqueda en YouTube.")
    elif "abre bloc de notas" in command:
            os.system("notepad.exe")
            speak("OK, Señor Navarro. El Bloc de notas ha sido abierto.")
    elif "jarvis abre un programa" in command:
            speak("¿Qué programa desea abrir, señor?")
            program = recognize_speech()
            os.startfile(program)
            speak("OK, Señor Navarro. El programa ha sido abierto.")
    elif "jarvis adiós " in command:
            speak("Hasta luego, Señor Navarro.")
            break
    else:
        # Si no se menciona "JARVIS", repetir el bucle de espera
        speak("Lo siento, Señor Navarro. No he entendido su consulta.")
