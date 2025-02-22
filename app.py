from flask import Flask, render_template, request, jsonify
from summary import summarize_email

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        email_text = request.form.get('email_text')
        print(f"Received email text: {email_text[:100]}...")  # Print first 100 chars
        
        if not email_text:
            return jsonify({'error': 'No email text provided'}), 400
            
        print("Calling summarize_email function...")
        summary = summarize_email(email_text)
        print(f"Received summary: {summary}")
        
        return jsonify({'summary': summary})
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Log the error
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 