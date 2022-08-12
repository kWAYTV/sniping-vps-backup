# Sniping VPS Backup Script
# kwayservices.top

# ---- IMPORTS ----
import os, paramiko, time, pystyle, dhooks
from pystyle import Colors, Colorate, Center
from dhooks import Webhook

# ---- VARIABLES ----
global works
vps_1_ip = "" # Fill it with the vps 1 ip.
vps_2_ip = "" # Fill it with the vps 2 ip.
vps_3_ip = ""  # Fill it with the vps 3 ip.
vps_1_user = "" # Fill it with the vps 1 user.
vps_2_user = "" # Fill it with the vps 2 user.
vps_3_user = "" # Fill it with the vps 3 user.
vps_1_pass = "" # Fill it with the vps 1 user.
vps_2_pass = "" # Fill it with the vps 2 pass.
vps_3_pass = "" # Fill it with the vps 3 pass.
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this.
scriptDir = os.getcwd() # Get the script directory , don't touch this.
works = True # Don't touch this.
repeatBackup = 3600 # How many seconds between each backup, default is 3600 (1 hour).
mode = "" # Don't touch this.
hook = Webhook('URL HERE') # Change this to your URL.

# ---- MAIN ----
logo = """

██╗░░░██╗██████╗░░██████╗  ██████╗░░█████╗░░█████╗░██╗░░██╗██╗░░░██╗██████╗░
██║░░░██║██╔══██╗██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║░░░██║██╔══██╗
╚██╗░██╔╝██████╔╝╚█████╗░  ██████╦╝███████║██║░░╚═╝█████═╝░██║░░░██║██████╔╝
░╚████╔╝░██╔═══╝░░╚═══██╗  ██╔══██╗██╔══██║██║░░██╗██╔═██╗░██║░░░██║██╔═══╝░
░░╚██╔╝░░██║░░░░░██████╔╝  ██████╦╝██║░░██║╚█████╔╝██║░╚██╗╚██████╔╝██║░░░░░
░░░╚═╝░░░╚═╝░░░░░╚═════╝░  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░"""

def printLogo():
    print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, logo, 1)))

def backupTkns():
    try:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, "Starting backup of vps 1 tokens...", 1)))
        hook.send(" **[VPS-BACKUP]** Starting backup of `vps 1` tokens...")
        vps1 = paramiko.SSHClient()
        vps1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        vps1Transport = paramiko.Transport((vps_1_ip, 22))
        vps1Transport.connect(username=vps_1_user, password=vps_1_pass)
        vps1SFTP = paramiko.SFTPClient.from_transport(vps1Transport)
        vps1SFTP.get('/root/tokens.txt', f'{scriptDir}/tokens/tokens1.txt')
        vps1SFTP.close()
        vps1Transport.close()
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "Backup of vps 1 tokens completed!", 1)))
        hook.send(" **[VPS-BACKUP]** Backup of `vps 1` tokens completed!")
    except Exception as e:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "Failed! Error: " + str(e), 1)))
        hook.send(" **[VPS-BACKUP]** Failed! `Error`: " + str(e))
        pass

    try:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, "Starting backup of vps 2 tokens...", 1)))
        hook.send(" **[VPS-BACKUP]** Starting backup of `vps 2` tokens...")
        vps2 = paramiko.SSHClient()
        vps2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        vps2Transport = paramiko.Transport((vps_2_ip, 22))
        vps2Transport.connect(username=vps_2_user, password=vps_2_pass)
        vps2SFTP = paramiko.SFTPClient.from_transport(vps2Transport)
        vps2SFTP.get('/root/tokens.txt', f'{scriptDir}/tokens/tokens2.txt')
        vps2SFTP.close()
        vps2Transport.close()
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "Backup of vps 2 tokens completed!", 1)))
        hook.send(" **[VPS-BACKUP]** Backup of `vps 2` tokens completed!")
    except Exception as e:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "Failed! Error: " + str(e), 1)))
        hook.send(" **[VPS-BACKUP]** Failed! `Error`: " + str(e))
        pass

    try:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, "Starting backup of vps 3 tokens...", 1)))
        hook.send(" **[VPS-BACKUP]** Starting backup of `vps 3` tokens...")
        vps3 = paramiko.SSHClient()
        vps3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        vps3Transport = paramiko.Transport((vps_3_ip, 22))
        vps3Transport.connect(username=vps_3_user, password=vps_3_pass)
        vps3SFTP = paramiko.SFTPClient.from_transport(vps3Transport)
        vps3SFTP.get('/root/tokens.txt', f'{scriptDir}/tokens/tokens3.txt')
        vps3SFTP.close()
        vps3Transport.close()
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "Backup of vps 3 tokens completed!", 1)))
        hook.send(" **[VPS-BACKUP]** Backup of `vps 3` tokens completed!")
    except Exception as e:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "Failed! Error: " + str(e), 1)))
        hook.send(" **[VPS-BACKUP]** Failed! `Error`: " + str(e))
        pass

