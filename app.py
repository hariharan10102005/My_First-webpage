from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Form
    item = request.form.get('item')
    if item == 'Primium Ticket':
        price = 210
    elif item == 'First Class Ticket':
        price = 190
    elif item == 'Second Class Ticket':
        price = 150
    elif item == 'Lower Class Ticket':
        price = 120
    else:
        price = 0

    qty = request.form.get('qty',0)
    
    
   qty =int(qty_input) if qty_input else 0
except ValueError:
       qty = 0


    
    # Bill calculation
    total = price * qty
return render_template('index.html', total=total,
                      item=item, qty=qty)
    
    return f"""
    <h2>--- Bill Receipt ---</h2>
    <p>Item: {item}</p>
    <p>Price: Rs.{price}</p>
    <p>Quantity: {qty}</p>
    <hr>
    <h3>Total Amount: Rs.{total}</h3>
    <a href="/">Next Bill</a>
    """


if __name__ == '__main__':

    app.run()


