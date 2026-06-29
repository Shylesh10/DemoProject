class CheckOutInformation:

    def __init__(self,page):
        self.page = page

    def checkout_info(self):
        self.page.get_by_placeholder("First Name").fill("Demo")
        self.page.get_by_placeholder("Last Name").fill("Test")
        self.page.get_by_placeholder("Zip/Postal Code").fill("560001")
        self.page.locator("#continue").click()

