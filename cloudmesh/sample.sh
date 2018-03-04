#!/bin/bash

# copy controller files before deleting swagger code
cp ~/hid-sp18-502/cloudmesh/swagger_example/server/dir/flaskConnexion/swagger_server/controllers/default_controller.py ~/hid-sp18-502/cloudmesh/default_controller.py

cp ~/hid-sp18-502/cloudmesh/swagger_example/server/dir/flaskConnexion/swagger_server/controllers/dir_controller.py ~/hid-sp18-502/cloudmesh/dir_controller.py

# delete swagger code
rm -rf swagger_example

# create new serverside code by using .yaml file
java -jar ~/cloudmesh/swagger-codegen-cli.jar generate -i ~/hid-sp18-502/cloudmesh/dir.yaml -l python-flask -o ~/hid-sp18-502/cloudmesh/swagger_example/server/dir/flaskConnexion -D supportPython2=true

# delete default controller developed by swagger
rm -rf ~/hid-sp18-502/cloudmesh/swagger_example/server/dir/flaskConnexion/swagger_server/controllers/default_controller.py`

# copy controller files from swagger folder back to conntrollers folder.
cp ~/hid-sp18-502/cloudmesh/default_controller.py ~/hid-sp18-502/cloudmesh/swagger_example/server/dir/flaskConnexion/swagger_server/controllers/default_controller.py

cp ~/hid-sp18-502/cloudmesh/dir_controller.py ~/hid-sp18-502/cloudmesh/swagger_example/server/dir/flaskConnexion/swagger_server/controllers/dir_controller.py

# create virtualenv
virtualenv RESTServer
source ./RESTServer/bin/activate

# change directory
cd ~/hid-sp18-502/cloudmesh/swagger_example/server/dir/flaskConnexion`
pip install -r requirements.txt
python setup.py install

