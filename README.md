<h1>Micromort Microservice</h1>


Installation Instructions:
---------

1. Open a terminal, navigate to the parent folder which should contain the project, and enter ```git clone https://github.com/bcvance/micromort-microservice.git```
2. Open the newly created directory, which should be named "micromort-microservice" in your code editor of choice
3. Once the "micromort-microservice" directory is open in your editor, create a virtual environment for your project with ```python3 -m venv venv``` in the terminal
4. Activate the virtual environment with ```source venv/bin/activate```
5. Once the venv is activated, download the project's dependencies with ```pip install -r "requirements.txt"```. Depending on your system, you may see the error ```No matching distribution found for Django===4.1.4```; in this case, change the Django version in requirements.txt to the most recent available version shown by the error.
6. Run initial migrations for the database with ```python manage.py migrate``` in the terminal
7. Start up the dev server with ```python manage.py runserver```
8. If you would like to run the test cases, in your terminal enter ```./manage.py test``` from the parent directory (micromort-microservice)
9. If you would like to test the API on your own, any API platform (such as Postman) will work. Be sure that the ```Content-Type``` header is set to ```application/json``` or else you may receive errors. By default, the Django Framework, with which this project was built, will start the server at ```http://127.0.0.1:8000/```, so POST requests for this endpoint can be made to ```http://127.0.0.1:8000/api/```


Navigating the codebase:
---------
The main API endpoint function can be found ```in ./api/views.py```    
The input schema validator can be found in ```./api/utils/validators.py```  
The micromort calculation model can be found in ```./api/utils/micromort_model.py```  
The test cases can be found in ```./api/tests.py```  
And finally, the json input files used for testing can be found in ```./api/unit_testing/api_inputs```  

