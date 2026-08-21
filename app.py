
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super-secret-key-lost-and-found'

# Temporary database (List to store items)
items = [
    {"id": 1, "title": "MacBook Pro M2", "category": "Electronics", "location": "Library 2nd Floor", "contact": "9876543210", "type": "Lost", "status": "Active"},
    {"id": 2, "title": "Gold Bracelet", "category": "Accessories", "location": "Cafeteria", "contact": "8765432109", "type": "Found", "status": "Active"}
]

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    title = request.form.get('title')
    category = request.form.get('category')
    location = request.form.get('location')
    contact = request.form.get('contact')
    item_type = request.form.get('type') # 'Lost' or 'Found'

    if title and category and location and contact:
        new_item = {
            "id": len(items) + 1,
            "title": title,
            "category": category,
            "location": location,
            "contact": contact,
            "type": item_type,
            "status": "Active"
        }
        items.append(new_item)
        flash('Item posted successfully!', 'success')
    else:
        flash('Please fill out all fields!', 'error')

    return redirect(url_for('index'))

@app.route('/resolve/<int:item_id>')
def resolve_item(item_id):
    for item in items:
        if item['id'] == item_id:
            item['status'] = 'Resolved'
            flash('Item marked as resolved!', 'success')
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)