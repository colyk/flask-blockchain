from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
import blockChain

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # print(request.method )
    if request.method == 'POST':
        text = request.form['text']
        if len(text) < 1:
            return redirect(url_for('index'))
        try:
            make_proof = request.form['make_proof']
        except Exception:
            make_proof = False
        blockChain.write_block(text, make_proof)
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
