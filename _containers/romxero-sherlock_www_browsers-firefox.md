---
id: 9513
name: "romxero/sherlock_www_browsers"
branch: "master"
tag: "firefox"
commit: "0d32fcfd9fd4a7189bbbeae353acd38dd99a1c17"
version: "d9d3d0a12bf268aca44a91bda116dc00"
build_date: "2020-04-06T01:38:20.133Z"
size_mb: 475
size: 177106975
sif: "https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/firefox/2020-04-06-0d32fcfd-d9d3d0a1/d9d3d0a12bf268aca44a91bda116dc00.simg"
url: https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/firefox/2020-04-06-0d32fcfd-d9d3d0a1/
recipe: https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/firefox/2020-04-06-0d32fcfd-d9d3d0a1/Singularity
collection: romxero/sherlock_www_browsers
---

# romxero/sherlock_www_browsers:firefox

```bash
$ singularity pull shub://romxero/sherlock_www_browsers:firefox
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
  apt-get -ym install firefox-esr 

%environment
  export IMAGE_NAME="firefox"
%runscript
	firefox
```

## Collection

 - Name: [romxero/sherlock_www_browsers](https://github.com/romxero/sherlock_www_browsers)
 - License: None

