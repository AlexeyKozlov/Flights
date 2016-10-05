# -*- coding: utf-8 -*-

import pytest

from fixture.application import Application
from model.flight import Flight


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_buy_tickets(app):
    app.session.login(username="alexey", password="lolo")
    app.fill_flight_details()
    app.choose_flight()
    app.fill_reservation(Flight(name="Alexey", lastname="Kozlov", name2="Alexey's", lastname2="Wife"))
    app.session.logout()


def test_buy_tickets_2(app):
    app.session.login(username="alexey", password="lolo")
    app.fill_flight_details()
    app.choose_flight()
    app.fill_reservation(Flight(name="Vania", lastname="Taiwania", name2="Zozo", lastname2="Koleso"))
    app.session.logout()

