---
id: 3711
name: "Cavatica2/Code"
branch: "master"
tag: "latest"
commit: "96a3b5e2a68f5217b6b8e82646d1e303c1bb7b26"
version: "92d11461ba093583903a499519b8c798"
build_date: "2019-07-27T00:52:01.700Z"
size_mb: 1560
size: 732491807
sif: "https://datasets.datalad.org/shub/Cavatica2/Code/latest/2019-07-27-96a3b5e2-92d11461/92d11461ba093583903a499519b8c798.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Cavatica2/Code/latest/2019-07-27-96a3b5e2-92d11461/
recipe: https://datasets.datalad.org/shub/Cavatica2/Code/latest/2019-07-27-96a3b5e2-92d11461/Singularity
collection: Cavatica2/Code
---

# Cavatica2/Code:latest

```bash
$ singularity pull shub://Cavatica2/Code:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: r-base

%post
		apt-get update
		apt-get install sudo
		sudo apt-get install -y git
		sudo apt-get install -y curl
		sudo apt-get install -y wget
		sudo apt-get install -y libwww-perl
		sudo apt-get install -y libglu1-mesa
		sudo apt-get install -y libgtk2.0-0
		wget http://ftp.us.debian.org/debian/pool/main/libp/libpng/libpng12-0_1.2.49-1+deb7u2_amd64.deb
		sudo apt-get install -y ./libpng12-0_1.2.49-1+deb7u2_amd64.deb
		echo 'install.packages(c("ggplot2",  "RColorBrewer", "plotrix", "readr", "RISmed", "stringr", "igraph"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \
&& Rscript /tmp/packages.R
		git clone https://github.com/incertae-sedis/cavatica.git
#		wget https://github.com/Cavatica2/Code/blob/master/Mango_Mint_1.24_64bit.tgz?raw=true
#		tar xf 'Mango_Mint_1.24_64bit.tgz?raw=true'

%apprun cavatica
		cd /cavatica/data/output
		ln -s ../test/*.tsv .
		../../code/script.sh
		find /cavatica/data/output -type l | xargs rm

## Please register and download your own copy of Mango, extract, and copy the folder to the root directory of the container to use the following app.
%apprun Mango
		cd /Mango_Mint_1.24_64bit
		./Mango

%runscript
		bash

%environment
		export PATH=/:$PATH

%help
I am a singularity container for the cavatica tool, which was build by the maintainers during the NSF Cyber Carpentry 2018. Please register and download your own copy of Mango, extract, and copy the folder to the root directory of the container to use the Mango GUI app from within the container.

%labels
	Maintainer Anuja Majmundar, Elena Auer, Gaurav Kandoi, Meysam Ghaffari
```

## Collection

 - Name: [Cavatica2/Code](https://github.com/Cavatica2/Code)
 - License: None

