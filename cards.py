import json
from flask import Flask, render_template
from modules.airtable_call import airtable_call


app = Flask(__name__)

@app.route('/cards', methods=['GET'])
def hello(city='Tallahassee'):
    cards = airtable_call()
    return render_template('cards.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
