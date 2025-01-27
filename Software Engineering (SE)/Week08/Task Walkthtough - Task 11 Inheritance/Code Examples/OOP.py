"""
Task Walkthrough - Task 11 Inheritance.
Practical example using the real-world
context of webpage forms.
"""


class LoginForm:
	"""
	Resembles as basic login form.
	"""
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.test = "A"  # Testing multiple inheritance.

	def confirmation(self):
		print(f"Hi, {self.username} you are in!")


class Search:
	"""
	Resembles as basic search form.
	Using this class as a second super class
	to demonstrate multiple inheritance.
	"""
	def __init__(self, search_term="test"):
		self.search_term = search_term
		self.test = "B"  # Testing multiple inheritance.


class RegisterForm(LoginForm):
	"""
	Single inheritance demonstration.
	The form adopts all attributes from the LoginForm class.
	The arguments are passed to the super class for
	initialization of the object.
	Additional attributes can be added to this new
	class.
	"""
	def __init__(self, username, password, email):
		super().__init__(username, password)
		self.email = email

	def confirmation(self):
		"""
		The confirmation method is being overridden. This
		new behaviour overwrites the original result.
		This allows the same methods to be used with
		differing results depending on context.
		"""
		print(f"Hi, {self.username} you are registered!")


class UserSearchForm(LoginForm, Search):
	"""
	Multiple inheritance demonstration.
	Since we are inheriting from two classes we need
	two super calls. The first does not need to be specified
	since the first class in order is always the default.
	"""
	def __init__(self, username, password, search_term):
		super().__init__(username, password)
		Search.__init__(self, search_term)  # Comment out and check result!


mistery_object = UserSearchForm("Fred", "1234", "test")
# Due to the method resolution order (MRO) in Python strange behaviour
# can occur when working with multiple inheritance.
# In the above example the MRO places LoginForm before Search.
# Only one super can be initialized at a time.
# Try running the below with line 64 and then without line 64.
# Since the Search class is manually initialized after the super
# call on line 63, Search overrides LoginForm as top of the order.
print(mistery_object.test)
