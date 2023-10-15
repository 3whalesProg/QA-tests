import time
from pages.AreaPage import AreaPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddItemByReloadTest(AreaPage):
    def __init__(self, driver):
        super().__init__()
        wait = WebDriverWait(driver, 500)

        wait.until(EC.element_to_be_clickable(self.LAST_ITEM))

        LAST_CHILD_NAME = driver.find_element(self.LAST_ITEM[0], self.LAST_ITEM[1]).text


        wait.until(EC.element_to_be_clickable(self.ADD_ITEM))#открываем меню
        driver.find_element(self.ADD_ITEM[0], self.ADD_ITEM[1]).click()


        wait.until(EC.element_to_be_clickable((self.ADD_AREA_ITEM)))#Нажимаем "Районы"
        driver.find_element(self.ADD_AREA_ITEM[0], self.ADD_AREA_ITEM[1]).click()

        wait.until(EC.element_to_be_clickable(self.INPUT_AREA_NAME))

        driver.get('https://demo.app.stack-it.ru/fl/accounts')

        wait.until(EC.element_to_be_clickable(self.LAST_ITEM))

        if driver.find_element(self.LAST_ITEM[0], self.LAST_ITEM[1]).text == LAST_CHILD_NAME:
            print("Тест4 пройден")
        else:
            print("Тест4 провален")
