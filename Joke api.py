import requests

def joke():
    # API url for random joke
    url = "https://official-joke-api.appspot.com/random_joke"
    
    #fetches the data from the API
    response = requests.get(url)

    # Check if the request was successful and prints the joke if not it prints an error message
    if response.status_code == 200:
        joke_data = response.json()
        setup = joke_data['setup']
        punchline = joke_data['punchline']
        print(f"{setup}\n{punchline}")
        
        # Save joke to file
        joke_txt(f"{setup}\n{punchline}")
    else:
        print("Failed to retrieve a joke.")

def joke_txt(entry, filename="joke.txt"):
    # Append so old jokes aren’t lost
    with open(filename, "a") as file:
        file.write(entry + "\n")

joke()
