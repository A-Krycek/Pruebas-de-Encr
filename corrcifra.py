mensaje = "hola mundo"
clave = "python"

encriptado = ""
for i in range(len(mensaje)):
    encriptado += chr(ord(mensaje[i]) ^ ord(clave[i % len(clave)]))

print("Texto encriptado:", encriptado)

desencriptado = ""
for i in range(len(encriptado)):
    desencriptado += chr(ord(encriptado[i]) ^ ord(clave[i % len(clave)]))

print("Texto desencriptado:", desencriptado)
