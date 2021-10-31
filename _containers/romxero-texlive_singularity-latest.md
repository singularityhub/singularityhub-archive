---
id: 9509
name: "romxero/texlive_singularity"
branch: "master"
tag: "latest"
commit: "a931e62f8033ade189155635fa48f8d5f5690ee0"
version: "1339f68519093be21ab759c5914b2e4b"
build_date: "2019-06-04T11:19:56.917Z"
size_mb: 715
size: 276168735
sif: "https://datasets.datalad.org/shub/romxero/texlive_singularity/latest/2019-06-04-a931e62f-1339f685/1339f68519093be21ab759c5914b2e4b.simg"
url: https://datasets.datalad.org/shub/romxero/texlive_singularity/latest/2019-06-04-a931e62f-1339f685/
recipe: https://datasets.datalad.org/shub/romxero/texlive_singularity/latest/2019-06-04-a931e62f-1339f685/Singularity
collection: romxero/texlive_singularity
---

# romxero/texlive_singularity:latest

```bash
$ singularity pull shub://romxero/texlive_singularity:latest
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
  apt-get -ym install texlive texlive-base texlive-font-utils ghostscript

%environment
  export IMAGE_NAME="tex_live_sherlock"
```

## Collection

 - Name: [romxero/texlive_singularity](https://github.com/romxero/texlive_singularity)
 - License: None

