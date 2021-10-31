---
id: 3613
name: "MarissaLL/singularity-containers"
branch: "master"
tag: "pgdspider_2.1.1.5"
commit: "e34376dabe1cf7634e40ed8f2eed3207be3d5594"
version: "8b5077adfd4db0dbe951247fb1fbfd13"
build_date: "2020-04-27T22:26:29.877Z"
size_mb: 735
size: 293158943
sif: "https://datasets.datalad.org/shub/MarissaLL/singularity-containers/pgdspider_2.1.1.5/2020-04-27-e34376da-8b5077ad/8b5077adfd4db0dbe951247fb1fbfd13.simg"
url: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/pgdspider_2.1.1.5/2020-04-27-e34376da-8b5077ad/
recipe: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/pgdspider_2.1.1.5/2020-04-27-e34376da-8b5077ad/Singularity
collection: MarissaLL/singularity-containers
---

# MarissaLL/singularity-containers:pgdspider_2.1.1.5

```bash
$ singularity pull shub://MarissaLL/singularity-containers:pgdspider_2.1.1.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels

	MAINTAINER "Marissa Le Lec"
	VERSION "PGDSpider 2.1.1.5"

%post

	apt-get update
	apt-get install -y build-essential language-pack-en wget unzip openjdk-8-jre
	wget http://www.cmpg.unibe.ch/software/PGDSpider/PGDSpider_2.1.1.5.zip
	unzip PGDSpider_2.1.1.5.zip
	cp -r PGDSpider_2.1.1.5 /opt/pgdspider
	rm -r PGDSpider_2.1.1.5

%environment
	
	export PATH="${PATH}:/opt/pgdspider"

%runscript

	/usr/bin/java -jar /opt/pgdspider/PGDSpider2-cli.jar "$@"
```

## Collection

 - Name: [MarissaLL/singularity-containers](https://github.com/MarissaLL/singularity-containers)
 - License: None

