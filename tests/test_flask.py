# import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# #print(BASE_DIR)
# from movies_catalogue import main
# from main import app #<<<--------- jak to zrobic poprawnie, kompilator podkreśla No name 'app' in module 'main'
# from movies_catalogue import tmdb_client  #<<<--------- terminal wyrzuca błąd ModuleNotFoundError: No module named 'tmdb_client'
# from unittest.mock import Mock
# import pytest

@pytest.mark.parametrize('list_type', (
  ('now_playing'),
  ('top_rated'),
  ('upcoming'),
  ('popular')
))  

def test_homepage(monkeypatch, list_type):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.api_get", api_mock)

   with app.test_client() as client:
       response = client.get(f"/?list_type={list_type}")
       assert response.status_code == 200
       api_mock.assert_called_once_with(list_type)