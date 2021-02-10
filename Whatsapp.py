import pywhatkit as wt
try:
	wt.sendwhatmsg("+52NumeroCelular", "Hello world", 16,23)
	#Hora, Minuto
	print("Successfully sent!")
except:
	print("An unexpected error!")
