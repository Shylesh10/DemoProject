class CheckoutOverview:

    def __init__(self,page):
        self.page = page

    def checkout_overview(self):
        self.page.locator("#finish").click()


        