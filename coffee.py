import requests, colorama, time, os


def _exit():
    time.sleep(5)
    exit()


def check_hook(hook):
    info = requests.get(hook).text
    if "\"message\": \"Unknown Webhook\"" in info:
        return False
    return True


def main(webhook, name, delay, amount, message, hookDeleter):
    counter = 0
    while True if amount == "inf" else counter < int(amount):
        try:
            data = requests.post(webhook, json={"content": str(message), "name": str(name), "avatar_url": "https://media.discordapp.net/attachments/1074303752963620927/1075834730597056543/89078867.png?width=935&height=701"})
            if data.status_code == 204:
                print(f"{colorama.Back.MAGENTA} {colorama.Fore.WHITE}[+] Sent{colorama.Back.RESET}")
            else:
                print(f"{colorama.Back.RED} {colorama.Fore.WHITE}[-] Fail{colorama.Back.RESET}")
        except:
            print()
        time.sleep(float(delay))
        counter += 1
    if hookDeleter.lower() == "y":
        requests.delete(webhook)
        print(f'{colorama.Fore.MAGENTA}webhook deleted')
    print(f'{colorama.Fore.GREEN}Finished...')


def initialize():
    print(f"""{colorama.Fore.MAGENTA}
                   
    
        (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    |_____________| ___
    |             |/ _ \\
    |               | | |
    |               |_| |
    |             |\___/
     \___________/
                        Coffee Spammer
                        v 1.1.2
     """)
    webhook = input("Enter ur webhook > ")
    name = input("Enter a webhook name > ")
    message = input("Enter a message > ")
    delay = input("Enter a delay > ")
    amount = input("Enter an amount [int/inf] > ")
    hookDeleter = input("Delete webhook after spam? [Y/N] > ")
    try:
        delay = float(delay)
    except ValueError:
        _exit()
    if not check_hook(webhook) or (not amount.isdigit() and amount != "inf") or (hookDeleter.lower() != "y" and hookDeleter.lower() != "n"):
        _exit()
    else:
        main(webhook, name, delay, amount, message, hookDeleter)
        _exit()



if __name__ == '__main__':
    os.system('cls')
    os.system('title @ogBoard  t.me/coffeespammer')
    colorama.init()
    initialize()



