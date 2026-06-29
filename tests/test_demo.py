from playwright.sync_api import Playwright,expect
import time
import json
import pytest
from page.checkoutcomplete import CheckoutComplete
from page.checkoutoverview import CheckoutOverview
from page.checkoutinfo import CheckOutInformation
from page.checkout import Checkout
from page.add_to_cart import AddToCart
from page.login import LoginPage


with open("data/credentials.json") as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['credentials']
    

@pytest.mark.parametrize('user_credentials',user_credentials_list)
def test_e2e(playwright: Playwright,browser_instance,user_credentials):
    username = user_credentials["userName"]
    password = user_credentials["passWord"]
    login = LoginPage(browser_instance)
    login.navigate()
    login.login(username,password)
    addtocart = AddToCart(browser_instance)
    addtocart.add_to_cart()
    checkout = Checkout(browser_instance)
    checkout.checkout()
    checkoutinfo = CheckOutInformation(browser_instance)
    checkoutinfo.checkout_info()
    checkoutoverview = CheckoutOverview(browser_instance)
    checkoutoverview.checkout_overview()
    verify_order_complete = CheckoutComplete(browser_instance)
    expect(verify_order_complete.get_success_header()).to_contain_text("Thank you for your order!")
    
    
