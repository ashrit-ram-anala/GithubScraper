from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

    if request.method == 'POST':
        data = request.json

        
        if data.get('ref') == 'refs/heads/main': 
            print("Received push event. Running scraper...")
            subprocess.call(['python3', 'scraper.py'])
            return jsonify({"message": "Scraper executed successfully!"}), 200
        else:
            return jsonify({"message": "Ignored non-main branch push"}), 200

    return jsonify({"message": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
