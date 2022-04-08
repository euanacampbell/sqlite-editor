# Sqlite Editor

A website tool for testing knowledge of SQL.

## Usage

```bash
pip3 install -r requirements.txt
```
```bash
python3 app.py
```

## Limiting users
Instead of allowing the application to be accessed by any user, access can be limited through the ALLOWED_USERS environment variable.
The below setup will only allow a user to access the screens with a code of 'euan' or 'guest'.

```bash
export ALLOWED_USERS='["euan","guest"]'
```

## Changing questions
The questions and expected output can be changed through the below file. Updating the SQL will change how the expected output looks on the screen.

> /assets/datasets/questions.py

## License
[MIT](https://choosealicense.com/licenses/mit/)