import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from tests.AddItem_test import AddItemTest
from tests.DelItem_test import DelItemTest
from tests.EditItem_test import EditItemTest
from tests.AddItemByReload_test import AddItemByReloadTest
from tests.AddItemWithoutPos_test import AddItemWithoutPosTest

def SignUp(driver):
    USER_NAME = 'DEMOWEB'
    PASSWORD = 'awdrgy'

    wait = WebDriverWait(driver, 500)
    wait.until(EC.element_to_be_clickable((By.ID, "input-38"))) #Ждем пока загрузиться элемент

    #Находим элементы и вводим данные
    name_input = driver.find_element(By.ID, 'input-38')
    password_input = driver.find_element(By.ID, 'input-41')
    name_input.send_keys(USER_NAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.ENTER)

    try:
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@class="ma-1 v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--default primary"]').click()
    except: print('-')


def start():
    #Создаем веб драйвер
    service = Service(executable_path=r"./webdriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    #Переходим на сайт
    driver.maximize_window()
    driver.get('https://demo.app.stack-it.ru/fl/')

    SignUp(driver) #Проходим авторизацю

    driver.get('https://demo.app.stack-it.ru/fl/accounts')

    random_name = "test" + str(random.randint(0,100000))

    AddItemTest(driver, random_name) #Добавление обычного элемента без попыток "Сломать"
    EditItemTest(driver, random_name) #Редактирование элемента
    DelItemTest(driver) #Удаление элемента
    AddItemByReloadTest(driver) #Создание элемента с пустым названием
    random_name = "test" + str(random.randint(0, 100000))
    AddItemWithoutPosTest(driver, random_name) #Создание элемента с позицией "-"





start()