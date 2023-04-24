import json
import pytest

from model_bakery import baker

from currency.models import Source
from app.tests.fixtures.constants_api import payload, test_load, test_patch, test_patch_load, test_put, test_put_load


def prepare_source():
    source = baker.prepare(Source)
    body = {
        'source_url': source.source_url,
        'name': source.name,
        'code_name': source.code_name,
    }
    return source, body


# def make_source():
#     source = baker.make(Source)
#     body = {
#         'source_url': source.source_url,
#         'name': source.name,
#         'code_name': source.code_name,
#     }
#     return source, body


def test_api_source_list(api_client):
    response = api_client.get('/api/currency/sources/')
    assert response.status_code == 200


@pytest.mark.parametrize('field', [('source_url'), ('name'), ('code_name'),])
def test_api_source_create(api_client, field):

    initial_count = Source.objects.count()
    source, body = prepare_source()
    response = api_client.post('/api/currency/sources/', data=body, format='json')
    assert response.status_code == 201
    assert Source.objects.count() == initial_count + 1
    assert json.loads(response.content)[field] == body[field]


# для проверки
def test_api_source_bad_post(api_client):

    response = api_client.post('/api/currency/sources/')
    assert response.status_code == 400
    assert response.json() == {
            'source_url': ['This field is required.'],
            'name': ['This field is required.'],
            'code_name': ['This field is required.']
        }


def test_api_source_retrieve(api_client):

    dispatch = api_client.post('/api/currency/sources/', data=payload, format='json')
    response = api_client.get('/api/currency/sources/1/')
    assert dispatch.status_code == 201
    assert response.status_code == 200
    assert json.loads(response.content) == test_load


def test_api_source_patch(api_client):

    dispatch = api_client.post('/api/currency/sources/', data=payload, format='json')
    response = api_client.patch('/api/currency/sources/1/', data=test_patch, format='json')
    assert dispatch.status_code == 201
    assert response.status_code == 200
    assert json.loads(response.content) == test_patch_load


def test_api_source_put(api_client):

    dispatch = api_client.post('/api/currency/sources/', data=payload, format='json')
    response = api_client.put('/api/currency/sources/1/', data=test_put, format='json')
    assert dispatch.status_code == 201
    assert response.status_code == 200
    assert json.loads(response.content) == test_put_load


def test_api_source_delete(api_client):

    dispatch = api_client.post('/api/currency/sources/', data=payload, format='json')
    initial_count = Source.objects.count()
    response = api_client.delete('/api/currency/sources/1/')
    assert dispatch.status_code == 201
    assert response.status_code == 204
    assert Source.objects.count() == initial_count - 1
