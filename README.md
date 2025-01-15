
# Volleyball Auto Reserve

This is a Selenium-based project designed to automate the process of reserving volleyball drop-in spots. The problem this project addresses is the difficulty of reserving spots in a timely manner, especially when spots fill up almost instantly. Often, when I'm available to book, I can only secure a spot for myself, leaving no room for my girlfriend. This automation tool aims to ensure that both of us can reserve spots, even when time is tight.

## Features

- Automates the process of reserving a volleyball spot.
- Provides a fast and efficient solution to secure spots before they fill up.
- Helps when you're unavailable to manually book or are only able to book for one person.

## Set up

To set up this project on your local machine, follow these steps:

### 1. Clone the repository

Start by cloning the repository to your local machine:

`git clone https://github.com/kevintian4/volleyball-auto-reserve.git`

### 2. Install dependencies

Once your virtual environment is active, install the necessary dependencies by running:

`pip install -r requirements.txt`

### 3. Set up environment variables

Create a `.env` file in the root directory of your project and add your own account credentials in the `.env` file. For example:

```bash
EMAIL = "myemail101@gmail.com"
PASSWORD = "strongPassword123"
```

### 4. Run the firstLogin.py and manually login once

After you have logged in once, you will never need to run this file again as your cookies will be saved and login will be automatic upon running `main.py`

### 5. For future reservations, simply run main.py

