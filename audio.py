from gtts import gTTS

texto = "Hola, este es mi texto de prueba"
lenguaje = 'es'

audio = gTTS(text = texto, lang = lenguaje, slow = False)
audio.save('audio.mp3')

print("Proceso Terminado")