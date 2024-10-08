import ctypes
import winreg
from colorama import init, Fore

init(autoreset=True)
RED = Fore.RED
MAGENTA = Fore.MAGENTA
GREEN = Fore.GREEN
BLUE = Fore.CYAN

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False 
   
def main():
    
    #check if user is administrator or not
    if not is_admin():
        print(f"{RED}Run script as administrator.")
        return
        
    #define registry path and name
    regPath = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
    valName = "WriteProtect"
        
    #user menu
    print(f"{BLUE}-------------------------------------------------\n")
    print("\t\tWRITE BLOCKER")
    print(f"{BLUE}\n1. Enable Write Protection")
    print(f"{BLUE}2. Disable Write Protection")
    choice = input(f"{BLUE}\nEnter an option (1 or 2): ")
    
    while(choice!='1' and choice!='2'):
        choice = input(f"{RED}\nInvalid Choice! Enter an option (1 or 2): ")

    #set/reset write protection 
    print(f"{BLUE}\n-------------------------------------------------\n")
    
    try:
        reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regPath, 0, winreg.KEY_SET_VALUE)   #open registry editor
        
        if choice=='1':
            winreg.SetValueEx(reg, valName, 0, winreg.REG_DWORD, 1) #set write protect
            print(f"{GREEN}\tWRITE PROTECTION: ON.")
        elif choice=='2':
            winreg.SetValueEx(reg, valName, 0, winreg.REG_DWORD, 0) #remove write protect
            print(f"{MAGENTA}\tWRITE PROTECTION: OFF.")
            
        winreg.CloseKey(reg)    #close registry editor
    except PermissionError:
        print(f"{RED}Permission denied. Run script as administrator.")
    except Exception as ex:
        print(f"{RED}An error occured! {ex}")
        
    print(f"{BLUE}\n-------------------------------------------------")
    
    #done :)
if __name__ == "__main__":
    main()