from flask import Flask, render_template, request
from wallstreet import Stock

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock', methods=['POST'])
def stock():
    if request.method == 'POST':
        symbol = request.form['symbol']
        try:
            stock = Stock(symbol)
            price = stock.price
            return render_template('stock.html', symbol=symbol, price=price, change=stock.change)
        except:
            error = "Invalid symbol or something went wrong."
            return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
