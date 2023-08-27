from pages.CheckBoxPage import CheckBoxPage
class TestCheckBox:
    
    def test_base(self, checkBoxPage: CheckBoxPage):
        checkBoxPage.goto()
        checkBoxPage.checkItem('home')
        checkBoxPage.expandItem('home')
        checkBoxPage.validateResult()
        
        