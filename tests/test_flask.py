from unittest.mock import Mock
from flask import Flask, render_template, request, redirect
from movies_catalogue.main import app
from movies_catalogue import tmdb_client
import pytest

@pytest.mark.parametrize('list_type', (
  ('now_playing'),
  ('top_rated'),
  ('upcoming'),
  ('popular')
))  

def test_homepage(monkeypatch, list_type):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("movies_catalogue.tmdb_client.api_get", api_mock)

   with app.test_client() as client:
       response = client.get(f"/?list_type={list_type}")
       assert response.status_code == 200
       api_mock.assert_called_once_with(list_type)