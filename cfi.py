import requests

import datetime
import time
from colorama import init, Fore, Style
import sys
import os
init(autoreset=True)


def print_welcome_message():
    print(r"""
      _______
    /        /|
   /        / |
  /________/  |
 |        |   |
 | CuDem  |  /
 |        | /
 ---------
""")

    print(Fore.GREEN + Style.BRIGHT + "Cyberfinance BOT")
    print(Fore.GREEN + Style.BRIGHT + "Tool phat trien boi Airdrop Cu Dem by @Bido1102")
    print(Fore.GREEN + Style.BRIGHT + "Tham gia Telegram Channel: https://t.me/Muafbclone")
    print(Fore.GREEN + Style.BRIGHT + "Donate :) 087 668 0001 MOMO / Zalopay / HD Bank")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def fetch_access_token(init_data):
    url = "https://api.cyberfin.xyz/api/v1/game/initdata"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://g.cyberfin.xyz',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'
    }
    data = f'{{"initData":"{init_data}"}}'
    response = requests.post(url, headers=headers, data=data)
    # print(response.json())
    if response.status_code == 201:
        return response.json()['message']['accessToken']
    else:
        print("Failed to fetch access token")
        return None

def read_tokens():
    with open('initdata.txt', 'r') as file:
        return [line.strip() for line in file if line.strip()]

