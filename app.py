from flask import Flask, render_template, request
import spacy
from spacy import displacy

app = Flask(__name__)

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_text', methods=['POST'])
def process_text():
    text = request.form['text']

    # Process the text
    doc = nlp(text)

    # Visualize the dependency tree using displacy
    html_dep = displacy.render(doc, style="dep", page=True)

    # Extract named entities
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]

    return render_template('result.html', text=text, html_dep=html_dep, entities=entities)

if __name__ == '__main__':
    app.run(debug=True)
