class Checkout:

    def __init__(self,page):
        self.page = page

    def checkout(self):
        self.page.locator("#checkout").click()