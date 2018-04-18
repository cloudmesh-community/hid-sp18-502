# Swagger Service for Key value pair

## Acknowledgement 
Thanks to Shagufta and Karan Kamatgi for giving us a starting point in implementing this service on docker.
Thanks to Ramyashree for Mongodb implementation.

## Implementation :
* The specification of the Swagger REST service is defined in the YAML file `variabl.yaml` file
* Logic to connect to database and fetch results is documented in `default_controller.py`
* The server-side code was generated using Swagger Codegen

## Steps for Execution :

* clone the repository

* navigate to the directory 

        `cd /hid-sp18-502/swagger/swagger-docker/`


* Using docker to run the Database Description swagger service :

	- `make docker-all` -- actually creates the docker image, 
	starts the container and runs the service(Mandatory to execute)

* For optional Debug purpose
	- `make docker-build` -- creates the docker image only

	- `make docker-start` -- starts the container and runs the REST service

	- `make docker-stop` -- stops the container 

	- `make docker-remove` -- removes the docker image

	- `make docker-clean` -- stops the container and remove the image
  
* Test the service :
  Mongo service will be up and running, check the below API in browser 
  
  	for example - `http://localhost:8080/cloudmesh/variable/var`

  Please make sure to run the following command in a seperate terminal after 
  running `make docker-all`
  
  	`make docker test` -- curl for the database description details

## Service Descprition

This swagger REST service allows users to query the database to fetch all the variables and their values.
It can also be used to search specific variable given its name as id. Service returns a json object containing
name, value and type of the variable.
