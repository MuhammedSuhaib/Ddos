import threading
import requests

# Target website (your own server)
target_url = "https://your-website.com"

# Number of threads (simulated users)
num_threads = 5  # set number as needed

def attack():
    while True:
        try:
            response = requests.get(target_url)
            print(f"Sent request - Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

threads = []

for i in range(num_threads):
    thread = threading.Thread(target=attack)
    threads.append(thread)
    thread.start()

# Optional: join threads if you want to wait for them
for thread in threads:
    thread.join()
