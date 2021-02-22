# ch_robinson_web_app

C.H. Robinson web app for path finding.


# Application Logic

Code for Django project root can be found in the north_american_transport folder while the frontend can be found in the path_finder folder, mostly in the `views.py` file.


Breadth first search was used to find routes between the countries. The data was modeled as a dictionary (see `views.py`). Originially, the data points (countries) were associated with one another by the django `ManyToManyField`. Each country was given an ID (1,2,3,...) which was used as the primary key. I thought I could simply convert this into a temporary Node class with a field for bordering countries associated with the. `ManyToManyField` and run BFS on the collection of  points. However, this proved not to be as simple as I'd hoped, and I ended up changing the way I modeled the data. The original model for countries can still be found in `models.py`. 



# Presentation Logic

Django forms were used to read input from users (see `forms.py`). This greatly simplified the process of retrieving the data, manipulating it, and returning new data. Also, a huge benefit was constraints could be placed directly on the forms themselves such as max character length. And, to provide an aesthetic touch, the django-crispy-forms library was used to 'crisp' up those visuals. Django-crispy-forms is another great library, as it allowed me to customize the form's visual properties directly on the form right from its initialization, rather than strewn about in html and css.

The app consists of only one page. Static files can be found in the `/static/` and `/assets/` folders. The `index` page waits for a post request in the form of a form (haha), cleans and validates the data, and sends the generated list of strings back to the client. The map was provided for testing purposes and additional visual detail.


# Data 

Initially, the data was modeled using Django's model library, as can be seen in `map_data.json`. The data were then loaded in as fixtures pre-deployment. They were associated with a sqlite3 database, as is the default for Django projects. This made the initial set up of the web app easy and lightweight, but my approach to solving the shortest path problem conflicted with this structure. After too many failures to count, I decided I would use python's native dictionary structure, which proved to be much more manageable.




