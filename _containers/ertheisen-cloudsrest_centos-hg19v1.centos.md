---
id: 6504
name: "ertheisen/cloudsrest_centos"
branch: "master"
tag: "hg19v1.centos"
commit: "ed24b4e6052d9937577721ef38ed79f5b750d8e5"
version: "872b33cf062f5590baa06e41327cf096"
build_date: "2019-06-14T18:25:03.475Z"
size_mb: 6868
size: 2549145631
sif: "https://datasets.datalad.org/shub/ertheisen/cloudsrest_centos/hg19v1.centos/2019-06-14-ed24b4e6-872b33cf/872b33cf062f5590baa06e41327cf096.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ertheisen/cloudsrest_centos/hg19v1.centos/2019-06-14-ed24b4e6-872b33cf/
recipe: https://datasets.datalad.org/shub/ertheisen/cloudsrest_centos/hg19v1.centos/2019-06-14-ed24b4e6-872b33cf/Singularity
collection: ertheisen/cloudsrest_centos
---

# ertheisen/cloudsrest_centos:hg19v1.centos

```bash
$ singularity pull shub://ertheisen/cloudsrest_centos:hg19v1.centos
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:centos:centos7.4.1708

%help
Singularity container containing following apps for RNA-seq and processing.
 fastqc_pre : FastQC pre-trim
 trim_qc : Fastq trimming with Trim Galore and FastQC post trim
 rnaseq_STAR: Use to generate readcounts from fastq data using STAR; requires loading the STAR index in /genomes/STAR and the gff file in genomes/anno
 rnaseq_full: full pipeline from fastqc to readcounts

%files
	fastqc_pre.py /
	trim_qc.py /
	rnaseq_STAR.py /
	rnaseq.py /


%post
	mkdir /genomes
	mkdir /genomes/test
	mkdir /genomes/spike
	mkdir /genomes/STAR
	mkdir /genomes/anno
	mkdir /data
	mkdir /appscripts

    yum -y install epel-release \
                   git \
                   wget \
                   cairo-devel \
                   firefox.x86_64 \
                   libX11 \
                   libXt \
                   libXt-devel \
                   libX11-devel \
                   xorg-x11* \
                   xauth \
                   dbus-x11 \
                   freetype \
				   less \
				   ed \
				   ca-certificates \
				   ghostscript-fonts \
				   tkinter \
       			   openssl-devel \
        		   libxml2-devel \
				   centos-release-scl \
				   readline-devel \
				   gcc-c++ \
				   gcc-gfortran \
				   zlib-devel \
				   bzip2-devel \
				   xz-devel \
				   pcre-devel \
        		   udunits2-devel

    yum -y install netcdf-devel \
				   netcdf4-python \
				   python-pip \
				   python-pandas \
				   python-matplotlib \
                   mesa-libGL \
				   libpng-devel \
				   libjpeg-devel \
				   libtiff-devel 

	yum install -y libcurl-devel
	yum install -y libX11-devel libXt-devel 
	yum install -y cairo pango-devel 
	yum install -y libicu-devel
	yum install -y texinfo 
	yum install -y texlive-latex-bin-bin 
	yum install -y make 
	yum install -y which 
	yum install -y qpdf 
	yum install -y valgrind
	yum install -y curl 
	yum install -y unzip
	yum install -y perl 
	yum install -y java-1.8.0-openjdk-headless
	yum install -y qpdf 
	yum install -y valgrind
	yum install -y BEDTools

	rm -rf /var/lib/apt/lists/*

	yum -y install R
 	yum -y install R-devel
	mkdir -p /usr/local/lib64/R/bin
	ln -s /usr/bin/R /usr/local/lib64/R/bin/R

	## workaround X11/png clash in Jupyter Notebook
	## see: https://github.com/IRkernel/IRkernel/issues/388
	echo "options(bitmapType='cairo')" >> /usr/lib64/R/Rprofile.site
	echo "options(device=png)" >> /usr/lib64/R/Rprofile.site

	## set library, Rprofile where IRkernel installed
	echo 'export R_LIBS=/usr/lib64/R/library R_ENVIRON=/usr/lib64/R/Rprofile.site' >> $SINGULARITY_ENVIRONMENT

	## python, Jupyter
	yum -y install https://centos7.iuscommunity.org/ius-release.rpm
	yum -y install python36u
	yum -y install python36u-pip \
				   python36u-devel \
				   python36u-setuptools


	python3.6 -m pip install wheel
	python3.6 -m pip install jupyter
	python3.6 -m pip install pandas
	python3.6 -m pip install matplotlib
	python3.6 -m pip install scipy
	python3.6 -m pip install numpy
	python3.6 -m pip install pybedtools
	python3.6 -m pip install pysam
	python3.6 -m pip install cutadapt
	python3.6 -m pip install py2bit
	python3.6 -m pip install pyBigWig
	python3.6 -m pip install deeptools

	## error on mkdir permission for /run/users/1001 where Jupyter likes to run
	chmod -R 777 /run

	## install X11 for Jupyter
	#https://www.itzgeek.com/how-tos/linux/centos-how-tos/install-gnome-gui-on-centos-7-rhel-7.html
	ln -sf /lib/systemd/system/runlevel5.target /etc/systemd/system/default.target

	## locales
	echo 'export LANG=en_US.UTF-8 LANGUAGE=C LC_ALL=C LC_CTYPE=C LC_COLLATE=C  LC_TIME=C LC_MONETARY=C LC_PAPER=C LC_MEASUREMENT=C' >> $SINGULARITY_ENVIRONMENT

	#BiocManager to allow further install of packages
	mkdir /usr/share/doc/R-3.5.2/html
	R --slave -e 'install.packages("BiocManager", repos="https://cloud.r-project.org/", quiet=T)'
	R --slave -e 'library("BiocManager"); BiocManager::install("IRkernel", dependencies=TRUE, update=TRUE, ask=FALSE); IRkernel::installspec(user = FALSE)'
	R --slave -e 'library("BiocManager"); BiocManager::install("Cairo", dependencies=TRUE, update=TRUE, ask=FALSE)'
	R --slave -e 'library("BiocManager"); BiocManager::install("csaw", dependencies=TRUE, update=TRUE, ask=FALSE)'

	cd /tmp

	curl -SLO http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.4.zip
	unzip fastqc_v0.11.4.zip -d /opt
	rm fastqc_v0.11.4.zip
	chmod a+x /opt/FastQC/fastqc

	echo 'export PATH=/opt/FastQC:$PATH' >> $SINGULARITY_ENVIRONMENT

	cd /tmp

	mkdir /opt/trim_galore-0.4.5

	curl -fsSL https://github.com/FelixKrueger/TrimGalore/archive/0.4.5.tar.gz -o trim_galore-0.4.5.tar.gz
	tar xvzf trim_galore-0.4.5.tar.gz
	mv TrimGalore-0.4.5/trim_galore /opt/trim_galore-0.4.5

	chmod a+x /opt/trim_galore-0.4.5

	echo 'PATH=/opt/trim_galore-0.4.5:$PATH' >> $SINGULARITY_ENVIRONMENT

	python -m pip install scipy
	python -m pip install pybedtools
	python -m pip install pysam==0.11.2.2
	python -m pip install numpy
	python -m pip install wheel
	python -m pip install macs2
	python -m pip install pysam
	python -m pip install cython
	python -m pip install edd

	wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.4.3/bowtie2-2.3.4.3-linux-x86_64.zip/download
	unzip download
	rm download
	mv bowtie2-2.3.4.3-linux-x86_64 /opt/bowtie2-2.3.4.3

	echo 'PATH=/opt/bowtie2-2.3.4.3:$PATH' >> $SINGULARITY_ENVIRONMENT

	yum install -y openssh-server openssh-client rsync grsync

	mkdir /opt/UCSC-utils
	cd /opt/UCSC-utils
	rsync -aP rsync://hgdownload.soe.ucsc.edu/genome/admin/exe/linux.x86_64/ ./

	echo 'PATH=/opt/UCSC-utils:$PATH' >> $SINGULARITY_ENVIRONMENT
	echo 'PATH=/opt/UCSC-utils/blat:$PATH' >> $SINGULARITY_ENVIRONMENT

	cd /tmp

	mkdir /opt/STAR-2.6.1d

	curl -SLO https://github.com/alexdobin/STAR/archive/2.6.1d.tar.gz
	tar -xzf 2.6.1d.tar.gz
	mv STAR-2.6.1d/ /opt

	chmod a+x /opt/STAR-2.6.1d/bin

	echo 'PATH=/opt/STAR-2.6.1d/bin/Linux_x86_64_static:$PATH' >> $SINGULARITY_ENVIRONMENT

	yum -y install samtools

	mv /fastqc_pre.py /appscripts/
	mv /trim_qc.py /appscripts/
	mv /rnaseq_STAR.py /appscripts/
	mv /rnaseq.py /appscripts/


%apprun fastqc_pre
	python /appscripts/fastqc_pre.py

%apprun trim_qc
	python /appscripts/trim_qc.py

%apprun rnaseq_STAR
	python /appscripts/rnaseq_STAR.py

%apprun rnaseq_full
	python /appscripts/rnaseq.py
```

## Collection

 - Name: [ertheisen/cloudsrest_centos](https://github.com/ertheisen/cloudsrest_centos)
 - License: None

