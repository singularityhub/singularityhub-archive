---
id: 5098
name: "keceli/container_nwchem"
branch: "master"
tag: "2.1.0"
commit: "6732fe1f39ba668eef8178983872e55a6eaf6981"
version: "01d79baaf9bbe4832fc46017f6a3e9f9"
build_date: "2018-10-03T03:26:38.340Z"
size_mb: 622
size: 184213535
sif: "https://datasets.datalad.org/shub/keceli/container_nwchem/2.1.0/2018-10-03-6732fe1f-01d79baa/01d79baaf9bbe4832fc46017f6a3e9f9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/keceli/container_nwchem/2.1.0/2018-10-03-6732fe1f-01d79baa/
recipe: https://datasets.datalad.org/shub/keceli/container_nwchem/2.1.0/2018-10-03-6732fe1f-01d79baa/Singularity
collection: keceli/container_nwchem
---

# keceli/container_nwchem:2.1.0

```bash
$ singularity pull shub://keceli/container_nwchem:2.1.0
```

## Singularity Recipe

```singularity
From: ubuntu:latest
Bootstrap: docker

%post
echo "************************************************************"
echo "Installling essential components"
echo "************************************************************" 
	apt-get -y update
	apt-get -y install make build-essential zlib1g-dev libncurses5-dev wget git
echo "************************************************************"
echo "Installling openmpi 2.1.0"
echo "************************************************************"    
	cd /usr/local/src 
	wget https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.0.tar.bz2
	tar -xjf openmpi-2.1.0.tar.bz2
	cd openmpi-2.1.0  
	./configure --prefix=/usr/local
	make -j 16
	make install
	ldconfig
echo "************************************************************"
echo "Installling mpiBench from https://github.com/LLNL/mpiBench"
echo "************************************************************"
	cd /usr/local/src
	git clone https://github.com/LLNL/mpiBench
	cd mpiBench
	make
	
%runscript
	exec /usr/local/src/mpiBench/mpiBench
```

## Collection

 - Name: [keceli/container_nwchem](https://github.com/keceli/container_nwchem)
 - License: None

