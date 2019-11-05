#!/bin/bash

pythonVersion=`python -V`
pythonPath=`which python`
goodVersionRegex="Python 3.7*"
yes="yes"
no="no"
minicondaPath="~/miniconda3/"
pythonPath="~/miniconda3/bin"

if [[ $pythonVersion =~ $goodVersionRegex ]] 
then
	echo "Python is already installed, do you want to reinstall it ?";
	#while [ -z $response ] || [ $response != "yes" ] || [  $response != "no" ]
	#do
	#	read -p "[yes|no]>" response
	#done
	#while read -n1 -r -p "[yes|no]" && [[ $REPLY != q ]];
	#do
		#case $REPLY in
		#y) echo "Yes";;
		#n) echo "No";;
		#*) echo "What?";;
	#	if [ $REPLY ==  'yes' ] || [ $REPLY ==  'no']
	#	then
	#		break
	#done
	#read -p "[yes|no]>" ans
	#while [ "$ans" != "$yes" ] || [ $ans !=  "$no" ]
	#do
	#	read -p "[yes|no]>" ans
	#	echo "$ans  la reponse"
	#done
	#if [ "$ans" == "yes" ]
	#then
	rm -rf minicondaPath
	rm  -rf /Users/graziella/miniconda/
	rm  miniconda.sh
	echo "Python has been remove"
	ls $HOME
	curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh > ~/miniconda.sh
	bash ~/miniconda.sh -b -p $HOME/miniconda
	export PATH="$HOME/miniconda/bin:$PATH"
	echo "Pyhon has been installed"
#	else
#		echo "exit"
#	fi
	#echo "Ok votre response est $ans";
else
		echo "Not good";
fi
echo "$pythonVersion"
