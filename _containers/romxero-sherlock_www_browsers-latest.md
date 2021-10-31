---
id: 9511
name: "romxero/sherlock_www_browsers"
branch: "master"
tag: "latest"
commit: "0d32fcfd9fd4a7189bbbeae353acd38dd99a1c17"
version: "75e6c36416af5c2acb45171f01f281b6"
build_date: "2021-02-08T19:50:20.989Z"
size_mb: 734
size: 316166175
sif: "https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/latest/2021-02-08-0d32fcfd-75e6c364/75e6c36416af5c2acb45171f01f281b6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/sherlock_www_browsers/latest/2021-02-08-0d32fcfd-75e6c364/
recipe: https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/latest/2021-02-08-0d32fcfd-75e6c364/Singularity
collection: romxero/sherlock_www_browsers
---

# romxero/sherlock_www_browsers:latest

```bash
$ singularity pull shub://romxero/sherlock_www_browsers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:stretch-slim

%labels
Author "Randall Cab White - rcwhite@stanford.edu"


#########
#%setup
#########

#Downlaod packages
%post
  apt-get -ym update
  apt-get -ym install wget firefox-esr bzip2
	wget -O firefox.tar.bz2 "https://download.mozilla.org/?product=firefox-devedition-latest-ssl&os=linux64&lang=en-US"
	tar xvf firefox.tar.bz2
%environment
  export IMAGE_NAME="firefox_dev_edition"
%runscript
	/firefox/firefox-bin
```

## Collection

 - Name: [romxero/sherlock_www_browsers](https://github.com/romxero/sherlock_www_browsers)
 - License: None

