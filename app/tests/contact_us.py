from currency.models import ContactUs


def test_get_contact_us(client):
    response = client.get('/currency/contactus/create/')
    assert response.status_code == 200


def test_post_empty_form_200(client):
    response = client.post('/currency/contactus/create/')
    assert response.status_code == 200


# def test_post_empty_form(client):
#     response = client.post('/currency/contactus/create/')
#     assert response.context_data['form']._errors == {   # проверка на то, что поля при создании отправляются пустыми
#         'name': ['This field is required.'],
#         'email': ['This field is required.'],
#         'subject': ['This field is required.'],
#         'message': ['This field is required.']
#     }


def test_post_invalid_data(client):
    payload = {                                 # данные, которые мы хотим отправить в запросе
        'name': 'Taras',
        'email': 'INVALID_EMAIL',               # для теста задаем не валидный email
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contactus/create/', data=payload)
    assert response.status_code == 200


def test_post_invalid_email_error(client):
    payload = {
        'name': 'Taras',
        'email': 'INVALID_EMAIL',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contactus/create/', data=payload)
    assert response.context_data['form']._errors == {'email': ['Enter a valid email address.']}  # не валидный email


# тест для проверки валидности
# mailoutbox-текстура, в которой хранится все отправленное по email, settings-для проверки с какого email идет отправка
def test_post_valid_data(client, mailoutbox, settings):
    # def test_post_valid_data(client):
    initial_count = ContactUs.objects.count()  # проверка, что объект создается, вначале объектов 0
    payload = {
        'name': 'Taras',
        'email': 'taras@example.com',
        'subject': 'This field is required.',
        'message': 'This field is required.'
    }
    response = client.post('/currency/contactus/create/', data=payload)
    assert response.status_code == 302
    assert response['location'] == '/currency/contactus/list/'  # на какую страницу после create идет переход
    assert len(mailoutbox) == 1  # проверка, что тело email не пустое

    # проверка на email, с которого идет отправка, правильней указывать mailoutbox[0].from_email == settings.EMAIL_HOST
    assert mailoutbox[0].from_email == 'User@gmail.com'
    assert ContactUs.objects.count() == initial_count + 1  # проверка, что объект создается
