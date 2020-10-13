# cade-path2
This is a demo Resources folder for the CADE2 pathway-based simulation tool

1. If you don't already have Docker on your system, download and install it from https://store.docker.com/search?type=edition&offering=community
2. If you don't already have Git on your system, download and install it from https://git-scm.com/downloads
3. Clone this project
```sh
	git clone https://github.com/charliemccay/cade-path2
```



To run a simulation outside docker-compose you need to mount the Resources folder in this project in the CADE2 Docker container.  

This Resources file assumes that you have a locally running FHIR server - this can be stood up using the following command:

docker run -it -p 8080:8080 smartonfhir/hapi:r2-empty

Once the FHIR server is running, open another terminal window.  From there you can then run the CADE container which will post the patients and observations to the FHIR server.  Having each container running in its own terminal will allow you to see what is happening more easily.  Note that you need to provide an absolute path for the Resources folder, hence the $(pwd).

docker run -v $(pwd)/Resources:/app/Resources --network="host" ramseysys/cade-2:latest start.py

The FHIR server can be stopped with ctrl-c.  When it is started again it the contents will remain unless the container is deleted.  This implementation of CADE uses UUIDs for the resource identifiers, so can be run multiple times without clashing identifiers - every time someone is born they are assumed to be a new person.

The BPMN models can be edited with the Camunda Modelling tool: https://camunda.com/download/modeler/
