import json
import os
from http import HTTPStatus

import pytest
from chalice.config import Config
from chalice.local import LocalGateway

import app

@pytest.fixture
def api():
    return LocalGateway(app.app,Config())

def test_get_hello_world(api):
    response =  api.handle_request(method='GET', path='/', headers={}, body=None)
    print(response)
    assert response['statusCode'] == HTTPStatus.OK
    response = json.loads(response['body'])
    assert response['hello'] == 'world'

def test_sum(api):
    response = api.handle_request(method='GET', path='/sum?num1=1&num2=2', headers={}, body = None )
    print(response)
    assert response['statusCode'] == HTTPStatus.OK
    response = json.loads(response['body'])
    assert int(response['sum']) == 3