def backupInvs():
    try:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, "Starting backup of vps 1 invites...", 1)))
        hook.send(" **[VPS-BACKUP]** Starting backup of `vps 1` invites...")
        vps1 = paramiko.SSHClient()
        vps1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        vps1Transport = paramiko.Transport((vps_1_ip, 22))
        vps1Transport.connect(username=vps_1_user, password=vps_1_pass)
        vps1SFTP = paramiko.SFTPClient.from_transport(vps1Transport)
        vps1SFTP.get('/root/invites.txt', f'{scriptDir}/invites/invites1.txt')
        vps1SFTP.close()
        vps1Transport.close()
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "Backup of vps 1 invites completed!", 1)))
        hook.send(" **[VPS-BACKUP]** Backup of `vps 1` invites completed!")
    except Exception as e:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "Failed! Error: " + str(e), 1)))
        hook.send(" **[VPS-BACKUP]** Failed! `Error`: " + str(e))
        pass

    try:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, "Starting backup of vps 2 invites...", 1)))
        hook.send(" **[VPS-BACKUP]** Starting backup of `vps 2` invites...")
        vps2 = paramiko.SSHClient()
        vps2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        vps2Transport = paramiko.Transport((vps_2_ip, 22))
        vps2Transport.connect(username=vps_2_user, password=vps_2_pass)
        vps2SFTP = paramiko.SFTPClient.from_transport(vps2Transport)
        vps2SFTP.get('/root/invites.txt', f'{scriptDir}/invites/invites2.txt')
        vps2SFTP.close()
        vps2Transport.close()
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "Backup of vps 2 invites completed!", 1)))
        hook.send(" **[VPS-BACKUP]** Backup of `vps 2` invites completed!")
    except Exception as e:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "Failed! Error: " + str(e), 1)))
        hook.send(" **[VPS-BACKUP]** Failed! `Error`: " + str(e))
        pass

    try:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, "Starting backup of vps 3 invites...", 1)))
        hook.send(" **[VPS-BACKUP]** Starting backup of `vps 3` invites...")
        vps3 = paramiko.SSHClient()
        vps3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        vps3Transport = paramiko.Transport((vps_3_ip, 22))
        vps3Transport.connect(username=vps_3_user, password=vps_3_pass)
        vps3SFTP = paramiko.SFTPClient.from_transport(vps3Transport)
        vps3SFTP.get('/root/invites.txt', f'{scriptDir}/invites/invites3.txt')
        vps3SFTP.close()
        vps3Transport.close()
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "Backup of vps 3 invites completed!", 1)))
        hook.send(" **[VPS-BACKUP]** Backup of `vps 3` invites completed!")
    except Exception as e:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "Failed! Error: " + str(e), 1)))
        hook.send(" **[VPS-BACKUP]** Failed! `Error`: " + str(e))
        pass

