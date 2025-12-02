
# Directorio raíz donde buscar los archivos
directorio_base = "Archivos"
import win32com.client as win32
import os
from cryptography.fernet import Fernet



def cargar_clave(ruta="clave.key"):
    with open(ruta, "rb") as f:
        return f.read()



def descifrar_archivo(archivo_cifrado, archivo_salida, key):
    cipher = Fernet(key)

    # Leer contenido cifrado
    with open(archivo_cifrado, "rb") as f:
        encrypted_data = f.read()

    # Descifrar
    decrypted_data = cipher.decrypt(encrypted_data)

    # Guardar archivo original
    with open(archivo_salida, "wb") as f:
        f.write(decrypted_data)

    print(f"Archivo descifrado: {archivo_salida}")
        


key=cargar_clave()
descifrar_archivo("Instructivo_Escalamiento_14.docx.1pj9p3EEul", "Instructivo_Escalamiento_14.docx", key)
print("¡Proceso completado!")

