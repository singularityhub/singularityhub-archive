---
id: 9512
name: "romxero/sherlock_www_browsers"
branch: "master"
tag: "chromium"
commit: "2fd427d06022c200c1fabce07763e37c88d58a5a"
version: "4ccdda64a53c3d9c640a41ac40409028"
build_date: "2019-08-20T19:22:35.493Z"
size_mb: 740
size: 283672607
sif: "https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/chromium/2019-08-20-2fd427d0-4ccdda64/4ccdda64a53c3d9c640a41ac40409028.simg"
url: https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/chromium/2019-08-20-2fd427d0-4ccdda64/
recipe: https://datasets.datalad.org/shub/romxero/sherlock_www_browsers/chromium/2019-08-20-2fd427d0-4ccdda64/Singularity
collection: romxero/sherlock_www_browsers
---

# romxero/sherlock_www_browsers:chromium

```bash
$ singularity pull shub://romxero/sherlock_www_browsers:chromium
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
  apt-get -ym install chromium-shell chromium-l10n chromium-driver chromium

%environment
  export IMAGE_NAME="chromium"
%runscript
	chromium --no-sandbox
```

## Collection

 - Name: [romxero/sherlock_www_browsers](https://github.com/romxero/sherlock_www_browsers)
 - License: None