def checkFiles():
    try:
        with open(f"{scriptDir}/tokens/tokens1.txt") as t1:
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, 'There is a "tokens1.txt" txt in the tokens directory! Skipping...', 1)))
            pass
    except FileNotFoundError:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, 'There is no "tokens1.txt" txt in the tokens directory!', 1)))
        pass
    try:
        with open(f"{scriptDir}/tokens/tokens2.txt") as t1:
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, 'There is a "tokens2.txt" txt in the tokens directory! Skipping...', 1)))
            pass
    except FileNotFoundError:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, 'There is no "tokens2.txt" txt in the tokens directory!', 1)))
        pass
    try:
        with open(f"{scriptDir}/tokens/tokens3.txt") as t1:
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, 'There is a "tokens3.txt" txt in the tokens directory! Skipping...', 1)))
            pass
    except FileNotFoundError:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, 'There is no "tokens3.txt" txt in the tokens directory!', 1)))
        pass
    try:
        with open(f"{scriptDir}/invites/invites1.txt") as t1:
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, 'There is a "invites1.txt" txt in the invites directory! Skipping...', 1)))
            pass
    except FileNotFoundError:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, 'There is no "invites1.txt" txt in the invites directory!', 1)))
        pass
    try:
        with open(f"{scriptDir}/invites/invites2.txt") as t1:
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, 'There is a "invites2.txt" txt in the invites directory! Skipping...', 1)))
            pass
    except FileNotFoundError:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, 'There is no "invites2.txt" txt in the invites directory!', 1)))
        pass
    try:
        with open(f"{scriptDir}/invites/invites3.txt") as t1:
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, 'There is a "invites3.txt" txt in the invites directory! Skipping...', 1)))
            pass
    except FileNotFoundError:
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, 'There is no "invites3.txt" txt in the invites directory!', 1)))
        pass


def start():
    try:
        clear()
        printLogo()
        print("\n Checking for folders!")
        if os.path.exists("tokens"):
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "There is a tokens directory in the root directory! Skipping...", 1)))
            pass
        else:
            os.mkdir("tokens")
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "Created tokens directory in the root directory!", 1)))
        if os.path.exists("invites"):
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "There is a invites directory in the root directory! Skipping...", 1)))
            pass
        else:
            os.mkdir("invites")
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, "Created invites directory in the root directory!", 1)))
        print("\n Checking for files!")
        checkFiles()
        works = True
        mode = ""
        print("\n Tokens Backup")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, "Starting backup of tokens...", 1)))
        hook.send(" **[VPS-BACKUP]** `Starting` backup of tokens...")
        mode = "tokens"
        backupTkns()
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, "Finished backup of tokens...", 1)))
        hook.send(" **[VPS-BACKUP]** `Finished` backup of tokens...")
        print("\n Invites Backup")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, "Starting backup of invites...", 1)))
        hook.send(" **[VPS-BACKUP]** `Starting` backup of invites...")
        mode = "invites"
        backupInvs()
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_blue, "Finished backup of invites...", 1)))
        hook.send(" **[VPS-BACKUP]** `Finished` backup of invites...")
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, "\n Done!", 1)))
        hook.send(" **[VPS-BACKUP]** `Done`!")
    except Exception as e:
        print("Failed to backup " + mode + "! Error: " + str(e))
        hook.send(" **[VPS-BACKUP]** `Failed` to backup " + mode + "! Error: " + str(e))
        pass
        works = False


try:
    import os, paramiko, time, pystyle, dhooks
    print("\n Imports successful!")
    try:
        while works == True:
            start()
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, f"Sleeping for {repeatBackup} seconds and repeating.", 1)))
            hook.send(f" **[VPS-BACKUP]** `Sleeping` for `{repeatBackup}` seconds and repeating.")
            time.sleep(repeatBackup)
    except KeyboardInterrupt:
        works = False
        print("\n Exiting...")
        time.sleep(1)
        exit()
        pass
except:
    print("\n Imports failed! Trying to install...")
    z = "python -m pip install "; os.system('%sparamiko' % (z)); os.system('%spystyle' % (z)); os.system('%sos-sys' % (z)); os.system('%stime' % (z)); os.system('%sdhooks' % (z))
    print("\n Let's test!")
    try:
        while works == True:
            start()
            print(Center.XCenter(Colorate.Horizontal(Colors.white_to_red, f"Sleeping for {repeatBackup} seconds and repeating.", 1)))
            hook.send(f" **[VPS-BACKUP]** Sleeping for `{repeatBackup}` seconds and repeating.")
            time.sleep(repeatBackup)
    except KeyboardInterrupt:
        works = False
        print("\nExiting...")
        hook.send(" **[VPS-BACKUP]** `Exiting` because of *KeyboardInterrupt*!")
        time.sleep(1)
        exit()
        pass