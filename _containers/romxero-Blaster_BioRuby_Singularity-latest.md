---
id: 6333
name: "romxero/Blaster_BioRuby_Singularity"
branch: "master"
tag: "latest"
commit: "20cb1b37c203145b4228bfa6cebf449a5d9def50"
version: "0a43e3141517d205a700ea7c1a386965"
build_date: "2019-01-18T22:38:50.426Z"
size_mb: 521
size: 185339935
sif: "https://datasets.datalad.org/shub/romxero/Blaster_BioRuby_Singularity/latest/2019-01-18-20cb1b37-0a43e314/0a43e3141517d205a700ea7c1a386965.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/Blaster_BioRuby_Singularity/latest/2019-01-18-20cb1b37-0a43e314/
recipe: https://datasets.datalad.org/shub/romxero/Blaster_BioRuby_Singularity/latest/2019-01-18-20cb1b37-0a43e314/Singularity
collection: romxero/Blaster_BioRuby_Singularity
---

# romxero/Blaster_BioRuby_Singularity:latest

```bash
$ singularity pull shub://romxero/Blaster_BioRuby_Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Author "Randall Cab White - rcwhite@stanford.edu"

#########
#%setup
#########

##Just grabbing default packages from ubuntu repository
%post
	apt-get -ym update
	apt-get -ym install wget curl gnupg2
	apt-get -ym install git cmake build-essential

#making the software cache dir
	mkdir -p /software_cache

#changing directory
	cd /software_cache
	
#Getting RVM 
	gpg2 --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
	\curl -sSL https://get.rvm.io | bash -s stable

#Grab the old ruby version 
	wget https://cache.ruby-lang.org/pub/ruby/1.8/ruby-1.8.7.tar.gz
	tar zxvf ruby-1.8.7.tar.gz
	cd ruby* 
	./configure
	make
	make install


#changing directory
	cd /software_cache

#bioruby download
	wget http://bioruby.org/archive/bioruby-1.5.2.tar.gz
	tar zxvf bioruby-1.5.2.tar.gz
	cd bioruby-1.5.2
	ruby setup.rb

#changing directory
	cd /software_cache


#Grab RubyGems 1.8
	wget https://github.com/rubygems/rubygems/archive/v1.8.30.tar.gz
	tar zxvf v1.8.30.tar.gz 
	cd rubygems-1.8.30/
	ruby setup.rb 

%runscript
	exec /usr/local/bin/ruby "$@"

%environment
	export IMAGE_NAME="BioRuby"
```

## Collection

 - Name: [romxero/Blaster_BioRuby_Singularity](https://github.com/romxero/Blaster_BioRuby_Singularity)
 - License: None

