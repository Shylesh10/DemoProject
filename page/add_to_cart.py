class AddToCart:

    def __init__(self,page):
        self.page = page

    def add_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()
        self.page.locator(".shopping_cart_link").click()