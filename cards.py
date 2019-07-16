import json
from flask import Flask, render_template
from modules.airtable_call import airtable_call


# CARDS_PER_ROW = 3
# let's worry about grouping/rows in the front-end using CSS.
# This way we can be responsive to screen size without having to rewrite
# back-end logic

app = Flask(__name__)

@app.route('/cards', methods=['GET'])
def hello(city='Tallahassee'):
    cards = airtable_call()
    return render_template('cards.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
