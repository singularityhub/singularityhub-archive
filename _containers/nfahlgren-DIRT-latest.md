---
id: 4563
name: "nfahlgren/DIRT"
branch: "master"
tag: "latest"
commit: "9d50257ca5e998314f587082c14c83468a6b9cc0"
version: "fa15f3d93fd368e6348c4e5e0a4577c2"
build_date: "2018-08-31T03:21:36.371Z"
size_mb: 1288
size: 477380639
sif: "https://datasets.datalad.org/shub/nfahlgren/DIRT/latest/2018-08-31-9d50257c-fa15f3d9/fa15f3d93fd368e6348c4e5e0a4577c2.simg"
url: https://datasets.datalad.org/shub/nfahlgren/DIRT/latest/2018-08-31-9d50257c-fa15f3d9/
recipe: https://datasets.datalad.org/shub/nfahlgren/DIRT/latest/2018-08-31-9d50257c-fa15f3d9/Singularity
collection: nfahlgren/DIRT
---

# nfahlgren/DIRT:latest

```bash
$ singularity pull shub://nfahlgren/DIRT:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%help
	Container for running DIRT 1.1 - An automatic highthroughput root phenotyping platform
	(c) 2014 Alexander Bucksch - bucksch@uga.edu
	Web application by Abhiram Das - abhiram.das@gmail.com
	Singularity container by Chris Cotter - cotter@uga.edu

	http://dirt.iplantcollaborative.org

	University of Georgia
	------------------------------------------------------------
	Program usage: python main.py (please configure the program with the options.csv file)
	<run file path> full path to file with the root image
	<unique id> ID which will be a folder name in the working directory. Integer value needed
	<mask threshold> multiplier for the automatically determined mask threshold. 1.0 works fine and is default. If flashlight is used, the 0.6 is a good choice.
	<excised root> 1 - excised root analysis is on, 0 - excised root analysis is off
	<crown root> 1 - crown root analysis is on, 0 - crown root analysis is off
	<segmentation> 1 -  is on, 0 - is off
	<marker diameter> a simple decimal e.g. 25.4. If 0.0 is used, then the output will have pixels as unit.
	<stem reconstruction> 1 - reconstruction is turned on, 0 - reconstruction is turned off
	<plots> 1 - plotting data is stored, 0 - plotting data is not stored
	<output format> 1 - the full trait set is put into one excel file containing empty cells for traits that were not computed, 0 - only computed files are written to the output file
	<working directory> full path to folder were the result is stored
	<trait file path> full path to .csv file containing the traits to be computed

	Example:
	singularity run DIRT.simg /Documents/image_name.jpg 8 25.0 1 1 1 25.1 0 0 0 /Documents/image_folder/ /Documents/traits.csv

%labels
	Maintainer Chris Cotter
	Version v1.0

%post
	# Required for graph-tools
	apt-key adv --keyserver pgp.skewed.de --recv-key 612DEFB798507F25
	echo 'deb http://downloads.skewed.de/apt/xenial xenial universe' | tee -a  /etc/apt/sources.list
	echo 'deb-src http://downloads.skewed.de/apt/xenial xenial universe' | tee -a  /etc/apt/sources.list

	apt-get update
	apt-get -y install git python2.7 python-pip python-graph-tool

	cd /opt
	git clone git://github.com/nfahlgren/DIRT.git
	cd /opt/DIRT
	sed -i 's#/usr/local/bin/zbarimg#/usr/bin/zbarimg#' /opt/DIRT/DirtOcr/__init__.py
	pip install -r /opt/DIRT/requirements.txt

	#cleanup
	apt-get clean
	apt-get purge

%environment
	export LC_ALL=C    #Required for pip to run correctly
	export DISPLAY=:0  #Addresses "Failed to connect to Mir:" error

%runscript
	python /opt/DIRT/main.py "$@"
```

## Collection

 - Name: [nfahlgren/DIRT](https://github.com/nfahlgren/DIRT)
 - License: [Other](None)

