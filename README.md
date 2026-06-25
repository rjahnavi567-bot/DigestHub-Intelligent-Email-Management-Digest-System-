## 🚧 Development Status

This project is currently under active development. New features such as AI-powered email summarization, Gmail integration, and automated digest generation are being implemented.

# 📧 DigestHub – Intelligent Email Management & Digest System 

An intelligent email management system built with **Python, Flask, and SQLite** that organizes, categorizes, stores, and displays emails through a user-friendly web dashboard. The project aims to simplify email management by enabling quick search, efficient categorization, and easy access to important messages.

---

## 🚀 Project Overview

Managing large volumes of emails can be time-consuming and overwhelming. Email Digest Bot addresses this challenge by automatically organizing emails into categories and providing a centralized dashboard for searching and viewing email content.

The application stores emails in a database, tracks category statistics, and allows users to retrieve emails quickly through a clean web interface.

---

## ✨ Current Features

### Email Storage

* Stores emails in a SQLite database.
* Maintains subject, sender, category, and email content.

### Automatic Categorization

* Organizes emails into predefined categories.
* Displays category-wise email counts.

### Search Functionality

* Search emails using keywords.
* Retrieve relevant emails instantly.

### Interactive Dashboard

* User-friendly Flask-based web interface.
* Displays categorized email data.

### Email Viewer

* Open and read complete email content.
* Easy navigation through stored emails.

### Database Integration

* Efficient email storage using SQLite.
* Lightweight and easy to maintain.

---

## 🛠️ Technology Stack

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Core Programming Language  |
| Flask      | Backend Web Framework      |
| SQLite     | Database Storage           |
| HTML       | Frontend Structure         |
| CSS        | User Interface Styling     |
| Jinja2     | Dynamic Template Rendering |

---

## 🏗️ Project Architecture

```text
Email Source
      │
      ▼
Email Processing Layer
(Parse & Categorize Emails)
      │
      ▼
SQLite Database
(Store Email Information)
      │
      ▼
Flask Backend
(Search & Retrieval Logic)
      │
      ▼
Web Dashboard
(Display Emails & Statistics)
```

---

## 📂 Project Structure

```text
Email-Digest-Bot/
│
├── app.py
├── emails.db
│
├── templates/
│   ├── home.html
│   └── email_view.html
│
├── static/
│   ├── css/
│   └── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Email-Digest-Bot.git
cd Email-Digest-Bot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Browser

```text
http://127.0.0.1:5000
```

---

## 🎯 Future Enhancements

* AI-powered email summarization
* Gmail API integration
* Daily digest generation
* Email priority scoring
* Sentiment analysis
* Keyword extraction
* Smart filtering
* Multi-user authentication
* Export digest as PDF
* Automated notifications

---

## 📚 Learning Outcomes

Through this project, I gained experience in:

* Flask Web Development
* Database Design with SQLite
* Backend Development using Python
* Search and Filtering Systems
* Dynamic Template Rendering
* Full-Stack Application Development

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

**Jahnavi Reddy**

B.Tech CSE Student | Python Developer | Full Stack & AI Enthusiast

If you found this project useful, consider giving it a ⭐ on GitHub.
