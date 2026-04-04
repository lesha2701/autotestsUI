from playwright.sync_api import Page, TimeoutError, Response
from data.environment import host

class Base:

    def __init__(self, page: Page):
        self.page = page


    # методы для URL

    def open(self, uri):
        return self.page.goto(f"{host.get_base_url()}{uri}",
                              wait_until="domcontentloaded")
    

    # методы для ввода текста

    def input(self, locator, data):
        return self.page.locator(locator).fill(data)
    
    def input_by_index(self, locator, index, data):
        return self.page.locator(locator).nth(index).fill(data)
    
    def input_by_label(self, label_name, data):
        return self.page.get_by_label(label_name).fill(data)
    
    def input_by_placeholder(self, placeholder, data):
        return self.page.get_by_placeholder(placeholder).fill(data)

    
    # Методы для клика
    
    def click(self, locator):
        return self.page.locator(locator).click()
    
    def click_by_role(self, tag, name):
        return self.page.get_by_role(tag, name=name).click()
    
    def click_by_index(self, locator, index):
        return self.page.locator(locator).nth(index).click()
    

    # Ожидание

    def wait_element(self, locator):
        return self.page.is_visible(locator)

    def wait_element_for_click(self, locator):
        return self.page.wait_for_selector(locator).click()
    

    # Получение текста 
    
    def get_text(self, element):
        return self.page.locator(element).text_content()
    