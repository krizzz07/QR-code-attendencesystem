import json

# Function to load data from the JSON file
def load_data(filename):
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
    return data

# Function to save data to the JSON file
def save_data(filename, data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

# Load existing data from the JSON file (if it exists)
data = load_data("data.json")

# Get user input for name and ID
while True:
    name = input("Enter a name (or 'exit' to quit): ")
    if name == 'exit':
        break
    id = input("Enter an ID: ")
    
    # Check if the ID is already in use
    if any(user['id'] == id for user in data):
        print("ID already exists. Try again.")
    else:
        new_user = {
            "id": id,
            "name": name
        }
        data.append(new_user)
        print(f"User {name} with ID {id} added.")

# Save the updated data back to the JSON file
save_data("data.json", data)

print("Data has been appended to 'data.json'")
