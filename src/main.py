import os
import requests
from rich.console import Console

console = Console()

def main():
    console.print("Welcome! This Program aims to help you easily remove the Roblox Beta Client and restore the old Client.", style="bold")
    print("Made by Cy#0730.")
    console.print("This Project is Licensed under: GNU GENERAL PUBLIC LICENSE\nhttps://github.com/CyOfficial/RobloxBetaClientRemover/blob/main/LICENSE\n\n", style="underline yellow")

    console.print("This Program [underline]will modify[/] your current Roblox Installation. Would you like to continue?", style="yellow")
    consent = input("Y/N: ")
    if consent.lower() != "y":
        return console.print("User has decided to not proceed, Closing", style="bold red")

    console.print("Starting!", style="bold green")

    console.print("[INFO] Fetching current Roblox Version", style="blue")
    version = requests.get("http://setup.roblox.com/version")

    if version.status_code != 200:
        return console.print("Failed to fetch current Roblox Version!", style="bold red")

    console.print("[INFO] Current Roblox Version: " + version.text, style="blue")

    version_path = "C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Roblox\\Versions\\" + version.text
    launcher_path = version_path + "\\RobloxPlayerLauncher.exe"
    client_path = version_path + "\\RobloxPlayerBeta.exe"

    if os.path.exists(version_path) != True:
        return console.print("Failed to find the Roblox Folder!", style="bold red")

    if os.path.exists(launcher_path) != True:
        return console.print("Failed to find the Roblox Launcher!", style="bold red")

    if os.path.exists(client_path) != True:
        console.print("[INFO] Failed to find the Roblox Client, moving on.", style="bold blue")
    else:
        console.print("[INFO] Removing the Beta Client", style="blue")
        os.remove(client_path)

    console.print("[INFO] This Program will run the Roblox Launcher as an Administrator. If asked by UAC, please click \"Yes\" so the Launcher runs correctly.", style="bold blue")
    input("Please press any Key to continue.")

    os.system(r'''Powershell -Command "& { Start-Process \"''' + launcher_path + r'''\"-Verb RunAs } " ''')

    console.print("If the Launcher Opened correctly and finished Installing, this Program has succeeded to remove the Beta Client and restore the old Client.\nThank you for using this program!", style="bold green")

main()