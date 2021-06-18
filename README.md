
# Video Game News 

A news aggregator for daily video games news. The project developed in Python using Django framewor and New API. 
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
pip install htmldate    
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



  
## Badges

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

  
## Authors

- [@SergioSimental](https://github.com/SergioSimenta)

  

  

  
## Screenshots
Homepage
![Alt text](https://github.com/SergioSimental/VGN/blob/b71ee37d5afca7b6aa56a16340bd8b778da85cfe/homepage_screenshot.png)

Archives page
![App Screenshot](https://i.postimg.cc/LqFghFTf/archives-screenshot.png)
