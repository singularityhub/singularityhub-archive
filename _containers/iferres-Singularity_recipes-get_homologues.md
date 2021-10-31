---
id: 8369
name: "iferres/Singularity_recipes"
branch: "master"
tag: "get_homologues"
commit: "92f333e5574a67d7f8e20b7f9aa96281e508fe39"
version: "3604733037a576babc2c651c33955d94"
build_date: "2019-10-18T09:44:12.746Z"
size_mb: 1598
size: 628219935
sif: "https://datasets.datalad.org/shub/iferres/Singularity_recipes/get_homologues/2019-10-18-92f333e5-36047330/3604733037a576babc2c651c33955d94.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/iferres/Singularity_recipes/get_homologues/2019-10-18-92f333e5-36047330/
recipe: https://datasets.datalad.org/shub/iferres/Singularity_recipes/get_homologues/2019-10-18-92f333e5-36047330/Singularity
collection: iferres/Singularity_recipes
---

# iferres/Singularity_recipes:get_homologues

```bash
$ singularity pull shub://iferres/Singularity_recipes:get_homologues
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04


# Install dependencies from repos: GD for graphics, libidn11 for BLAST+
%post
	export DEBIAN_FRONTEND=noninteractive
	apt update && apt upgrade -y
	apt install -y software-properties-common
	add-apt-repository ppa:anton+/photo-video-apps -y
	apt update && apt upgrade -y
	apt install -y git htop curl make geeqie evince default-jre libgd-gd2-perl libidn11 libpython2.7 procps bc wget r-base r-base-dev
	apt autoremove && apt clean -y
	#curl -L http://cpanmin.us | perl - App::cpanminus
	cpan -i App::cpanminus
	export PERL_MM_USE_DEFAULT=1
	cpanm -if Inline::C 
	cpanm -if Inline::CPP@0.75
	git clone https://github.com/eead-csic-compbio/get_homologues.git
	cd get_homologues/
	git checkout 37fe5738fe2f7911bd1979b9cebebf3bedee69c1
	perl install.pl no_databases
	chmod a+wr db/
	cd ../

%environment 
	export PATH="/get_homologues:${PATH}"

%runscript
	#perl get_homologues/get_homologues.pl
	get_homologues.pl
	

%labels
	author Ignacio Ferres
```

## Collection

 - Name: [iferres/Singularity_recipes](https://github.com/iferres/Singularity_recipes)
 - License: None

