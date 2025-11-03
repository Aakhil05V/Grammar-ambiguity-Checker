from flask import Flask, render_template, request
import nltk
from nltk import CFG

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    grammar_text = ''
    sentence = ''
    if request.method == 'POST':
        grammar_text = request.form.get('grammar', '').strip()
        sentence = request.form.get('sentence', '').strip()
        try:
            grammar = CFG.fromstring(grammar_text)
            parser = nltk.ChartParser(grammar)
            trees = list(parser.parse(sentence.split())) if sentence else []
            ambiguous = len(trees) > 1
            result = {
                'parse_count': len(trees),
                'ambiguous': ambiguous,
            }
        except Exception as e:
            error = str(e)
    return render_template('index.html', result=result, error=error, grammar=grammar_text, sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True)
