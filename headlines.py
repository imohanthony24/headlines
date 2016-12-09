from flask import Flask
from flask import render_template
import feedparser

app = Flask(__name__)
BBC_FEED = "http://newsrss.bbc.co.uk/rss/newsonline_world_edition/front_page/rss.xml"
CNN = "http://rss.cnn.com/rss/edition_africa.rss"
rss_collection = [BBC_FEED, CNN]
@app.route('/')
def get_news() -> str:
	#"Pythonanywhere12"
	feed = feedparser.parse(rss_collection[0])
	first_article = feed['entries'][0]
	#articles =
	return render_template("home.html",article=first_article)

if __name__ == '__main__':
	app.run(port=5002, debug=True)

