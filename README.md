# CAISO Connector
[![Maintainability](https://api.codeclimate.com/v1/badges/4e78f9257cc5a90ef83e/maintainability)](https://codeclimate.com/github/caheredia/caiso_connector/maintainability) ![Build](https://github.com/caheredia/caiso_connector/workflows/Python%20application/badge.svg) ![Black](https://img.shields.io/badge/code%20style-black-000000.svg)

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
    docker-compose up
    ```

2.  The previous command will build and start the necessary containers. 

    navigate to `http://127.0.0.1:8000/docs` to interact with REST API

3. Populate database
	# TODO update this point and overall flow of instructions 
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

