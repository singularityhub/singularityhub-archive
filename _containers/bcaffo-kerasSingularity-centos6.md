---
id: 9407
name: "bcaffo/kerasSingularity"
branch: "master"
tag: "centos6"
commit: "487c2800f6ec17191eb51206800253c9d1f4b50b"
version: "3537646130caa233bc182d246631cbbb"
build_date: "2019-05-30T04:44:56.336Z"
size_mb: 2230
size: 799436831
sif: "https://datasets.datalad.org/shub/bcaffo/kerasSingularity/centos6/2019-05-30-487c2800-35376461/3537646130caa233bc182d246631cbbb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bcaffo/kerasSingularity/centos6/2019-05-30-487c2800-35376461/
recipe: https://datasets.datalad.org/shub/bcaffo/kerasSingularity/centos6/2019-05-30-487c2800-35376461/Singularity
collection: bcaffo/kerasSingularity
---

# bcaffo/kerasSingularity:centos6

```bash
$ singularity pull shub://bcaffo/kerasSingularity:centos6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos6.9

%environment
	## These are necessary since if they aren't included 
	## locale returns the wrong encoding
	## this seems to fix it
        export LC_ALL=en_US.UTF-8
        export LANG=en_US.UTF-8
        
%post
	yum -y -q update

	## Install sudo
	#####################	
	yum -y -q install sudo
	
	## This loads the community epel releases
	#####################
	yum -y -q install epel-release
	curl 'https://setup.ius.io/' -o setup-ius.sh
	sh setup-ius.sh
	rm setup-ius.sh
	
	yum -y -q update
	
	## These are the RHL / centos / fedora development tools library
	#####################
	yum -y -q groupinstall "Development Tools"

	## installs pyton 3.6
	#####################
	yum -y -q --enablerepo=ius install python36u-devel

	## installs pip for python 3.6
	#####################
	curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
	sudo python3.6 get-pip.py
	rm get-pip.py
	
	## Install library dependencies
	#####################	
	## these are all required by devtools
	yum install -y -q libxml2-devel
        yum install -y -q libcurl-devel
        yum install -y -q openssl-devel
        yum install -y -q libssh2-devel

	## required for the image packages
	yum install -y -q libpng-devel
        yum install -y -q libjpeg-turbo-devel

	## install R-devel
	#####################	
        yum -y -q --enablerepo=ius install R-devel
	
	## Install pip dependencies
	#####################
	## These are required for keras and tensorflow
	sudo pip3 -q install virtualenv
	sudo pip3 -q install tensorflow
	sudo pip3 -q install keras

	## install R packages
	#####################
	## This isn't good. It's the only way I could supress an annoying warning
	## just makes the missing documentation directory
	sudo mkdir /usr/share/doc/R-3.5.2/html
	
	## Install some core R packages
	sudo R -e 'install.packages("devtools", repos="http://cran.rstudio.com/", quiet = TRUE)'
	#sudo R -e 'install.packages("tidyverse",repos="http://cran.rstudio.com/", quiet = TRUE)'

	## These seem to be needed
	#yum -y -q update
	#yum -y -q install -y libpython-dev
  	#yum -y -q install -y libpython3-dev
	
	## installing R keras
	sudo R -e 'devtools::install_github("rstudio/keras", quiet = TRUE, args = "--no-html", build_vignettes = FALSE)'
```

## Collection

 - Name: [bcaffo/kerasSingularity](https://github.com/bcaffo/kerasSingularity)
 - License: None

