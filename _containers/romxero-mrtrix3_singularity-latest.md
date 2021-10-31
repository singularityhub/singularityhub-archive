---
id: 8659
name: "romxero/mrtrix3_singularity"
branch: "master"
tag: "latest"
commit: "2b3dfe3ad2c9f3feb245da1b0f42058ef61eb295"
version: "ee211eda12d12834a56c10c0a1694c1a"
build_date: "2019-10-02T16:56:42.138Z"
size_mb: 18022
size: 7617454111
sif: "https://datasets.datalad.org/shub/romxero/mrtrix3_singularity/latest/2019-10-02-2b3dfe3a-ee211eda/ee211eda12d12834a56c10c0a1694c1a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/mrtrix3_singularity/latest/2019-10-02-2b3dfe3a-ee211eda/
recipe: https://datasets.datalad.org/shub/romxero/mrtrix3_singularity/latest/2019-10-02-2b3dfe3a-ee211eda/Singularity
collection: romxero/mrtrix3_singularity
---

# romxero/mrtrix3_singularity:latest

```bash
$ singularity pull shub://romxero/mrtrix3_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bids/mrtrix3_connectome

%labels
Author "Sabir"

#########
#%setup
#########

#Downlaod packages
%post
  apt-get -ym update
  apt-get -ym install tcsh
  apt-get -ym install bc

%environment
  export IMAGE_NAME="mrtrix3_fix_v3"
```

## Collection

 - Name: [romxero/mrtrix3_singularity](https://github.com/romxero/mrtrix3_singularity)
 - License: None