def info_balance(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/game/mining/gamedata"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}', 
        'dnt': '1',
        'if-none-match': 'W/"173-kqxt3jfCFv2BCBRPJM7mhgWVfbI"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    crack_time = data['message']['miningData']['crackTime']
    now = datetime.datetime.now().timestamp()
    countdown = crack_time - now
    hours, remainder = divmod(countdown, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(f"{Fore.BLUE+Style.BRIGHT}[ Cracking ]:", f"{Fore.BLUE+Style.BRIGHT}{int(hours):02} gio {int(minutes):02} phut", f"{Fore.BLUE+Style.BRIGHT}se tiep tuc claim")

def claim_mining(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/mining/claim"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  
        'dnt': '1',
        'if-none-match': 'W/"173-kqxt3jfCFv2BCBRPJM7mhgWVfbI"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print(f"{Fore.YELLOW+Style.BRIGHT}[ Claim ]: {data['message']}")

def auto_upgrade_hammer(ini_token, max_level):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/apply"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    data = '{"boostType":"HAMMER"}'
    while True:

        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 201:
            sys.stdout.write(f"{Fore.RED+Style.BRIGHT}[ Hammer ]: Saldo tidak cukup\n")
            break
        response_data = response.json()
        current_level = response_data['message']['boostData']['hammerLevel']
        sys.stdout.write(f"\r{Fore.GREEN+Style.BRIGHT}[ Hammer ] Nang cap thanh cong. Level: {current_level}")
        if current_level >= max_level:
            sys.stdout.write(f"\n{Fore.GREEN+Style.BRIGHT}[ Hammer ] Cap do hien tai {current_level}\n")
            break
       

def auto_upgrade_egg(ini_token, max_level):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/apply"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    data = '{"boostType":"EGG"}'
    while True:
        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 201:
            sys.stdout.write(f"{Fore.RED+Style.BRIGHT}[ Egg Level ]: So du khong du\n")
            break
        response_data = response.json()
        current_level = response_data['message']['boostData']['eggLevel']
        sys.stdout.write(f"\r{Fore.GREEN+Style.BRIGHT}[ Egg Level ] Nang cap thanh cong. Level: {current_level}")
        if current_level >= max_level:
            sys.stdout.write(f"\n{Fore.GREEN+Style.BRIGHT}[ Egg Level ] Cap do hien tai {current_level}\n")
            break

def fetch_uuids(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/gametask/all"
    headers = {
        'Authorization': f'Bearer {ini_token}',  
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'dnt': '1',
        'if-none-match': 'W/"173-kqxt3jfCFv2BCBRPJM7mhgWVfbI"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    # print(response.json())
    if response.status_code == 200:
        tasks = response.json()['message']
        return [(task['uuid'], task['description']) for task in tasks if not task['isCompleted']]
    else:
        print("Failed to fetch tasks")
        return []

def complete_tasks(uuids, ini_token):
    base_url = "https://api.cyberfin.xyz/api/v1/gametask/complete/"
    headers = {
        'Authorization': f'Bearer {ini_token}',  
        'Content-Type': 'application/json'
    }
    for uuid, description in uuids:
        response = requests.patch(f"{base_url}{uuid}", headers=headers)
        response_data = response.json()

        if response.status_code == 200:    
            print(f"{Fore.GREEN+Style.BRIGHT}[ Task ]: {description} Completed")
        else:
            print(f"{Fore.RED+Style.BRIGHT}[ Task ]: {description} Gagal. {response_data['message']}")

def user_level(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/mining/boost/info"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'authorization': f'Bearer {ini_token}',  
        'dnt': '1',
        'if-none-match': 'W/"a4-LZ8zXP3aEql/rLf1iujkfLlL6Tk"',
        'origin': 'https://g.cyberfin.xyz',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['message']
        return data
    else:
        print(f"{Fore.RED+Style.BRIGHT}[ Gagal mendapatkan informasi level pengguna ]")

def get_mining_info(ini_token):
    url = "https://api.cyberfin.xyz/api/v1/game/mining/gamedata"
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {ini_token}',
        'cache-control': 'no-cache',
        'origin': 'https://g.cyberfin.xyz',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://g.cyberfin.xyz/',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126", "Microsoft Edge WebView2";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'secret-key': 'cyberfinance',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['message']
        balance = int(data['userData']['balance'])
        mining_rate = data['miningData']['miningRate']
       
        now = datetime.datetime.now().timestamp()
     
        print(f"{Fore.YELLOW+Style.BRIGHT}[ Balance ]: {balance:,}")
        print(f"{Fore.YELLOW+Style.BRIGHT}[ Minning Rate ]: {mining_rate}")
     
    else:
        print(f"{Fore.RED+Style.BRIGHT}[ Khong the lay duoc thong tin khai thac ]")

def main():
    print_welcome_message()
    user_input_task = input("Tu dong hoan thanh nhiem vu ? (y / n) : ")
    user_input_hammer = input("Tu dong nang cap bua ( Cracking Power ) ? (y / n) : ")
    if user_input_hammer == 'y':
        max_hammer_level = int(input("Cap do nang cap toi da? : "))
    
    user_input_egg = input("Tu dong nang cap trung? (y / n) : ")
    if user_input_egg == 'y':
        max_egg_level = int(input("Cap do nang cap toi da? : "))
 
    clear_console()
    while True:
        print_welcome_message()
        tokens = read_tokens()  
        for index, init_data in enumerate(tokens):
            ini_token = fetch_access_token(init_data)
            if not ini_token:
                continue
            print(f"{Fore.CYAN+Style.BRIGHT}============== [ Tai khoan so - {index + 1} ] ==============")  
            get_mining_info(ini_token)  
            datauser = user_level(ini_token)
            if datauser:
                level_hammer = int(datauser['hammerLevel'])
                level_egg = int(datauser['eggLevel'])
                print(f"{Fore.BLUE+Style.BRIGHT}[ Egg Level ]: {level_hammer}")
                print(f"{Fore.BLUE+Style.BRIGHT}[ Hammer Level ]: {level_egg}")
                if user_input_hammer.lower() == 'y':
                    if level_hammer >= max_hammer_level:
                        print(f"{Fore.RED+Style.BRIGHT}[ Hammer Level ]: Da o cap do {level_hammer} ")
                    else:
                        auto_upgrade_hammer(ini_token, max_hammer_level)
                if user_input_egg.lower() == 'y':
                    if level_egg >= max_egg_level:
                        print(f"{Fore.RED+Style.BRIGHT}[ Egg Level ]: Da o cap do {level_egg} ")
                    else:
                        auto_upgrade_egg(ini_token, max_egg_level)
            if user_input_task.lower() == 'y':
                uuids = fetch_uuids(ini_token)
                complete_tasks(uuids, ini_token)
          

            info_balance(ini_token)
            claim_mining(ini_token)
        for i in range(3600, 0, -1):
            sys.stdout.write(f"\r{Fore.CYAN+Style.BRIGHT}============ Xong, vui long cho {i} giay.. ============")
            sys.stdout.flush()
            time.sleep(1)
        print()  # Cetak baris baru setelah hitungan mundur selesai

        # Membersihkan konsol setelah hitungan mundur
        clear_console()
        time.sleep(5)  # Delay 5 detik sebelum memulai lagi

if __name__ == "__main__":
    main()
