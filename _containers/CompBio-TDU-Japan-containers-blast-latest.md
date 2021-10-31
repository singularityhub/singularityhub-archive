---
id: 5816
name: "CompBio-TDU-Japan/containers"
branch: "master"
tag: "blast-latest"
commit: "1b7d007008caa2a8838890a045b3e8ce5726612b"
version: "23e995c85e7c219584b89f0896c33183"
build_date: "2019-09-30T15:16:38.653Z"
size_mb: 701
size: 245792799
sif: "https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/blast-latest/2019-09-30-1b7d0070-23e995c8/23e995c85e7c219584b89f0896c33183.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CompBio-TDU-Japan/containers/blast-latest/2019-09-30-1b7d0070-23e995c8/
recipe: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/blast-latest/2019-09-30-1b7d0070-23e995c8/Singularity
collection: CompBio-TDU-Japan/containers
---

# CompBio-TDU-Japan/containers:blast-latest

```bash
$ singularity pull shub://CompBio-TDU-Japan/containers:blast-latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: alpine

%post
    VERSION=2.7.1
    apk --update --no-cache add --virtual=.build-deps ca-certificates wget
    apk --no-cache add bash libbz2 libidn
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-bin-2.28-r0.apk
    apk add --nocache glibc-2.28-r0.apk
    apk add --nocache glibc-bin-2.28-r0.apk
    wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${VERSION}/ncbi-blast-${VERSION}+-x64-linux.tar.gz
    tar xfvz ncbi-blast-${VERSION}+-x64-linux.tar.gz
    mv ncbi-blast-${VERSION}+/bin/* /usr/local/bin/
    rm glibc*.apk
    rm "/root/.wget-hsts"
    rm ncbi-blast-${VERSION}+-x64-linux.tar.gz
    rm -r ncbi-blast-${VERSION}+
    rm "/etc/apk/keys/sgerrand.rsa.pub"
    apk del .build-deps
    rm -r /usr/glibc-compat/bin
    rm -r /usr/glibc-compat/sbin
```

## Collection

 - Name: [CompBio-TDU-Japan/containers](https://github.com/CompBio-TDU-Japan/containers)
 - License: None

