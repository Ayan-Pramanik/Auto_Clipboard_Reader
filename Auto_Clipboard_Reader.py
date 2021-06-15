import time
import pyperclip
import keyboard
from selenium import webdriver
from selenium.webdriver.common import proxy
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type',1)
profile.set_preference('network.proxy.http',"127.0.0.1")
profile.set_preference('network.proxy.http_port',8080)
profile.update_preferences()
driver = webdriver.Firefox(proxy=profile,firefox_profile=profile,executable_path="C:\Program Files (x86)\geckodriver.exe")
while keyboard.is_pressed('q') == False:   
    if(pyperclip.paste()=='0'):
        continue
    else:
        driver.close()
        driver = webdriver.Firefox(proxy=profile,firefox_profile=profile,executable_path="C:\Program Files (x86)\geckodriver.exe")
        driver.get(pyperclip.paste())
        pyperclip.copy('0')
