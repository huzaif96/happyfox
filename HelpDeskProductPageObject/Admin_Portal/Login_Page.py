from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.driver.find_element(By.ID, "id_username").send_keys(username)
        self.driver.find_element(By.ID, "id_password").send_keys(password)
        self.driver.find_element(By.ID, "loginButton").click()

    def forgot_password(self):
        self.driver.find_element(By.LINK_TEXT, "Forgot password?").click()

    def navigate_to_happyfox_home_page_url(self, admin_portal_url):
        self.driver.get(admin_portal_url)

    def enter_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "loginButton").click()

    def validate_pending_tickets_title(self):
        pending_tickets_title = self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Pending Tickets')]")
        return pending_tickets_title is not None


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_home_page(self):
        if self.driver.current_url != "https://www.happyfox.com/home":
            raise RuntimeError("Not on the home page")

    def navigate_to_profile(self):
        self.driver.find_element(By.ID, "profileLink").click()


class TablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.row_locator = (By.XPATH, "//table[@id='dataTable']/tbody/tr")  # Corrected syntax

    def retrieve_row_texts(self):
        try:
            rows = self.driver.find_elements(*self.row_locator)  # Corrected syntax
            for i, row in enumerate(rows):
                row_text = row.text
                print(f"Row {i} Text: {row_text}")
        except Exception as e:
            print(f"Exception occurred while retrieving row texts: {e}")
