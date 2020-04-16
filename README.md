# python-web-scraper tutotial

To start let's take a look at what we are going to be scraping from the web.

`https://github.com/trending`

That is right we are going to make it nice and simple, so we are starting with the trending page of github.

# 1. Creating the project root folder

Go ahead and navigate to where you want your project to be located for me I have it under

`/Users/<USER>/Documents/Git/<NAME OF PROJECT ROOF FOLDER>` I named it python-web-scraper

Go to the folder and create virtual enviroment 

`pyhton3 -m venv env`

Wait for it to create the env folder in the root folder of your project.

# 2. Installing the needed dependencies

Open terminal and run the following:

`pip install requests beautifulsoup4`

This should install your dependencies and now we are ready to start

# 3. Python Code

In the root of your project create a file with `.py` extension 

Open the project with your preferred IDE and open the file. On the of your file we are going to import our modules. It would look like this.

`
import requests

from bs4 import BeautifulSoup

import csv
`




