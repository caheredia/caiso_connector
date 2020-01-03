# caiso_connector
This project connects to the CAISO OASIS API and downloads daily. Location Marginal Price (LMP) data. The CAISO payload comes in the form of a zip file. The zip file is unpacked through an ETL script. The ETL script parses the CSV for relevant data and persists data in a SQLite database. 

This database was chosen because of its ease of install and availability on most operating systems. In a real production ETL, I would have used an AWS managed database. 

## Display chart 
[rendered notebook](https://nbviewer.jupyter.org/github/caheredia/caiso_connector/blob/develop/LMP_plot.ipynb)

## Run in debug mode on local machine
```shell script
uvicorn app.main:app --reload
```

## Seed the database
To initially populate the database you'll need to run the following commnad, 
either from your local machine or from inside the docker container 
```shell script
python3 -m src.etl
```


## Docker container commands
### On local machine
- Build container `docker build -t caiso-docker .`
- Run container `docker run -it -p 80:80 caiso-docker`
### In the cloud or local
- Find out container number `docker ps`
- Enter container shell `docker exec -it <mycontainer> bash`


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
