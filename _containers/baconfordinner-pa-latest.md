---
id: 5156
name: "baconfordinner/pa"
branch: "master"
tag: "latest"
commit: "68a24aeac1ff08cdb49a0f123a2ff7ec341e9bdc"
version: "cb12d4bb3d9d7ad6191a97937fcd9b01"
build_date: "2018-10-07T18:30:41.801Z"
size_mb: 3013
size: 1528987679
sif: "https://datasets.datalad.org/shub/baconfordinner/pa/latest/2018-10-07-68a24aea-cb12d4bb/cb12d4bb3d9d7ad6191a97937fcd9b01.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/baconfordinner/pa/latest/2018-10-07-68a24aea-cb12d4bb/
recipe: https://datasets.datalad.org/shub/baconfordinner/pa/latest/2018-10-07-68a24aea-cb12d4bb/Singularity
collection: baconfordinner/pa
---

# baconfordinner/pa:latest

```bash
$ singularity pull shub://baconfordinner/pa:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:9.0-cudnn7-runtime
%labels
MAINTAINER Nicolas Hoferer

%post
apt-get update
apt-get update && apt-get install -y curl python3-numpy python3-pip enchant cmake vim ca-certificates
apt-get update && apt-get install -y libjpeg-dev libpng-dev git python3-dev
apt-get update && apt-get install -y python3-psycopg2 build-essential chrpath libssl-dev libxft-dev && apt-get clean && rm -rf /var/lib/apt/lists/*
apt-get update
pip3 install tensorflow-gpu==1.6.0
pip3 install numpy pandas sklearn scipy keras

export TERM=xterm-256color

pip3 install pyparsing rdflib
pip3 install SPARQLWrapper
pip3 install requests pyspotlight
pip3 install nltk
pip3 install --upgrade pip



%runscript
echo "Hello there"
sh ./BA_FS18/src/pipeline_train.sh baseline baseline/dev.tok > sqa2018_baseline.log
exec /bin/bash "$@"
```

## Collection

 - Name: [baconfordinner/pa](https://github.com/baconfordinner/pa)
 - License: None

