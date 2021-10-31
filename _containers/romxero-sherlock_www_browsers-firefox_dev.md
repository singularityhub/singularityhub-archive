---
id: 9514
name: "romxero/sherlock_www_browsers"
branch: "master"
tag: "firefox_dev"
commit: "0d32fcfd9fd4a7189bbbeae353acd38dd99a1c17"
version: "e9bdd2cc44b5c6ddda88fa5538648e27"
build_date: "2021-04-19T19:12:32.597Z"
size_mb: 734
size: 316166175
sif: "https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/firefox_dev/2021-04-19-0d32fcfd-e9bdd2cc/e9bdd2cc44b5c6ddda88fa5538648e27.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/sherlock_www_browsers/firefox_dev/2021-04-19-0d32fcfd-e9bdd2cc/
recipe: https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/firefox_dev/2021-04-19-0d32fcfd-e9bdd2cc/Singularity
collection: romxero/sherlock_www_browsers
---

# romxero/sherlock_www_browsers:firefox_dev

```bash
$ singularity pull shub://romxero/sherlock_www_browsers:firefox_dev
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

