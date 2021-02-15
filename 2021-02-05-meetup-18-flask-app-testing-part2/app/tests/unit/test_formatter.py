from app.api.person import formatter
import pytest

from app.model.person import Person


@pytest.mark.parametrize('person_test', [
    [Person(name='nis', primary_email='x@y')],
    [Person(name='pqr', primary_email='p@q'), Person(name='ikh', primary_email='p@j')],
])
def test_formatter(person_test):
    result = formatter(person_test)
    assert len(person_test) == len(result)
    assert person_test[0].primary_email == result[0]['primary email']
