## Premier League Winner Prediction 
![Python 3.10.11](https://img.shields.io/badge/Python-3.10.11-brightgreen.svg) ![scikit-learnn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg) <img src="https://img.shields.io/static/v1?label=&message=beautifulsoup&color=yellow" /> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/></br>

### How it was done
1. Starting from web scrapping from the <a href="https://fbref.com/en/comps/9/Premier-League-Stats">website-fbref.com</a> including team names of each season and each team data table from 2014 to 2024
You can look into bs4 code [here](https://github.com/rabibasukala01/premier-league-predictions/blob/main/PRE-PREDICT/scraping.ipynb).</br>
2. The EDA part and model making part is in [here](https://github.com/rabibasukala01/premier-league-predictions/blob/main/PRE-PREDICT/main.ipynb).
3. GradientBoostingClassifier remain high accuracy among others classifier with hyperparameter Tunings
4. Only 7 feature is used so it might be reason for only 66% accuracy or am i wrong? pull requests are welcome  

 If it helped you in anyway ,please do ⭐ the repository.

 A glimpse of the flask web app: </br>

 ![gif](https://github.com/rabibasukala01/premier-league-predictions/blob/main/web/demo.gif) </br>

 
 ### how to run locally this repo:
1. Clone the repo using git clone
2. create a virtual environment [prefered]
3. Install all the dependencies ``pip install -r requirements.txt``
4. `flask run --debug` to run the web app locally . Navigate to [url](http://127.0.0.1:5000/predict/) .

Happy coding! 
