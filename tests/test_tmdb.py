from flask import Flask, render_template, request, redirect
import tmdb_client
import pytest

def test_get_single_movie(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    assert details is not None

def test_get_movie_images(movie_id):
    movie_images_path = "backdrop_path"
    expected_default_size = 'w780'
    images_url = tmdb_client.get_movie_images(movie_id=movie_id)
    assert expected_default_size in images_url

def test_get_single_movie_cast(movie_id):
    cast = tmdb_client.get_single_movie_cast(movie_id)
    assert cast is not None



