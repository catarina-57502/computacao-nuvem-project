import os

from flask import Flask, render_template, json, request
import grpc

from suggestions_pb2 import gameRequest, reviewRequest, Game, Review
from suggestions_pb2_grpc import SuggestionsStub

app = Flask(__name__)

suggestions_host = os.getenv("SUGGESTIONS_HOST", "localhost")
suggestions_channel = grpc.insecure_channel(
    f"{suggestions_host}:50059")
suggestions_client = SuggestionsStub(suggestions_channel)

@app.route("/suggestionGames", methods=['GET'])
def suggestionsGames():
    suggGame = gameRequest(
        release_date = request.args.get('release_date'),
        developer = request.args.get('developer'),
        popular_tags = request.args.get('popular_tags'),
        genre = request.args.get('genre'),
        original_price = request.args.get('original_price')
    )
    suggGame_response = suggestions_client.GetGames(suggGame)
    map = {}
    i = 0
    for doc in suggGame_response.games:
        map[str(i)] = doc
        i+=1
    return json.dumps(map)

@app.route("/suggestionReviews", methods=['GET'])
def suggestionReviews():
    data = json.loads(request.data)
    suggReview = reviewRequest(
        app_name = data['app_name'],
        timestamp_updated = data['timestamp_updated'],
        recommended = data['recommended'],
        author_playtime_at_review = data['author_playtime_at_review']
    )
    suggReview_response = suggestions_client.GetReviews(suggReview)
    return suggReview_response.reviews