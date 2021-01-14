from flask import Flask, request

app = Flask(__name__)


@app.route('/add_product', methods=['GET', 'POST'])
def movies():

    if request.method == "GET":
        content = """
            <form action="/add_product" method = "POST">
                <label>
                    name:
                    <input type="text"
                            name = "name">
                </label>
                 <label>
                    description:
                    <input type="text"
                            name = "description">
                </label>
                 <label>
                    price:
                    <input type="number"
                            name = "price">
                </label>
                <label>
                    <button type="submit">
                    Submit<br>
                    </button>
                </label>

            </form>
            """
        return content
    else:
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        return f"Nazwa: {name}<br> Opis: {description}<br> Cena: {price}"




if __name__ == "__main__":
    app.run(debug=True)
