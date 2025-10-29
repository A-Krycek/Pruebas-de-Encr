mensaje = "hola mundo"
clave = "python"
encriptado = ""
for i, c in enumerate(mensaje):
    encriptado += chr(ord(c) ^ ord(clave[i % len(clave)]))
print("Texto encriptado:", encriptado)
desencriptado = ""
for i, c in enumerate(encriptado):
    desencriptado += chr(ord(c) ^ ord(clave[i % len(clave)]))
print("Texto desencriptado:", desencriptado)
