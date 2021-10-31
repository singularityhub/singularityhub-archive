---
id: 11337
name: "biobox-info/Salmon"
branch: "v0.14.1"
tag: "v0.14.1"
commit: "3833a46c687f916273efddc6b2a0a82f00fb39f8"
version: "5a9797c8a9e8a3b73913fd3f91a81d66f8975c5bc0524bd0d5e1547415070791"
build_date: "2019-10-22T12:55:32.402Z"
size_mb: 367.80859375
size: 385675264
sif: "https://datasets.datalad.org/shub/biobox-info/Salmon/v0.14.1/2019-10-22-3833a46c-5a9797c8/5a9797c8a9e8a3b73913fd3f91a81d66f8975c5bc0524bd0d5e1547415070791.sif"
url: https://datasets.datalad.org/shub/biobox-info/Salmon/v0.14.1/2019-10-22-3833a46c-5a9797c8/
recipe: https://datasets.datalad.org/shub/biobox-info/Salmon/v0.14.1/2019-10-22-3833a46c-5a9797c8/Singularity
collection: biobox-info/Salmon
---

# biobox-info/Salmon:v0.14.1

```bash
$ singularity pull shub://biobox-info/Salmon:v0.14.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: combinelab/salmon:0.14.1

%environment
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

%post

%labels
MAINTAINER BioBox
Version v1.0
```

## Collection

 - Name: [biobox-info/Salmon](https://github.com/biobox-info/Salmon)
 - License: None

