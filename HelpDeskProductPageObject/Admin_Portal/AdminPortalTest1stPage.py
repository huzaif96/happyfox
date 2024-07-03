from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from HelpDeskCommonMethods.webdriverbase import AppPage


class AdminPortalTest1stPage(AppPage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_status(self):
        self.hover_over_element_using_js(self.title())
        self.title().click()
        self.statuses().click()

    def click_priorities(self):
        self.sleep()
        self.hover_over_element_using_js(self.title())
        self.title().click()
        self.hover_over_element_using_js(self.priorities())
        self.priorities().click()

    def click_new_status(self):
        self.new_status().click()

    def enter_status_name(self, text):
        self.status_name().clear()
        self.status_name().send_keys(text)

    def click_status_colour_inner(self):
        self.status_colour_inner().click()

    def enter_status_colour(self, text):
        self.click_status_colour_inner()
        self.status_colour().clear()
        self.status_colour().send_keys(text)
        self.click_status_colour_inner()

    def enter_behavior(self, text):
        self.behavior().click()
        self.behavior().send_keys(text)
        self.behavior().send_keys(Keys.ENTER)

    def enter_status_description(self, text):
        self.status_description().clear()
        self.status_description().send_keys(text)

    def click_add_status(self):
        self.add_status().click()

    def click_statuses_section(self):
        self.scroll_to_element(self.statuses_section())
        self.statuses_section().click()

    def set_default_status(self, xpath):
        status_xpath = f"//div[contains(text(),'{xpath}')]//following::td[3]"
        try:
            abc = self.driver.find_element(By.XPATH, status_xpath)
            self.hover_over_element_using_js(abc)
            abc.click()
        except Exception as e:
            print(f"Exception while setting default status: {e}")
            raise

    def click_priority_section(self):
        self.priority_section().click()

    def click_new_priority(self):
        self.new_priority().click()

    def enter_priority_name(self, text):
        self.priority_name().clear()
        self.priority_name().send_keys(text)

    def enter_priority_description(self, text):
        self.priority_description().clear()
        self.priority_description().send_keys(text)

    def enter_priority_help_text(self, text):
        self.priority_help_text().clear()
        self.priority_help_text().send_keys(text)

    def click_add_priority(self):
        self.add_priority().click()

    def set_default_priority(self, xpath):
        priority_xpath = f"//span[contains(text(),'{xpath}')]//following::td[3]"
        try:
            pqr = self.driver.find_element(By.XPATH, priority_xpath)
            self.hover_over_element_using_js(pqr)
            pqr.click()
            self.sleep()
            self.sleep()
        except Exception as e:
            print(f"Exception while setting default priority: {e}")
            raise

    def click_added_priority(self, xpath):
        self.sleep()
        priority_xpath = f"//span[contains(text(),'{xpath}')]"
        self.scroll_to_element(priority_xpath)
        self.driver.find_element(By.XPATH, priority_xpath).click()

    def click_priority_delete_link(self):
        self.scroll_to_element(self.priority_delete_link())
        self.priority_delete_link().click()

    def set_new_default_priority(self):
        try:
            self.hover_over_element_using_js(self.new_default_priority())
            self.new_default_priority().click()
            self.choosing_new_default_priority().click()
            self.choosing_new_default_priority().send_keys("Low")
            self.choosing_new_default_priority().send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Exception while setting new default priority: {e}")
            raise

    def click_delete_confirm(self):
        try:
            self.delete_confirm().click()
            WebDriverWait(self.driver, self.WAIT_TIME_SEC).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast-body']")))
        except Exception as e:
            print(f"Exception while clicking delete confirmation: {e}")
            raise

    def click_added_status(self, xpath):
        self.sleep()
        status_xpath = f"//div[contains(text(),'{xpath}')]"
        self.scroll_to_element(status_xpath)
        self.driver.find_element(By.XPATH, status_xpath).click()

    def click_status_delete_link(self):
        self.scroll_to_element(self.status_delete_link())
        self.status_delete_link().click()

    def set_new_default_status(self):
        try:
            self.hover_over_element_using_js(self.new_default_status())
            self.new_default_status().click()
            self.new_default_status().send_keys(Keys.DOWN)
            self.new_default_status().send_keys(Keys.ENTER)
        except Exception as e:
            print(f"Exception while setting new default status: {e}")
            raise

    def switch_to_frames(self):
        self.switch_to_frame(self.to_frames())

    def switch_to_default_page(self):
        self.switch_to_default_content()

    def click_profile(self):
        self.sleep()
        self.wait_for_visible(self.profile())
        self.profile().click()

    def click_logout(self):
        self.logout().click()

    def sleep(self):
        time.sleep(2)

    def title(self):
        return self.driver.find_element(By.XPATH, "//span[@class='hf-top-bar_title_text hf-font-light']")

    def statuses(self):
        return self.driver.find_element(By.LINK_TEXT, "Statuses")

    def priorities(self):
        return self.driver.find_element(By.LINK_TEXT, "Priorities")

    def new_status(self):
        return self.driver.find_element(By.XPATH, "//button[@class='hf-mod-create']")

    def status_name(self):
        return self.driver.find_element(By.XPATH, "//input[@aria-label='Status Name']")

    def status_colour_inner(self):
        return self.driver.find_element(By.XPATH, "//div[@class='sp-preview-inner']")

    def status_colour(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Enter any valid color code format.']")

    def behavior(self):
        return self.driver.find_element(By.XPATH, "//div[@aria-label='Behavior']")

    def status_description(self):
        return self.driver.find_element(By.XPATH, "//textarea[@aria-label='Description']")

    def add_status(self):
        return self.driver.find_element(By.XPATH, "//button[@data-test-id='add-status']")

    def statuses_section(self):
        return self.driver.find_element(By.XPATH, "//a[@data-test-id='manage-statuses-left-nav']")

    def new_default_priority(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Choose Priority')]")

    def choosing_new_default_priority(self):
        return self.driver.find_element(By.XPATH, "//input[contains(@class,'ember-power-select-search-input')]")

    def priority_delete_link(self):
        return self.driver.find_element(By.XPATH, "//a[@data-test-id='priority-delete-trigger']")

    def new_default_status(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Choose Status')]")

    def to_frames(self):
        return self.driver.find_element(By.XPATH, "//iframe[@id='hfc-frame']")

    def profile(self):
        return self.driver.find_element(By.XPATH, "//div[@class='hf-avatar-image-container ember-view']//img[@class='hf-avatar-image hf-avatar-image_show']")

    def logout(self):
        return self.driver.find_element(By.XPATH, "//div[@class='hf-logout-icon']")


# Example usage:
if __name__ == "__main__":
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())
    test_page = AdminPortalTest1stPage(driver)
    test_page.get("https://your_admin_portal_url.com")
    test_page.click_statuses_section()
    test_page.click_add_status()
    test_page.enter_status_name("New Status")
    test_page.enter_status_description("Description of new status")
    test_page.enter_status_colour("#FF0000")
    test_page.click_add_status()
    test_page.click_profile()
    test_page.click_logout()
    driver.quit()