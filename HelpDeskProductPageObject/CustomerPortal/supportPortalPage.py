from selenium.webdriver.common.by import By
from HelpDeskCommonMethods.webdriverbase import AppPage
import time
from HelpDeskProductPageObject.Admin_Portal.AdminPortalTest2ndPage import AdminPortalTest2ndPage


class SupportPortalPage(AppPage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_happyfox_support_portal_url(self, url):
        self.driver.get(url)

    def enter_subject(self, text):
        self.subject().send_keys(text)

    def enter_message(self, text):
        self.message().send_keys(text)

    def click_add_cc(self):
        self.add_cc().click()

    def click_add_bcc(self):
        self.add_bcc().click()

    def enter_cc(self, text):
        self.cc().send_keys(text)

    def enter_bcc(self, text):
        self.bcc().send_keys(text)

    def adding_screenshot(self, abc):
        self.browse_file().send_keys(self.get_test_data_full_dir_path(abc))

    def enter_full_name(self, text):
        self.sleep()
        self.full_name().send_keys(text)

    def enter_email(self, text):
        self.sleep()
        self.email().send_keys(text)

    def enter_phone(self, text):
        self.phone().send_keys(text)

    def click_create_ticket(self):
        self.create_ticket().click()
        return AdminPortalTest2ndPage(self.driver)

    def sleep(self):
        time.sleep(1)

    def subject(self):
        return self.driver.find_element(By.ID, "id_subject")

    def message(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[@class='cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")

    def add_cc(self):
        return self.driver.find_element(By.ID, "add-cc")

    def add_bcc(self):
        return self.driver.find_element(By.ID, "add-bcc")

    def cc(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_cc']")

    def bcc(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_bcc']")

    def browse_file(self):
        return self.driver.find_element(By.XPATH, "//a[@class='hf-attach-file_link']")

    def full_name(self):
        return self.driver.find_element(By.ID, "id_name")

    def email(self):
        return self.driver.find_element(By.ID, "id_email")

    def phone(self):
        return self.driver.find_element(By.ID, "id_phone")

    def create_ticket(self):
        return self.driver.find_element(By.XPATH, "//button[@id='submit']")