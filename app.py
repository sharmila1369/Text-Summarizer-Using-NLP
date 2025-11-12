from flask import Flask, request, jsonify, render_template
from summary import extractive_summarization

# ✅ Create Flask app BEFORE using @app.route
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json(force=True)
        text = data.get('text', '')
        num_sentences = int(data.get('num_sentences', 2))

        if not text.strip():
            return jsonify({'error': 'No text provided'}), 400

        summary = extractive_summarization(text, num_sentences)
        return jsonify({'summary': summary})

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
