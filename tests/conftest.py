import factory
import pytest
from django.core.urlresolvers import reverse
from pytest_factoryboy import register
from rest_framework.test import APIClient

from adhocracy4.test import factories as a4_factories
from adhocracy4.test.helpers import patch_background_task_decorator
from liqd_product.apps.django_overwrites.urlresolvers import patch_reverse

from . import factories
from .partners import factories as partner_factories


def pytest_configure(config):
    # Patch the reverse function.
    # This is required as modules are imported by pytest prior to app init
    patch_reverse()
    # Patch email background_task decorators for all tests
    patch_background_task_decorator('adhocracy4.emails.tasks')


register(factories.UserFactory)
register(factories.UserFactory, 'user2')
register(factories.AdminFactory, 'admin')
register(factories.OrganisationFactory)
register(factories.PhaseFactory)
register(factories.ContentTypeFactory)
register(factories.CommentFactory)
register(factories.RatingFactory)
register(partner_factories.PartnerFactory)

register(a4_factories.ProjectFactory)
register(a4_factories.ModuleFactory)


@pytest.fixture
def apiclient():
    return APIClient()


@pytest.fixture
def smallImage():
    return factory.django.ImageField(width=200, height=200)


@pytest.fixture
def bigImage():
    return factory.django.ImageField(width=1400, height=1400)


@pytest.fixture
def ImageBMP():
    return factory.django.ImageField(width=1400, height=1400, format='BMP')


@pytest.fixture
def ImagePNG():
    return factory.django.ImageField(width=1400, height=1400, format='PNG')


@pytest.fixture
def image_factory():
    return factories.ImageFactory()


@pytest.fixture
def login_url():
    return reverse('account_login')


@pytest.fixture
def logout_url():
    return reverse('account_logout')


@pytest.fixture
def signup_url():
    return reverse('account_signup')