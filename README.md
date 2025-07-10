
# Setup

- Make a virtual environemnt, assuming you have virtualenv installed.
    - Command - **python -m venv venv**, if you're on Windows, **python3 -m venv venv**, if you're on Debian based Linux distro.
- Activate the virtual environment.
    - Command - **source ./venv/bin/activate** for Debian based Linux distro.
- Install the packages
    - Command - **pip install -r requirements.txt**
- Run the application
    - Command - **flask --app src/main run --debug**
