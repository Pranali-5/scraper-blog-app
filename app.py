from flask import Flask, request, jsonify
from scraper import scrape_content
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
scheduler = BackgroundScheduler()

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    content = scrape_content(url)
    return jsonify({'content': content})

def scheduled_scrape():
    # Example URL, replace with your logic
    url = "http://example.com"
    content = scrape_content(url)
    print(f"Scraped content from {url}: {content}")

scheduler.add_job(scheduled_scrape, 'interval', minutes=10)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True) 