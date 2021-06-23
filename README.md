
# Video Game News 

A news aggregator for daily video games news. 
User can search the API for articles using keywords related to gaming. 
The project developed in Python using Django framework and New API. 
Webpages are made using HTML Bootstrap 5 along with Python to get the articles information. 
Screenshots of app at the bottom.





## Project Structure

#### Virtual Environment

```
python -m venv folder_name
```

#### Dependencies

```
python -m pip --upgrade pip
pip install django 
pip install request   
```

| Dependencies | Description                       |
| :-------- | :-------------------------------- |
| `PIP` | **Required**. Install dependencies |
| `Django`    | **Required**. Web App framework|
| `request`    | **Required**. Fetch the articles|
| `htmldate`    | Used to get the current date|

#### Django

```
django-admin startproject folder_name
python manage.py makemigrations
python manage.py migrate
python manage.py runserver   
```
| Commands | Description                       |
| :-------- | :-------------------------------- |
| `django-admin startproject` | **Required**. Create Django project structure |
| `python manage.py makemigrations`    | **Required**. Create new migrations based on the changes you have made to your models|
| `python manage.py migrate`    | **Required**. Applying and unapplying migrations|
| `python manage.py runserver`    | **Required**. Run the web app |

## News API Reference

#### Get API KEY 
An account must be created to get a personal API key.

```http
https://newsapi.org
```

#### Using KEY
The url can be changed to get different news. Check documentation in News API.
```http
https://newsapi.org/v2/everything?q=gaming&from={DATE}&sortBy=popularity&language=en&apiKey={API_KEY}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `API_KEY` | `string` | **Required**. API key to fetch articles |
| `DATE`    | `string` | **Required**. Date to fetch daily articles|


## Script

#### Running Script 
Change bat file adding the path to python exe and scripts.py surrounded by single quotes.
Example: 'path\python.exe' 'path\scripts.py'

#### Set up Windows Task Scheduler
Create basic task, name the task, set to daily, change date and time to when you want to start running the script, start program, add path to scripts.py to Program/script text field and click finish. 


## Todo:
- Host web app
- Move scripts task onto server
- CI/CD

  
## Badges

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

  
## Authors

- [@SergioSimental](https://github.com/SergioSimenta)

  

  

  
## Screenshots
Homepage: Searched Xbox
![Alt text](https://github.com/SergioSimental/VGN/blob/6513209542d38657cd3184e1146ef0b84ebe2f82/homepage-search.png)

Archives Page
![App Screenshot](https://github.com/SergioSimental/VGN/blob/6513209542d38657cd3184e1146ef0b84ebe2f82/archives.png)

Xbox Search Result Page
![App Screenshot](https://github.com/SergioSimental/VGN/blob/6513209542d38657cd3184e1146ef0b84ebe2f82/search_result.png)
