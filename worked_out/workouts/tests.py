import pytest
from workouts.models import Client
from accounts.models import User

@pytest.fixture
def test_trainer(db):
    test_trainer = User.objects.create(first_name='Testy', last_name='User', username='testyuser', email='testyuser@testyuser.com')
    yield test_trainer
    test_trainer.delete()

@pytest.fixture
def test_client(test_trainer):
    test_client = Client.objects.create(trainer=test_trainer, first_name='Testy', last_name='User')
    yield test_client
    test_client.delete()

# Create your tests here.
def test_client_bmi(test_client):
    test_client.height_in = 72
    test_client.weight_lbs = 180
    assert test_client.bmi == pytest.approx(24.4, abs=.1)

def test_client_no_bmi(test_client):
    assert test_client.bmi is None