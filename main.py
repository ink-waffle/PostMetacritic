import praw
import os
import openai
import json
from Keys import openai_keys

openai.organization = openai_keys['organization']
openai.api_key = openai_keys['api_key']
# Load the JSON data from the file
with open('Source/reddit-oppenheimer-286.json', 'r') as json_file:
    comments_by_post = json.load(json_file)

class Post:
    def __init__(self, title, analysis, raw):
        self.title = title
        self.analysis = analysis
        self.raw = raw

redditSentiment = list()
iter = 0
for title, comments in comments_by_post.items():
    prompts = [{"role": "system", "content":
        'Analyse the sentiment of 16 Reddit comments under a post - "' + str(title) + '", use the delimiter "\n\n==COMMENT==\n\n" to distinguish individual comments. Your goal is to write sentiment analysis for each comment towards the topic - "movie Oppenheimer", in a format RATING - KEYWORDS. Where RATING is a number from 0 to 10, with 0 representing drastically negative attitude to the topic, 10 for a drastically positive, or 5 for neutral or a comment unrelated to a topic. KEYWORDS are 2-3 words or phrases, separated by a comma (,), taken from the comment most indicative of reasons for such attitude. Use a semicolon (;) as the delimiter between each entry.'}]
    delimeter = "\n\n==COMMENT==\n\n"
    prompt = delimeter.join(comments)
    prompts.append({"role": "user", "content": prompt})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k", messages=prompts)
    reply = chat.choices[0].message.content
    redditSentiment.append(Post(title, reply.split(';'), prompt))
    iter += 1
    print(iter + "/" + len(comments_by_post))