---
id: 7019
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "irap"
commit: "559652b0889a1804e75cc6a487a0e65ebdff2e43"
version: "588e4ceef45caf69ffea4c7a4c693679"
build_date: "2019-02-16T08:06:46.468Z"
size_mb: 6046
size: 2177433631
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/irap/2019-02-16-559652b0-588e4cee/588e4ceef45caf69ffea4c7a4c693679.simg"
url: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/irap/2019-02-16-559652b0-588e4cee/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/irap/2019-02-16-559652b0-588e4cee/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:irap

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:irap
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:nunofonseca/irap_fedora:v1.0.6b

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post  
yum -y install tbb
mkdir /apps
mkdir /scratch
chmod ugo+x /usr/bin/irap
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

