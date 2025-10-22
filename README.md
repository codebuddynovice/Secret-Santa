Markdown
🎅 Secret Santa Emailer

A simple and fun Python project that automates your Secret Santa gift exchange!  
This script randomly assigns Secret Santas and sends personalized emails to each participant using Gmail SMTP.

---

🧩 Features

- ✅ Random Secret Santa assignments (no one gifts themselves)
- 📧 Automatic email notifications via SMTP
- 🔒 Secure configuration using environment variables (`.env`)
- 💡 Lightweight and beginner-friendly Python script

---

🏗️ Project Structure

```

Secret-Santa/
│
├── secret_santa.py     # Main script (handles assignments and email sending)
├── .gitignore          # Ignore sensitive files and cache
├── README.md           # Project documentation (this file)
└── .env (optional)     # SMTP credentials and settings

````

---

⚙️ How It Works

1. Load participants (names + emails) from the script or an external file.
2. Randomly pair participants ensuring **no one is assigned themselves**.
3. Use Gmail’s SMTP server to send each participant an email revealing their giftee.
4. Optionally log all assignments for the organizer.

---

## 🧠 Architecture Diagram

<img width="124" height="136" alt="image" src="https://github.com/user-attachments/assets/e91c899e-01c6-4ba2-b826-90b90409c783" />

---

🔄 Process Flow

```
sequenceDiagram
    participant Organizer
    participant Script
    participant SMTP
    participant Participant

    Organizer->>Script: Run `python secret_santa.py`
    Script->>Script: Load .env (SMTP credentials)
    Script->>Script: Randomly assign pairs
    Script->>SMTP: Connect and authenticate
    loop For each participant
        Script->>SMTP: Send email (Your recipient is X!)
        SMTP->>Participant: Deliver email
    end
    Script->>Organizer: Log assignments (optional)
```

---

⚙️ Setup & Configuration

1️⃣ Install Requirements

Make sure you have Python 3 installed.
No external packages are required for basic functionality.

2️⃣ Set Up Environment Variables

Create a `.env` file in your project folder:

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=youremail@gmail.com
SENDER_PASSWORD=your_app_password
```

💡 *For Gmail accounts with 2FA, use an [App Password](https://myaccount.google.com/apppasswords).*

3️⃣ Add Participants

Inside `secret_santa.py`, list your participants in this format:

```python
participants = {
    "Alice": "alice@example.com",
    "Bob": "bob@example.com",
    "Charlie": "charlie@example.com"
}
```

4️⃣ Run the Script

```bash
python secret_santa.py
```

Each participant will receive an email with their assigned recipient.

---

🎨 Example Output

```bash
Assigning Secret Santas...
Email sent to Alice!
Email sent to Bob!
Email sent to Charlie!
All emails sent successfully! 🎁
```
---

🚀 Future Enhancements

🔹 Read participants from a CSV or JSON file
🔹 Add exclusions (e.g., couples shouldn’t gift each other)
🔹 Use HTML email templates
🔹 Add logging and error reporting
🔹 Web or CLI interface for signups

---

🧾 License
This project is open source under the [MIT License](LICENSE).

---

*Happy gifting and Merry Coding!* 🎁🎄
