import atexit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    def __init__(self):
        self.driver = None

    def before_suite(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Maximize window on start
        try:
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        except Exception as e:
            print(f"Exception during driver setup: {e}")
            raise

    def after_suite(self):
        if self.driver is not None:
            try:
                self.driver.close()
                self.driver.quit()
            except Exception as e:
                print(f"Exception during driver teardown: {e}")
                raise

    def get_driver(self):
        return self.driver


# Usage example: Instantiate BaseTest and set up driver before suite
if __name__ == "__main__":
    base_test = BaseTest()
    base_test.before_suite()

    # Ensure driver is closed and quit after suite
    atexit.register(base_test.after_suite)