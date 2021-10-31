---
id: 1503
name: "mvdoc/famface"
branch: "master"
tag: "latest"
commit: "3313138930b18f13bc80b7188a94b8a6cd0e6d0a"
version: "8b95f867920234ea9de113bd183975c1"
build_date: "2018-02-01T11:37:39.142Z"
size_mb: 1850
size: 646983711
sif: "https://datasets.datalad.org/shub/mvdoc/famface/latest/2018-02-01-33131389-8b95f867/8b95f867920234ea9de113bd183975c1.simg"
url: https://datasets.datalad.org/shub/mvdoc/famface/latest/2018-02-01-33131389-8b95f867/
recipe: https://datasets.datalad.org/shub/mvdoc/famface/latest/2018-02-01-33131389-8b95f867/Singularity
collection: mvdoc/famface
---

# mvdoc/famface:latest

```bash
$ singularity pull shub://mvdoc/famface:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
from: neurodebian:jessie

%post
    apt-get update
    apt-get install -y eatmydata wget
    wget -O- http://neuro.debian.net/lists/jessie.us-nh.full | tee /etc/apt/sources.list.d/neurodebian.sources.list
    apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
    apt-get update
    eatmydata apt-get install -y --no-install-recommends \
      python-mvpa2 fsl-core fsl-mni152-templates ants python-pip \
      python-datalad python-scipy python-numpy \
      python-sklearn python-dateutil convert3d
    eatmydata apt-get install -y python-nipype=0.11.0-1~nd80+1 
    mkdir /data /scripts /derivatives /ihome /idata

    # make entrypoint
    ENTRYPOINT="/startup.sh"
    if [ ! -f "$ENTRYPOINT" ]; then \
       echo '#!/usr/bin/env bash' >> $ENTRYPOINT \
       && echo 'set +x' >> $ENTRYPOINT \
       && echo 'source /etc/fsl/fsl.sh' >> $ENTRYPOINT \
       && echo 'if [ -z "$*" ]; then /usr/bin/env bash; else $*; fi' >> $ENTRYPOINT;
    fi
    chmod 777 $ENTRYPOINT

%runscript
    exec /startup.sh "$*"
```

## Collection

 - Name: [mvdoc/famface](https://github.com/mvdoc/famface)
 - License: [Other](None)

