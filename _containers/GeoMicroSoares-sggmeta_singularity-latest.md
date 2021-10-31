---
id: 5163
name: "GeoMicroSoares/sggmeta_singularity"
branch: "master"
tag: "latest"
commit: "e568c7bacd5543fefe83b1d3bc3b4a76175c4aa0"
version: "0d9d13bb9eab9038f3db07602b44e618"
build_date: "2018-10-23T17:47:48.160Z"
size_mb: 6056
size: 2369478687
sif: "https://datasets.datalad.org/shub/GeoMicroSoares/sggmeta_singularity/latest/2018-10-23-e568c7ba-0d9d13bb/0d9d13bb9eab9038f3db07602b44e618.simg"
url: https://datasets.datalad.org/shub/GeoMicroSoares/sggmeta_singularity/latest/2018-10-23-e568c7ba-0d9d13bb/
recipe: https://datasets.datalad.org/shub/GeoMicroSoares/sggmeta_singularity/latest/2018-10-23-e568c7ba-0d9d13bb/Singularity
collection: GeoMicroSoares/sggmeta_singularity
---

# GeoMicroSoares/sggmeta_singularity:latest

```bash
$ singularity pull shub://GeoMicroSoares/sggmeta_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:18.04

%help
	Tools required for the analysis of metagenomics data generated by the Ex^2EL laboratory 
(Aberystwyth University interdisciplinary Centre for Environmental Microbiology) in the context of project 
GEOCARB-CYMRU (http://www.nrn-lcee.ac.uk/geo-carb-cymru/).

%labels
	MAINTAINER André Soares

%environment

%post
	sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
	yes | apt-get update && apt-get upgrade -y
	yes | apt-get install software-properties-common
        yes | add-apt-repository ppa:ubuntu-toolchain-r/test
	#install git
	apt-get install -y git
	#install software-properties-common build-essential
	yes | apt-get install build-essential python3-pip python-pip
	yes | apt-get install autotools-dev g++ --fix-broken
	apt-get install --reinstall make
	yes | apt-get install automake autoconf zlib1g-dev
	#install fastp
	git clone https://github.com/OpenGene/fastp && cd fastp && make && make install
	#install Sickle
	yes | apt-get install zlib1g-dev
	cd && git clone https://github.com/najoshi/sickle && cd sickle && make
	#install IDBA 
	cd && git clone https://github.com/loneknightpy/idba && cd idba/ \
		&& ./build.sh
	#install metaSPADES
	yes | apt-get install wget
	cd && wget http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz && tar -xzf SPAdes-3.13.0-Linux.tar.gz && \
		cd SPAdes-3.13.0-Linux/bin/
	#install CheckM plus its dependency, pplacer, plus its dependencies, bah
	#add-apt-repository ppa:avsm/ocaml42+opam120
	yes | apt-get update
	yes | apt-get install ocaml opam
	cd && apt-get install -y \
	  camlp4-extra \
	  gawk \
	  libgsl0-dev \
	  libsqlite3-dev \
	  libz-dev \
	  m4 \
	  make \
	  ocaml \
	  patch \
	  opam
	opam init
	command -v ocamlc && ( ocamlc -version | grep -q 3.12.1 ) || opam switch install 3.12.1
	#opam init
	opam repo add pplacer-deps http://matsen.github.com/pplacer-opam-repository
	opam update pplacer-deps
	eval `opam config env`
	cd && git clone https://github.com/matsen/pplacer && cd pplacer && sed -i '/sqlite3.1.6.3/c\sqlite3' opam-requirements.txt && cat opam-requirements.txt && cat opam-requirements.txt | xargs opam install -y && make 
	cd && pip install checkm-genome
	#install kaiju
	cd && git clone https://github.com/bioinformatics-centre/kaiju.git && cd kaiju/src && make
	#install kraken2
	cd && git clone https://github.com/DerrickWood/kraken2 && cd kraken2 && ./install_kraken2.sh . && cp *-build $HOME/bin && cp *-inspect $HOME/bin
	#install MaxBin2
	cd && wget https://downloads.jbei.org/data/microbial_communities/MaxBin/getfile.php?MaxBin-2.2.5.tar.gz && tar -xzvf getfile.php\?MaxBin-2.2.5.tar.gz && cd MaxBin-2.2.5/src && make && cd .. && ./autobuild_auxiliary
	#install prokka
	cd && yes | apt-get install libdatetime-perl libxml-simple-perl libdigest-md5-perl git default-jre bioperl && cpan Bio::Perl && git clone https://github.com/tseemann/prokka.git && cd prokka/bin && ./prokka --setupdb
	#install minimap2
	cd && git clone https://github.com/lh3/minimap2 && cd minimap2 && make
	#install bowtie2-2.3.4.3
	yes | apt-get install libtbb-dev
	cd && wget https://kent.dl.sourceforge.net/project/bowtie-bio/bowtie2/2.3.4.3/bowtie2-2.3.4.3-linux-x86_64.zip && unzip bowtie2-2.3.4.3-linux-x86_64.zip && cd bowtie2-2.3.4.3-linux-x86_64 && cp $HOME/bin bowtie2 && cp $HOME/bin bowtie2-build && cp $HOME/bin bowtie2-inspect
	#install DAS_Tool, R
	yes | apt-get install r-base-core
	wget https://cran.r-project.org/src/contrib/data.table_1.11.8.tar.gz && R CMD INSTALL data.table_1.11.8.tar.gz
	wget https://cran.r-project.org/src/contrib/iterators_1.0.10.tar.gz && R CMD INSTALL iterators_1.0.10.tar.gz
	wget https://cran.r-project.org/src/contrib/foreach_1.4.4.tar.gz && R CMD INSTALL foreach_1.4.4.tar.gz
	wget https://cran.r-project.org/src/contrib/doMC_1.3.5.tar.gz && R CMD INSTALL doMC_1.3.5.tar.gz
	wget https://cran.r-project.org/src/contrib/Rcpp_0.12.19.tar.gz && R CMD INSTALL Rcpp_0.12.19.tar.gz
	wget https://cran.r-project.org/src/contrib/plyr_1.8.4.tar.gz && R CMD INSTALL plyr_1.8.4.tar.gz
	wget https://cloud.r-project.org/src/contrib/gtable_0.2.0.tar.gz && R CMD INSTALL gtable_0.2.0.tar.gz
	wget https://cloud.r-project.org/src/contrib/lazyeval_0.2.1.tar.gz && R CMD INSTALL lazyeval_0.2.1.tar.gz
	wget https://cran.r-project.org/src/contrib/glue_1.3.0.tar.gz && R CMD INSTALL glue_1.3.0.tar.gz
	wget https://cran.r-project.org/src/contrib/magrittr_1.5.tar.gz && R CMD INSTALL magrittr_1.5.tar.gz
	wget https://cran.r-project.org/src/contrib/stringi_1.2.4.tar.gz && R CMD INSTALL stringi_1.2.4.tar.gz
	wget https://cran.r-project.org/src/contrib/stringr_1.3.1.tar.gz && R CMD INSTALL stringr_1.3.1.tar.gz
	wget https://cloud.r-project.org/src/contrib/reshape2_1.4.3.tar.gz && R CMD INSTALL reshape2_1.4.3.tar.gz
	wget https://cloud.r-project.org/src/contrib/rlang_0.2.2.tar.gz && R CMD INSTALL rlang_0.2.2.tar.gz
        wget https://cloud.r-project.org/src/contrib/viridisLite_0.3.0.tar.gz && R CMD INSTALL viridisLite_0.3.0.tar.gz
	wget https://cran.r-project.org/src/contrib/labeling_0.3.tar.gz && R CMD INSTALL labeling_0.3.tar.gz
	wget https://cran.r-project.org/src/contrib/colorspace_1.3-2.tar.gz && R CMD INSTALL colorspace_1.3-2.tar.gz
	wget https://cran.r-project.org/src/contrib/munsell_0.5.0.tar.gz && R CMD INSTALL munsell_0.5.0.tar.gz
	wget https://cran.r-project.org/src/contrib/R6_2.3.0.tar.gz && R CMD INSTALL R6_2.3.0.tar.gz
	wget https://cran.r-project.org/src/contrib/RColorBrewer_1.1-2.tar.gz && R CMD INSTALL RColorBrewer_1.1-2.tar.gz
	wget https://cloud.r-project.org/src/contrib/scales_1.0.0.tar.gz && R CMD INSTALL scales_1.0.0.tar.gz
	wget https://cran.r-project.org/src/contrib/crayon_1.3.4.tar.gz && R CMD INSTALL crayon_1.3.4.tar.gz
	wget https://cran.r-project.org/src/contrib/assertthat_0.2.0.tar.gz && R CMD INSTALL assertthat_0.2.0.tar.gz
	wget https://cran.r-project.org/src/contrib/cli_1.0.1.tar.gz && R CMD INSTALL cli_1.0.1.tar.gz
	wget https://cran.r-project.org/src/contrib/fansi_0.4.0.tar.gz && R CMD INSTALL fansi_0.4.0.tar.gz
	wget https://cran.r-project.org/src/contrib/utf8_1.1.4.tar.gz && R CMD INSTALL utf8_1.1.4.tar.gz
	wget https://cran.r-project.org/src/contrib/pillar_1.3.0.tar.gz && R CMD INSTALL pillar_1.3.0.tar.gz
	wget https://cloud.r-project.org/src/contrib/tibble_1.4.2.tar.gz && R CMD INSTALL tibble_1.4.2.tar.gz
	wget https://cloud.r-project.org/src/contrib/withr_2.1.2.tar.gz && R CMD INSTALL withr_2.1.2.tar.gz
	wget https://cloud.r-project.org/src/contrib/digest_0.6.18.tar.gz && R CMD INSTALL digest_0.6.18.tar.gz
	wget https://cran.r-project.org/src/contrib/ggplot2_3.0.0.tar.gz && R CMD INSTALL ggplot2_3.0.0.tar.gz
	cd && git clone https://github.com/cmks/DAS_Tool.git && cd DAS_Tool && R CMD INSTALL ./package/*tar.gz && unzip ./db.zip -d db

%files
	#kraken2 databases? others?

%help
	If anything's needed, ans74@aber.ac.uk is the email.
```

## Collection

 - Name: [GeoMicroSoares/sggmeta_singularity](https://github.com/GeoMicroSoares/sggmeta_singularity)
 - License: None
