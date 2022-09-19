.PHONY: clean build
.DEFAULT_GOAL:=help

# Variables
LAYER_NAME=pymysql_layer



build: ## PIPELINE COMMAND: build Lambda layer
	mkdir -p build/python
	pip3 install -r requirements.txt --target build/python/lib/python3.8/site-packages
	cd ./build && zip -r9 ../$(LAYER_NAME).zip .

publish: ## PIPELINE COMMEND: publish Lambda layer
	@aws lambda publish-layer-version --layer-name $(LAYER_NAME) --description "New Lambda Layer" --zip-file fileb://$(LAYER_NAME).zip --compatible-runtimes python3.8