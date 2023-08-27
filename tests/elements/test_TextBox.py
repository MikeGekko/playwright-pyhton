from pages.TextBoxPage import TextBoxPage

class TestTextBox:
    
    def test_text_box_form(self, textBoxData, textBoxPage: TextBoxPage):
        textBoxPage.goto()
        textBoxPage.fillTextBox(**textBoxData)
        textBoxPage.validateResultBox(**textBoxData)
        