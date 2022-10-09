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
    # driver1 = Driver()
    # self.driver = driver1.getDriverMethod()
    # self.driver = driver
    self = BasePage(self)
    self.ad = AddNote(self)

@when(u'skip Welcome button')
def SkipWelcomeButtonAndVerifyPage(self):
    # cl.allureLogs("App lunched")
    print("1")
    self.ad.clickSkipButton()
    print("2")
    self.ad.verifyMainPage()
    print("3")
#
# # @when(u'Click on Add Note Button')
#
# @then(u'New Note should be displayed')
# def test_addNote(self):
#     self.ad.clickAddButton()
#     self.ad.enterNoteText()
#     self.ad.enterNoteTitle()
#     self.ad.navigateBack()
