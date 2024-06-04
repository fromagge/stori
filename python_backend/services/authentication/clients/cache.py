import os

import redis

redis_client = redis.StrictRedis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'), db=os.getenv('REDIS_DB'), decode_responses=True)


def make_access_key(user_id):
	return f'{user_id}_access'


def make_refresh_key(user_id):
	return f'{user_id}_refresh'


def store_token(user_id, token):
	expiration_time = os.getenv('TOKEN_EXPIRATION', 3600)
	access_name = make_access_key(user_id)
	redis_client.set(access_name, token, ex=expiration_time)


def store_refresh_token(user_id, refresh_token):
	refresh_token_expiration = os.getenv('REFRESH_TOKEN_EXPIRATION', 86400)
	refresh_name = make_refresh_key(user_id)
	redis_client.set(refresh_name, refresh_token, ex=refresh_token_expiration)


def get_token(user_id):
	access_name = make_access_key(user_id)
	if not redis_client.exists(access_name):
		return None
	return redis_client.get(access_name)


def get_refresh_token(user_id):
	refresh_name = make_refresh_key(user_id)
	return redis_client.get(refresh_name)
