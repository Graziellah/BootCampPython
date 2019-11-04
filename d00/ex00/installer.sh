#!/bin/bash

pythonVersion=`python -V`
pythonPath=`which python`
goodVersionRegex="Python 3.7*"

if [[ $pythonVersion =~ $goodVersionRegex ]];
then
	echo "Python is already installed, do you want to reinstall it ?";
	while [ -z $response] || [ $response != "yes"] || [ $response != "no"]
	do
		read -p "[yes|no]>" response
	done
	if [$response == "yes"]
	then
		echo"Python has been remove"
		echo"Pyhon has been installed"
	else
		echo"exit"
	echo "Ok votre response est $response"
else
	echo "Not good";
fi
echo "$pythonVersion"
