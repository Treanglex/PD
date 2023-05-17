from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import colorama
from colorama import Fore,Back,Style
import time
os.system("cls")
print("""

$$$$$$$\  $$$$$$$\  
$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ |  $$ |
$$$$$$$  |$$ |  $$ |
$$  ____/ $$ |  $$ |
$$ |      $$ |  $$ |
$$ |      $$$$$$$  |
\__|      \_______/  

""")
print("Payload Deneme 2023 @fatih.css")
time.sleep(0.1)
url   = input("URL GİR : ")
css = input("İNPUT NAME : ")
driver   = webdriver.Chrome()
time.sleep(1)
wl = open("Payload/SqlPayload.txt","r")
for i in wl:
    gidenurl = driver.get(url)
    gidencss = driver.find_element(By.CSS_SELECTOR, css)
    satır = wl.readline()
    gidencss.send_keys(satır)
    kaynakkodu = driver.page_source
    
    if satır in kaynakkodu:
        a = print(Fore.GREEN + "[İNFO] BAŞARILI AÇIK BULUNDU : ",satır)
        # with open("Bulunan/warning.txt","a") as acik:
            # acik.write("URL : ",url,"-----", a )
    else:
        print(Fore.GREEN + "[İNFO]" + Fore.RED +" BAŞARISIZ BULUNMADI : ",satır)
time.sleep(5)
