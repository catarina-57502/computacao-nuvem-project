import os

from flask import Flask, render_template, json, request
import grpc

from suggestions_pb2 import gameRequest, reviewRequest, Game, Review
from suggestions_pb2_grpc import SuggestionsStub

app = Flask(__name__)

suggestions_host = os.getenv("SUGGESTIONS_HOST", "localhost")
suggestions_channel = grpc.insecure_channel(
    f"{suggestions_host}:50051")
suggestions_client = SuggestionsStub(suggestions_channel)

@app.route("/suggestionGames", methods=['GET'])
def suggestionsGames():
    data = json.loads(request.data)
    suggGame = gameRequest(
        release_date = data['release_date'],
        developer = data['developer'],
        popular_tags = data['popular_tags'],
        genre = data['genre'],
        original_price = data['original_price']
    )
    suggGame_response = suggestions_client.getSuggGames(suggGame)
    return json.dumps(suggGame_response.message)

@app.route("/suggestionReviews", methods=['GET'])
def suggestionReviews():
    data = json.loads(request.data)
    suggReview = reviewRequest(
        app_name = data['app_name'],
        timestamp_updated = data['timestamp_updated'],
        recommended = data['recommended'],
        author_playtime_at_review = data['author_playtime_at_review']
    )
    suggReview_response = suggestions_client.getSuggReviews(suggReview)
    return json.dumps(suggReview_response.message)