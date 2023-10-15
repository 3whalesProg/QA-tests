from pages.AreaPage import AreaPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DelItemTest(AreaPage):
    def __init__(self, driver):
        super().__init__()
        wait = WebDriverWait(driver, 500)


        FIRST_CHILD_NAME = driver.find_element(self.FIRST_ITEM[0], self.FIRST_ITEM[1]).text


        wait.until(EC.element_to_be_clickable(self.FIRST_ITEM_CHECKBOX))#Выделяем последний элемент
        driver.find_element(self.FIRST_ITEM_CHECKBOX[0], self.FIRST_ITEM_CHECKBOX[1]).click()

        wait.until(EC.element_to_be_clickable(self.DEL_ITEM))#Нажимаем кнопку удалить
        driver.find_element(self.DEL_ITEM[0], self.DEL_ITEM[1]).click()

        wait.until(EC.element_to_be_clickable(self.DEL_ITEM_SUBMITE)) #Подтверждаем удаление
        driver.find_element(self.DEL_ITEM_SUBMITE[0], self.DEL_ITEM_SUBMITE[1]).click()
        time.sleep(2) #Не лучшая практика, но нам необходимо дождаться удаления элемента
        if FIRST_CHILD_NAME != driver.find_element(self.FIRST_ITEM[0], self.FIRST_ITEM[1]).text: #сравниваем название элемента которое мы удалили, с названием текущего последнего элемента
            print('Тест3 пройден')
        else:
            print('Тест3 провален')
