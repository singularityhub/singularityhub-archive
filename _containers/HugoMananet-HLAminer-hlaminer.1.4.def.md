---
id: 5862
name: "HugoMananet/HLAminer"
branch: "master"
tag: "hlaminer.1.4.def"
commit: "4bfa75597174f9a820d125271a26a9e08bac7c7c"
version: "b4c30511b65709981802509b8f4091a6"
build_date: "2018-12-21T17:01:17.099Z"
size_mb: 1148
size: 287576095
sif: "https://datasets.datalad.org/shub/HugoMananet/HLAminer/hlaminer.1.4.def/2018-12-21-4bfa7559-b4c30511/b4c30511b65709981802509b8f4091a6.simg"
url: https://datasets.datalad.org/shub/HugoMananet/HLAminer/hlaminer.1.4.def/2018-12-21-4bfa7559-b4c30511/
recipe: https://datasets.datalad.org/shub/HugoMananet/HLAminer/hlaminer.1.4.def/2018-12-21-4bfa7559-b4c30511/Singularity
collection: HugoMananet/HLAminer
---

# HugoMananet/HLAminer:hlaminer.1.4.def

```bash
$ singularity pull shub://HugoMananet/HLAminer:hlaminer.1.4.def
```

## Singularity Recipe

```singularity
#!/bin/bash


Bootstrap: docker

From: phusion/baseimage:0.10.2


%label

	MAINTAINER Hugo Mananet
	
	
	
%post

	mkdir /soft
	mkdir /work
	mkdir /user1
	mkdir /user2
	mkdir /tmp3
	
	apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y build-essential \
	wget \
	cpanminus \
	perl \
	tar \
	zlib1g-dev \
	make \
	gcc \
	autoconf \
	ca-certificates \
	curl \
	libbz2-dev \
	liblzma-dev \
	libncurses5-dev \
	libncursesw5-dev 


	mkdir -p /opt/
	wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && mv samtools-1.9.tar.bz2 /opt/
	wget https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2 && mv bcftools-1.9.tar.bz2 /opt/
	cd /opt/ && tar xjvf samtools-1.9.tar.bz2 && tar xjvf bcftools-1.9.tar.bz2

	cd /opt/samtools-1.9/ && ./configure && make
	cd /opt/ && rm samtools-1.9.tar.bz2

	cd /opt/bcftools-1.9/ && ./configure && make
	cd /opt/ && rm bcftools-1.9.tar.bz2

	ln -s /opt/samtools-1.9/samtools /bin
	ln -s /opt/bcftools-1.9/bcftools /bin
	ln -s /opt/samtools-1.9/misc/* /bin
	ln -s /opt/bcftools-1.9/misc/* /bin


	wget -P /opt/ https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2
	cd /opt/ && tar xjvf bwa-0.7.17.tar.bz2
	cd bwa-0.7.17 && make
	rm /opt/bwa-0.7.17.tar.bz2
	ln -s /opt/bwa-0.7.17/bwa /usr/local/bin/

	cpanm Bio::Perl
	cpanm Bio::SearchIO
	# cpanm XML::SAX
	cpanm Bio::SearchIO::blastxml

	wget -P /opt/ https://github.com/warrenlr/HLAminer/releases/download/v1.4/HLAminer_1-4.tar.gz
	cd /opt/ && tar -xzvf HLAminer_1-4.tar.gz 
	rm /opt/HLAminer_1-4.tar.gz
	mv /opt/HLAminer-1.4/HLAminer_v1.4/* /opt/
	rm -rf /opt/HLAminer-1.4/
	sed -i 's/#!\/home\/martink\/bin\/perl/#!\/usr\/bin\/perl/g' /opt/bin/parseXMLblast.pl
	sed -i 's/#!\/home\/martink\/bin\/perl510/#!\/usr\/bin\/perl/g' /opt/bin/parseXMLblast.old
	
	sed -i 's/#!\/usr\/bin\/env perl/#!\/usr\/bin\/perl/g' /opt/bin/HLAminer.pl

	sed -i 's/\.\.\/bin/\/opt\/bin/g' /opt/bin/*.sh
	sed -i 's/\.\.\/database/\/opt\/database/g' /opt/bin/*.sh
	sed -i 's/\/opt\/bin\/HLAminer\.pl/\/opt\/bin\/HLAminer\.pl -p \/opt\/database\/hla_nom_p\.txt/g' /opt/bin/*.sh
	sed -i 's/ncbiBlastConfig\.txt/\/opt\/bin\/ncbiBlastConfig\.txt/' /opt/bin/*.sh
	sed -i 's/program\:\.\.\/bin\/blastall/program\:\/opt\/bin\/blastall/g' /opt/bin/ncbiBlastConfig2-2-22.txt

	sed -i 's/\/home\/pubseq\/BioSw\/bwa\/bwa-0.5.9\/bwa/bwa/g' /opt/bin/*.sh
	sed -i 's/\/home\/pubseq\/BioSw\/bwa\/bwa-0.5.9\/bwa/bwa/g' /opt/database/*.sh
	sed -i 's/\.\.\/bin\/formatdb/formatdb/g' /opt/database/*.sh
	sed -i 's/formatdb/\/opt\/bin\/formatdb/g' /opt/database/*.sh

	cd /opt/database && ./updateHLAcoding.sh
	cd /opt/database && ./updateHLAgenomic.sh
	cd /opt/database && ./updateHLA-I_II_coding.sh
	cd /opt/database && ./updateHLA-I_II_genomic.sh
	cd /opt/database && ./update_p_designation.sh
	cd /opt/database && samtools faidx HLA_ABC_GEN.fasta


	chmod 775 /opt/bin/*
	PATH=$PATH:/opt/bin/
	export PATH

%environment

	PATH=$PATH:/opt/bin/
	export PATH
```

## Collection

 - Name: [HugoMananet/HLAminer](https://github.com/HugoMananet/HLAminer)
 - License: None

