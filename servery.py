from flask import Flask, request, send_from_directory
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('templates', 'index.html')

@app.route('/fetch_deals')
def fetch_deals():
    url = request.args.get('url')
    if not url:
        return "No URL provided.", 400

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text and clean up whitespace
        main_content = soup.get_text(separator=' ', strip=True)
        # Remove extra spaces
        main_content = re.sub(r'\s+', ' ', main_content)
        # Split into lines and remove empty lines
        lines = [line.strip() for line in main_content.split('.') if line.strip()]
        # Join lines with a single newline
        cleaned_content = '\n'.join(lines)
        
        return cleaned_content

    except requests.RequestException as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
