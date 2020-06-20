# CAISO Connector
[![Maintainability](https://api.codeclimate.com/v1/badges/4e78f9257cc5a90ef83e/maintainability)](https://codeclimate.com/github/caheredia/caiso_connector/maintainability) ![Build](https://github.com/caheredia/caiso_connector/workflows/Build/badge.svg) [![codecov](https://codecov.io/gh/caheredia/caiso_connector/branch/master/graph/badge.svg)](https://codecov.io/gh/caheredia/caiso_connector) ![Black](https://img.shields.io/badge/code%20style-black-000000.svg) 

This project connects to the CAISO OASIS API and downloads daily Location Marginal Price (LMP) data. The CAISO payload comes in the form of a zip file. The zip file is unpacked through an ETL script. The ETL script parses the CSV for relevant data and persists data in a SQLite database. 

This database was chosen because of its ease of install and availability on most operating systems. In a real production ETL, I would have used an AWS managed database. 

Code documentation [here](https://caheredia.github.io/caiso_connector/_build/html/index.html)
***
## Install instructions 

### Run project from Docker container
1. In a new directory, download [repo](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
    ```shell script
    docker-compose up
    ```

	- The previous command will build and start the necessary containers:
 		- *caiso_connector*: contains REST API, and ETL worker
		- *demo*: plotly dashboard server


navigate to `http://0.0.0.0:80/docs` to interact with REST API

2. Populate database
	# TODO update this process
    

# Outputs 
- This code generates a SQLite database located at `src/lmp.db`
- Locally, a REST API is located at `http://127.0.0.1:8000/docs`
- The code generates an interactive LMP chart `LMP_plot.html`. The chart can be rendered from the notebook `LMP_plot.ipynb` notebook, which is also rendered online here [rendered notebook](https://nbviewer.jupyter.org/github/caheredia/caiso_connector/blob/master/LMP_plot.ipynb)

***

# Run tests
```shell script
docker-compose exec web python -m pytest tests
```
which yields the following upon successful run 
```shell script
 ➜  caiso_connector git:(master) docker-compose exec web python -m pytest tests
============================ test session starts =============================
platform linux -- Python 3.7.7, pytest-5.3.2, py-1.8.1, pluggy-0.13.1
rootdir: /code
collected 7 items

tests/test_api.py .....                                                [ 71%]
tests/test_connector.py ..                                             [100%]

============================= 7 passed in 0.65s ==============================
```

# References 
- [CAISO OASIS](http://oasis.caiso.com/mrioasis/logon.do?reason=application.baseAction.noSession#)
- [OASIS API FAQ](http://www.caiso.com/Documents/OASISFrequentlyAskedQuestions.pdf#search=OASIS%20API)
- [Interface Specification for OASIS](http://www.caiso.com/Documents/OASIS-InterfaceSpecification_v5_1_8Clean_Independent2019Release.pdf#search=OASIS%20INTERFACE)
- [New England LMP FAQ](https://iso-ne.com/participate/support/faq/lmp)
- [Docker image suited for python app](https://pythonspeed.com/articles/base-image-python-docker-images/)
- [Install SQLite on a specific OS](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm)

