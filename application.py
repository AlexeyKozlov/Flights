from selenium.webdriver.firefox.webdriver import WebDriver


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def click_purchase(self):
        wd = self.wd
        wd.find_element_by_xpath(
            "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[7]/td/table/tbody/tr/td[2]/a/img").click()

    def fill_reservation(self, flight):
        wd = self.wd
        self.click_book_flight()
        wd.find_element_by_name("passFirst0").click()
        wd.find_element_by_name("passFirst0").clear()
        wd.find_element_by_name("passFirst0").send_keys(flight.name)
        wd.find_element_by_name("passLast0").click()
        wd.find_element_by_name("passLast0").clear()
        wd.find_element_by_name("passLast0").send_keys(flight.lastname)
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[3]/select//option[1]").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[3]/select//option[1]").click()
        wd.find_element_by_name("passFirst1").click()
        wd.find_element_by_name("passFirst1").clear()
        wd.find_element_by_name("passFirst1").send_keys(flight.name2)
        wd.find_element_by_name("passLast1").click()
        wd.find_element_by_name("passLast1").clear()
        wd.find_element_by_name("passLast1").send_keys(flight.lastname2)
        wd.find_element_by_name("creditnumber").click()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td/table/tbody/tr[2]/td[1]/select//option[3]").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td/table/tbody/tr[2]/td[1]/select//option[3]").click()
        wd.find_element_by_name("creditnumber").click()
        wd.find_element_by_name("creditnumber").clear()
        wd.find_element_by_name("creditnumber").send_keys("111222333444")
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td/table/tbody/tr[2]/td[3]/select[1]//option[2]").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td/table/tbody/tr[2]/td[3]/select[1]//option[2]").click()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td/table/tbody/tr[2]/td[3]/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td/table/tbody/tr[2]/td[3]/select[2]//option[3]").click()
        wd.find_element_by_name("cc_frst_name").click()
        wd.find_element_by_name("cc_frst_name").clear()
        wd.find_element_by_name("cc_frst_name").send_keys("Alexey")
        wd.find_element_by_name("cc_mid_name").click()
        wd.find_element_by_name("cc_mid_name").clear()
        wd.find_element_by_name("cc_mid_name").send_keys("Kozlov")
        wd.find_element_by_name("cc_mid_name").click()
        wd.find_element_by_name("cc_mid_name").clear()
        wd.find_element_by_name("cc_mid_name").send_keys()
        wd.find_element_by_name("cc_last_name").click()
        wd.find_element_by_name("cc_last_name").clear()
        wd.find_element_by_name("cc_last_name").send_keys("Kozlov")
        wd.find_element_by_name("billAddress1").click()
        wd.find_element_by_name("billAddress1").clear()
        wd.find_element_by_name("billAddress1").send_keys("9 Autumn St")
        wd.find_element_by_name("billAddress2").click()
        wd.find_element_by_name("billAddress2").send_keys("")
        wd.find_element_by_name("billCity").click()
        wd.find_element_by_name("billCity").clear()
        wd.find_element_by_name("billCity").send_keys("Somerville")
        wd.find_element_by_name("billState").click()
        wd.find_element_by_name("billState").clear()
        wd.find_element_by_name("billState").send_keys("MA")
        wd.find_element_by_name("billZip").click()
        wd.find_element_by_name("billZip").clear()
        wd.find_element_by_name("billZip").send_keys("02145")
        wd.find_element_by_name("delAddress1").click()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[15]/td[2]/input").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[15]/td[2]/input").click()
        wd.find_element_by_name("buyFlights").click()

    def click_book_flight(self):
        wd = self.wd
        wd.find_element_by_name("reserveFlights").click()

    def choose_flight(self):
        wd = self.wd
        self.click_select_flight()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[5]/td[1]/input").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[5]/td[1]/input").click()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[5]/td[1]/input").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[5]/td[1]/input").click()

    def click_select_flight(self):
        wd = self.wd
        wd.find_element_by_name("findFlights").click()

    def fill_flight_details(self):
        wd = self.wd
        wd.find_element_by_name("tripType").click()
        wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[3]/td[2]/b/select//option[2]").click()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td[2]/select//option[4]").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td[2]/select//option[4]").click()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[6]/td[2]/select//option[5]").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[6]/td[2]/select//option[5]").click()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td[2]/select[1]//option[11]").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td[2]/select[1]//option[11]").click()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td[2]/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td[2]/select[2]//option[2]").click()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[1]").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[1]").click()
        if not wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[10]/td[2]/select//option[3]").is_selected():
            wd.find_element_by_xpath(
                "//div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[10]/td[2]/select//option[3]").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("userName").click()
        wd.find_element_by_name("userName").clear()
        wd.find_element_by_name("userName").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("login").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://newtours.demoaut.com/mercurysignon.php")


    def destroy(self):
        self.wd.quit()