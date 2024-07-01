import sys
from HelpDeskProductTests.CommonTests import CommonTests1

class AdminPortalTest2(CommonTests1):

    def scenario2(self):
        try:
            method_name = sys._getframe().f_code.co_name
            class_name = self.__class__.__name__
            print("Start of method:", method_name, "in class:", class_name)
            self.login_as_admin()
            self.test_case_1()
            self.test_case_2()
            self.test_case_3()
        except Exception as e:
            print("Error in", method_name, ":", str(e))
            assert False, "Error in " + method_name + ": " + str(e)


# Usage
if __name__ == "__main__":
    admin_test = AdminPortalTest2()
    admin_test.scenario2()