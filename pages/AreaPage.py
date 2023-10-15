from selenium.webdriver.common.by import By

class AreaPage:
    def __init__(self):
        self.url = 'https://demo.app.stack-it.ru/fl/accounts'

        #locators
        self.ADD_ITEM = (By.XPATH, '//*[@title="Добавить запись"]')
        self.ADD_AREA_ITEM = (By.XPATH, '//*[@data-cy="stack-menu-list-item"]')
        self.INPUT_AREA_NAME = (By.XPATH, '//*[@data-test-id="Название района"]')
        self.INPUT_AREA_POS = (By.XPATH, '//*[@data-test-id="Номер в списке"]')
        self.SUBMIT_ADD_ITEM = (By.XPATH, '//*[@class="ma-1 v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--small primary"]')
        self.LAST_ITEM = (By.XPATH, '/html/body/div[2]/div/main/div/div[1]/div/div[1]/div[1]/table/tbody/tr[last()]')

        self.FIRST_ITEM = (By.XPATH, '/html/body/div[2]/div/main/div/div[1]/div/div[1]/div[1]/table/tbody/tr[1]')
        self.FIRST_ITEM_CHECKBOX = (By.XPATH, '/html/body/div[2]/div/main/div/div[1]/div/div[1]/div[1]/table/tbody/tr[1]/td[1]')

        self.LAST_ITEM_CHECKBOX = (By.XPATH, '/html/body/div[2]/div/main/div/div[1]/div/div[1]/div[1]/table/tbody/tr[last()]/td[1]')
        self.DEL_ITEM = (By.XPATH, '/html/body/div[2]/div/main/div/div[1]/div/div[1]/header/div/div[3]/button[4]')
        self.DEL_ITEM_SUBMITE = (By.XPATH, '/html/body/div[2]/div[3]/div/div/form/div/div[2]/button[1]')

        self.EDIT_ITEM = (By.XPATH, '/html/body/div[2]/div[2]/main/div/div[1]/div/div[1]/div[1]/table/tbody/tr[last()]/td[4]/div/div/button')
        self.EDIT_ITEM_INPUT_NAME = (By.XPATH, '/html/body/div[2]/div[4]/div/div/form/div/div/div[1]/div/div/div/div[1]/div/input')
        self.EDIT_ITEM_INPUT_POS = (By.XPATH, '/html/body/div[2]/div[4]/div/div/form/div/div/div[2]/div/div/div/div/div/input')
        self.EDIT_ITEM_SUBMITE = (By.XPATH, '/html/body/div[2]/div[4]/div/div/div/button[1]')
