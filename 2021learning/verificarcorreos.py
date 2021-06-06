def verificarcorreo(gmail):
    if gmail.split('@')[1] == 'gmail.com' and gmail.count('@')==1:
        print("Email correcto")
        print(gmail)
        return 1
    else:
        print("Email incorrecto")
        return 0

correo=input('Introduce el gmail ')
verificarcorreo(correo)
