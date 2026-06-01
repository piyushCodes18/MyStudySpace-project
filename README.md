# 📚 MyStudySpace

MyStudySpace is a productivity-focused web application designed to help students manage their studies efficiently in one place. It combines task management, goal tracking, note-taking, focus sessions, ambient study sounds, and progress analytics into a clean and user-friendly dashboard.

---

## 🚀 Features

### 🔐 User Authentication
- Simple Login / Sign-Up interface
- Stores user information locally using browser Local Storage
- Personalized welcome message

### 🎯 Daily Goal Setting
- Set your primary goal for the day
- Goal is saved locally and can be updated anytime

### ✅ To-Do List Manager
- Add study tasks
- Mark tasks as completed
- Delete completed or unwanted tasks
- Progress automatically updates based on completed tasks

### 📝 Notes Section
- Create and save study notes
- Notes persist even after page refresh
- Quick access to important information

### ⏱️ Focus Timer
- Pomodoro-style study timer
- Preset durations:
  - 15 Minutes
  - 25 Minutes
  - 45 Minutes
  - 60 Minutes
- Start, Pause, and Reset functionality
- Timer progress saved automatically

### 🎵 Ambient Study Sounds
- Play relaxing background sounds while studying
- Supports custom audio URLs
- Helps improve focus and concentration

### 📊 Progress Tracking
- Visual representation of study progress
- Tracks:
  - Completed Tasks
  - Remaining Tasks
  - Goal Completion
  - Notes Activity

### 📈 Interactive Charts
Built using Chart.js:

#### Overall Progress Chart
Displays:
- Completed Tasks
- Remaining Tasks

#### Subject-wise Progress Chart
Displays:
- Math
- Physics
- Chemistry
- Biology
- Social Studies

### 🌙 Dark Mode
- One-click Dark Mode toggle
- Preference saved automatically

### 📱 Responsive Design
- Works across desktops, tablets, and mobile devices
- Flexible and modern UI

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| HTML5 | Structure |
| CSS3 | Styling |
| JavaScript (Vanilla JS) | Functionality |
| Local Storage API | Data Persistence |
| Chart.js | Progress Visualization |

---

## 📂 Project Structure

```text
MyStudySpace/
│
├── index.html
├── main.html
├── progress.html
│
├── css/
│   └── style.css
│
├── js/
│   ├── app.js
│   ├── timer.js
│   └── progress.js
│
└── README.md
```

---

## ⚙️ How to Run

### Method 1: Using VS Code Live Server

1. Clone the repository

```bash
git clone https://github.com/your-username/MyStudySpace.git
```

2. Open the project in VS Code

3. Install the Live Server extension

4. Right-click `index.html`

5. Click:

```text
Open with Live Server
```

---

## 💾 Data Storage

This project does not require a database.

All user data is stored locally using:

```javascript
localStorage
```

Stored data includes:

- Username
- Email
- Tasks
- Notes
- Daily Goals
- Timer State
- Dark Mode Preference

---

## 📸 Application Pages

### Login Page
- User Login / Sign Up

### Dashboard
- Goal Management
- To-Do List
- Notes
- Focus Timer
- Ambient Sounds
- Resources Section

### Progress Page
- Overall Progress Chart
- Subject Progress Chart

---

## 🎯 Future Improvements

Potential future enhancements include:

- Backend Integration
- Cloud Database Support
- User Accounts & Authentication
- Study Streak Tracking
- Calendar & Schedule Management
- PDF Resource Library
- AI Study Assistant
- Notifications & Reminders
- Export Notes as PDF
- Multi-user Support

---

## 🧑‍💻 Author

**Piyush Arora**

B.Tech Computer Science Engineering Student

---

## 📄 License

This project is developed for educational and learning purposes.

Feel free to fork, modify, and improve it for your own use.

---

⭐ If you found this project useful, consider giving the repository a star.
