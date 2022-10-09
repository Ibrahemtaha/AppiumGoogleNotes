from appium import webdriver
from appium.webdriver.appium_service import AppiumService

class Driver:
    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformVersion'] = '11'
        desired_caps['deviceName'] = 'Device1'
        # desired_caps['app'] = ('D:/appium/Android_Demo_App.apk')
        desired_caps['appPackage'] = 'com.google.android.keep'
        desired_caps['appActivity'] = 'com.google.android.keep.activities.BrowseActivity'
        # desired_cap = {'browserstack.acceptInsecureCerts': 'true'}
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return driver