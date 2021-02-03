from flask import Blueprint, jsonify, request
from . import db
from .models import Movie

main = Blueprint('main', __name__)


@main.route('/api/add-movie', methods=['POST'])
def add_movie():
    """
    This function does the job of adding one entry of movie to the database
    """
    movie_data = request.get_json()

    if (movie_data == None):
        return 'Bad Request', 400

    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])

    db.session.add(new_movie)
    db.session.commit()

    return 'Done', 201


@main.route('/api/movie/all', methods=['GET'])
def movies():
    """
    This function does the job of getting all the movies from the database
    """
    query_result = Movie.query.all()
    movies_list = []
    for movie in query_result:

        movies_list.append({
            'id': movie.id,
            'title': movie.title,
            'rating': movie.rating
        })

    return jsonify({'movies': movies_list}), 200
