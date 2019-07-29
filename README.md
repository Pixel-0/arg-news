# News Highlight

## Built By [Brayo  Mumo](https://github.com/brayomumo/)

## Description
Sirius News Highlights is a web application that displays a list of various news sources like BBC and CNN. On choosing a news source, it will preview the top news articles of the day. Clicking a news article will redirect the user to read it fully from the news source. It achieves this by using the [News API](https://newsapi.org/).

You can view the site at: https://brayomumo-newshighlight.herokuapp.com/

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* See various news sources 
* Select the ones they prefer
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click an article** | Redirected to the news source's site to read the entire article |

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/brayomumo/News-Highlight
        $ cd News-Highlight

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python 
        
* Installing Flask and other Modules

        $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
        $ python3.6 -m pip install Flask-Script
        
* Setting up the API Key
        
        To be able to gather article info from the News API you will need an API Key.
        
        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it: 
        
                export NEWS_API_KEY='<Your-Api-Key>'
                python3.6 manage.py server
                
        * Insert the API Key you received from News Api where <Your-Api-Key> is.
        
* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py tests
        
## Technologies Used
* Python3.6
* Flask

## License
MIT &copy;2019 [Brayomumo](https://github.com/brayomumo/)