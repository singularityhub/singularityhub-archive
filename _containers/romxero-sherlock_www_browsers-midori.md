---
id: 9515
name: "romxero/sherlock_www_browsers"
branch: "master"
tag: "midori"
commit: "0d32fcfd9fd4a7189bbbeae353acd38dd99a1c17"
version: "442fecca6f61a7de60af1083b7c23b12"
build_date: "2020-02-27T21:45:50.334Z"
size_mb: 436
size: 155598879
sif: "https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/midori/2020-02-27-0d32fcfd-442fecca/442fecca6f61a7de60af1083b7c23b12.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/sherlock_www_browsers/midori/2020-02-27-0d32fcfd-442fecca/
recipe: https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/midori/2020-02-27-0d32fcfd-442fecca/Singularity
collection: romxero/sherlock_www_browsers
---

# romxero/sherlock_www_browsers:midori

```bash
$ singularity pull shub://romxero/sherlock_www_browsers:midori
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
  apt-get -ym install midori gnome-icon-theme
%environment
  export IMAGE_NAME="midori"
%runscript
	midori
```

## Collection

 - Name: [romxero/sherlock_www_browsers](https://github.com/romxero/sherlock_www_browsers)
 - License: None

