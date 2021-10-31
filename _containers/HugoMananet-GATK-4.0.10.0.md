---
id: 5756
name: "HugoMananet/GATK"
branch: "master"
tag: "4.0.10.0"
commit: "fbe5aa686b7286305829fc5288f8e381e277d798"
version: "5b669b0e010a1647d305752b0dc54e89"
build_date: "2018-11-30T19:45:32.056Z"
size_mb: 3865
size: 1910857759
sif: "https://datasets.datalad.org/shub/HugoMananet/GATK/4.0.10.0/2018-11-30-fbe5aa68-5b669b0e/5b669b0e010a1647d305752b0dc54e89.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/HugoMananet/GATK/4.0.10.0/2018-11-30-fbe5aa68-5b669b0e/
recipe: https://datasets.datalad.org/shub/HugoMananet/GATK/4.0.10.0/2018-11-30-fbe5aa68-5b669b0e/Singularity
collection: HugoMananet/GATK
---

# HugoMananet/GATK:4.0.10.0

```bash
$ singularity pull shub://HugoMananet/GATK:4.0.10.0
```

## Singularity Recipe

```singularity
#!/bin/bash
#

Bootstrap: docker

From: phusion/baseimage:0.10.2


%label

	MAINTAINER Hugo Mananet


%environment

	JAVA_LIBRARY_PATH=/usr/lib/jni
	JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
	export JAVA_LIBRARY_PATH JAVA_HOME
	PATH=/opt/conda/envs/gatk/bin:/opt/miniconda/bin:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin
	export PATH
	. /opt/miniconda/etc/profile.d/conda.sh
	conda activate gatk

%files

	install_R_packages.R
	# gatk-4.0.10.0.zip


%post

	echo "\n\n######## Installing utilities needed by GATK 4.0.10.0 ########\n\n"
	apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y python && \
	apt-get install -y wget \
	unzip \
	aria2 \
	bedtools \
	samtools \
	openjdk-8-jdk \
	tabix \
	software-properties-common && \
	apt-get -y clean  && \
	apt-get -y autoclean  && \
	apt-get -y autoremove

	apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv-keys E084DAB9 && \
	add-apt-repository "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" && \
	apt-get update && \
	apt-get install -y --force-yes \
	r-base-dev=3.2.5-1xenial \
	r-base-core=3.2.5-1xenial && \
	apt-get -y clean && \
	apt-get -y autoremove && \
	apt-get -y autoclean


	Rscript install_R_packages.R
	rm install_R_packages.R

	echo "\n\n######## Installing the GATK 4.0.10.0 suite ########\n\n"
	aria2c -m 20 -x 16 -s 16 https://github.com/broadinstitute/gatk/releases/download/4.0.10.0/gatk-4.0.10.0.zip
	unzip gatk-4.0.10.0.zip
	mv gatk-4.0.10.0/ /opt/
	rm gatk-4.0.10.0.zip
	ln -s /opt/gatk-4.0.10.0/gatk /usr/bin/gatk
	ln -s /opt/gatk-package-4.0.10.0-local.jar /usr/bin/gatk-4.0.10.0.jar




	aria2c -m 20 -x 16 -s 16 https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
	bash -f Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda


	PATH=/opt/conda/envs/gatk/bin:/opt/miniconda/bin:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin
	export PATH
	ln -s /opt/miniconda/etc/profile.d/conda.sh /etc/profile.d/conda.sh

	conda env create -f /opt/gatk-4.0.10.0/gatkcondaenv.yml


%runscript


	exec gatk "$@"
```

## Collection

 - Name: [HugoMananet/GATK](https://github.com/HugoMananet/GATK)
 - License: None

