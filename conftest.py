import pytest
import data.constants as constant
from pages.TextBoxPage import TextBoxPage
from pages.BasePage import BasePage
from pages.CheckBoxPage import CheckBoxPage
from playwright.sync_api import Page


#Session settings

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


#Import data

@pytest.fixture(scope="session")
def textBoxData():
    return constant.textBoxData


# Pages

@pytest.fixture(scope="function")
def basePage(page: Page):
    return BasePage(page)

@pytest.fixture(scope="function")
def textBoxPage(page: Page):
    return TextBoxPage(page)

@pytest.fixture(scope="function")
def checkBoxPage(page: Page):
    return CheckBoxPage(page)


# API

@pytest.fixture(scope="function")
def getCreated(page: Page):
    return page.request.fetch(
                method='GET',
                url_or_request='/created')


@pytest.fixture(scope="function")
def getBadRequest(page: Page):
    return page.request.fetch(
                method='GET',
                url_or_request='/bad-request')