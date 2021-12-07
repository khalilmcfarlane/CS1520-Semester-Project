from google.cloud import datastore



def get_client():
    return datastore.Client()

def create_post():
    client = get_client()
    key = client.key('post')
    return datastore.Entity(key)

class PostsManager():
     def __init__(self):
        self.countOfPosts = 0

     def find_post(self, title):
         """Queries for post by title"""
         client = get_client()         
         query = client.query(kind='post')
         query.add_filter("title", "=", title)
         post = None
         for entity in query.fetch():
             post = entity
         return post

     def store_post(self, title, article, username):
        """Stores new posts"""
        blog = create_post()
        self.countOfPosts = self.countOfPosts + 1
        blog['title'] = title
        blog['article'] = article
        blog['username'] = username 
        print(username)
        client = get_client()
        client.put(blog)

     def return_posts(self):
        client = get_client()
        query = client.query(kind='post')
        
        defaultPost = {}
        defaultsPosts = []
        if self.countOfPosts == 0:
            defaultPost['article'] = 'no posts yet'
            defaultPost['username'] = 'n/a'
            defaultPost['title'] = 'no title'
            defaultsPosts.append(defaultPost)
            return defaultsPosts
        
        posts = list(query.fetch())
        return posts
