#!/bin/bash

# copy controller files before deleting swagger code
cp ~/hid-sp18-502/swagger/swagger_example/server/var/flaskConnexion/swagger_server/controllers/default_controller.py ~/hid-sp18-502/swagger/default_controller.py

cp ~/hid-sp18-502/swagger/swagger_example/server/var/flaskConnexion/swagger_server/controllers/var_controller.py ~/hid-sp18-502/swagger/var_controller.py

# delete swagger code
rm -rf swagger_example

# create new serverside code by using .yaml file
swagger-codegen generate -i ~/hid-sp18-502/swagger/variabl.yaml -l python-flask -o ~/hid-sp18-502/swagger/swagger_example/server/var/flaskConnexion -D supportPython2=true

# delete default controller developed by swagger
rm -rf ~/hid-sp18-502/swagger/swagger_example/server/var/flaskConnexion/swagger_server/controllers/default_controller.py

# copy controller files from swagger folder back to conntrollers folder.
cp ~/hid-sp18-502/swagger/default_controller.py ~/hid-sp18-502/swagger/swagger_example/server/var/flaskConnexion/swagger_server/controllers/default_controller.py

cp ~/hid-sp18-502/swagger/var_controller.py ~/hid-sp18-502/swagger/swagger_example/server/var/flaskConnexion/swagger_server/controllers/var_controller.py`

# create virtualenv
virtualenv RESTServer
source RESTServer/bin/activate

# change directory and install requirements of server side code
cd ~/hid-sp18-502/swagger/swagger_example/server/var/flaskConnexion
pip install -r requirements.txt
python setup.py install

