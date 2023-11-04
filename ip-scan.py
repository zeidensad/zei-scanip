import socket
import ipaddress
from colorama import Fore, Style, init

init()

def is_valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

def port_scan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((host, port))
        print(f"Le port {port} est ouvert", Fore.GREEN, "[OPEN]", Style.RESET_ALL)
    except:
        print(f"Le port {port} est fermé", Fore.RED, "[CLOSED]", Style.RESET_ALL)
    finally:
        s.close()


print("""
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄    ▄    ▄▄▄ ▄▄▄▄▄▄▄ 
█       █       █      █  █  █ █  █   █       █
█  ▄▄▄▄▄█       █  ▄   █   █▄█ █  █   █    ▄  █
█ █▄▄▄▄▄█     ▄▄█ █▄█  █       █  █   █   █▄█ █
█▄▄▄▄▄  █    █  █      █  ▄    █  █   █    ▄▄▄█
 ▄▄▄▄▄█ █    █▄▄█  ▄   █ █ █   █  █   █   █    
█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█ █▄▄█▄█  █▄▄█  █▄▄▄█▄▄▄█    
	""")

print("\033[1;37mAuthor : Zeiden.web\033[0m / \033[1;31myoutube : \033[4;31mhttps://www.youtube.com/@zeidenweb\033[0m / \033[1;34mdiscord : \033[4;34mzeiden.web\033[0m")


target_host = input("Entrez l'adresse IP du site web à scanner: ")

if not is_valid_ip(target_host):
    print(Fore.RED, "Adresse IP invalide", Style.RESET_ALL)
    exit()

target_ports = range(1, 1025)

option = input("Entrez '1' pour scanner les ports, ou '2' pour avoir mes info de contacte : ")

if option == "1":
    for port in target_ports:
        port_scan(target_host, port)
elif option == "2":
    print(f"{Fore.CYAN}\n{'-'*50}\nInformations\n{'-'*50}{Style.RESET_ALL}\n")
    print("Voici mon Youtube : https://youtube.com/@zeidensad4923")
    print("Voici mon Discord : https://discord.gg/")
else:
    print("Option invalide. Veuillez entrer '1' ou '2'.")
