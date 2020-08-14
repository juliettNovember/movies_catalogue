import sys
sys.path.insert(0, '/Users/justynanowakowska/Documents/Projekty/movies_project/movies_catalogue')
from flask import Flask, render_template, request, redirect
from movies_catalogue import main
from main import app
from movies_catalogue import tmdb_client
import pytest
from unittest.mock import Mock

def test_get_single_movie():
    single_movie = tmdb_client.get_single_movie(movie_id=2)
    assert single_movie is not None

#Wroce do tego :)
# def test_get_single_movie_cast(monkeypatch):
#    mock_single_movie_cast = ['Movie 1', 'Movie 2']
#    requests_mock = Mock()
#    response = requests_mock.return_value
#    response.json.return_value = mock_single_movie_cast
#    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

#    single_movie_cast = tmdb_client.get_single_movie_cast(movie_id=2)
#    assert single_movie_cast == mock_single_movie_cast

def test_get_single_movie_cast():
    single_movie_cast = tmdb_client.get_single_movie_cast(movie_id=3)
    assert single_movie_cast is not None

def test_get_movie_images():
    images_url = tmdb_client.get_movie_images(movie_id=2)
    assert images_url is not None


# def test_homepage(monkeypatch):
#    api_mock = Mock(return_value={'results': []})
#    monkeypatch.setattr("tmdb_client.api_get", api_mock)

#    with app.test_client() as client:
#        response = client.get('/')
#        assert response.status_code == 200
#        api_mock.assert_called_once_with('popular')

list_type = [
    (list1, list2, list3, list4)
]

@pytest.mark.parametrize('now_playing, top_rated, upcoming, popular', list_type)
def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.api_get", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular')

# @pytest.mark.parametrize('now_playing, top_rated, upcoming, popular', testdata)
# def test_list_type(list_type):
#     response = client.get(f"/movie/{now_playing}")
#     assert response is not None
        
