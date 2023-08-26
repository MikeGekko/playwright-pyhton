from playwright.sync_api import APIResponse, expect, Page


class TestAPI:

    
    def test_created(self, page: Page):
        responce:APIResponse = page.request.fetch(
            method='GET',
            url_or_request='/created')
        assert responce.status == 201
        assert responce.status_text == 'Created'
        

    def test_base(self, page: Page):
        responce:APIResponse = page.request.fetch(
            method='GET',
            url_or_request='/bad-request')
        assert responce.status == 400
        assert responce.status_text == 'Bad Request'