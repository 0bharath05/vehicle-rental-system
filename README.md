# Vehicle Rental System

I made a web application that lets people rent vehicles manage rentals, calculate costs and generate invoices. The Vehicle Rental System includes user authentication, dashboard analytics and image-based vehicle listings.

---

## Features

* User Authentication. You can log in and register

* Vehicle Listing with Images. You can see the vehicles with pictures

* Dashboard with Analytics. You can see revenue, rentals and availability

* Track Rental Start and Return Time. You can keep track of when you rent and return a vehicle

* Automatic Cost Calculation based on Distance. The system calculates the cost based on how you drive

* Invoice Generation after Vehicle Return. You get an invoice after you return the vehicle

* Search Vehicles by Name. You can search for vehicles by name

* SQLite Database Integration. The system uses a database to store information

* CSV-based Vehicle Data Import. You can import vehicle data from a file

---

## Technologies Used

* Frontend: HTML, CSS, JavaScript. These are the technologies used for the user interface

* Backend: Python (Flask). This is the technology used for the server

* Database: SQLite. This is the technology used for storing data

* Version Control: Git and GitHub. These are the technologies used for tracking changes

---

## Project Structure

```

vehicle_rental_app/

── app.py

│── database.db

│── vehicles.csv

│── requirements.txt

│

├── templates/

│   ├── index.html

│   ├── login.html

│   ├── register.html

│   ├── dashboard.html

│   ├── invoice.html

│

├── static/

│   ├── style.css

│   ├── script.js

│   ├── images/

│

└── screenshots/

```

---

## How to Run the Project

### 1. Clone the Repository

```

git clone https://github.com/yourusername/vehicle-rental-system.git

```

### 2. Navigate to Project Folder

```

cd vehicle_rental_app

```

### 3. Install Dependencies

```

pip install -r requirements.txt

```

### 4. Run the Application

```

python app.py

```

### 5. Open in Browser

```

http://127.0.0.1:5000

```

---

## Default Admin Login

```

Username: admin

Password: admin

```

---

## Dashboard Features

* Total Revenue Generated. You can see how money the system has made

* Total Rentals. You can see how many vehicles have been rented

* Available Vehicles. You can see which vehicles are available

---

## Invoice System

After returning a vehicle the Vehicle Rental System automatically generates:

* Vehicle Name. The name of the vehicle

* Distance Travelled (KM). How far the vehicle was driven

* Total Cost. The cost of the rental

* Rental Time Details. When the vehicle was rented and returned

---


## Future Improvements

* Online Payment Integration. People could pay online

* Mobile Responsive Design. The system would work well on devices

* Cloud Deployment (Render / AWS). The system could be deployed on the cloud

* Vehicle Image Upload Feature. People could upload pictures of vehicles

* Password Encryption. Passwords would be encrypted for security

---

## Author

**Bharath**

---

## Project Highlights

This Vehicle Rental System project demonstrates:

* Full-stack web development using Flask. I used Flask to make the system

* Database integration with SQLite. I used SQLite for the database

* Real-world application features, like billing and analytics. The system has features that are used in life

* Clean UI/UX with responsive design. The system is easy to use and looks good

---

## License

This Vehicle Rental System project is developed for educational purposes.
