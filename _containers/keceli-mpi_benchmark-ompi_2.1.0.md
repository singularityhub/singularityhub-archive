---
id: 1479
name: "keceli/mpi_benchmark"
branch: "master"
tag: "ompi_2.1.0"
commit: "2aba2430dcd10fec1353a04e2b0dc653d299c19c"
version: "18d12578b65734a76e8a7d9da8476be8"
build_date: "2018-01-26T02:08:37.333Z"
size_mb: 621
size: 192323615
sif: "https://datasets.datalad.org/shub/keceli/mpi_benchmark/ompi_2.1.0/2018-01-26-2aba2430-18d12578/18d12578b65734a76e8a7d9da8476be8.simg"
url: https://datasets.datalad.org/shub/keceli/mpi_benchmark/ompi_2.1.0/2018-01-26-2aba2430-18d12578/
recipe: https://datasets.datalad.org/shub/keceli/mpi_benchmark/ompi_2.1.0/2018-01-26-2aba2430-18d12578/Singularity
collection: keceli/mpi_benchmark
---

# keceli/mpi_benchmark:ompi_2.1.0

```bash
$ singularity pull shub://keceli/mpi_benchmark:ompi_2.1.0
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

 - Name: [keceli/mpi_benchmark](https://github.com/keceli/mpi_benchmark)
 - License: None

