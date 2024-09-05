# Todo list

### This site allows you to create, organize, and prioritize your tasks with ease.

## Installing / Getting started

### Python3 must be already installed

```shell
git clone https://github.com/Anon920/restaurant_kitchen_service.git
cd restaurant-kitchen-service
```
```shell
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```
## Set Up Database
```shell
python manage.py makemigrations
python manage.py migrate
```

## Start the app
```shell
python manage.py runserver
```

At this point, the app runs at http://127.0.0.1:8000/.

## Demo

### DB Structura:

![todo-list.drawio.png](img%20and%20diagram%2Ftodo-list.drawio.png)

### Task

![Tasks.png](img%20and%20diagram%2FTasks.png)

### Tag

![tags.png](img%20and%20diagram%2Ftags.png)
