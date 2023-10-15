import time

from pages.AreaPage import AreaPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditItemTest(AreaPage):
    def __init__(self, driver, random_name):
        super().__init__()
        wait = WebDriverWait(driver, 500)
        random_name = random_name
        wait.until(EC.element_to_be_clickable(self.LAST_ITEM_CHECKBOX))  # Выделяем последний элемент
        driver.find_element(self.LAST_ITEM_CHECKBOX[0], self.LAST_ITEM_CHECKBOX[1]).click()

        wait.until(EC.element_to_be_clickable(self.EDIT_ITEM))  #Начинаем редактирование элемента
        driver.find_element(self.EDIT_ITEM[0], self.EDIT_ITEM[1]).click()

        wait.until(EC.element_to_be_clickable(self.EDIT_ITEM_INPUT_NAME))  #Меняем название элемента
        driver.find_element(self.EDIT_ITEM_INPUT_NAME[0], self.EDIT_ITEM_INPUT_NAME[1]).send_keys('_edited')

        #Меняем название элемента рассчиытвая на то, что он будет первым в списке
        driver.find_element(self.EDIT_ITEM_INPUT_POS[0], self.EDIT_ITEM_INPUT_POS[1]).send_keys('-10000')

        wait.until(EC.element_to_be_clickable(self.EDIT_ITEM_SUBMITE))  #Подтвержаем создание редактирование элемента
        driver.find_element(self.EDIT_ITEM_SUBMITE[0], self.EDIT_ITEM_SUBMITE[1]).click()

        driver.get('https://demo.app.stack-it.ru/fl/accounts')
        wait.until(EC.element_to_be_clickable(self.FIRST_ITEM))
        if random_name + '_edited' == driver.find_element(self.FIRST_ITEM[0], self.FIRST_ITEM[1]).text:
            print('Тест2 пройден')
        else:
            print('Тест2 провален')
