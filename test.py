import unittest
import foodpass
import config

browser = foodpass.FoodPass()

class FoodPassTests(unittest.TestCase):
    
    def test_config(self):
        validConfig = True
        if config is not None:
            if (config.userList) == 0:
                validConfig = False
            else: 
                for user in config.userList:
                    self.assertNotEqual(user.username, "",     "Empty username.")
                    self.assertNotEqual(user.username, "User", "Default username.") 
                    self.assertNotEqual(user.password, "",     "Empty password.") 
                    self.assertGreater(len(user.meals), 0,     "Empty meal list.") 
        else:
            validConfig = False
        
        self.assertTrue(validConfig, "Invalid Config.")

    def test_webdriverinit(self):        
        browser.driver.get("https://www.google.com/")
        isHtml = browser.driver.page_source.startswith("<html")
        self.assertTrue(isHtml)

    def test_login(self):
        r = browser.login(config.userList[0].username , config.userList[0].password)
        self.assertTrue(r)


if __name__ == '__main__':  
    unittest.main()
