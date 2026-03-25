import os

def buscar_usuario():
    # El usuario ingresa un dato
    nombre = input("Introduce el nombre de usuario: ")
    
    # ¡PELIGRO! Concatenar la entrada directamente en un comando de shell
    # Si el usuario escribe: "admin; rm -rf /", borraría archivos.
    os.system("ls /home/" + nombre)

def login_inseguro():
    # Otro error común: Contraseñas escritas directamente en el código
    password = "admin_password_123"
    print("Iniciando sesión...")

buscar_usuario()