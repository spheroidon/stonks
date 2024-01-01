from flask import Flask, render_template, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    if request.method == 'POST':
        ticker = request.form['ticker']
        stock = yf.Ticker(ticker)
        data = stock.history(period='3mo')  # You can adjust the period as needed
        labels = data.index.strftime('%Y-%m-%d').tolist()
        values = data['Close'].tolist()
        return {'labels': labels, 'values': values}

if __name__ == '__main__':
    app.run(debug=True,port=30025)
