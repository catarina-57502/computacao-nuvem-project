import os

from flask import Flask, render_template, json, request
import grpc

from suggestions_pb2 import gameRequest, reviewRequest, Game, Review
from suggestions_pb2_grpc import SuggestionsStub

app = Flask(__name__)


suggestions_channel = grpc.insecure_channel(os.environ['suggestionsserver_KEY'])
suggestions_client = SuggestionsStub(suggestions_channel)


def DocToGame(game):
    return  {
        "url" : game.url,
        "types" : game.types,
        "name" : game.name,
        "desc_snippet" : game.desc_snippet,
        "recent_reviews" : game.recent_reviews,
        "all_reviews" : game.all_reviews,
        "release_date" : game.release_date,
        "developer" : game.developer,
        "publisher" : game.publisher,
        "popular_tags" : game.popular_tags,
        "game_details" : game.game_details,
        "languages" : game.languages,
        "achievements" : game.achievements,
        "genre" : game.genre,
        "game_description" : game.game_description,
        "mature_content" : game.mature_content,
        "minimum_requirements" : game.minimum_requirements,
        "recommended_requirements" : game.recommended_requirements,
        "original_price" : game.original_price,
        "discount_price" : game.discount_price,
        "_id" : game._id
    }

def DocToReview(review):
    return  {
        "review_id" : review.review_id,
     "app_id" : review.app_id,
     "app_name" : review.app_name,
     "language" : review.language,
     "review" : review.review,
     "timestamp_created" : review.timestamp_created,
     "timestamp_updated" : review.timestamp_updated,
     "recommended" : review.recommended,
     "votes_helpful" : review.votes_helpful,
     "votes_funny" : review.votes_funny,
     "weighted_vote_score" : review.weighted_vote_score,
     "comment_count" : review.comment_count,
     "steam_purchase" : review.steam_purchase,
     "received_for_free" : review.received_for_free,
     "written_during_early_access" : review.written_during_early_access,
     "author_steamid" : review.author_steamid,
     "author_num_games_owned" : review.author_num_games_owned,
     "author_num_reviews" : review.author_num_reviews,
     "author_playtime_forever" : review.author_playtime_forever,
     "author_playtime_last_two_weeks" : review.author_playtime_last_two_weeks,
     "author_playtime_at_review" : review.author_playtime_at_review,
     "author_last_played" : review.author_last_played,
     "_id" : review._id
    }

@app.route('/healthz', methods=['GET'])
def healthz():
    return json.dumps("Ok")

@app.route("/suggestions/games", methods=['GET'])
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
        map[str(i)] = DocToGame(suggGame_response.games[str(i)])
        i+=1
    return json.dumps(map)

@app.route("/suggestions/reviews", methods=['GET'])
def suggestionReviews():
    suggReview = reviewRequest(
        app_name = str(request.args.get('app_name')),
        maxResults = str(request.args.get('maxResults')),
    )
    suggReview_response = suggestions_client.GetReviews(suggReview)
    map = {}
    i = 0
    for doc in suggReview_response.games:
        map[str(i)] = DocToReview(suggReview_response.games[str(i)])
        i+=1
    return json.dumps(map)