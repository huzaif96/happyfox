from selenium.webdriver.common.by import By
from HelpDeskCommonMethods.webdriverbase import AppPage
import time


class AdminPortalTest2ndPage(AppPage):
    def __init__(self, driver):
        super().__init__(driver)

    def title(self):
        return self.driver.find_element(By.XPATH, "//span[@class='hf-top-bar_title_text hf-font-light']")

    def pending_tickets(self):
        return self.driver.find_element(By.XPATH, "//a[contains(text(),'Pending Tickets')]")

    def click_pending_tickets(self):
        self.hover_over_element_using_js(self.pending_tickets())
        self.pending_tickets().click()

    def open_customer_ticket(self, xpath):
        ticket = f"//a[@title='{xpath}']"
        try:
            pqr = self.driver.find_element(By.XPATH, ticket)
            self.hover_over_element_using_js(pqr)
            pqr.click()
            self.sleep()
        except Exception as e:
            print(f"Exception while opening customer ticket: {e}")
            raise

    def contact_name(self):
        return self.driver.find_element(By.XPATH, "//a[@data-test-id='ticket-side-pane-contact-name']")

    def get_contact_name(self):
        contact_name = self.contact_name().text
        print(contact_name)
        return contact_name

    def email_text(self):
        return self.driver.find_element(By.XPATH,
                                        "//a[@data-test-id='ticket-side-pane-contact-name']//following::div[1]/div[1]/span[1]")

    def get_email_text(self):
        email_text = self.email_text().text
        print(email_text)
        return email_text

    def status_text(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'status')]//following::div[1]")

    def get_status_text(self):
        status_text = self.status_text().text
        print(status_text)
        return status_text

    def priority_text(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(text(),'status')]//following::div[1]//following::span[1]/div/div/div/div[2]")

    def get_priority_text(self):
        priority_text = self.priority_text().text
        print(priority_text)
        return priority_text

    def click_reply_button(self):
        self.reply_button().click()

    def canned_action(self):
        return self.driver.find_element(By.XPATH, "//span[@data-test-id='canned-action-trigger']")

    def click_canned_action(self):
        self.canned_action().click()

    def search_canned_action(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Search more Canned Actions']")

    def choose_canned_action(self):
        return self.driver.find_element(By.XPATH, "//li[@class='ember-power-select-option']")

    def click_search_canned_action(self, abc):
        try:
            self.search_canned_action().click()
            self.search_canned_action().send_keys(abc)
            self.choose_canned_action().click()
        except Exception as e:
            print(f"Exception while searching canned action: {e}")
            raise

    def click_apply_canned_action(self):
        self.apply_canned_action().click()

    def send_reply(self):
        self.reply_button().click()
        self.sleep()

    def agent_portal(self):
        return self.driver.find_element(By.XPATH, "//a[contains(text(),'Agent Portal')]")

    def goto_agent_portal(self):
        self.agent_portal().click()

    def close_ticket(self):
        return self.driver.find_element(By.XPATH, "//a[@data-test-id='details-close']")

    def close_the_ticket(self):
        self.close_ticket().click()
        return AdminPortalTest1stPage(self.driver)

    def sleep(self):
        time.sleep(2)