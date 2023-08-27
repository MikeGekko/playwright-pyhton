from playwright.sync_api import APIResponse


class TestAPI:

    def test_created_api_call(self, getCreated: APIResponse):
        responce = getCreated
        assert responce.status == 201
        assert responce.status_text == 'Created'
        

    def test_bad_request_api_call(self, getBadRequest: APIResponse):
        responce = getBadRequest
        assert responce.status == 400
        assert responce.status_text == 'Bad Request'