---
id: 7363
name: "JFresnedo/AmpSeq"
branch: "master"
tag: "ampseq"
commit: "23d27295960bc47c354361814b7fb40091c241f0"
version: "0c0395fd85f969bc22ba66c6795906ad"
build_date: "2021-04-12T20:01:37.928Z"
size_mb: 6505
size: 3107274783
sif: "https://datasets.datalad.org/shub/JFresnedo/AmpSeq/ampseq/2021-04-12-23d27295-0c0395fd/0c0395fd85f969bc22ba66c6795906ad.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/JFresnedo/AmpSeq/ampseq/2021-04-12-23d27295-0c0395fd/
recipe: https://datasets.datalad.org/shub/JFresnedo/AmpSeq/ampseq/2021-04-12-23d27295-0c0395fd/Singularity
collection: JFresnedo/AmpSeq
---

# JFresnedo/AmpSeq:ampseq

```bash
$ singularity pull shub://JFresnedo/AmpSeq:ampseq
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%labels
	Maintainer Jonathan Fresnedo
	AmpSeq Sigularity Container

%post
	apt update 
	apt install -y apt-transport-https software-properties-common
	apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
	add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
	apt update
	apt install -y r-base
	apt update
	apt-add-repository universe
	apt update
	apt install -y git wget perl openjdk-8-jdk build-essential libtool libncurses5-dev libgtextutils-dev automake libbz2-dev liblzma-dev zlib1g-dev autoconf autogen cpanminus libgd-graph-perl libbio-samtools-perl git-lfs g++ cmake git-all pkg-config sed gnuplot-nox m4 libevent-dev gettext yaggo nano
	export LC_ALL=C.UTF-8
	export LANG=C.UTF-8
	echo 'export LC_ALL=C.UTF-8' >> "$SINGULARITY_ENVIRONMENT"
	echo 'export LANG=C.UTF-8' >> "$SINGULARITY_ENVIRONMENT"
	echo "export PATH=/usr/local/bin:$PATH" >> "$SINGULARITY_ENVIRONMENT"
	# Installing individual packages
	make /home
 	cd home
	git clone https://github.com/samtools/htslib.git
	cd htslib
	make
	make install
	cd ..	
	git clone https://github.com/samtools/samtools.git
	cd samtools	
	make
	make install
	cd ..
	git clone https://github.com/samtools/bcftools.git
	cd bcftools
	make
	make install
	cd ..	
	cpanm PerlIO::gzip
	cpanm GD::Graph
	cpanm GD::Graph::bars
	cpanm Bio::SeqIO
	cpanm Getopt::Std
	git clone https://github.com/lh3/bwa.git
	cd bwa
	make
	cp bwa /usr/local/bin
	cd ..
	git clone https://github.com/broadinstitute/picard.git
	cd picard
	./gradlew shadowJar
	cd ..
	cp -r picard /usr/local/bin
	rm -r picard
	git clone https://github.com/broadinstitute/gatk.git
	cd gatk
	./gradlew bundle
	cd ..
	cp -r gatk /usr/local/bin
	rm -r gatk	
	wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip
	unzip Trimmomatic-0.38.zip
	cp -r Trimmomatic-0.38 /usr/local/bin
	rm Trimmomatic-0.38.zip
	rm -r Trimmomatic-0.38/
	wget http://hannonlab.cshl.edu/fastx_toolkit/fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2
	tar -xvjf fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2	
	cp bin/* /usr/local/bin
	rm -r bin
	rm fastx_toolkit_0.0.13_binaries_Linux_2.6_amd64.tar.bz2
	wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast%2B/2.8.1/ncbi-blast-2.8.1%2B-x64-linux.tar.gz
	tar -xvzf ncbi-blast-2.8.1+-x64-linux.tar.gz 
	cp ncbi-blast-2.8.1+/bin/* /usr/local/bin
	rm -r ncbi-blast-2.8.1+
	rm ncbi-blast-2.8.1+-x64-linux.tar.gz
	wget https://sourceforge.net/projects/flashpage/files/FLASH-1.2.11.tar.gz
	tar -xvzf FLASH-1.2.11.tar.gz
	cd FLASH-1.2.11
	make
	cp flash /usr/local/bin	
	cd ..
	rm FLASH-1.2.11.tar.gz
	rm -r FLASH-1.2.11
	wget http://www.clustal.org/download/current/clustalw-2.1.tar.gz
	tar -xvzf clustalw-2.1.tar.gz
	cd clustalw-2.1
	./configure	
	make
	make install
	cd ..
	rm -r clustalw-2.1
	rm clustalw-2.1.tar.gz
	wget http://www.clustal.org/omega/clustalo-1.2.4-Ubuntu-x86_64
	chmod u+x clustalo-1.2.4-Ubuntu-x86_64
	cp clustalo-1.2.4-Ubuntu-x86_64 /usr/local/bin/clustalo
	rm clustalo-1.2.4-Ubuntu-x86_64
	wget https://github.com/gmarcais/Jellyfish/releases/download/v2.2.10/jellyfish-2.2.10.tar.gz
	tar -vxzf jellyfish-2.2.10.tar.gz
	cd jellyfish-2.2.10/
	./configure
	make
	make install
	cd ..
	rm -r jellyfish-2.2.10.tar.gz	
	rm -r jellyfish-2.2.10
	git clone https://github.com/vcftools/vcftools.git
	cd vcftools
	./autogen.sh
	./configure
	make
	make install
	cd ..
	rm -r vcftools
	cd /usr/local/bin
	git clone https://github.com/primer3-org/primer3.git
	cd primer3/src
	make
	make install
	# done
```

## Collection

 - Name: [JFresnedo/AmpSeq](https://github.com/JFresnedo/AmpSeq)
 - License: None

