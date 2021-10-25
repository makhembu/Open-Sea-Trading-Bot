#!pip install undetected_chromedriver
import sys, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException, NoSuchWindowException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
sys.path.insert(0, '../')
from config import *
import undetected_chromedriver as uc
from threading import Thread
import tkinter as tk
import os
import zipfile
import random
from random import randrange
import termcolor
#from typer import Typer
os.system('color')
# import time 
# from datetime import date

# os.system('tzutil /s "Hawaiian Standard Time"')
# os.system('date -s "16 SEP 2021 18:00:00"')
# os.system('time -s "22:00:00"')
# date(year=2021, month=9, day=15).isoformat()
# os.environ['TZ'] = 'Hawaiian Standard Time'
# time.tzset()



print("""
 _______   _______    ______   __    __  __      __  ______    ______  
/       \ /       \  /      \ /  |  /  |/  \    /  |/      \  /      \ 
$$$$$$$  |$$$$$$$  |/$$$$$$  |$$ |  $$ |$$  \  /$$//$$$$$$  |/$$$$$$  |
$$ |__$$ |$$ |__$$ |$$ |  $$ |$$  \/$$/  $$  \/$$/ $$ |  $$ |$$ \__$$/ 
$$    $$/ $$    $$< $$ |  $$ | $$  $$<    $$  $$/  $$ |  $$ |$$      \ 
$$$$$$$/  $$$$$$$  |$$ |  $$ |  $$$$  \    $$$$/   $$ |  $$ | $$$$$$  |
$$ |      $$ |  $$ |$$ \__$$ | $$ /$$  |    $$ |   $$ \__$$ |/  \__$$ |
$$ |      $$ |  $$ |$$    $$/ $$ |  $$ |    $$ |   $$    $$/ $$    $$/ 
$$/       $$/   $$/  $$$$$$/  $$/   $$/     $$/     $$$$$$/   $$$$$$/  
""")


proxy = ''
proxy.split(':')
#url_list = ['https://opensea.io/assets/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/1', 'https://opensea.io/assets/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/2', 'https://opensea.io/assets/0xba30e5f9bb24caa003e9f2f0497ad287fdf956233', 'https://opensea.io/assets/0xf43aaa80a8f9de69bc71aea989afceb8db7b690f/4', 'https://opensea.io/assets/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/5']
url_list = []
#link = 'https://opensea.io/assets/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/{}'
# rng1 = input("type minimum link number: ")
# rng2 = input("type maximum link number: ")
with open('urls.txt', 'r') as fd:
    for line in fd:
        url_list.append(line)
for url in url_list:
    print(url)
# rng1 = int(rng1)
# rng2 = int(rng2)
# rng = random.randint(rng1, rng2)
#range1 = input("type minimum link number: ")
#range1 = int(range1)
#range2 = input("type maximum link number: ")
#range2 = int(range2)
num_threads = input('number of browsers to run: ')
#for i in range(range1, range2): 
#    random.shuffle(url_list)
#    url = link.format(i)
#    url_list.append(url)


chunk_size = 1

list_chunked = [url_list[i:i + chunk_size] for i in range(0, len(url_list), chunk_size)]
for rl in list_chunked:
    print(rl)

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

def login():
    try:
        for handle in windowshandle:
            if handle != main_page:
                login = handle
                try:
                    browser.switch_to.window(login)
                    print(browser.title)
                    time.sleep(1)
                    try:
                        browser.find_element_by_xpath("//button[normalize-space()='Next']").click()
                        WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Connect']"))).click()
                    except NoSuchElementException:
                        pass
                    time.sleep(2)
                except NameError:
                    pass
            else:
                pass
        browser.switch_to.window(main_page)
    except NoSuchWindowException:
        pass
    return

