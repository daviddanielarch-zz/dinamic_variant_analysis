import django.template.defaultfilters
import pytest
from django.db.models import QuerySet


def queryset_check_length(value):
    """
    New |length implementation which checks for a queryset instance value type and raises an error
    """
    if isinstance(value, QuerySet):
        raise Exception('Calling length with a QuerySet')
    else:
        # call the default length templatetag
        return django.template.defaultfilters.length(value)


@pytest.fixture(autouse=True)
def template_length_check(monkeypatch):
    # Replace the length templatetag implementation with a custom one
    monkeypatch.setitem(django.template.defaultfilters.register.filters, 'length', queryset_check_length)
