import socket

def send_email():
    smtp_server = input("SMTP server (ej: smtp.gmail.com): ")
    smtp_port = 1025

    sender = input("Remitente: ")
    recipient = input("Destinatario: ")
    subject = input("Asunto: ")
    message = input("Mensaje: ")

    data = f"Subject: {subject}\r\nTo: {recipient}\r\nFrom: {sender}\r\n\r\n{message}\r\n.\r\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((smtp_server, smtp_port))

    def recv():
        print(s.recv(1024).decode())

    def send(cmd):
        print(f"> {cmd}")
        s.send((cmd + "\r\n").encode())

    recv()
    send(f"HELO localhost")
    recv()
    send(f"MAIL FROM:<{sender}>")
    recv()
    send(f"RCPT TO:<{recipient}>")
    recv()
    send("DATA")
    recv()
    s.send(data.encode())
    recv()
    send("QUIT")
    recv()
    s.close()

send_email()