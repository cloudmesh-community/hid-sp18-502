## Reference Material Used: 
Following links were used to find the commands to connect to azure and create virtual machines

* https://docs.microsoft.com/en-us/azure/virtual-machines/windows/python

* https://github.com/Azure-Samples/virtual-machines-python-manage/blob/master/example.py

## Acknowledgement:

* Thanks to Professor Laszewski, Gregor for guiding me in the right direction. Thanks to Pathan, Shagufta for giving me a starting point for the project.

## Prerequisites for Execution

* git clone the repository.

* you should have docker installed on your machine.

* you should have account on Azure along with active subscription.

* create clientid, secret and tenant id by following instruction given in following link:
https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal

* Assign Contributor role to your registered Application.

* go to project-code directory.

* In the **cred.yaml**, make sure to update the `clientId`, `clientSecret`, `tenantId` and `subscript` with 
your Azure account details created in above steps.

## Instructions for executing the project using docker

* Follow the prerequisites mentioned above

* Build and run the docker image using the following make command from Makefile
  
  * ```sudo make docker-all```
  
* If you need to stop the docker container, use the following make command.
  
  * ```make docker-stop```
  
* Test the service using the following make command from within the container
  
  * ```sudo make test```
  
* Refer to project paper for all the commands that can be used to test the service


