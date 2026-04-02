from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime
import csv

app = Flask(__name__)
app.secret_key = "secret123"

# ---------------- DATABASE ---------------- #

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            rent_per_km INTEGER,
            available INTEGER,
            image TEXT
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS rentals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id INTEGER,
            user_name TEXT,
            id_proof TEXT,
            start_time TEXT,
            end_time TEXT,
            km INTEGER,
            cost INTEGER
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT
        )
    ''')

    # LOAD CSV
    try:
        with open('vehicles.csv', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cur.execute("SELECT * FROM vehicles WHERE name=?", (row['name'],))
                if cur.fetchone() is None:
                    cur.execute(
                        "INSERT INTO vehicles (name, rent_per_km, available, image) VALUES (?, ?, 1, ?)",
                        (row['name'], int(row['rent_per_km']), row['image'])
                    )
    except:
        print("CSV missing")

    # Admin
    cur.execute("SELECT * FROM users WHERE role='admin'")
    if cur.fetchone() is None:
        cur.execute("INSERT INTO users VALUES (NULL,'admin','admin','admin')")

    conn.commit()
    conn.close()


# ---------------- AUTH ---------------- #

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE username=? AND password=?",
                            (request.form['username'], request.form['password'])).fetchone()
        conn.close()

        if user:
            session['user'] = user['username']
            session['role'] = user['role']
            return redirect('/')
        else:
            return "Invalid login"

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# ---------------- MAIN ---------------- #

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user' not in session:
        return redirect('/login')

    conn = get_db_connection()

    search = request.form.get('search')

    if search:
        vehicles = conn.execute("SELECT * FROM vehicles WHERE name LIKE ?",
                                ('%' + search + '%',)).fetchall()
    else:
        vehicles = conn.execute("SELECT * FROM vehicles").fetchall()

    rentals = conn.execute('''
        SELECT rentals.*, vehicles.name as vehicle_name
        FROM rentals JOIN vehicles ON rentals.vehicle_id = vehicles.id
    ''').fetchall()

    total = conn.execute("SELECT SUM(cost) FROM rentals").fetchone()[0] or 0

    conn.close()

    return render_template('index.html',
                           vehicles=vehicles,
                           rentals=rentals,
                           user=session['user'],
                           role=session['role'],
                           total=total)


# ---------------- DASHBOARD ---------------- #

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()

    total_revenue = conn.execute("SELECT SUM(cost) FROM rentals").fetchone()[0] or 0
    total_rentals = conn.execute("SELECT COUNT(*) FROM rentals").fetchone()[0]
    available = conn.execute("SELECT COUNT(*) FROM vehicles WHERE available=1").fetchone()[0]

    conn.close()

    return render_template('dashboard.html',
                           revenue=total_revenue,
                           rentals=total_rentals,
                           available=available)


# ---------------- RENT ---------------- #

@app.route('/rent', methods=['POST'])
def rent():
    conn = get_db_connection()

    conn.execute('''
        INSERT INTO rentals (vehicle_id,user_name,id_proof,start_time,end_time,km,cost)
        VALUES (?,?,?,?,NULL,0,0)
    ''', (request.form['vehicle_id'], session['user'], request.form['id_proof'], datetime.now()))

    conn.execute("UPDATE vehicles SET available=0 WHERE id=?",
                 (request.form['vehicle_id'],))

    conn.commit()
    conn.close()

    return redirect('/')


@app.route('/return/<int:vehicle_id>', methods=['POST'])
def return_vehicle(vehicle_id):
    km = int(request.form['km'])

    conn = get_db_connection()

    rental = conn.execute(
        "SELECT * FROM rentals WHERE vehicle_id=? AND end_time IS NULL",
        (vehicle_id,)
    ).fetchone()

    vehicle = conn.execute("SELECT * FROM vehicles WHERE id=?", (vehicle_id,)).fetchone()

    cost = km * vehicle['rent_per_km']

    conn.execute('''
        UPDATE rentals SET end_time=?, km=?, cost=? WHERE id=?
    ''', (datetime.now(), km, cost, rental['id']))

    conn.execute("UPDATE vehicles SET available=1 WHERE id=?", (vehicle_id,))

    conn.commit()
    conn.close()

    return redirect(f'/invoice/{rental["id"]}')


# ---------------- INVOICE ---------------- #

@app.route('/invoice/<int:rental_id>')
def invoice(rental_id):
    conn = get_db_connection()

    data = conn.execute('''
        SELECT rentals.*, vehicles.name as vehicle_name
        FROM rentals JOIN vehicles ON rentals.vehicle_id = vehicles.id
        WHERE rentals.id=?
    ''', (rental_id,)).fetchone()

    conn.close()

    return render_template('invoice.html', r=data)


# ---------------- RUN ---------------- #

if __name__ == '__main__':
    init_db()
    app.run(debug=True)