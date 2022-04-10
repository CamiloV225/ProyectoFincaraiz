import os
import random
from time import sleep
from selenium import webdriver

a=1
if(not os.path.isdir("FincaRaíz")):
    os.mkdir("FincaRaíz")

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe') #dirrección del driver de selenium que va a controlar el navegador

driver.get('https://www.fincaraiz.com.co/apartamentos/venta/zona-sur/cali?pagina=40') #colocar la última pagina

for i in range(39): #el rango sería uno menos que el total de paginas 
    apartamentos = driver.find_elements_by_xpath('//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-lg-4 MuiGrid-grid-xl-4"]')

    for apartamento in apartamentos:
        car = apartamento.find_element_by_xpath('.//section[@class="MuiGrid-root MuiGrid-container"]/div[2]/span[1]').text
        print(car)
        
        barrio = apartamento.find_element_by_xpath('.//div[@class="MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-grid-xs-12"]').text
        print(barrio)

        por = apartamento.find_element_by_xpath('.//article/a/div[2]/footer/div/div/div').text
        print(por)

        nombre = apartamento.find_element_by_xpath('.//article/a/div[2]/footer/div/span/b').text
        print(nombre)
        
        precio = apartamento.find_element_by_xpath('.//section[@class="MuiGrid-root MuiGrid-container"]/div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12"]/span/b').text
        print(precio)

        link = apartamento.find_element_by_xpath('.//article/a[@href]')
        print(link.get_attribute("href"))
        
        if nombre == "Apartamento en venta" or nombre == "Apartamento en Venta":
            with open(f'{"FincaRaíz"}/{nombre} {a}.txt', 'w', encoding='utf-8') as f:
                f.write(precio)
                f.write('\n\n')
                f.write(car)
                f.write('\n\n')
                f.write(barrio)
                f.write('\n\n')
                f.write(nombre)
                f.write('\n\n')
                f.write(por)
                f.write('\n\n')
                f.write(link.get_attribute("href"))
                a=a+1
        else:
            with open(f'{"FincaRaíz"}/{nombre}.txt', 'w', encoding='utf-8') as f:
                f.write(precio)
                f.write('\n\n')
                f.write(car)
                f.write('\n\n')
                f.write(barrio)
                f.write('\n\n')
                f.write(nombre)
                f.write('\n\n')
                f.write(por)
                f.write('\n\n')
                f.write(link.get_attribute("href"))
   
    try:
        boton = driver.find_element_by_xpath('//button[@class="MuiButtonBase-root MuiPaginationItem-root MuiPaginationItem-page MuiPaginationItem-outlined MuiPaginationItem-rounded"]')
        boton.click()
        sleep(random.uniform(15.0, 20.0))
    except:
        break


