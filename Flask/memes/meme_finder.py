from flask import Flask, render_template, request, redirect, url_for
import json
import requests

def get_meme():
    url = "https://meme-api.com/gimme/wholesomememes"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

app = Flask(__name__)
@app.route("/")
 
def index():
    meme_img, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_img, subreddit=subreddit)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)