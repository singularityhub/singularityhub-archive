---
id: 15609
name: "bioinformapping/GOMAP-PlantSpecific"
branch: "main"
tag: "latest"
commit: "6e5061737071005f26d454650909d86983116787"
version: "906dc8a9e8128ffe702a4c47893c0b58c6f08acc8db4528db075578856de5c18"
build_date: "2021-02-28T19:44:36.795Z"
size_mb: 371.66015625
size: 389713920
sif: "https://datasets.datalad.org/shub/bioinformapping/GOMAP-PlantSpecific/latest/2021-02-28-6e506173-906dc8a9/906dc8a9e8128ffe702a4c47893c0b58c6f08acc8db4528db075578856de5c18.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/bioinformapping/GOMAP-PlantSpecific/latest/2021-02-28-6e506173-906dc8a9/
recipe: https://datasets.datalad.org/shub/bioinformapping/GOMAP-PlantSpecific/latest/2021-02-28-6e506173-906dc8a9/Singularity
collection: bioinformapping/GOMAP-PlantSpecific
---

# bioinformapping/GOMAP-PlantSpecific:latest

```bash
$ singularity pull shub://bioinformapping/GOMAP-PlantSpecific:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: r-base:latest

%labels
GOMAP_OWNER Wimalanathan Kokulapalan
GOMAP_MAINTAINER Wimalanathan Kokulapalan 
GOMAP_PLANT_SPECIFIC_VERSION v0.1

%environment
    export LC_ALL=C 
    export DEBIAN_FRONTEND=noninteractive
	export SCRIPT_LOC=/opt/PlantSpecific
 
%post
	export DEBIAN_FRONTEND="noninteractive"
	echo "Running post      "
	
	apt-get update && \
	apt-get install -y python3.9 git

	git clone https://github.com/bioinformapping/GOMAP-PlantSpecific.git &&
	cp -R GOMAP-PlantSpecific/PlantSpecific /opt/

	chmod 755 /opt/PlantSpecific/filterPlantSpecific.R

    #Installing the necessary R packages
	R -e 'install.packages(c("argparse","data.table","ontologyIndex","tools"), repos="https://mirror.las.iastate.edu/CRAN/", INSTALL_opts="--no-html")'

	echo "Completed Post   "

%runscript
	/opt/PlantSpecific/filterPlantSpecific.R "$@"
```

## Collection

 - Name: [bioinformapping/GOMAP-PlantSpecific](https://github.com/bioinformapping/GOMAP-PlantSpecific)
 - License: None

