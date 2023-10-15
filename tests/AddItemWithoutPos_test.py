import time

from pages.AreaPage import AreaPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class AddItemWithoutPosTest(AreaPage):
    def __init__(self, driver, random_name):
        super().__init__()
        wait = WebDriverWait(driver, 500)

        wait.until(EC.element_to_be_clickable(self.ADD_ITEM))  # открываем меню
        driver.find_element(self.ADD_ITEM[0], self.ADD_ITEM[1]).click()

        wait.until(EC.element_to_be_clickable((self.ADD_AREA_ITEM)))  # Нажимаем "Районы"
        driver.find_element(self.ADD_AREA_ITEM[0], self.ADD_AREA_ITEM[1]).click()

        wait.until(EC.element_to_be_clickable(self.INPUT_AREA_NAME))  # Вводим случайное название
        driver.find_element(self.INPUT_AREA_NAME[0], self.INPUT_AREA_NAME[1]).send_keys(random_name)

        wait.until(EC.element_to_be_clickable(self.INPUT_AREA_POS))
        driver.find_element(self.INPUT_AREA_POS[0], self.INPUT_AREA_POS[1]).send_keys(Keys.BACK_SPACE*10)
        driver.find_element(self.INPUT_AREA_POS[0], self.INPUT_AREA_POS[1]).send_keys('-')

        driver.find_element(self.SUBMIT_ADD_ITEM[0], self.SUBMIT_ADD_ITEM[1]).click()
        time.sleep(1.5)

        if random_name != driver.find_element(self.LAST_ITEM[0], self.LAST_ITEM[1]).text:
            print('Тест5 пройден')
        else:
            print('Тест5 провален')