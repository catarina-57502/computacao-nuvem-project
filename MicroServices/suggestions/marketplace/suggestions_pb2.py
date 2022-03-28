# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: suggestions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11suggestions.proto\"s\n\x0bgameRequest\x12\x14\n\x0crelease_date\x18\x01 \x01(\t\x12\x11\n\tdeveloper\x18\x02 \x01(\t\x12\x14\n\x0cpopular_tags\x18\x03 \x01(\t\x12\r\n\x05genre\x18\x04 \x01(\t\x12\x16\n\x0eoriginal_piece\x18\x05 \x01(\t\"\xb5\x03\n\x04Game\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05types\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0c\x64\x65sc_snippet\x18\x04 \x01(\t\x12\x16\n\x0erecent_reviews\x18\x05 \x01(\t\x12\x13\n\x0b\x61ll_reviews\x18\x06 \x01(\t\x12\x14\n\x0crelease_date\x18\x07 \x01(\t\x12\x11\n\tdeveloper\x18\x08 \x01(\t\x12\x11\n\tpublisher\x18\t \x01(\t\x12\x14\n\x0cpopular_tags\x18\n \x01(\t\x12\x14\n\x0cgame_details\x18\x0b \x01(\t\x12\x11\n\tlanguages\x18\x0c \x01(\t\x12\x14\n\x0c\x61\x63hievements\x18\r \x01(\t\x12\r\n\x05genre\x18\x0e \x01(\t\x12\x18\n\x10game_description\x18\x0f \x01(\t\x12\x16\n\x0emature_content\x18\x10 \x01(\t\x12\x1c\n\x14minimum_requirements\x18\x11 \x01(\t\x12 \n\x18recommended_requirements\x18\x12 \x01(\t\x12\x16\n\x0eoriginal_price\x18\x13 \x01(\t\x12\x16\n\x0e\x64iscount_price\x18\x14 \x01(\t\"t\n\rreviewRequest\x12\x10\n\x08\x61pp_name\x18\x01 \x01(\t\x12\x19\n\x11timestamp_updated\x18\x02 \x01(\x05\x12\x13\n\x0brecommended\x18\x03 \x01(\x08\x12!\n\x19\x61uthor_playtime_at_review\x18\x04 \x01(\x05\"\xbe\x04\n\x06Review\x12\x11\n\treview_id\x18\x01 \x01(\x05\x12\x0e\n\x06\x61pp_id\x18\x02 \x01(\x05\x12\x10\n\x08\x61pp_name\x18\x03 \x01(\t\x12\x10\n\x08language\x18\x04 \x01(\t\x12\x0e\n\x06review\x18\x05 \x01(\t\x12\x19\n\x11timestamp_created\x18\x06 \x01(\x05\x12\x19\n\x11timestamp_updated\x18\x07 \x01(\x05\x12\x13\n\x0brecommended\x18\x08 \x01(\x08\x12\x15\n\rvotes_helpful\x18\t \x01(\x05\x12\x13\n\x0bvotes_funny\x18\n \x01(\x05\x12\x1b\n\x13weighted_vote_score\x18\x0b \x01(\x05\x12\x15\n\rcomment_count\x18\x0c \x01(\x05\x12\x16\n\x0esteam_purchase\x18\r \x01(\x08\x12\x19\n\x11received_for_free\x18\x0e \x01(\x08\x12#\n\x1bwritten_during_early_access\x18\x0f \x01(\x08\x12\x16\n\x0e\x61uthor_steamid\x18\x10 \x01(\x05\x12\x1e\n\x16\x61uthor_num_games_owned\x18\x11 \x01(\x05\x12\x1a\n\x12\x61uthor_num_reviews\x18\x12 \x01(\x05\x12\x1f\n\x17\x61uthor_playtime_forever\x18\x13 \x01(\x05\x12&\n\x1e\x61uthor_playtime_last_two_weeks\x18\x14 \x01(\x05\x12!\n\x19\x61uthor_playtime_at_review\x18\x15 \x01(\x05\x12\x1a\n\x12\x61uthor_last_played\x18\x16 \x01(\x05\"$\n\x0cGameResponse\x12\x14\n\x05games\x18\x01 \x03(\x0b\x32\x05.Game\"*\n\x0eReviewResponse\x12\x18\n\x07reviews\x18\x01 \x03(\x0b\x32\x07.Review2m\n\x0bSuggestions\x12+\n\x0cgetSuggGames\x12\x0c.gameRequest\x1a\r.GameResponse\x12\x31\n\x0egetSuggReviews\x12\x0e.reviewRequest\x1a\x0f.ReviewResponseb\x06proto3')



