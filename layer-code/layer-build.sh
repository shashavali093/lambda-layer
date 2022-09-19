#!/bin/bash

#########################LAMBDA LAYER BUILDING############################


cd layer-code

############################ Replacing LayerName ##################
sed -i 's/pymysql_layer/'"${LayerName}"'/g' Makefile


echo "Building ${LayerName}....."
make build
echo "Publishing ${LayerName}....."
make publish
