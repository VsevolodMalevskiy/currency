# from rest_framework.test import APIClient


# def test_get_api_rate_list():  # не требуется, так как в conftest создана фикстура dsf api_client():
#     client = APIClient()
#     response = client.get('/api/currency/rates/')
def test_get_api_rate_list(api_client):
    response = api_client.get('/api/currency/rates/')
    assert response.status_code == 200


def test_post_api_rate_list(api_client):
    response = api_client.post('/api/currency/rates/')
    assert response.status_code == 400
    assert response.json() == {
            'buy': ['This field is required.'],
            'sale': ['This field is required.'],
            'source': ['This field is required.'],
        }


# def test_get_api_rate_list(api_client):
#     response = api_client.get('/api/currency/rates/')
#     assert response.status_code == 200
#
#
# def test_pots_api_rate_list(api_client):
#     response = api_client.post('/api/currency/rates/')
#     assert response.status_code == 400
#     assert response.json() == {
#         'buy': ['This field is required.'],
#         'sale': ['This field is required.'],
#         'source': ['This field is required.']
#     }
