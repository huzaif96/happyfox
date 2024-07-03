import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AppPage:
    PATH_TO_TEST_DATA_FILE = "src/main/resources/"
    WINDOWS_PATH_TO_TEST_DATA_DIR = "src/main/resources/"
    WAIT_TIME_SEC = 60

    def __init__(self, driver):
        self.driver = driver
        self.java_script_executor = None
        self.wait_implicitly()
        self.maximize_window()

    def get_driver(self):
        return self.driver

    def get(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def maximize_window(self):
        self.driver.maximize_window()

    def wait_implicitly(self, time_out_in_seconds=WAIT_TIME_SEC):
        self.driver.implicitly_wait(time_out_in_seconds)

    def clear_and_type(self, element, text):
        element.clear()
        element.send_keys(text)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def hover_over_element_using_js(self, element):
        js = """
            var evObj = document.createEvent('MouseEvents');
            evObj.initEvent('mouseover', true, false);
            arguments[0].dispatchEvent(evObj);
        """
        self.get_javascript_executor().execute_script(js, element)

    def get_javascript_executor(self):
        if self.java_script_executor is None:
            self.java_script_executor = self.driver
        return self.java_script_executor

    def scroll_to_element_by_locator(self, locator):
        try:
            element = self.driver.find_element(By.XPATH, locator)
            self.scroll_to_element(element)
        except Exception as ex:
            print(f"Exception in scroll_to_element_by_locator: {ex}")

    def scroll_to_element(self, element):
        self.get_javascript_executor().execute_script("arguments[0].scrollIntoView(false)", element)
        time.sleep(1)

    def wait_for_visible(self, element):
        wait = WebDriverWait(self.driver, self.WAIT_TIME_SEC)
        wait.until(EC.element_to_be_clickable(element))

    def get_current_working_directory(self):
        return os.getcwd()

    def get_test_data_full_dir_path(self, file_name):
        path = self.PATH_TO_TEST_DATA_FILE
        if self.get_operating_system_type() == 'Windows':
            path = self.WINDOWS_PATH_TO_TEST_DATA_DIR
        return os.path.join(self.get_current_working_directory(), path, file_name)

    def get_operating_system_type(self):
        return platform.system()