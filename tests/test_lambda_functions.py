from chalice.test import Client
from app import app

def test_foo_function():
    with Client(app) as client:
        result  = client.lambda_.invoke('foo')
        print(result.payload)
        assert result.payload == {'hello': 'world'}

def test_bar_function():
    with Client(app) as client:
        result = client.lambda_.invoke('bar', {'my': 'event'})
        print(result.payload)
        assert result.payload == {'event': {'my': 'event'}}