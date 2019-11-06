#!/bin/bash

pythonVersion=`python -V`
pythonPath=`which python`
goodVersionRegex="Python 3.7*"
yes="yes"
no="no"
minicondaPath="/sgoinfre/goinfre/Perso/ghippoda/miniconda3"
pythonPath="/sgoinfre/goinfre/Perso/ghippoda/miniconda3/bin"

installPython () {
	curl -s https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh  > ~/miniconda.sh
	bash ~/miniconda.sh -p -b $minicondaPath > /dev/null
	$bash export PATH=$pythonPath:$PATH
	echo "Python has been installed"
}

removePython () {
	rm -rf $minicondaPath
	rm  ~/miniconda.sh
	#echo "Python has been remove"
}

if [[ $pythonVersion =~ $goodVersionRegex ]] 
then
	echo "Python is already installed, do you want to reinstall it ?"
	yesptrn="yes"; noptrn="no"; yesword="yes"; noword="no"
	while true; do
		read -p "[${yesword}|${noword}]> " yn
		case $yn in
			${yesptrn##^} )  removePython;  echo "Pyhton has been remove";  installPython; break;;
			${noptrn##^} ) echo "exit"; exit;;
			* ) echo "Answer ${yesword} / ${noword}.";;
		esac
	done
else
	removePython
	installPython
fi
echo "$pythonVersion"
