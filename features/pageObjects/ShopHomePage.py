import time

from selenium.webdriver.common.by import By


class ShopHomePage:

    def __init__(self, driver):
        self.driver = driver

    add_to_wishlist_xpath = (By.XPATH, "//span[contains(text(),'Add to wishlist')]")
    wishlist_btn_xpath = (By.XPATH, "//*[@id='blog']/div[3]/div[1]/div/div/div[3]/div[3]/a/i")

    def get_add_to_wishlist_buttons(self):
        return self.driver.find_elements(*ShopHomePage.add_to_wishlist_xpath)

    def add_products_to_wishlist(self):
        add_to_wishlist_btns = self.get_add_to_wishlist_buttons()
        cntr = 1
        for btn in add_to_wishlist_btns:
            if cntr <= 4:
                btn.click()
                time.sleep(5)
                cntr = cntr + 1
        time.sleep(5)

    def get_wishlist_btn(self):
        return self.driver.find_element(*ShopHomePage.wishlist_btn_xpath)
