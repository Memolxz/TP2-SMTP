# Implementacion SMTP con socket y MailHog

Este script implementa una conexión SMTP simple utilizando sockets en Python. Sirve para enviar correos de prueba localmente usando MailHog como servidor SMTP local.

El script abre una conexión TCP con el servidor SMTP local (MailHog). Después, envia los comandos SMTP correspondientes (HELO, MAIL FROM, RCPT TO, DATA, etc.) y envía el mensaje.


# Requisitos
* Python 3.x

* MailHog (para simular el servidor SMTP)

# Instrucciones de uso
## 1. Instalar MailHog
### En Linux
```
sudo apt-get -y install golang-go
```
Asegurarse de que la version instalada de go sea >= 1.23.0
```
go install github.com/mailhog/MailHog@latest
```
Esto instala MailHog en tu $GOPATH/bin (normalmente ~/go/bin).

## 2. Ejecutar MailHog
Desde la terminal correr:

```
~/go/bin/MailHog
```
Esto iniciará un servidor SMTP en localhost puerto 1025

Y tambien una interfaz web para visualizar los correos enviados en http://localhost:8025

## 3. Ejecutar el script SMTP
Ejecutar el script:

```
python3 smtp.py
```
Ingresar los datos pedidos por la consola:

* SMTP server: localhost

* Remitente: [dirección de correo]

* Destinatario: [dirección de correo]

* Asunto: [el asunto]

* Mensaje: [el cuerpo del mensaje]

Al terminar presionar enter y se enviará el correo.

## 4. Ver el mensaje enviado
Ver el mensaje enviado en http://localhost:8025

Ahí se puede ver los mensajes que se enviaron desde el script.
(Se resetea cada vez que se cierra el servidor)