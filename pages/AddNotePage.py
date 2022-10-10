from base.BasePage import BasePage
import utilities.CustomLogger as cl

class AddNote(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator values in Main page for Add
    _SkipwelcomeButton = "com.google.android.keep:id/skip_welcome"  #id
    _mainPageSeachBar = "com.google.android.keep:id/toolbar"                 #id
    _addNoteButton = "com.google.android.keep:id/new_note_button"   #id
    _enterNoteText = "com.google.android.keep:id/edit_note_text"    #id
    _enterTitleText= "com.google.android.keep:id/editable_title"    #id
    _NoteAssertion = "com.google.android.keep:id/browse_note_interior_content" #SourceID
    _titleOfNote = "com.google.android.keep:id/index_note_title" #id


    def clickSkipButton(self):
        self.clickElement(self._SkipwelcomeButton, "id")

    def verifyMainPage(self):
        element = self.isDisplayed(self._mainPageSeachBar,"id")
        assert element == True
       # assert self.isDisplayed(self._mainPage,"id") is True
    def clickAddButton(self):
        self.clickElement(self._addNoteButton, "id")
        cl.allureLogs("Click on Add Note button")

    def enterNoteText(self):
        self.getElement(self._enterNoteText,"id").clear()
        # self.clearNoteText(self)
        self.sendText("First Automation Note",self._enterNoteText,"id")

    def enterNoteTitle(self):
        # self.sendText(self._enterTitleText,"id").clear()
        self.sendText("First Title",self._enterTitleText,"id")

    def clearNoteText(self):
        self.getElement(self._enterNoteText, "id").clear()

    def clearNoteTitle(self):
        self.getElement(self._enterTitleText, "id").clear()

    def navigateBack(self):
        print (" entered navigate back")
        #self.waitForElement(self,self._enterTitleText,)
        self.driver.implicitly_wait(20)
        self.driver.back()

    # def validateNoteCreation(self):
    #     self.waitForElement(self._mainPageSeachBar,"id")
    #     element3 = self.isDisplayed(self._titleOfNote, "id")
    #     print(element3)
    #     element2 = self.getElement(self._titleOfNote,"id")
    #     assert element2.text == "First Title" is True
       # assert self.isDisplayed(self._mainPage,"id") is True


