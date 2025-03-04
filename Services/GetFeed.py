from API import API
import datetime
def get_feed():
    to_date = datetime.datetime.now()
    from_date = to_date - datetime.timedelta(days=1)
    posts = API.API().get_posts(from_date, to_date)
    return posts