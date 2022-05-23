import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

def archivo(apto):
    with open('FincaRaíz808.csv', 'a',encoding="latin-1",newline='') as f:
        thewriter = csv.writer(f)
        thewriter.writerow(apto.values())

def aptos (nombre,barrio,estado,precio,por,codigo,estrato,estadoApto,habitaciones,banos,areaTotal,areaPriv):
    apto = {
            'Nombre' : nombre,
            'Barrio' : barrio,
            'Estado' : estado,
            'Precio': precio,
            'Vendedor': por,
            'Codigo': codigo,
            'Estrato' : estrato,
            'Estado Apartamento' : estadoApto,
            'Habitaciones' : habitaciones,
            'Baños' : banos,
            'Área Total' : areaTotal,
            'Área privada' : areaPriv,
        }
    print(apto)
    archivo(apto)
    apto.clear()  


def webScraping(driver):
    for pag in range(1,41):
        driver.get(f'https://www.fincaraiz.com.co/apartamentos/venta/zona-sur/cali?pagina={pag}') 
        apartamentos = driver.find_elements(By.XPATH,'//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-lg-4 MuiGrid-grid-xl-4"]')
        for apartamento in apartamentos:
            sleep(random.uniform(7.0, 9.0))
            try:
                estado = apartamento.find_element(By.XPATH,'.//article/a/ul/li[1]/div/span').text.split('·')[0]
                nombre = apartamento.find_element(By.XPATH,'.//article/a/div[2]/footer/div/span/b').text
                por = apartamento.find_element_by_xpath('.//article/a/div[2]/footer/div/div/div').text
                s = por.split(' ')[0]
                if s == "Por":
                    por = por.split('Por ')[1]
                barrio = apartamento.find_element(By.XPATH,'.//div[@class="MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-grid-xs-12"]').text.split("-")[0]
                precio = apartamento.find_element(By.XPATH,'.//section[@class="MuiGrid-root MuiGrid-container"]/div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12"]/span/b').text
                link = apartamento.find_element(By.XPATH,'.//article/a[@href]')
                stringurl = link.get_attribute("href")
            except:
                print('Error404')
            if estado == "Proyecto":
                driver.execute_script("window.open('');") 
                driver.switch_to.window(driver.window_handles[1]) 
                driver.get(stringurl)
                sleep(random.uniform(7.0, 9.0))
                try:
                    estrato = driver.find_element(By.XPATH,'//section/div/div/div[2]/div/div[1]/div[2]/p[2]').text
                except:
                    estrato = "None"
                    print('Error 1')
                try:
                    estadoApto = driver.find_element(By.XPATH,'//section/div/div/div[2]/div/div[2]/div[2]/p[2]').text
                except:
                    estadoApto = "None"
                    print('Error 2')
                try:
                    habitaciones = driver.find_element(By.XPATH,'//table/tbody/tr/td[3]/div/p[@class]').text
                except:
                    habitaciones = "None"
                    print('Error 3')
                try:
                    banos = driver.find_element(By.XPATH,'//table/tbody/tr/td[4]/div/p[@class]').text
                except:
                    banos = "None"
                    print('Error 4')
                try:
                    areaTotal = driver.find_element(By.XPATH,'//table/tbody/tr/td[1]/p[@class]').text
                except:
                    areaTotal = "None"
                    print('Error 5')
                try:
                    areaPriv = driver.find_element(By.XPATH,'//table/tbody/tr/td[2]/p[@class]').text
                except:
                    areaPriv = "None"
                    print('Error 6')
                try:
                    driver.find_element(By.XPATH,'//div[@id="general"]/div[1]/div[1]/p[2]/span').click()
                    sleep(random.uniform(4.0, 6.0))
                    codigo = driver.find_element(By.XPATH,'//div[@id="general"]/div[1]/div[1]/div/div/div/p[2]').text.split(":")[1].split(" ")[1]
                except:
                    codigo = "None"
                    print('Error 7') 
                aptos (nombre,barrio,estado,precio,por,codigo,estrato,estadoApto,habitaciones,banos,areaTotal,areaPriv)
                driver.close() 
                driver.switch_to.window(driver.window_handles[0])
            elif estado == "Usado":
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(stringurl)
                sleep(random.uniform(7.0, 9.0))
                car=[]
                value=[]
                try:
                    caracteristicas = driver.find_elements(By.XPATH,'//section/div/div/div[2]/div/div/div[2]')
                    for carac in caracteristicas:
                        c = carac.find_element(By.XPATH,'./p[1]').text
                        v = carac.find_element(By.XPATH,'./p[2]').text
                        car.append(c)
                        value.append(v)
                    try:
                        habitaciones = value[car.index("Habitaciones")]
                    except:
                        habitaciones = "None"
                        print('Error 3')
                    try:
                        estrato = value[car.index("Estrato")]
                    except:
                        estrato = "None"
                        print('Error 1')
                    try:
                        estadoApto = value[car.index("Estado")]
                    except:
                        estadoApto = "None"
                        print('Error 2')
                    try:
                        banos = value[car.index("Baños")]
                    except:
                        banos = "None"
                        print('Error 4')
                    try:
                        areaTotal = value[car.index("Área construída")]
                    except:
                        areaTotal = "None"
                        print('Error 5')
                    try:
                        areaPriv = value[car.index("Área privada")]
                    except:
                        areaPriv = "None"
                        print('Error 6')
                    try:
                        driver.find_element(By.XPATH,'//div[@id="general"]/div[1]/div[1]/p[2]/span').click()
                        sleep(random.uniform(4.0, 6.0))
                        codigo = driver.find_element(By.XPATH,'//div[@id="general"]/div[1]/div[1]/div/div/div/p[2]').text.split(":")[1].split(" ")[1]
                    except:
                        codigo = "None"
                        print('Error 7')
                    aptos (nombre,barrio,estado,precio,por,codigo,estrato,estadoApto,habitaciones,banos,areaTotal,areaPriv)
                    car.clear()
                    value.clear()
                    driver.close() 
                    driver.switch_to.window(driver.window_handles[0])
                except:
                        print("Error808") 

def principal():
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
    webScraping(driver)

if __name__=='__main__':
    principal()
