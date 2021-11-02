from google.cloud import datastore

def get_client():
    return datastore.Client()

def create_post():
    client = get_client()
    key = client.key('new_post')
    return datastore.Entity(key)

class PostsManager():

     def store_post(self, title, article):
        """Stores new posts"""
        blog = create_post()
        blog['title'] = title
        blog['article'] = article
        client = get_client()
        client.put(blog)