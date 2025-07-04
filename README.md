## 🏡 Housing Price Predictor(Boston)

A stylish and intelligent web application that predicts house prices in Boston using Linear Regression and a modern frontend built with Flask, HTML, CSS, and JavaScript.

---

### 🔮 Features

* 📊 **Linear Regression** based ML model
* 🌐 Web app powered by **Flask**
* ✨ Clean, glassy, animated frontend with:

  * Home page with intro & button
  * Step-by-step feature input form
  * Beautiful result display page
* 🎯 Real-time price prediction
* 💥 Proper error handling for bad inputs

---

### 📸 Screenshots


HOME PAGE:
https://github.com/codedbyasim/House-Price-Predection/blob/main/Screenshots/Home.PNG
FORM PAGE:
https://github.com/codedbyasim/House-Price-Predection/blob/main/Screenshots/Form1.PNG
RESULT:
https://github.com/codedbyasim/House-Price-Predection/blob/main/Screenshots/Result.PNG

---

### 🧠 Technologies Used

| Area             | Tech Stack                        |
| ---------------- | --------------------------------- |
| Machine Learning | Scikit-learn, NumPy, Pandas       |
| Frontend         | HTML5, CSS3, JavaScript (vanilla) |
| Backend          | Python + Flask                    |
| Styling          | Custom animations + glassmorphism |
| Model Saving     | Pickle (`.pkl` files)             |

---

### 📦 Installation Guide

```bash
# 1. Clone the repository
git clone https://github.com/codedbyasim/House-Price-Predection.git
cd House-Price-Predection

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # for macOS/Linux
venv\Scripts\activate     # for Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

### 🚀 Run the App

```bash
python app.py
```

Now open your browser and go to:
**[http://localhost:5000](http://localhost:5000)**

---

### 📂 Folder Structure

```
├── app.py
├── linear_model.pkl
├── scaler.pkl
├── poly.pkl
├── requirements.txt
├── templates/
│   ├── home.html
│   ├── predict.html
│   └── result.html
├── static/
│   └── style.css
└── BostonHousing.csv
```

---

### 🏗️ Dataset Info

We use the famous **Boston Housing Dataset**, which includes features like:

* Crime rate
* Land zoning
* Avg. rooms
* Distance to employment centers
* Tax, pupil-teacher ratio
* % of lower-income population, etc.

---

### 👨‍💻 About the Developer

**Asim Hanif**
A passionate Software Engineering student focused on solving real-world problems using Machine Learning and Web Development.

> 📬 Want to collaborate? Let’s connect!

---

### 📜 License

MIT License — feel free to use, modify, or build on it.

---




