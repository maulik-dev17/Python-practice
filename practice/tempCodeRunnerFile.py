
    "course": "Python",
    "hobbies": ["movie", "cricket", "music"]
}

# Print complete dictionary
print("Complete Dictionary:")
print(details)

# Print all keys and values
print("\nAll Keys and Values:")

for key, value in details.items():
    print(key, ":", value)

# Print first hobby
print("\nFirst Hobby:")
print(details["hobbies"][0])