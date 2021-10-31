---
id: 14594
name: "j23414/singularity_event"
branch: "main"
tag: "latest"
commit: "6658031658478e856ffb6567c71de2c99c45b876"
version: "44d1a34a8767c8583ddf44f078478048"
build_date: "2020-10-12T18:59:50.452Z"
size_mb: 219.0
size: 85463071
sif: "https://datasets.datalad.org/shub/j23414/singularity_event/latest/2020-10-12-66580316-44d1a34a/44d1a34a8767c8583ddf44f078478048.sif"
url: https://datasets.datalad.org/shub/j23414/singularity_event/latest/2020-10-12-66580316-44d1a34a/
recipe: https://datasets.datalad.org/shub/j23414/singularity_event/latest/2020-10-12-66580316-44d1a34a/Singularity
collection: j23414/singularity_event
---

# j23414/singularity_event:latest

```bash
$ singularity pull shub://j23414/singularity_event:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%labels
    MAINTAINER Jennifer Chang
    EMAIL jenchang@iastate.edu

%runscript
    echo "This is a usage statement"

%post
    apt-get -y update
    apt-get -y install gcc
```

## Collection

 - Name: [j23414/singularity_event](https://github.com/j23414/singularity_event)
 - License: None

