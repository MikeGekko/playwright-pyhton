from pages.TextBoxPage import TextBoxPage

class TestTextBox:
    
    def test_base(self, textBoxData, textBoxPage: TextBoxPage):
        textBoxPage.goto()
        textBoxPage.fillTextBox(**textBoxData)
        textBoxPage.validateResultBox(**textBoxData)
        