# caiso_connector
Connect to CAISO API and pull down data 

## Docker container maintanence 
- Find out container number `docker ps`
- Enter container shell `docker exec -it <mycontainer> bash`

# Todo 
- add tests for fastapi 
- create etls for fastapi  


# References 
- [CAISO OASIS](http://oasis.caiso.com/mrioasis/logon.do?reason=application.baseAction.noSession#)
- [OASIS API FAQ](http://www.caiso.com/Documents/OASISFrequentlyAskedQuestions.pdf#search=OASIS%20API)
- [Interface Specification for OASIS](http://www.caiso.com/Documents/OASIS-InterfaceSpecification_v5_1_8Clean_Independent2019Release.pdf#search=OASIS%20INTERFACE)
- [Docker image suited for python app](https://pythonspeed.com/articles/base-image-python-docker-images/)
- [Install SQLite on a specific OS](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm)
