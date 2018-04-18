SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAMLFILE=variabl.yaml
DESTDIR=server/var/flaskConnexion
CREATED=server

all: service start 
	@echo "DONE"

docker-all: docker-build docker-start 
	@echo "DONE"

docker-build:
	@echo "building the image from docker file..."
	docker pull mongo:latest
	docker run --name mongo -d mongo mongod --smallfiles
	@echo "image DONE"

docker-pull:
	@echo "pulling the image from dockerhub..."
	docker pull ankita/variable
	@echo "image DONE"

docker-start:
	@echo "starting the service in container..."
	docker build -t ankita/variable .
	docker run --link mongo:mongo -p 8080:8080 ankita/variable


docker-stop:
	@echo "stoping the service..."
	docker stop $$(docker ps -alq)
	@echo "service stopped"

docker-remove:
	@echo "removing the image..."
	docker rmi -f ankita/variable
	@echo "image removed"

docker-clean: docker-stop docker-remove
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)
	 
service: dest
	@echo "creating the service..."
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) 
	
	rm *.jar
	pip install --upgrade pip
	pip install pymongo

	cp -r *.py $(DESTDIR)/swagger_server/controllers
	cp error.py $(DESTDIR)/swagger_server/models
	cp var.py $(DESTDIR)/swagger_server/models
	cp base_model_.py $(DESTDIR)/swagger_server/models
	
	
	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install 
	
	

start:  
	@echo "starting the service..."
	cd $(DESTDIR) && python -m swagger_server

test:
	curl http://localhost:8080/cloudmesh/variable/var

            
stop:
	@echo "stopping the service"
	ps -ef | grep swagger_server | grep -v "grep" | awk '{print $$2}' | xargs kill -9
	@echo "service stopped"

clean:
	@echo "removing service files created"
	rm -rf $(CREATED)
