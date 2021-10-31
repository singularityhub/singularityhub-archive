---
id: 8434
name: "iferres/Singularity_recipes"
branch: "master"
tag: "pgap"
commit: "4e3800fbad819fb96836528025170a2836aa564a"
version: "aaf62701980603563555920c5843b5f7"
build_date: "2020-10-19T08:34:46.683Z"
size_mb: 827
size: 300822559
sif: "https://datasets.datalad.org/shub/iferres/Singularity_recipes/pgap/2020-10-19-4e3800fb-aaf62701/aaf62701980603563555920c5843b5f7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/iferres/Singularity_recipes/pgap/2020-10-19-4e3800fb-aaf62701/
recipe: https://datasets.datalad.org/shub/iferres/Singularity_recipes/pgap/2020-10-19-4e3800fb-aaf62701/Singularity
collection: iferres/Singularity_recipes
---

# iferres/Singularity_recipes:pgap

```bash
$ singularity pull shub://iferres/Singularity_recipes:pgap
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04


%post
	export DEBIAN_FRONTEND=noninteractive
	apt update
	apt install -y software-properties-common
	add-apt-repository -y ppa:openjdk-r/ppa  
	apt update && apt upgrade -y
	apt install -y make gcc patch wget mafft mcl openjdk-7-jre-headless phylip libexpat-dev pkg-config libgd-dev build-essential libxml-libxml-perl
	apt clean -y
	export PERL_MM_USE_DEFAULT=1
	cpan -i App::cpanminus
	cpanm -i Statistics::LineFit
	cpanm -i Statistics::Distributions
	cpanm -i Bio::AlignIO # Falla acá en build pero no en shell (?)
	wget https://downloads.sourceforge.net/project/pgap/PGAP-1.2.1/PGAP-1.2.1.tar.gz
	tar -xzf PGAP-1.2.1.tar.gz 
	rm -f PGAP-1.2.1.tar.gz
	chmod a+x PGAP-1.2.1/*.pl

%runscript 
	/PGAP-1.2.1/PGAP.pl "$@"

%labels 
	author Ignacio Ferres
```

## Collection

 - Name: [iferres/Singularity_recipes](https://github.com/iferres/Singularity_recipes)
 - License: None

