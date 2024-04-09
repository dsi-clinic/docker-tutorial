.PHONY: build run interactive notebook run_pipeline

build:
	docker build . -t docker_test_image

run: build
	docker run -v "$$PWD":/tmp docker_test_image

interactive: build
	docker run -it -v "$$PWD":/tmp docker_test_image /bin/bash

run_pipeline: build
	docker run -v "$$PWD":/tmp docker_test_image /tmp/scripts/run_pipeline.py

notebook: build
	docker run -it -v "$$PWD":/tmp -p 8888:8888 docker_test_image jupyter notebook --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password='' --ip='*' 