_GAMEREQUEST = DESCRIPTOR.message_types_by_name['gameRequest']
_GAME = DESCRIPTOR.message_types_by_name['Game']
_REVIEWREQUEST = DESCRIPTOR.message_types_by_name['reviewRequest']
_REVIEW = DESCRIPTOR.message_types_by_name['Review']
_GAMERESPONSE = DESCRIPTOR.message_types_by_name['GameResponse']
_REVIEWRESPONSE = DESCRIPTOR.message_types_by_name['ReviewResponse']
gameRequest = _reflection.GeneratedProtocolMessageType('gameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GAMEREQUEST,
  '__module__' : 'suggestions_pb2'
  # @@protoc_insertion_point(class_scope:gameRequest)
  })
_sym_db.RegisterMessage(gameRequest)

Game = _reflection.GeneratedProtocolMessageType('Game', (_message.Message,), {
  'DESCRIPTOR' : _GAME,
  '__module__' : 'suggestions_pb2'
  # @@protoc_insertion_point(class_scope:Game)
  })
_sym_db.RegisterMessage(Game)

reviewRequest = _reflection.GeneratedProtocolMessageType('reviewRequest', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWREQUEST,
  '__module__' : 'suggestions_pb2'
  # @@protoc_insertion_point(class_scope:reviewRequest)
  })
_sym_db.RegisterMessage(reviewRequest)

Review = _reflection.GeneratedProtocolMessageType('Review', (_message.Message,), {
  'DESCRIPTOR' : _REVIEW,
  '__module__' : 'suggestions_pb2'
  # @@protoc_insertion_point(class_scope:Review)
  })
_sym_db.RegisterMessage(Review)

GameResponse = _reflection.GeneratedProtocolMessageType('GameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GAMERESPONSE,
  '__module__' : 'suggestions_pb2'
  # @@protoc_insertion_point(class_scope:GameResponse)
  })
_sym_db.RegisterMessage(GameResponse)

ReviewResponse = _reflection.GeneratedProtocolMessageType('ReviewResponse', (_message.Message,), {
  'DESCRIPTOR' : _REVIEWRESPONSE,
  '__module__' : 'suggestions_pb2'
  # @@protoc_insertion_point(class_scope:ReviewResponse)
  })
_sym_db.RegisterMessage(ReviewResponse)

_SUGGESTIONS = DESCRIPTOR.services_by_name['Suggestions']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GAMEREQUEST._serialized_start=21
  _GAMEREQUEST._serialized_end=136
  _GAME._serialized_start=139
  _GAME._serialized_end=576
  _REVIEWREQUEST._serialized_start=578
  _REVIEWREQUEST._serialized_end=694
  _REVIEW._serialized_start=697
  _REVIEW._serialized_end=1271
  _GAMERESPONSE._serialized_start=1273
  _GAMERESPONSE._serialized_end=1309
  _REVIEWRESPONSE._serialized_start=1311
  _REVIEWRESPONSE._serialized_end=1353
  _SUGGESTIONS._serialized_start=1355
  _SUGGESTIONS._serialized_end=1464
# @@protoc_insertion_point(module_scope)