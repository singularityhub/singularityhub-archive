---
id: 1302
name: "khanlab/bids-validator"
branch: "master"
tag: "0.25.0"
commit: "bd49d17a89e7153444f5dfe0957a45858da2f72f"
version: "640c69f72f4ca294463aa44aa77c41bf"
build_date: "2018-01-15T15:00:26.184Z"
size_mb: 376
size: 130568223
sif: "https://datasets.datalad.org/shub/khanlab/bids-validator/0.25.0/2018-01-15-bd49d17a-640c69f7/640c69f72f4ca294463aa44aa77c41bf.simg"
url: https://datasets.datalad.org/shub/khanlab/bids-validator/0.25.0/2018-01-15-bd49d17a-640c69f7/
recipe: https://datasets.datalad.org/shub/khanlab/bids-validator/0.25.0/2018-01-15-bd49d17a-640c69f7/Singularity
collection: khanlab/bids-validator
---

# khanlab/bids-validator:0.25.0

```bash
$ singularity pull shub://khanlab/bids-validator:0.25.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:trusty

%setup
mkdir -p $SINGULARITY_ROOTFS/src
cp -Rv . $SINGULARITY_ROOTFS/src

%post 

## Install the validator
apt-get update && \
apt-get install -y curl git&& \
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
apt-get remove -y curl && \
apt-get install -y nodejs && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

cd /src
TAG=${SINGULARITY_BUILDDEF#Singularity.}
git checkout $TAG
sed -i -E "s/0.0.0/$TAG/" package.json
npm install -g /src

%runscript
exec /usr/bin/bids-validator $@
```

## Collection

 - Name: [khanlab/bids-validator](https://github.com/khanlab/bids-validator)
 - License: None

