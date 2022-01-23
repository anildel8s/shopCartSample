from selenium.webdriver.common.by import By


class ShopCartPage:

    def __init__(self, driver):
        self.driver = driver

    product_price_on_cart_xpath = (By.CSS_SELECTOR, "td[class='product-price'] span bdi")

    def get_product_price_from_cart(self):
        productPrice = self.driver.find_element(*ShopCartPage.product_price_on_cart_xpath).text
        return productPrice[1:]
