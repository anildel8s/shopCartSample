import time
from typing import Any

from selenium.webdriver.common.by import By


class ShopWishlistPage:
    def __init__(self, driver):
        self.driver = driver

    product_price_css = (By.CSS_SELECTOR, "td[class='product-price']")
    shopcart_btn_xpath = (By.XPATH, "//*[@id='blog']/div[2]/div[1]/div/div/div[3]/div[1]/div/div/a/i")
    shopcart_table_css = (By.CSS_SELECTOR, "table.shop_table")
    shopcart_table_price_css = (By.CSS_SELECTOR, "span bdi")
    shopcart_table_add_to_cart_css = (By.CSS_SELECTOR, "a[class*='add_to_cart']")
    add_cart_btn_with_prices: list[list[Any]] = []
    low_price = 0

    def get_products_price_on_wishlist(self):
        return self.driver.find_elements(*ShopWishlistPage.product_price_css)

    def get_lowest_prices_with_addcart_btns(self):
        tableObj = self.driver.find_element(*ShopWishlistPage.shopcart_table_css)
        tab_index = 0
        for tabRow in tableObj.find_elements(By.CSS_SELECTOR, "tr"):
            for tabCell in tabRow.find_elements(*ShopWishlistPage.product_price_css):
                table_priceObjs = tabCell.find_elements(*ShopWishlistPage.shopcart_table_price_css)
                if len(table_priceObjs) == 1:
                    price = table_priceObjs[0].text
                    price = price[1:]
                else:
                    price1 = table_priceObjs[0].text
                    price1 = price1[1:]
                    price2 = table_priceObjs[1].text
                    price2 = price2[1:]
                    if price1 < price2:
                        price = price1
                    else:
                        price = price2
                add_to_cart_btn = tabRow.find_element(*ShopWishlistPage.shopcart_table_add_to_cart_css)
                temp_list = [price, add_to_cart_btn]
                ShopWishlistPage.add_cart_btn_with_prices.append(temp_list)
            tab_index = tab_index + 1
        return ShopWishlistPage.add_cart_btn_with_prices

    def get_lowest_price_on_wishlist(self):
        ShopWishlistPage.low_price = ShopWishlistPage.add_cart_btn_with_prices[0][0]
        for price in ShopWishlistPage.add_cart_btn_with_prices:
            if price[0] <= ShopWishlistPage.low_price:
                ShopWishlistPage.low_price = price[0]
        return ShopWishlistPage.low_price

    def get_lowest_price_product_to_cart(self):
        for price in ShopWishlistPage.add_cart_btn_with_prices:
            if price[0] == ShopWishlistPage.low_price:
                price[1].click()
                time.sleep(5)
                break

    def get_shopcart_btn(self):
        return self.driver.find_element(*ShopWishlistPage.shopcart_btn_xpath)
