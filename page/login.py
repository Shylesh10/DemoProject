class LoginPage:

    def __init__(self,page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self,username,password):
        # self.page.get_by_placeholder("Username").fill("standard_user")
        # self.page.get_by_placeholder("Password").fill("secret_sauce")
        self.page.get_by_placeholder("Username").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.locator("#login-button").click()




  