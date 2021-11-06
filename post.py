from google.cloud import datastore

def get_client():
    return datastore.Client()

def create_post():
    client = get_client()
    key = client.key('post')
    return datastore.Entity(key)

class PostsManager():
     
     def query_posts(self):
         '''Generic post query function'''
         client = get_client()
         query = client.query(kind='post')
         post = None
         for entity in query.fetch():
             post = entity
         return post

     
     def query_post_by_title(self, title):
         """Queries for post by title"""
         client = get_client()         
         query = client.query(kind='post')
         query.add_filter("title", "=", title)
         post = None
         for entity in query.fetch():
             post = entity
         return post

     def query_post_by_username(self, username):
          """Queries for post by user"""
          client = get_client()         
          query = client.query(kind='post')
          query.add_filter("username", "=", username)
          post = None
          for entity in query.fetch():
             post = entity
          return post                


     def store_post(self, title, article):
        """Stores new posts"""
        blog = create_post()
        blog['title'] = title
        blog['article'] = article
        client = get_client()
        client.put(blog)
    
     def store_user(self, username):
        """Associates user with post: Used when user needs to see all posts"""
        blog = create_post()
        blog['username'] = username
        client = get_client()
        client.put(blog)
