---
id: 2720
name: "sbutcher/container-R"
branch: "master"
tag: "latest"
commit: "637a67e1817dde2309f50d8c28ff0e63ff60c8db"
version: "eafd68b9f02178e1e6ca7db9aa308b00"
build_date: "2019-10-07T12:21:18.179Z"
size_mb: 854
size: 302391327
sif: "https://datasets.datalad.org/shub/sbutcher/container-R/latest/2019-10-07-637a67e1-eafd68b9/eafd68b9f02178e1e6ca7db9aa308b00.simg"
url: https://datasets.datalad.org/shub/sbutcher/container-R/latest/2019-10-07-637a67e1-eafd68b9/
recipe: https://datasets.datalad.org/shub/sbutcher/container-R/latest/2019-10-07-637a67e1-eafd68b9/Singularity
collection: sbutcher/container-R
---

# sbutcher/container-R:latest

```bash
$ singularity pull shub://sbutcher/container-R:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%post

	echo "##### Installing Development Tools YUM group #####"
	apt-get update
        apt-get -y install build-essential wget git binutils binutils-dev cmake gcc g++ gfortran bzip2  xz-utils liblzma-dev make libcurl4-openssl-dev libreadline-dev libpcre3-dev libbz2-dev zlib1g-dev
        sleep 60
        echo "Sleeping for a bit"
	wget https://cran.r-project.org/src/base/R-latest.tar.gz
	tar zxf R-latest.tar.gz
	cd R-*
	./configure --enable-R-shlib --with-x=no
	make
	make install


	echo "##### getting the R code #####"

%test
        R --version

%runscript
	echo "##### Loading R #####"
	exec R
```

## Collection

 - Name: [sbutcher/container-R](https://github.com/sbutcher/container-R)
 - License: None

