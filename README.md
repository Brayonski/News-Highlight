News Highlight
===================

- - - -
Author: [Brian Mutai](https://github.com/brayonski)
## Description
[News Highlight](https://github.com/Brayonski/News-Highlight) is a web appliction that displays a list of news sources from around the world. A user is able to click on a news source and view a list of articles from that source. Clicking on the news article will then redirect you to the news article's web page.

------------------------------------------------------------------------

## User Requirements

1. Your users should be able to see various news sources and select the ones they prefer
2. Your users should be able to see all the news articles from that news source
3. The user should see the image description and time the news article was created.
4. The user should also be able to click on an article and read it fully from the news source.

## Features

+ [x] List various news sources.
+ [x] List articles from the selected news source
+ [x] Redirect user to the actual article
+ [x] Categorize news sources 
+ [ ] Use flask sessions to save a users article snippet
+ [ ] Use browser cookies to store favourite news sources


## Installation

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python 3.6.4

### Cloning the repository
```bash
git clone https://github.com/Brayonski/News-Highlight && cd news-Highlight
```

### Creating a virtual environment
```bash
sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
```

### Installing dependencies
```bash
pip3 install -r requirements
```
The following libraries are required
* Flask==0.12.2
* Flask-Bootstrap==3.3.7.1
* Flask-Script==2.0.6
* gunicorn==19.7.1


### Running Tests
```bash
python3 manage.py test
```

### Running the web app in development
```bash
python3 manage.py server
```
Open the app on your browser, by default on `127.0.0.1:5000`.

## Live Demo

The web app can be accessed from the following link


## Quickstart

```
usage: manage.py [-?] {server,test,shell,runserver} ...

positional arguments:
  {server,test,shell,runserver}
    server              Runs the Flask development server i.e. app.run()
    test                Run the unit tests.
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help            show this help message and exit
```

## Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)

## Contributing

- Git clone [https://github.com/Brayonski/News-Highlight]
- Write your tests on `tests/`
- If everything is OK. push your changes and make a pull request. ;)

## License ([MIT License](http://choosealicense.com/licenses/mit/))

This project is licensed under the MIT Open Source license, (c) [Brian Mutai](https://github.com/Brayonski)