#importamos las librerías

import os
import ftplib
from datetime import datetime
import zipfile
import smtplib
from email.mime.text import MIMEText

#añadimos el servidor
servidor_ftp = "ftp.com"
usuario = "usuario"
contraseña = "contraseña"

#comprimimos el directorio public_html
dir_local = "/var/www/html/public_html"

#copia de seguridad
now = datetime.now()
copia_seguridad = f"backup{now.year}{now.month:02d}{now.day:02d}.zip"

# Comprimir el directorio
with zipfile.ZipFile(, 'w') as backup_zip:
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            backup_zip.write(os.path.join(root, file))

#conexion al servidor FTP
ftp = ftplib.FTP(ftp_server)
ftp.login(ftp_usuario, ftp_contraseña)

#eliminar copias de seguridad antiguas
backups = ftp.nlst()
if len(backups) > 10:
    backups.sort(key=lambda x: os.path.getmtime(x))
    oldest_backup = backups[0]
    ftp.delete(oldest_backup)

# Cerrar la conexión FTP
ftp.quit()

# Borrar el archivo de copia de seguridad local
os.remove(backup_name)

#correo de confirmacion
gmail = "copia@ejemplo.com"
receiver_email = "aalcauce317@ieszaidinvergeles.org"
contraseña = "contraseña"
mensaje = MIMEText("Copia realizada con éxito.")
mensaje["Subject"] = "Copia de seguridad completada"
