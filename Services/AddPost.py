from API import API
from Models import Post
def add_post(post: Post):
    if post is None or len(post.creator_name) == 0 or len(post.content) == 0:
        return None
    did_add = API.add_post(post)
    return did_add