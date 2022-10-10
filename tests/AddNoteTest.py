# from base.DriverClass import Driver
# import utilities.CustomLogger as cl
# from base.BasePage import BasePage
import allure
from pages.AddNotePage import AddNote
import unittest
import pytest
import utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class AddNotesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObject(self):
        self.ad = AddNote(self.driver)

    @pytest.mark.run(order=1)
    def test_openNotesApp(self):
        cl.allureLogs("App lunched")
        self.ad.clickSkipButton()
        self.ad.verifyMainPage()

    @pytest.mark.run(order=2)
    def test_addNote(self):
        self.ad.clickAddButton()
        self.ad.enterNoteText()
        self.ad.enterNoteTitle()
        self.ad.navigateBack()

    # @pytest.mark.run(order=3)
    # def test_assert(self):
    #     assert False
    # @pytest.mark.run(order=3)
    # def test_Assert(self):
    #     self.ad.validateNoteCreation()


####
# # D:\pycharmProjects\AppiumGoogleNotes\reports\allurereports
# # py.test --alluredir=D:\pycharmProjects\AppiumGoogleNotes\reports\allurereports -v -s AddNoteTest.py
# py.test -v -s  C:\Users\Ibrahem.taha\Documents\Ibrahem\Appium\AppiumGoogleNotes\tests\AddNoteTest.py
#
# # IMPORTNAT: problem was Set Allure.bat to Envirounment Variables AND user Full path of file
# # python -m pytest -v -s  D:\pycharmProjects\AppiumGoogleNotes\tests\AddNoteTest.py  --alluredir=D:\pycharmProjects\AppiumGoogleNotes\reports\allurereports
#
# # To use Allure: allure serve D:\pycharmProjects\AppiumGoogleNotes\reports\allurereports
