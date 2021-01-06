# Stream Point Bot v0.1
# Made by Erv
import time
import os
from selenium import webdriver, common
import Selenium2Library
from colorama import Fore, Back, Style
import ctypes
import yaml
from urllib.request import urlopen

ctypes.windll.kernel32.SetConsoleTitleW("SPB - V1 - By Erv")

status = Fore.RED + "Disabled" + Style.RESET_ALL
channel = Fore.RED + "N/A" + Style.RESET_ALL
points = Fore.RED + "N/A" + Style.RESET_ALL

def header():
    os.system('cls')
    print(Style.RESET_ALL + "   ▄████████    ▄███████▄ ▀█████████▄  ")
    print("  ███    ███   ███    ███   ███    ███ ")
    print("  ███    █▀    ███    ███   ███    ███ ")
    print("  ███          ███    ███  ▄███▄▄▄██▀  ")
    print("▀███████████ ▀█████████▀  ▀▀███▀▀▀██▄  ")
    print("         ███   ███          ███    ██▄ ")
    print("   ▄█    ███   ███          ███    ███ ")
    print(" ▄████████▀   ▄████▀      ▄█████████▀  ")
    print(Style.RESET_ALL + "────────────────────────────────────────")
    print("Stream Points Bot: " + status)
    print(Style.RESET_ALL + "Channel: " + Fore.GREEN + channel + Style.RESET_ALL  + " Points: " + Fore.GREEN + points + Style.RESET_ALL)
    print("────────────────────────────────────────")

header()
print(Fore.GREEN + "Starting stream point bot...")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging
options.add_argument('--disable-extensions')
options.add_argument('--profile-directory=Default')
options.add_argument("--incognito")
options.add_argument("--disable-plugins-discovery");
# options.add_argument("--headless") # Turns Chrome into headless browser
options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=options)
driver.set_window_position(-10000, 0)
driver.set_window_size(1280, 720)
#driver.set_window_position(200, 0)

def bot():
    url = "https://www.twitch.tv/" + channel
    driver.get(url)
    login = False
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#login-username").send_keys(username)
        driver.find_element_by_css_selector("#password-input").send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button").click()
        time.sleep(5)
        try:
            captcha = driver.find_element_by_css_selector("body > div.ReactModalPortal > div > div > div > div > div > div.modal__close-button > button > span > div > div > div > svg")
            driver.set_window_position(200, 0)
            input("Finish Captcha and enter any key here...")
        except:
            pass
        driver.set_window_position(-10000, 0)
        time.sleep(5)
        try:
            verifycd = driver.find_element_by_css_selector("body > div.ReactModalPortal > div > div > div > div > div > div.tw-border-radius-medium.tw-flex.tw-overflow-hidden > div > div > div.tw-mg-b-1 > div:nth-child(2) > div > div:nth-child(1) > div > input")
            code = input("Enter verification code: ")
            verifycd.send_keys(code)
            login = True
        except:
            pass
    except:
        print("Login Error")
    while login:
        try:
            try:
                driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div/div/button/span").click()
            except:
                pass
            global status
            status = Fore.GREEN + "Enabled" + Style.RESET_ALL
            global points
            points = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/section/div/div[5]/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/button/div/div/div/div[2]/span").text
            header()
        except:
            pass
        time.sleep(10)
    else:
        pass

def start():
    header()
    global channel
    channel = input("Channel Name: ")
    print("Gathering credentials from config file...")
    with open('config.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        global username
        username = data["username"]
        global password
        password = data["password"]
    bot()


if __name__ == '__main__':
    start()
