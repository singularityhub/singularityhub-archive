---
id: 14166
name: "drmach/test_singularity"
branch: "master"
tag: "latest"
commit: "82e693988d8e8fcc699fac3fc8c0115d046d663a"
version: "c9d577c7304abbfec2105f76e50e79dd"
build_date: "2020-09-03T11:18:22.563Z"
size_mb: 316.0
size: 120193055
sif: "https://datasets.datalad.org/shub/drmach/test_singularity/latest/2020-09-03-82e69398-c9d577c7/c9d577c7304abbfec2105f76e50e79dd.sif"
url: https://datasets.datalad.org/shub/drmach/test_singularity/latest/2020-09-03-82e69398-c9d577c7/
recipe: https://datasets.datalad.org/shub/drmach/test_singularity/latest/2020-09-03-82e69398-c9d577c7/Singularity
collection: drmach/test_singularity
---

# drmach/test_singularity:latest

```bash
$ singularity pull shub://drmach/test_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
	MAINTAINER Marios
	
%runscript

    echo "Testing singularity hub builds with github"

%post
 
   echo "Very simple case to see if it works"
   apt-get update
   apt-get install -y software-properties-common
   apt-get update
   apt-get install -y wget
   add-apt-repository http://dl.openfoam.org/ubuntu
   sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"
   apt-get update
   apt-get install -y git
   mkdir marios
   cd marios
   touch file1
```

## Collection

 - Name: [drmach/test_singularity](https://github.com/drmach/test_singularity)
 - License: None

