from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time



for i in range(1,597):
    driver=webdriver.Firefox()
    url="https://www.inmuebles24.com/departamentos-en-renta-en-ciudad-de-mexico"
    output_name=""'Downloads\inmuebles24-sep-2023\list_of_apartments'
    if i==1:
        url+=".html"
    else:
        url+="-pagina-"+str(i)+".html"
    driver.implicitly_wait(10)
    #WebDriverWait(driver,40)
    driver.get(url=url)
    time.sleep(15)
    html_content=driver.page_source
    output_name+=str(i)+".html"
    with open(output_name,'w',encoding='utf-8') as f:
        f.write(html_content)
    driver.close()