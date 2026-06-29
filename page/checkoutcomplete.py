from playwright.sync_api import expect

class CheckoutComplete:

    def __init__(self,page):
        self.page = page
        self.success_header = page.locator(".complete-header")


    def get_success_header(self):
        return self.success_header



