import unittest

class UserAuth:
    def login(self, username, password):
        return username == "admin" and password == "password"
    

class UserProfile:
    def __init__(self, user_auth):
        self.auth = user_auth

    def get_profile(self, username, password):
        if self.auth.login(username, password):
            return {"username": username, "role": "admin"}
        return None


class TestIntegration(unittest.TestCase):

    def test_login_and_profile(self):
        auth = UserAuth()
        profile = UserProfile(auth)

        self.assertEqual(profile.get_profile("admin", "password"), 
                         {"username": "admin", "role": "admin"})
        self.assertIsNone(profile.get_profile("user", "wrongpass"))

if __name__ == '__main__':
    unittest.main()