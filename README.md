# CAISO Connector
This project connects to the CAISO OASIS API and downloads daily Location Marginal Price (LMP) data. The CAISO payload comes in the form of a zip file. The zip file is unpacked through an ETL script. The ETL script parses the CSV for relevant data and persists data in a SQLite database. 

This database was chosen because of its ease of install and availability on most operating systems. In a real production ETL, I would have used an AWS managed database. 

Code documentation [here](https://caheredia.github.io/caiso_connector/_build/html/index.html)
***
## Install instructions 
Below are two methods to install and run this code.

### Run project from local machine
- prerequisites: 
    - Python >= 3.7
    - a new python virtual environment
1. Install [Poetry](https://python-poetry.org/)——a python dependency manager.
    ```shell script
    pip install poetry==0.12.17
    ```
2. Download code repository 
    ```shell script
    git clone git@github.com:caheredia/caiso_connector.git
    ```
3. Install dependencies with poetry, first configure poetry to not install a new virtual environment 
    ```shell script
    poetry config settings.virtualenvs.create false
    ```
    ```shell script
    poetry install
    ```
4. Install SQLite

   Mac OSX comes with SQLite pre-installed. Otherwise, [here](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm) are instructions for installing the database on other Operating Systems. 
5. Populate the database

    To initially populate the database you'll need to run the following command: 
    ```shell script
    python3 -m src.etl
    ```
6. Start the [FastAPI](https://fastapi.tiangolo.com/) REST API server 
    The `--reload` flag runs the server in debug mode 
    ```shell script
    uvicorn app.main:app --reload
    ```
   
   navigate to `http://127.0.0.1:8000/docs` to interact with REST API

### Run project from Docker container
1. In a new directory, download code repository 
    ```shell script
    git clone git@github.com:caheredia/caiso_connector.git
    ```
2. Build container `docker build -t caiso-docker .`

3.  Run container `docker run -it -p 80:80 caiso-docker`

    navigate to `http://127.0.0.1:8000/docs` to interact with REST API

4. Populate database
    From inside the docker container run step 5 from above. 
    
**Useful docker commands, in the cloud or local**

- Find container number `docker ps`
- Enter container shell `docker exec -it <mycontainer> bash`
***

# Outputs 
- This code generates a SQLite database located at `src/lmp.db`
- Locally, a REST API is located at `http://127.0.0.1:8000/docs`
- The code generates an interactive LMP chart `LMP_plot.html`. The chart can be rendered from the notebook `LMP_plot.ipynb` notebook, which is also rendered online here [rendered notebook](https://nbviewer.jupyter.org/github/caheredia/caiso_connector/blob/master/LMP_plot.ipynb)

***

# Run tests
```shell script
python3 -m pytest tests/
```
which yields the following upon successful run 
```shell script
(caiso) ➜  caiso_connector git:(develop) python3 -m pytest tests/
========================================================== test session starts ===========================================================
platform darwin -- Python 3.7.3, pytest-5.3.2, py-1.8.1, pluggy-0.13.1
rootdir: /Users/cristian/Documents/2019/caiso_connector
collected 7 items                                                                                                                        

tests/test_api.py .....                                                                                                            [ 71%]
tests/test_connector.py ..                                                                                                         [100%]

=========================================================== 7 passed in 23.89s ===========================================================
(caiso) ➜  caiso_connector git:(develop) 

```

# References 
- [CAISO OASIS](http://oasis.caiso.com/mrioasis/logon.do?reason=application.baseAction.noSession#)
- [OASIS API FAQ](http://www.caiso.com/Documents/OASISFrequentlyAskedQuestions.pdf#search=OASIS%20API)
- [Interface Specification for OASIS](http://www.caiso.com/Documents/OASIS-InterfaceSpecification_v5_1_8Clean_Independent2019Release.pdf#search=OASIS%20INTERFACE)
- [New England LMP FAQ](https://iso-ne.com/participate/support/faq/lmp)
- [Docker image suited for python app](https://pythonspeed.com/articles/base-image-python-docker-images/)
- [Install SQLite on a specific OS](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm)

# Todo 
- use History on Demand API to demonstrate async downloads 

{"message": "URL failed 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=31.5493%2C97.1467&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE, status code 401", "payload": {"message": "401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=31.5493%2C97.1467&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE", "status_code": 401, "start_timer_s": 1585087963.008348, "url_params": {"format": "json", "units": "s", "pointType": "nearest", "geocode": "31.5493,97.1467", "startDateTime": "201601010000", "endDateTime": "201601072359", "apiKey": "PASSWORD HERE"}}, "timestamp": "2020-03-24T22:12:43.141697", "version": "0.0.1", "metadata": {"level": "ERROR", "code": {"pathname": "/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py", "module": "http_utils", "function": "get_file_buf", "line_number": 105}}, "instance": {"node": "Cristians-MBP", "system": "Darwin", "machine": "x86_64", "python": "3.7.6"}, "stack_trace": "Traceback (most recent call last):\n  File \"/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py\", line 100, in get_file_buf\n    s.raise_for_status()\n  File \"/Users/cristian/miniconda3/envs/wlearn/lib/python3.7/site-packages/requests/models.py\", line 941, in raise_for_status\n    raise HTTPError(http_error_msg, response=self)\nrequests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=31.5493%2C97.1467&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE"}
{"message": "URL failed 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=33.35%2C-99.54&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE, status code 401", "payload": {"message": "401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=33.35%2C-99.54&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE", "status_code": 401, "start_timer_s": 1585087963.006824, "url_params": {"format": "json", "units": "s", "pointType": "nearest", "geocode": "33.35,-99.54", "startDateTime": "201601010000", "endDateTime": "201601072359", "apiKey": "PASSWORD HERE"}}, "timestamp": "2020-03-24T22:12:43.146301", "version": "0.0.1", "metadata": {"level": "ERROR", "code": {"pathname": "/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py", "module": "http_utils", "function": "get_file_buf", "line_number": 105}}, "instance": {"node": "Cristians-MBP", "system": "Darwin", "machine": "x86_64", "python": "3.7.6"}, "stack_trace": "Traceback (most recent call last):\n  File \"/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py\", line 100, in get_file_buf\n    s.raise_for_status()\n  File \"/Users/cristian/miniconda3/envs/wlearn/lib/python3.7/site-packages/requests/models.py\", line 941, in raise_for_status\n    raise HTTPError(http_error_msg, response=self)\nrequests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=33.35%2C-99.54&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE"}
{"message": "URL failed 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=34.197%2C-101.382&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE, status code 401", "payload": {"message": "401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=34.197%2C-101.382&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE", "status_code": 401, "start_timer_s": 1585087963.006326, "url_params": {"format": "json", "units": "s", "pointType": "nearest", "geocode": "34.197,-101.382", "startDateTime": "201601010000", "endDateTime": "201601072359", "apiKey": "PASSWORD HERE"}}, "timestamp": "2020-03-24T22:12:43.148870", "version": "0.0.1", "metadata": {"level": "ERROR", "code": {"pathname": "/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py", "module": "http_utils", "function": "get_file_buf", "line_number": 105}}, "instance": {"node": "Cristians-MBP", "system": "Darwin", "machine": "x86_64", "python": "3.7.6"}, "stack_trace": "Traceback (most recent call last):\n  File \"/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py\", line 100, in get_file_buf\n    s.raise_for_status()\n  File \"/Users/cristian/miniconda3/envs/wlearn/lib/python3.7/site-packages/requests/models.py\", line 941, in raise_for_status\n    raise HTTPError(http_error_msg, response=self)\nrequests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=34.197%2C-101.382&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE"}
{"message": "URL failed 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=27.0011%2C-97.5994&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE, status code 401", "payload": {"message": "401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=27.0011%2C-97.5994&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE", "status_code": 401, "start_timer_s": 1585087963.007068, "url_params": {"format": "json", "units": "s", "pointType": "nearest", "geocode": "27.0011,-97.5994", "startDateTime": "201601010000", "endDateTime": "201601072359", "apiKey": "PASSWORD HERE"}}, "timestamp": "2020-03-24T22:12:43.156157", "version": "0.0.1", "metadata": {"level": "ERROR", "code": {"pathname": "/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py", "module": "http_utils", "function": "get_file_buf", "line_number": 105}}, "instance": {"node": "Cristians-MBP", "system": "Darwin", "machine": "x86_64", "python": "3.7.6"}, "stack_trace": "Traceback (most recent call last):\n  File \"/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py\", line 100, in get_file_buf\n    s.raise_for_status()\n  File \"/Users/cristian/miniconda3/envs/wlearn/lib/python3.7/site-packages/requests/models.py\", line 941, in raise_for_status\n    raise HTTPError(http_error_msg, response=self)\nrequests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=27.0011%2C-97.5994&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE"}
{"message": "URL failed 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=33.5826%2C-96.6179&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE, status code 401", "payload": {"message": "401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=33.5826%2C-96.6179&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE", "status_code": 401, "start_timer_s": 1585087963.007317, "url_params": {"format": "json", "units": "s", "pointType": "nearest", "geocode": "33.5826,-96.6179", "startDateTime": "201601010000", "endDateTime": "201601072359", "apiKey": "PASSWORD HERE"}}, "timestamp": "2020-03-24T22:12:43.157248", "version": "0.0.1", "metadata": {"level": "ERROR", "code": {"pathname": "/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py", "module": "http_utils", "function": "get_file_buf", "line_number": 105}}, "instance": {"node": "Cristians-MBP", "system": "Darwin", "machine": "x86_64", "python": "3.7.6"}, "stack_trace": "Traceback (most recent call last):\n  File \"/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py\", line 100, in get_file_buf\n    s.raise_for_status()\n  File \"/Users/cristian/miniconda3/envs/wlearn/lib/python3.7/site-packages/requests/models.py\", line 941, in raise_for_status\n    raise HTTPError(http_error_msg, response=self)\nrequests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=33.5826%2C-96.6179&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE"}
{"message": "URL failed 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=32.9048%2C-97.3841&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE, status code 401", "payload": {"message": "401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=32.9048%2C-97.3841&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE", "status_code": 401, "start_timer_s": 1585087963.0061288, "url_params": {"format": "json", "units": "s", "pointType": "nearest", "geocode": "32.9048,-97.3841", "startDateTime": "201601010000", "endDateTime": "201601072359", "apiKey": "PASSWORD HERE"}}, "timestamp": "2020-03-24T22:12:43.157396", "version": "0.0.1", "metadata": {"level": "ERROR", "code": {"pathname": "/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py", "module": "http_utils", "function": "get_file_buf", "line_number": 105}}, "instance": {"node": "Cristians-MBP", "system": "Darwin", "machine": "x86_64", "python": "3.7.6"}, "stack_trace": "Traceback (most recent call last):\n  File \"/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py\", line 100, in get_file_buf\n    s.raise_for_status()\n  File \"/Users/cristian/miniconda3/envs/wlearn/lib/python3.7/site-packages/requests/models.py\", line 941, in raise_for_status\n    raise HTTPError(http_error_msg, response=self)\nrequests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=32.9048%2C-97.3841&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE"}
{"message": "URL failed 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=29.4241%2C98.4936&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE, status code 401", "payload": {"message": "401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=29.4241%2C98.4936&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE", "status_code": 401, "start_timer_s": 1585087963.0080261, "url_params": {"format": "json", "units": "s", "pointType": "nearest", "geocode": "29.4241,98.4936", "startDateTime": "201601010000", "endDateTime": "201601072359", "apiKey": "PASSWORD HERE"}}, "timestamp": "2020-03-24T22:12:43.157586", "version": "0.0.1", "metadata": {"level": "ERROR", "code": {"pathname": "/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py", "module": "http_utils", "function": "get_file_buf", "line_number": 105}}, "instance": {"node": "Cristians-MBP", "system": "Darwin", "machine": "x86_64", "python": "3.7.6"}, "stack_trace": "Traceback (most recent call last):\n  File \"/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py\", line 100, in get_file_buf\n    s.raise_for_status()\n  File \"/Users/cristian/miniconda3/envs/wlearn/lib/python3.7/site-packages/requests/models.py\", line 941, in raise_for_status\n    raise HTTPError(http_error_msg, response=self)\nrequests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=29.4241%2C98.4936&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE"}
{"message": "URL failed 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=30.5755%2C-102.551&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE, status code 401", "payload": {"message": "401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=30.5755%2C-102.551&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE", "status_code": 401, "start_timer_s": 1585087963.007815, "url_params": {"format": "json", "units": "s", "pointType": "nearest", "geocode": "30.5755,-102.551", "startDateTime": "201601010000", "endDateTime": "201601072359", "apiKey": "PASSWORD HERE"}}, "timestamp": "2020-03-24T22:12:43.161972", "version": "0.0.1", "metadata": {"level": "ERROR", "code": {"pathname": "/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py", "module": "http_utils", "function": "get_file_buf", "line_number": 105}}, "instance": {"node": "Cristians-MBP", "system": "Darwin", "machine": "x86_64", "python": "3.7.6"}, "stack_trace": "Traceback (most recent call last):\n  File \"/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py\", line 100, in get_file_buf\n    s.raise_for_status()\n  File \"/Users/cristian/miniconda3/envs/wlearn/lib/python3.7/site-packages/requests/models.py\", line 941, in raise_for_status\n    raise HTTPError(http_error_msg, response=self)\nrequests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=30.5755%2C-102.551&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE"}
{"message": "URL failed 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=32.214%2C-100.057&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE, status code 401", "payload": {"message": "401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=32.214%2C-100.057&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE", "status_code": 401, "start_timer_s": 1585087963.00753, "url_params": {"format": "json", "units": "s", "pointType": "nearest", "geocode": "32.214,-100.057", "startDateTime": "201601010000", "endDateTime": "201601072359", "apiKey": "PASSWORD HERE"}}, "timestamp": "2020-03-24T22:12:43.165585", "version": "0.0.1", "metadata": {"level": "ERROR", "code": {"pathname": "/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py", "module": "http_utils", "function": "get_file_buf", "line_number": 105}}, "instance": {"node": "Cristians-MBP", "system": "Darwin", "machine": "x86_64", "python": "3.7.6"}, "stack_trace": "Traceback (most recent call last):\n  File \"/Users/cristian/Documents/2020/lagrange/wlearn/utils/http_utils.py\", line 100, in get_file_buf\n    s.raise_for_status()\n  File \"/Users/cristian/miniconda3/envs/wlearn/lib/python3.7/site-packages/requests/models.py\", line 941, in raise_for_status\n    raise HTTPError(http_error_msg, response=self)\nrequests.exceptions.HTTPError: 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=32.214%2C-100.057&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE"}
{"message": "URL failed 401 Client Error: Unauthorized for url: https://api.weather.com//v3/wx/hod/conditions/historical/point?format=json&units=s&pointType=nearest&geocode=33.0917%2C-95.0417&startDateTime=201601010000&endDateTime=201601072359&apiKey=PASSWORD+HERE,