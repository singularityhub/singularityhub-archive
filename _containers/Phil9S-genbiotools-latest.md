---
id: 12032
name: "Phil9S/genbiotools"
branch: "master"
tag: "latest"
commit: "d12811d032d526e4804b0987aa1c02957e10fa5c"
version: "83424413f5ad4a646e2a74facbd168d6"
build_date: "2020-01-20T23:30:53.917Z"
size_mb: 1327.0
size: 780627999
sif: "https://datasets.datalad.org/shub/Phil9S/genbiotools/latest/2020-01-20-d12811d0-83424413/83424413f5ad4a646e2a74facbd168d6.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Phil9S/genbiotools/latest/2020-01-20-d12811d0-83424413/
recipe: https://datasets.datalad.org/shub/Phil9S/genbiotools/latest/2020-01-20-d12811d0-83424413/Singularity
collection: Phil9S/genbiotools
---

# Phil9S/genbiotools:latest

```bash
$ singularity pull shub://Phil9S/genbiotools:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%setup

%files

%environment
	export LC_ALL=C

%post
	#update all
	apt-get update

	#get required linux distro 
	apt-get install -y wget git autoconf automake make gcc perl libncurses5-dev unzip \
			zlib1g-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libssl-dev \
			default-jdk python3.6
	
	#Clone and build htslib
    	git clone https://github.com/samtools/htslib.git
    	cd htslib/
    	autoheader && autoconf && ./configure && make && make install
	cd 

	#Download and build samtools
	wget https://github.com/samtools/samtools/releases/download/1.10/samtools-1.10.tar.bz2
	bzip2 -d samtools-1.10.tar.bz2 && tar -xf samtools-1.10.tar
	cd samtools-1.10/
	./configure && make && make install
	cd

	#Download and build BCFtools
	wget https://github.com/samtools/bcftools/releases/download/1.10.2/bcftools-1.10.2.tar.bz2
	bzip2 -d bcftools-1.10.2.tar.bz2 && tar -xf bcftools-1.10.2.tar
	cd bcftools-1.10.2
	./configure && make && make install
	cd

	#Download and build bwa/bwakit-minimal
	wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2
	bzip2 -d bwa-0.7.17.tar.bz2
	tar -xf bwa-0.7.17.tar
	cd bwa-0.7.17
	make
	cp bwa /usr/bin/
	cp bwakit/* /usr/bin/
	cd
	
	#Download and install bwa-mem2
	wget https://github.com/bwa-mem2/bwa-mem2/releases/download/v2.0pre1/bwa-mem2-2.0pre1_x64-linux.tar.bz2
	bzip2 -d bwa-mem2-2.0pre1_x64-linux.tar.bz2
	tar -xf bwa-mem2-2.0pre1_x64-linux.tar
	cp bwa-mem2-2.0pre1_x64-linux/* /usr/bin/

	#Download and build minimap2
	git clone https://github.com/lh3/minimap2
	cd minimap2 && make
	cp minimap2 /usr/bin/
	cd

	#Download and install freebayes
	wget https://github.com/ekg/freebayes/releases/download/v1.3.1/freebayes-v1.3.1
	chmod +u+x freebayes-v1.3.1
	cp freebayes-v1.3.1 /usr/bin/freebayes

	#Download and setup VarScan and making wrapper script
	wget https://github.com/dkoboldt/varscan/releases/download/2.4.2/VarScan.v2.4.2.jar
	printf '#!/bin/bash\n$(java -jar /usr/bin/VarScan.v2.4.2.jar $*)' > VarScan
	chmod +u+x VarScan
	mv VarScan /usr/bin/
	mv VarScan.v2.4.2.jar /usr/bin/

	#Download and install GATK package
	wget https://github.com/broadinstitute/gatk/releases/download/4.1.4.1/gatk-4.1.4.1.zip
	unzip gatk-4.1.4.1.zip
	mv gatk-4.1.4.1/gatk-package-4.1.4.1-local.jar /usr/bin/
	mv gatk-4.1.4.1/gatk /usr/bin/
	ln /usr/bin/python3.6 /usr/bin/python
	
	#Download and install picard
	wget https://github.com/broadinstitute/picard/releases/download/2.21.6/picard.jar
	printf '#!/bin/bash\n$(java -jar /usr/bin/picard.jar $*)' > picard
	chmod +u+x picard
	mv picard /usr/bin/
	mv picard.jar /usr/bin/
	
	#Make output directory
	mkdir /data/
	
	#Clean up
	rm -r *
	apt-get check
	apt-get autoclean

%runscript
	echo "There is no RUN script for this container - Please use EXEC to use containerised applications."
	echo "See singularity run-help for more information."

%labels
    Author P.SMITH (CRUK-CI)
    Version v0.1

%help
    	This is container contains installations of mutiple genomic tools which can be utilised using the EXEC command.
	Included tools are:
	
	HTSlib (and susequent utilities)
	bwa
	bwa-mem2
	minimap2
	samtools
	bcftools
	gatk
	Picard
	freebayes
	VarScan

	Tools can be used as expected by preappending singularity exec [THIS_CONTAINER] [application] [commandlineOptions]
```

## Collection

 - Name: [Phil9S/genbiotools](https://github.com/Phil9S/genbiotools)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

