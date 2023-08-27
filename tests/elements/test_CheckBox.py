from pages.CheckBoxPage import CheckBoxPage
class TestCheckBox:
    
    def test_check_box(self, checkBoxPage: CheckBoxPage):
        checkBoxPage.goto()
        checkBoxPage.checkItem('home')
        checkBoxPage.expandItem('home')
        checkBoxPage.validateResult()
        
        