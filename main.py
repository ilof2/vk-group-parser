#! venv/bin/python3
import requests
import json
import os


group_id = '-29534144'
count = 100
access_token = os.environ['ACCESS_TOKEN'] 

# https://api.vk.com/method/wall.get?&v=5.52
url = 'https://api.vk.com/method/wall.get'

def parse_json(json_obj):

	''' Parse count of likes, comments, reposts and views of post. Return a tuple with all data '''

	posts = json_obj['response']['items']
	posts_inf = list()
	for post in posts:
		text = post['text']
		likes = 'likes '+ str(post['likes']['count'])
		comments = 'comments ' + str(post['comments']['count'])
		reposts = 'reposts ' + str(post['reposts']['count'])
		views = 'views ' + str(post['views']['count'])
		posts_inf.append((text, likes, comments, reposts, views))
	return posts_inf

def write_json(json_obj):

	''' Writing all posts json information in the .json file '''

	with open('posts.json', 'w') as file:
		json.dump(json_obj, file, indent=4, ensure_ascii=False)

def get_json(url):

	''' Makes a GET request for this url '''

	r = requests.get(url, params={'owner_id': group_id , 'count': count, 'offset': 0,'access_token': access_token, 'v': 5.87})
	return r.json()


def main():
	obj = get_json(url)
	l = parse_json(obj)
	for post in l:
		for inf in post:
			print(inf)
		print('#######################################')

if __name__ == '__main__':
	main()