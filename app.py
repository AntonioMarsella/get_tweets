from flask import Flask, redirect, request, jsonify
import tweepy
import os
from dotenv import load_dotenv
from functions import *
import sys

sys.path.append("./")

load_dotenv()


api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_KEY_SECRET")

app = Flask(__name__)


@app.route("/")
def index():
    print(request.args)
    handle = request.args.get("handle", None)
    print("You requested", handle)
    return jsonify({"results": list(get_all_tweets_json(handle))})


app.run()
