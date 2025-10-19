Secret Santa Emailer

A Python script that randomly assigns Secret Santas and sends personalized emails using Gmail SMTP.

## Features
- Random pairings
- Secure email delivery
- Easy setup with `.env`

## Setup
1. Clone the repo  
2. Run `pip install python-dotenv`  
3. Add a `.env` file:
   ```
   email=your_email@gmail.com
   password=your_app_password
   ```
4. Customize `names_and_emails` in `secret_santa.py`

## Run
```bash
python secret_santa.py
```

Each participant gets an email with their Secret Santa assignment!
```

Let me know if you want to add a preview mode or contributor section!
