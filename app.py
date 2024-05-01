from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/menu.db'  # Путь к вашей базе данных
db = SQLAlchemy(app)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<MenuItem(id={self.id}, name={self.name}, price={self.price})>"

@app.route('/menu', methods=['GET'])
def get_menu():
    menu_items = MenuItem.query.all()
    menu = [{'id': item.id, 'name': item.name, 'price': item.price} for item in menu_items]
    return jsonify(menu)

if __name__ == '__main__':
    app.run(debug=True)
