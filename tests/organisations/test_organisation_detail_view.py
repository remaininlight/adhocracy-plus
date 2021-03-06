import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_hide_private_projects(client, user, project_factory, organisation):
    public = project_factory(organisation=organisation)
    private = project_factory(is_public=False, organisation=organisation)

    client.login(username=user, password='password')
    url = reverse('organisation',
                  kwargs={'organisation_slug': organisation.slug})
    response = client.get(url)
    assert response.status_code == 200

    project_list = response.context['project_list']
    assert public in project_list
    assert private not in project_list


@pytest.mark.django_db
def test_show_private_projects_participant(
    client, user, project_factory, organisation
):
    public = project_factory(organisation=organisation)
    private = project_factory(is_public=False, organisation=organisation)
    private.participants.add(user)

    client.login(username=user, password='password')
    url = reverse('organisation',
                  kwargs={'organisation_slug': organisation.slug})
    response = client.get(url)
    assert response.status_code == 200

    project_list = response.context['project_list']
    assert public in project_list
    assert private in project_list


@pytest.mark.django_db
def test_show_private_projects_initiators(
    client, user, project_factory, organisation
):
    public = project_factory(organisation=organisation)
    private = project_factory(is_public=False, organisation=organisation)
    private.organisation.initiators.add(user)

    client.login(username=user, password='password')
    url = reverse('organisation',
                  kwargs={'organisation_slug': organisation.slug})
    response = client.get(url)
    assert response.status_code == 200

    project_list = response.context['project_list']
    assert public in project_list
    assert private in project_list
