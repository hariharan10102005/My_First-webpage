from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Value vandha number-ah mathu, illana crash aagaama 0 nu vechukko
    qty_input = request.form.get('qty', '0')
    try:
        qty = int(qty_input) if qty_input and qty_input.isdigit() else 0
    except:
        qty = 0

    item = request.form.get('item')
    prices = {'Shirt': 500, 'Pant': 700, 'T-Shirts': 300}
    price = prices.get(item, 0)

    total = price * qty 
    return render_template('index.html', total=total, item=item, qty=qty)

if __name__ == "__main__":
    app.run()
