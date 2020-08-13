from flask import Flask, render_template, request, redirect
from movies_catalogue import tmdb_client
import pytest
from unittest.mock import Mock

def test_get_single_movie():
    single_movie = tmdb_client.get_single_movie(movie_id=2)
    assert single_movie is not None

def test_get_single_movie_cast(monkeypatch):
   mock_single_movie_cast = ['Movie 1', 'Movie 2']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


   single_movie_cast = tmdb_client.get_single_movie_cast(movie_id=2)
   assert single_movie_cast == mock_single_movie_cast


# def test_get_single_movie_cast():
#     single_movie_cast = tmdb_client.get_single_movie_cast(movie_id=3)
#     assert single_movie_cast is not None

# def test_get_movie_images():
#     backdrop_path = "backdrop_path"
#     expected_default_size = 'w780'
#     images_url = tmdb_client.get_movie_images(movie_id=2)
#     assert expected_default_size in images_url



