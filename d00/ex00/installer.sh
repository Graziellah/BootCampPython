#!/bin/bash

pythonVersion=`python -V`
pythonPath=`which python`
goodVersionRegex="Python 3.7*"
yes="yes"
no="no"
minicondaPath="/sgoinfre/goinfre/Perso/ghippoda/miniconda3"
pythonPath="/sgoinfre/goinfre/Perso/ghippoda/miniconda3/bin"

installPython () {
	curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh > ~/miniconda.sh
	bash ~/miniconda.sh -b -p $minicondaPath
	export PATH=$pythonPath:$PATH
	echo "Python has been installed"
}

removePython () {
	rm -rf minicondaPath
	rm  -rf $minicondaPath
	rm  ~/miniconda.sh
	echo "Python has been remove"
}

if [[ $pythonVersion =~ $goodVersionRegex ]] 
then
	echo "Python is already installed, do you want to reinstall it ?";
	echo "[yes|no]>> "
	read response
	while test "$response" != "yes" || "$response" != "no"
	do	echo "[yes|no]>> "
		read response
	done
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
#	ls $HOME
#	else
#		echo "exit"
#	fi
	#echo "Ok votre response est $ans";
else
	removePython
	installPython
fi
echo "$pythonVersion"
