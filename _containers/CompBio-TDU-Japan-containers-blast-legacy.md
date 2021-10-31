---
id: 4867
name: "CompBio-TDU-Japan/containers"
branch: "master"
tag: "blast-legacy"
commit: "ab664c077b9ff86bdc2dfcd1d96e004011194fce"
version: "8fdca7aa1d4ac6c2017c5e1b22092aa7"
build_date: "2018-11-16T10:50:05.360Z"
size_mb: 629
size: 217899039
sif: "https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/blast-legacy/2018-11-16-ab664c07-8fdca7aa/8fdca7aa1d4ac6c2017c5e1b22092aa7.simg"
url: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/blast-legacy/2018-11-16-ab664c07-8fdca7aa/
recipe: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/blast-legacy/2018-11-16-ab664c07-8fdca7aa/Singularity
collection: CompBio-TDU-Japan/containers
---

# CompBio-TDU-Japan/containers:blast-legacy

```bash
$ singularity pull shub://CompBio-TDU-Japan/containers:blast-legacy
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: alpine

%post
    apk --update --no-cache add --virtual=.build-deps ca-certificates wget
    apk --no-cache add bash libbz2
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-bin-2.28-r0.apk
    apk add --nocache glibc-2.28-r0.apk
    apk add --nocache glibc-bin-2.28-r0.apk
    wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.4.0/ncbi-blast-2.4.0+-x64-linux.tar.gz
    tar xfvz ncbi-blast-2.4.0+-x64-linux.tar.gz
    mv ncbi-blast-2.4.0+/bin/* /usr/local/bin/
    rm glibc*.apk
    rm "/root/.wget-hsts"
    rm ncbi-blast-2.4.0+-x64-linux.tar.gz
    rm -r ncbi-blast-2.4.0+
    rm "/etc/apk/keys/sgerrand.rsa.pub"
    apk del .build-deps
    rm -r /usr/glibc-compat/bin
    rm -r /usr/glibc-compat/sbin
```

## Collection

 - Name: [CompBio-TDU-Japan/containers](https://github.com/CompBio-TDU-Japan/containers)
 - License: None

