import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import time
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_title():
    cls()
    print(r"""
  /$$$$$$  /$$      /$$ /$$$$$$$$ /$$$$$$$ 
 /$$__  $$| $$$    /$$$|__  $$__/| $$__  $$
| $$  \__/| $$$$  /$$$$   | $$   | $$  \ $$
|  $$$$$$ | $$ $$/$$ $$   | $$   | $$$$$$$/
 \____  $$| $$  $$$| $$   | $$   | $$____/ 
 /$$  \ $$| $$\  $ | $$   | $$   | $$      
|  $$$$$$/| $$ \/  | $$   | $$   | $$      
 \______/ |__/     |__/   |__/   |__/      
                                          
""")

def show_info():
    cls()
    print(r"""

.___        _____                            __  .__               
|   | _____/ ____\___________  _____ _____ _/  |_|__| ____   ____  
|   |/    \   __\/  _ \_  __ \/     \\__  \\   __\  |/  _ \ /    \ 
|   |   |  \  | (  <_> )  | \/  Y Y  \/ __ \|  | |  (  <_> )   |  \
|___|___|  /__|  \____/|__|  |__|_|  (____  /__| |__|\____/|___|  /
         \/                        \/     \/                    \/ 

                          
""")

def show_srv():
    cls()
    print(r"""


                __             _________                                
  ______ ______/  |_______    /   _____/ ______________  __ ___________ 
 /  ___//     \   __\____ \   \_____  \_/ __ \_  __ \  \/ // __ \_  __ \
 \___ \|  Y Y  \  | |  |_> >  /        \  ___/|  | \/\   /\  ___/|  | \/
/____  >__|_|  /__| |   __/  /_______  /\___  >__|    \_/  \___  >__|   
     \/      \/     |__|             \/     \/                 \/       


                                    
""")

def show_send():
    cls()
    print(r"""

  _________                  .___.__                
 /   _____/ ____   ____    __| _/|__| ____    ____  
 \_____  \_/ __ \ /    \  / __ | |  |/    \  / ___\ 
 /        \  ___/|   |  \/ /_/ | |  |   |  \/ /_/  >
/_______  /\___  >___|  /\____ | |__|___|  /\___  / 
        \/     \/     \/      \/         \//_____/  

                                       
""")

def show_ok():
    cls()
    print(r"""

  _________                                          _____     .__  .__         ._.
 /   _____/__ __   ____  ____  ____   ______ _______/ ____\_ __|  | |  | ___.__.| |
 \_____  \|  |  \_/ ___\/ ___\/ __ \ /  ___//  ___/\   __\  |  \  | |  |<   |  || |
 /        \  |  /\  \__\  \__\  ___/ \___ \ \___ \  |  | |  |  /  |_|  |_\___  | \|
/_______  /____/  \___  >___  >___  >____  >____  > |__| |____/|____/____/ ____| __
        \/            \/    \/    \/     \/     \/                       \/      \/

                                  
""")

def show_err():
    cls()
    print(r"""
 _____                       
|  ___|                      
| |__ _ __ _ __ ___  _ __    
|  __| '__| '__/ _ \| '__|   
| |__| |  | | | (_) | |      
\____/_|  |_|  \___/|_|      
                             
""")

def test_smtp(email, pwd):
    show_srv()
    
    domain = email.split('@')[-1].lower()
    servers = [
        ('smtp.office365.com', 587),
        (f'smtp.{domain}', 587),
        ('smtp-mail.outlook.com', 587),
        (f'mail.{domain}', 587),
        ('smtp.gmail.com', 587),
        ('outlook.office365.com', 587)
    ]
    
    if 'amerike.edu.mx' in domain:
        servers.insert(0, ('smtp.amerike.edu.mx', 587))
    
    print("\n[*] Detectando servidor...")
    
    for srv, port in servers:
        try:
            print(f"[*] Probando {srv}...")
            
            s = smtplib.SMTP(srv, port, timeout=5)
            s.ehlo()
            s.starttls()
            
            s.login(email, pwd)
            
            s.quit()
            print(f"[+] Successful connection!")
            time.sleep(1.5)
            return srv, port
            
        except smtplib.SMTPAuthenticationError:
            print(f"[+] Servidor correcto, contraseña incorrecta")
            time.sleep(1.5) 
            return srv, port
            
        except Exception:
            print(f"[-] Fail")
            time.sleep(0.5)
    
    print("[!] Usando servidor predeterminado")
    time.sleep(1.5) 
    return 'smtp.office365.com', 587

def send_auto():
    cls()
    print("\nSugerencias para evitar problemas con SMTP:")
    print("- Verifica tu contraseña")
    print("- Activa aplicaciones menos seguras")
    print("- Usa contraseña de aplicación si tienes 2FA")
    
    input("\n>> Presione Enter para continuar...")
    
    show_title()
    
    print("\n" + "#"*50)
    print("#            MAILING SYSTEM                      #")
    print("#              SMTP PROJECT                      #")
    print("#"*50 + "\n")

    from_email = input(">> Tu correo electrónico: ")
    
    to_email = input(">> Correo del destinatario: ")
    
    show_info()
    
    print("\n-- Datos del remitente --")
    sender_name = input(">> Nombre completo: ")
    sender_id = input(">> ID o Matricula: ")
    
    pwd = getpass.getpass(">> Password: ")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = f"SMTP PROJECT - Remitente: {sender_name}"
    body = f"""
    Datos del remitente:
    
    Nombre: {sender_name}
    ID: {sender_id}
    Correo electrónico: {from_email}

Submitted by SMTP PROJECT.                                                                                  
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    smtp_srv, port = test_smtp(from_email, pwd)
    
    show_send()
    print(f"\n[*] sending mail...")
    time.sleep(1)
    try:
        server = smtplib.SMTP(smtp_srv, port)
        server.ehlo()
        server.starttls()
        
        server.login(from_email, pwd)
        
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        
        server.quit()
        
        show_ok()
        print("\n" + "#"*50)
        print("             MAIL SENT SUCCESSFULLY!             ")
        print("#"*50)
        print(f"De: {from_email}")
        print(f"Para: {to_email}")
        print(f"Servidor: {smtp_srv}")
        print("#"*50)
        
    except Exception as e:
        show_err()
        print("\n" + "!"*50)
        print("             ERROR             ")
        print(f"{str(e)}")
        print("!"*50)
        print("\nSugerencias:")
        print("- Verifica tu contraseña")
        print("- Activa aplicaciones menos seguras")
        print("- Usa contraseña de aplicación si tienes 2FA")

if __name__ == "__main__":
    send_auto()
    input("\n>> Presione Enter para salir...")