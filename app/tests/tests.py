
def test_index(client):         # client -> django.test.Client
    response = client.get('/')
    assert response.status_code == 200


# @pytest.mark.skip('SKIP')  # для исключения теста. при тестировании выдаст .S
def test_rate_list(client):
    response = client.get('/currency/rate/list/')
    assert response.status_code == 200


def test_login(client):
    response = client.get('/auth/login/')
    assert response.status_code == 200


def test_sign_up(client):
    response = client.get('/account/signup/')
    assert response.status_code == 200

"""
. - Success
F - Failed - ошибка в тесте
E - Exception - код полностью сломался
S - Skipped - тест пропущен
"""
