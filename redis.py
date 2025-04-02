# Import module
import redis

# Create connection
r = redis.Redis(host='localhost', port=6379, db=0)

# Setting key-value pair
r.set('eid', '101')

# Get value for given key
value=r.get('eid')

# Print the value
print(value)