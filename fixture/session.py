


class SessionHelper:

    def __init__(self, app):
        self.app=app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("userName").click()
        wd.find_element_by_name("userName").clear()
        wd.find_element_by_name("userName").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("login").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[7]/td/table/tbody/tr/td[2]/a/img").click()