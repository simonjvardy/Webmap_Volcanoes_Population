![Simon Vardy](https://github.com/simonjvardy/simonjvardy/blob/main/assets/img/GitHub-name.png)

## About ##

This small Python app is a coding project to try out the Folium library to build an interactive map of US Volcano locations, overlayed on Stamen Terrain map tiles.

---

## Technologies ##

### **Languages** ###

- [Python3](https://www.python.org/)
  - Used to create the main application functionality
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
  - Used as the main markup language for the website content.

#### **Dependencies** ####

- [Pandas](https://pandas.pydata.org/)
  - Used to read the volcano CSV data file
- [Folium](http://python-visualization.github.io/folium/)
  - Used to build the HTML file with leaflet.js library

---

## Deployment ##

The website was developed using Gitpod using Git pushed to GitHub, which hosts the repository. I made the following steps to deploy the site:

### **Cloning Webmap_Volcanoes_Population from GitHub** ###

#### **Prerequisites** ###

Ensure the following are installed locally on your computer:

- [Python 3.6 or higher](https://www.python.org/downloads/)
- [PIP3](https://pypi.org/project/pip/) Python package installer
- [Git](https://git-scm.com/) Version Control

#### **Cloning the GitHub repository** ####

- navigate to [simonjvardy/Webmap_Volcanoes_Population](https://github.com/simonjvardy/Webmap_Volcanoes_Population) GitHub repository.
- Click the **Code** button
- **Copy** the clone url in the dropdown menu
- Using your favourite IDE open up your preferred terminal.
- **Navigate** to your desired file location.

Copy the following code and input it into your terminal to clone Sportswear-Online:

```Python
git clone https://github.com/simonjvardy/Webmap_Volcanoes_Population.git
```


#### **Creation of a Python Virtual Environment** ####


*Note: The process may be different depending upon your own OS - please follow this [Python help guide](https://python.readthedocs.io/en/latest/library/venv.html) to understand how to create a virtual environment.*


#### **Install the App dependencies and external libraries** ####

- In your IDE terminal window, install the dependencies from the requirements.txt file with the following command:

```Python
pip3 install -r requirements.txt
```

#### **Build the initial `index.html` page** ####

- in you IDE terminal window, enter:

```python
python3 map2_volcanoes.py
```

Run `index.html` locally to check the map and marker layer is functioning correctly