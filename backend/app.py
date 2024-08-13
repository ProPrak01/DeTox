from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize the Hugging Face zero-shot classifier
classifier = pipeline("zero-shot-classification")

@app.route('/classify', methods=['POST'])
def classify():
    # Extract the list of video titles and the category from the request
    data = request.json
    titles = data.get('titles', [])
    category = data.get('category', '')

    # Perform zero-shot classification for each title
    results = []
    for title in titles:
        result = classifier(title, [category])
        # Check if the category has the highest score
        is_match = result['labels'][0].lower() == category.lower()
        results.append(is_match)

    # Return the classification results
    return jsonify(results)

# Vercel's serverless function handler
def handler(request):
    return app(request.environ, start_response)
