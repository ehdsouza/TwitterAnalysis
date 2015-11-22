__author__ = "Gourav"

from flask import Flask
from flask import jsonify
from flask import make_response

app = Flask(__name__)

feeds = [
    {"created_at": "Thu Nov 19 20:18:57 +0000 2015", "id": 667436924836122626, "id_str": "667436924836122626",
     "text": "Hartlepool Latest: Hartlepool Receive Advice Following Paris Tragedy https:\/\/t.co\/LYldUxmENc",
     "source": "\u003ca href=\"http:\/\/twitterfeed.com\" rel=\"nofollow\"\u003etwitterfeed\u003c\/a\u003e",
     "truncated": False, "in_reply_to_status_id": None, "in_reply_to_status_id_str": None, "in_reply_to_user_id": None,
     "in_reply_to_user_id_str": None, "in_reply_to_screen_name": None,
     "user": {"id": 20004483, "id_str": "20004483", "name": "Vital Hartlepool", "screen_name": "vitalhartlepool",
              "location": None, "url": "http:\/\/www.vitalhartlepool.co.uk", "description": None, "protected": False,
              "verified": False, "followers_count": 821, "friends_count": 38, "listed_count": 15, "favourites_count": 0,
              "statuses_count": 3765, "created_at": "Tue Feb 03 21:13:14 +0000 2009", "utc_offset": 0,
              "time_zone": "Lisbon", "geo_enabled": False, "lang": "en", "contributors_enabled": False,
              "is_translator": False, "profile_background_color": "9AE4E8",
              "profile_background_image_url": "http:\/\/pbs.twimg.com\/profile_background_images\/287700443\/BG_copy_LQ.jpg",
              "profile_background_image_url_https": "https:\/\/pbs.twimg.com\/profile_background_images\/287700443\/BG_copy_LQ.jpg",
              "profile_background_tile": True, "profile_link_color": "0084B4", "profile_sidebar_border_color": "BDDCAD",
              "profile_sidebar_fill_color": "DDFFCC", "profile_text_color": "333333",
              "profile_use_background_image": True,
              "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1437421370\/New_box._normal.jpg",
              "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1437421370\/New_box._normal.jpg",
              "default_profile": False, "default_profile_image": False, "following": None, "follow_request_sent": None,
              "notifications": None}, "geo": None, "coordinates": None, "place": None, "contributors": None,
     "is_quote_status": False, "retweet_count": 0, "favorite_count": 0, "entities": {"hashtags": [], "urls": [
        {"url": "https:\/\/t.co\/LYldUxmENc", "expanded_url": "http:\/\/bit.ly\/1I1WcC3",
         "display_url": "bit.ly\/1I1WcC3", "indices": [69, 92]}], "user_mentions": [], "symbols": []},
     "favorited": False, "retweeted": False, "possibly_sensitive": False, "filter_level": "low", "lang": "en",
     "timestamp_ms": "1447964337916"}
]


@app.route('/twitter/api/v1/feeds', methods=['GET'])
def get_twitter_feeds():
    return jsonify({
        'feeds': feeds
    })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
