from users import User

# Create a new user and store the data
user = User('test_name', 'test_email', 'test_role')
user.store_data()

# Load the data and print it
loaded_user = User.load_data_by_user_name('test_name')
print(loaded_user.__dict__)