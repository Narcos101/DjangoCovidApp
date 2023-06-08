# COVID-19 Tracker Application

<p align="center">
  <a href="https://github.com/Narcos101/DjangoCovidApp">
    <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cdc.gov%2Fmedia%2Fsubtopic%2Fimages.htm&psig=AOvVaw0p1QqWyUrPDqwmue2G6pWF&ust=1686298879354000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCOjBjf-es_8CFQAAAAAdAAAAABAE" alt="Logo" width="150" height="120">
  </a>
  
  ## 📌 Introduction
  
  This is a Django Application which consumes a [COVID-19 Data API](https://github.com/mathdroid/covid-19-api) to provide real-time statistics and data insight about the COVID-19 Pandemic that is currently wreaking a havoc around the world. The primary purpose of the project was to create a statistical visualization for the data obtained from this API and allow the user to get real-time updates about the Pandemic situation.
  
  ## 🏁 Technology Stack

* [Django](https://www.djangoproject.com/)


## 🏃‍♂️ Local Installation

1. Drop a ⭐ on the Github Repository. 
2. Clone the Repo by going to your local Git Client and pushing in the command: 

```sh
https://github.com/Narcos101/DjangoCovidApp.git
```

3. Install the Django Package using pip: 
```sh
pip install django
```

4. After moving to the main directory, Apply Database migrations,:
```sh
python manage.py makemigrations
python manage.py migrate
```
5. Atlast run the server:
```sh
python manage.py runserver
```

## 📜 LICENSE

[MIT](https://github.com/Narcos101/DjangoCovidApp/blob/main/LICENSE)
