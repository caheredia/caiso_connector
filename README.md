# caiso_connector
![Build Status](https://codebuild.us-west-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiRDhSU2M5NW5MVkZpOGwraW9HbnpSSW91d1hTOUpMa3FoYjF2alNmUXZjQlkwTU81UFFPWDJHNG1XTWxkSjlySkE0YWwrUndKc1JWQm5GQVRmdDNRckdjPSIsIml2UGFyYW1ldGVyU3BlYyI6IldwL3NaR3BNeEdXUmdYbjAiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)


Connect to CAISO API and pull down data 

## Run in debug mode on local machine
`uvicorn app.main:app --reload `

## Docker container commands
### On local machine
- Build container `docker build -t caiso-docker .`
- Run container `docker run -it -p 80:80 caiso-docker`
### In the cloud or local
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
