from selenium import webdriver
from scrapy import Selector
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import scraper_helper
import os
import multiprocessing
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ProcessPoolExecutor
import time
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
LOGGER.setLevel(logging.WARNING)


pd.DataFrame({
    'Collection Name': None, 'Link': None,
    'ID': None, 'Rarity Score': None,
    'Method': None, 'Attributes': None
    }, index=[0]).to_csv(
        'data.csv', index=False, mode='a')


def get_driver():
    driver = getattr(ProcessPoolExecutor, 'driver', None)
    if driver is None:
        options = Options()
        options.add_argument("--disable-blink-features")
        options.add_argument("start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-logging')
        options.add_argument('--headless')
        options.add_argument(
            '--no-sandbox')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument(
            "--disable-blink-features=AutomationControlled")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument(
            f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=options)
        setattr(ProcessPoolExecutor, 'driver', driver)
    return driver


def scraping(url):
    driver = get_driver()
    driver.get(url)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[@class="p-2 m-auto bg-white border-pink-700 shadow-md rounded-2xl lg:flex lg:flex-row bg dark:border-gray-900"]'))
    )

    resp = Selector(text=driver.page_source)
    name = resp.xpath(
        '//div[@class="text-lg font-bold text-left text-pink-700 dark:text-gray-300"]/text()').get()
    rarity_score = resp.xpath(
        '//div[@class="px-2 mx-1 mb-0 text-lg font-extrabold text-green-500 bg-white rounded-md dark:bg-gray-800"]/text()').get()
    id_ = resp.xpath(
        '//div[@class="flex-grow text-sm text-right text-gray-400"]/text() | //div[@class="text-lg font-bold text-left text-pink-700 dark:text-gray-300"]/text()').get()
    rarity_score = scraper_helper.cleanup(rarity_score)
    id_ = scraper_helper.cleanup(id_)
    id_ = id_.split('#')
    id_ = id_[-1]
    name = scraper_helper.cleanup(name)
    name = name.split('#')
    name = name[0]
    method = resp.xpath(
        '//div[@class="px-4 mb-1 mt-0.5 text-xs font-normal text-pink-200"]/text()').get()
    method = scraper_helper.cleanup(method)
    attribute = [scraper_helper.cleanup(x) for x in resp.xpath(
        '//div[@class="flex flex-row items-baseline px-1 overflow-hidden text-sm"]/div[1]/text()').getall()]
    value = [scraper_helper.cleanup(z) for z in resp.xpath(
        '//div[@class="flex-grow overflow-hidden"]/text()').getall()]
    data = zip(attribute, value)
    attrValue = []
    for attr, val in data:
        list_of_data = attr + ':'+val
        attrValue.append(list_of_data)
    attrValue = '|'.join(attrValue)
    data2 = {
        'Collection Name': name,
        'Link': driver.current_url,
        'ID': id_,
        'Rarity Score': rarity_score,
        'Method': method,
        'Attributes': attrValue
    }
    pd.DataFrame(data2, index=[0]).to_csv(
        'data.csv', index=False, mode='a', header=False)


def unthreaded_driver():
    options = Options()
    options.add_argument("--disable-blink-features")
    options.add_argument("start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-logging')
    options.add_argument(
        '--no-sandbox')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(
        "--disable-blink-features=AutomationControlled")
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument(
        f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=options)
    return driver


def category_scraper(urls):
    driver = unthreaded_driver()
    product_urls = []
    for url in urls:
        driver.get(url)
        time.sleep(10)
        while True:
            resp = Selector(text=driver.page_source)
            links = [f'https://rarity.tools{x}' for x in resp.xpath(
                '//div[@class="overflow-hidden rounded-md m-0.5"]/a/@href').getall()]
            for link in links:
                product_urls.append(link)
            try:
                btn = driver.find_element_by_xpath(
                    '//div[contains(text(),"Next >")]')
                driver.execute_script('arguments[0].click();', btn)
                time.sleep(2)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@class="flex flex-row flex-wrap justify-start px-1 py-2 pt-1 ml-4 lg:px-2"]')))
            except:
                break
    driver.quit()

    return product_urls


def main(rows):
    tic = time.perf_counter()
    multiprocessing.freeze_support()
    maxprocessors = 6
    with ProcessPoolExecutor(max_workers=maxprocessors) as executor:
        executor.map(scraping, rows, chunksize=20)
    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")


if __name__ == '__main__':
    row = pd.read_csv('urls.csv')
    rows = row['urls'].to_list()
    print(rows)
    urls = category_scraper(rows)
    print(len(urls))
    print(urls)
    main(urls)

try:
    os.mkdir('collections')
except:
    pass

def proce(x):
    x = x.split('/view')
    x = x[0].split('/')
    x = x[-1]
    return x

df = pd.read_csv('data.csv')


df['Attributes']= df['Attributes'].fillna('None')
df['ID'] = df['ID'].fillna('None')
df = df[df['ID'] != 'None']
df['Collection Name'] = df['Link'].apply(proce)

for _,group in df.groupby('Collection Name'):
    rows = group.to_dict('records')
    filename = rows[0]['Collection Name'].strip()
    att_dict = {}
    specs  = {}
    main_data = []
    for row in rows:
        for x in row['Attributes'].split('|'):
            a = x.split(':')[0]
            att_dict[a] =  None            
    for row in rows:
        for x in row['Attributes'].split('|'):
            a = x.split(':')[0]
            b = x.split(':')[-1]
            specs[a] =  b            
        specs = {**att_dict,**specs}
        row = {**row,**specs}
        # row = {**row,**att_dict}
        row.pop('Attributes')
        main_data.append(row)
    try:
        pd.DataFrame(main_data,index=list(range(len(main_data)))).to_csv(f'collections/{filename}.csv',index=False,mode='a')
    except:
        pass

