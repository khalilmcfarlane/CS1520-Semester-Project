from google.cloud import datastore

def get_client():
    return datastore.Client()

def create_post():
    client = get_client()
    key = client.key('post')
    return datastore.Entity(key)

class PostsManager():
     
     def find_post(self, title):
         """Queries for post by title"""
         client = get_client()         
         query = client.query(kind='post')
         query.add_filter("title", "=", title)
         post = None
         for entity in query.fetch():
             post = entity
         return post

     def store_post(self, title, article, tag):
        """Stores new posts"""
        blog = create_post()
        blog['title'] = title
        blog['article'] = article
        blog['tag'] = tag
        client = get_client()
        client.put(blog)