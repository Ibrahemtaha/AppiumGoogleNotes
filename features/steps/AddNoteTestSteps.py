from base.DriverClass import Driver
# import utilities.CustomLogger as cl
from base.BasePage import BasePage
import allure
from pages.AddNotePage import AddNote
import unittest
import pytest
from behave import *
import utilities.CustomLogger as cl

@given(u'Lunch the app')
def lunchGoogleNoteApp(self):
    driver1 = Driver()
    self.driver = driver1.getDriverMethod()
    # self.driver = driver
    print("1")
    self.bs = BasePage(self)
    print("2")
    # self.bs.waitForElement()
    self.ad = AddNote(self.driver)
    print("3")

@when(u'skip Welcome button')
def SkipWelcomeButtonAndVerifyPage(self):
    # cl.allureLogs("App lunched")
    self.driver.implicitly_wait(19) # seconds
    self.ad.clickSkipButton()
    self.driver.implicitly_wait(19)  # seconds
    self.ad.verifyMainPage()
print("222")
#
# # @when(u'Click on Add Note Button')
#
@then(u'New Note should be displayed')
def test_addNote(self):
    print("51")
    self.driver.implicitly_wait(19)
    print("52")
    self.ad.clickAddButton()
    print("53")
    self.ad.enterNoteText()
    print("54")
    self.ad.enterNoteTitle()
    print("55")
    self.ad.navigateBack()
    print("56")
