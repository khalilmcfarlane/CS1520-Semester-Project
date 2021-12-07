from google.cloud import datastore

def get_client():
    return datastore.Client()

def create_user():
    client = get_client()
    key = client.key('user')
    return datastore.Entity(key)


class User_manager():
    """An object representing a single chat message."""
    def find_user(self, username):
        client = get_client()
        query = client.query(kind = 'user')
        query.add_filter("username", "=", username) # find the specified username 
        user = None
        # if query.fetch.asList.size() == 0:
        #     return None

        for entity in query.fetch():
            user = entity
        return user


    def register(self, username, password, age, city, major, school):
        """Register a new user"""
        user = self.find_user(username)
        if user is not None:
            return "Username is taken"

        user = create_user()
        user['username'] = username
        user['password'] = password
        user['age'] = age
        user['city'] = city
        user['major'] = major
        user['school'] = school
        client = get_client()
        client.put(user)
        #add check for when username is satisfied

    def login(self, username, password):
        """Find a registed user"""
        user = self.find_user(username)
        if user == None:
            return "User Not Found"

        if user['password'] != password:
            return "Wrong Password"
        
        return user