def sup():
    browser.refresh()
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.btn-primary.first-time-flow__button"))).click()
def setup():
    global list_chunked
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_extension('C:\\Users\\thexfaciliy\\OneDrive\\Desktop\\Proxyos5\\metamask.crx')
    chrome_options.add_extension('C:\\Users\\thexfaciliy\\OneDrive\\Desktop\\Proxyos5\\bpproxyswitch.crx')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    browser = uc.Chrome(options=chrome_options)
    set_viewport_size(browser, 800, 600)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    browser.refresh()
    time.sleep(1)
    browser.refresh()
    browser.refresh()
    browser.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Get Started']"))).click()     
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button'))).click()
    #time.sleep(2)
    ActionChains(browser).move_to_element(WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='I Agree']")))).click().perform()
    time.sleep(1)
    recovery = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/form/div[4]/div[1]/div/input')))
    recovery.send_keys(secret_key)
    #password = 'Ilym2021'
    pasword = browser.find_element_by_xpath('//*[@id="password"]')
    pasword.send_keys(metamaskpass)
    fonfirmpass = browser.find_element_by_xpath('//*[@id="confirm-password"]')
    fonfirmpass.send_keys(metamaskpass)
    browser.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[7]/div').click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/form/button'))).click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/button'))).click()
    print('Assigning proxies')
    browser.get('chrome-extension://bapeomcobggcdleohggighcjbeeglhbn/popup.html')
    proxies = []
    with open('C:\\Users\\thexfaciliy\\OneDrive\\Desktop\\Proxyos5\\proxies.txt', 'r') as f:
        for line in f:
            proxies.append(line.strip())
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'editProxyList'))).click()
    for proxy in proxies:
        proxybox = browser.find_element_by_id('proxiesTextArea')
        proxybox.send_keys(str(proxy) + '\n')
    browser.find_element_by_id('addProxyOK').click()
    time.sleep(1)
    lent = len(proxies) - 1
    rando = random.randint(2,int(lent))
    xpath = '//*[@id="proxySelectDiv"]/div/div/ul/li['+ str(rando) +']'
    print(xpath)
    ActionChains(browser).move_to_element(browser.find_element_by_xpath(xpath)).click().perform()
    time.sleep(3)
    print('signing in')
    browser.get('https://opensea.io/assets/0xba30e5f9bb24caa003e9f2f0497ad287fdf95623/1')
    windowshandle = browser.window_handles
    main_page = browser.current_window_handle
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Make offer')]"))).click()
    try:
        sign = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Sign In"]'))).click()
        WebDriverWait(browser, 10).until(EC.new_window_is_opened(windowshandle))
        for handle in browser.window_handles:
            if handle != main_page:
                login = handle
                browser.switch_to.window(login)
                print(browser.title)
                time.sleep(1)
                try:
                    browser.find_element_by_xpath("//button[normalize-space()='Next']").click()
                    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Connect']"))).click()
                except NoSuchElementException:
                    pass
                time.sleep(2)
            else:
                pass            
        browser.switch_to.window(main_page)
    except TimeoutException or NoSuchWindowException:
        browser.refresh()
        time.sleep(1)
        ActionChains(browser).move_to_element(WebDriverWait(browser, 600).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Sign In"]')))).click().perform()
        WebDriverWait(browser, 10).until(EC.new_window_is_opened(windowshandle))
        login()
        browser.switch_to.window(main_page)
    for key in (list_chunked):
        for url in key:
            start_time = time.time()
            key.remove(url)
            browser.get(url)
            #list_chunked.remove(key)
            print(url)
            link = url
            try:
                main_page = browser.current_window_handle
                time.sleep(0.2)
                windowshandle = browser.window_handles
                try:
                    browser.find_element_by_xpath("//a[normalize-space()='Navigate back home']")
                    print('found navigate back home')
                except NoSuchElementException:
                    print('Looking for offer')

                try:
                    offer = browser.find_element_by_xpath("//button[contains(text(),'Make offer')]")
                    print('found it')
                except:
                    print('no offer button')
                ActionChains(browser).move_to_element(offer).click().perform()
                #browser.find_element_by_xpath("//button[contains(text(),'Make offer')]").click()
                

                try:
                    checkbox = WebDriverWait(browser,1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="review-confirmation"]')))
                    browser.execute_script("arguments[0].click();",checkbox)
                except:
                    print('no check2')
                    time.sleep(1)
                    pass
                try:
                    #sign = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Sign In"]'))).click()
                    browser.find_element_by_xpath('//button[normalize-space()="Sign In"]').click()
                    try:
                        WebDriverWait(browser, 10).until(EC.new_window_is_opened(windowshandle))
                        for handle in browser.window_handles:
                            if handle != main_page:
                                login = handle
                                browser.switch_to.window(login)
                                print(browser.title)
                                time.sleep(1)
                                try:
                                    browser.find_element_by_xpath("//button[normalize-space()='Next']").click()
                                    WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Connect']"))).click()
                                except NoSuchElementException:
                                    pass
                                time.sleep(2)
                            else:
                                pass   
                    except:
                        while True:
                            browser.find_element_by_xpath('//button[normalize-space()="Sign In"]')
                            browser.refresh()
                            browser.find_element_by_xpath('//button[normalize-space()="Sign In"]').click()
                          
                    browser.switch_to.window(main_page)
                except:
                    print('signed in')
                pass
                try:
                    inputs = browser.find_element_by_xpath("//input[@placeholder='Amount']").send_keys(am)
                except NoSuchElementException:
                    print('not here')
                    break
                try:
                    WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Make Offer')]")))
                except TimeoutException:
                    try:
                        browser.find_element_by_xpath("//input[@placeholder='Amount']").send_keys(Keys.CONTROL, 'a')
                        time.sleep(0.5)
                        browser.find_element_by_xpath("//input[@placeholder='Amount']").send_keys(Keys.BACKSPACE)
                        inputs = browser.find_element_by_xpath("//input[@placeholder='Amount']").send_keys(am)
                        WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Make Offer')]")))
                    except:
                        break

                dropdwn = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='7 days']")))
                ActionChains(browser).move_to_element(dropdwn).click().perform()
                custom = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Custom date']")))
                browser.execute_script("arguments[0].scrollIntoView();", custom)
                custom.click()


                browser.find_element_by_xpath("//i[@value='calendar_today']").click()
                inputs = browser.find_elements_by_css_selector('input')
                for element in inputs:
                    if element.get_attribute('type') == 'datetime-local':
                        ActionChains(browser).move_to_element(element).send_keys(dates).perform()
                        ActionChains(browser).move_to_element(dropdwn).click().perform()
                        offer = browser.find_element_by_xpath("//button[contains(text(),'Make Offer')]")
                        ActionChains(browser).move_to_element(offer).click().perform()
                        print('made an offer')
                        print(termcolor.colored("made an offer", "green"))
                        break
                    else:
                        continue
                try:
                    WebDriverWait(browser, 30).until(EC.new_window_is_opened(windowshandle))
                except TimeoutException:
                    print('no window')
                    ActionChains(browser).move_to_element(offer).click().perform()
                    try:
                        WebDriverWait(browser, 30).until(EC.new_window_is_opened(windowshandle))
                    except TimeoutException:
                        print('no window')
                        continue

                try:
                    for handle in browser.window_handles:
                        if handle != main_page:
                            signin_page = handle
                            try:
                                browser.switch_to.window(signin_page)
                                print(browser.title)
                                time.sleep(1)
                                try:
                                    signa = browser.find_element_by_css_selector('button.button.btn-secondary.btn--large.request-signature__footer__sign-button')
                                    browser.execute_script("arguments[0].click();", signa)
                                except:
                                    reject = browser.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div[4]/footer/button[1]')
                                    ActionChains(browser).move_to_element(reject).click().perform()
                                time.sleep(2)
                            except NameError:
                                print('namerror')
                                continue
                        else:
                            pass
                    browser.switch_to.window(main_page)
                except NoSuchWindowException:
                    pass
                try:
                    for handle in browser.window_handles:
                        if handle != main_page:
                            signin_page = handle
                            try:
                                browser.switch_to.window(signin_page)
                                print(browser.title)
                                time.sleep(1)
                                signa = browser.find_element_by_css_selector('button.button.btn-secondary.btn--large.request-signature__footer__sign-button')
                                browser.execute_script("arguments[0].click();", signa)
                                time.sleep(2)
                            except NameError:
                                print('namerror')
                                continue
                        else:
                            pass
                    browser.switch_to.window(main_page)
                except NoSuchWindowException:
                    pass
            except:
                print('did not finish')
                key.append(url)
            current_time = time.time()
            elapsed = current_time - start_time
            print("Finished iterating in: " + str(int(elapsed)) + " seconds")
    browser.close()
thread_list = []
starta_time = time.time()
for i in range(int(num_threads)):
    process = Thread(target=setup)
    thread_list.append(process)
    process.start()
    time.sleep(2)
currenta_time = time.time()
elapseda = currenta_time - starta_time
print("Finished Whole process: " + str(int(elapseda)) + " seconds")
minutes = elapseda/60
print('Done in ' + str(elapseda) + 'seconds') 



   
