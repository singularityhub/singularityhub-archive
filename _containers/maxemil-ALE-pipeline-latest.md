---
id: 1477
name: "maxemil/ALE-pipeline"
branch: "master"
tag: "latest"
commit: "d33481b2b7b453caaaa03b3d16afffe16f77a4c5"
version: "bb6fbe7100bafa91e4a8e49e88094e0f"
build_date: "2020-08-13T13:48:02.942Z"
size_mb: 1062
size: 366252063
sif: "https://datasets.datalad.org/shub/maxemil/ALE-pipeline/latest/2020-08-13-d33481b2-bb6fbe71/bb6fbe7100bafa91e4a8e49e88094e0f.simg"
url: https://datasets.datalad.org/shub/maxemil/ALE-pipeline/latest/2020-08-13-d33481b2-bb6fbe71/
recipe: https://datasets.datalad.org/shub/maxemil/ALE-pipeline/latest/2020-08-13-d33481b2-bb6fbe71/Singularity
collection: maxemil/ALE-pipeline
---

# maxemil/ALE-pipeline:latest

```bash
$ singularity pull shub://maxemil/ALE-pipeline:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:jessie

%post
#### install system dependencies
apt-get update
apt-get clean
apt-get install --no-install-recommends -qy \
                  cmake \
                  g++-4.9 \
                  git \
                  libboost-all-dev \
                  make \
                  python3 \
                  wget

#### install bpp
cd /opt/

echo "deb http://biopp.univ-montp2.fr/repos/apt/ Trusty main" >> /etc/apt/sources.list;
wget http://biopp.univ-montp2.fr/repos/apt/conf/biopp.gpg.key
apt-key add biopp.gpg.key
apt-get update
apt-get install -qy libbpp-phyl-dev

#### compile and install ALE
git clone git://github.com/ssolo/ALE /usr/local/ALE
mkdir /usr/local/ALE/build

cd /usr/local/ALE/build

echo "export LD_LIBRARY_PATH=/usr/local/lib/" >> $SINGULARITY_ENVIRONMENT

cmake ..  -DCMAKE_CXX_COMPILER=/usr/bin/g++-4.9 && make -j 4

for binary in /usr/local/ALE/build/bin/*; do ln -s $binary /usr/local/bin/; done

%labels
Maintainer	max-emil.schon@icm.uu.se
```

## Collection

 - Name: [maxemil/ALE-pipeline](https://github.com/maxemil/ALE-pipeline)
 - License: None

