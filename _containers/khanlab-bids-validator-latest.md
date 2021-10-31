---
id: 1192
name: "khanlab/bids-validator"
branch: "master"
tag: "latest"
commit: "44d3f1780d35492e9a378dd3001dfffa5119bbbf"
version: "8ab66a12ee15ffc161bcd25a76002e69"
build_date: "2018-01-03T20:54:05.630Z"
size_mb: 348
size: 119361567
sif: "https://datasets.datalad.org/shub/khanlab/bids-validator/latest/2018-01-03-44d3f178-8ab66a12/8ab66a12ee15ffc161bcd25a76002e69.simg"
url: https://datasets.datalad.org/shub/khanlab/bids-validator/latest/2018-01-03-44d3f178-8ab66a12/
recipe: https://datasets.datalad.org/shub/khanlab/bids-validator/latest/2018-01-03-44d3f178-8ab66a12/Singularity
collection: khanlab/bids-validator
---

# khanlab/bids-validator:latest

```bash
$ singularity pull shub://khanlab/bids-validator:latest
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
apt-get install -y curl && \
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
apt-get remove -y curl && \
apt-get install -y nodejs && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

npm install -g /src

%runscript
exec /usr/bin/bids-validator $@
```

## Collection

 - Name: [khanlab/bids-validator](https://github.com/khanlab/bids-validator)
 - License: None

