from playwright.sync_api import APIResponse


class TestAPI:

    def test_created(self, getCreated: APIResponse):
        responce = getCreated
        assert responce.status == 201
        assert responce.status_text == 'Created'
        

    def test_bad_request(self, getBadRequest: APIResponse):
        responce = getBadRequest
        assert responce.status == 400
        assert responce.status_text == 'Bad Request'