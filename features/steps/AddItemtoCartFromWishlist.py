from behave import *
import time
from features.pageObjects.ShopHomePage import ShopHomePage
from features.pageObjects.ShopWishlistPage import ShopWishlistPage
from features.pageObjects.ShopCartPage import ShopCartPage


@given(u'I add four different products to my wish list')
def step_impl(context):
    context.homePage = ShopHomePage(context.driver)
    context.homePage.add_products_to_wishlist()


@when(u'I view my wishlist table')
def step_impl(context):
    context.homePage.get_wishlist_btn().click()
    time.sleep(5)


@then(u'I find total four selected item in the wishlist')
def step_impl(context):
    context.wishlistPage = ShopWishlistPage(context.driver)
    context.products_on_wishlist = context.wishlistPage.get_products_price_on_wishlist()
    assert len(context.products_on_wishlist) == 4


@when(u'I search for the lowest price product')
def step_impl(context):
    context.wishlistPage.get_lowest_prices_with_addcart_btns()
    context.lowest_price = context.wishlistPage.get_lowest_price_on_wishlist()
#   print("Lowest price found on product:" + context.lowestPrice)


@when(u'I am able to add the lowest price item to my cart')
def step_impl(context):
    context.wishlistPage.get_lowest_price_product_to_cart()


@then(u'I am able to verify the item in my cart')
def step_impl(context):
    context.wishlistPage.get_shopcart_btn().click()
    time.sleep(5)
    context.ShopCartPage = ShopCartPage(context.driver)
    context.product_price_on_cart = context.ShopCartPage.get_product_price_from_cart()
    assert context.lowest_price == context.product_price_on_cart

