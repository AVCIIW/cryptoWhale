from database import getbalance, isregistered, register

print("Testing database connection...")

user_id = '1251558282863317045'
print(f"User {user_id} registered: {isregistered(user_id)}")
print(f"Balance: ${getbalance(user_id)}")

test_user = '999999999999999999'
print(f"\nTest user {test_user} registered: {isregistered(test_user)}")

print("\nDatabase connection works!")
