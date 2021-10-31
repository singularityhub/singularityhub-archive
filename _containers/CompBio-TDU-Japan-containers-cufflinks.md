---
id: 2356
name: "CompBio-TDU-Japan/containers"
branch: "master"
tag: "cufflinks"
commit: "58478a9f251d425fc6f576e300ac0cf22907274b"
version: "9d0449c1e0b921af0e013dc37f7719a1"
build_date: "2018-11-16T10:50:05.387Z"
size_mb: 232
size: 71061535
sif: "https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/cufflinks/2018-11-16-58478a9f-9d0449c1/9d0449c1e0b921af0e013dc37f7719a1.simg"
url: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/cufflinks/2018-11-16-58478a9f-9d0449c1/
recipe: https://datasets.datalad.org/shub/CompBio-TDU-Japan/containers/cufflinks/2018-11-16-58478a9f-9d0449c1/Singularity
collection: CompBio-TDU-Japan/containers
---

# CompBio-TDU-Japan/containers:cufflinks

```bash
$ singularity pull shub://CompBio-TDU-Japan/containers:cufflinks
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine

%post
    apk add --update --no-cache --virtual build-deps build-base ca-certificates wget
    apk --no-cache add bash python-dev python 
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-2.28-r0.apk
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.28-r0/glibc-bin-2.28-r0.apk
    apk add --nocache glibc-2.28-r0.apk
    apk add --nocache glibc-bin-2.28-r0.apk
    rm glibc*.apk
    wget http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz
    tar -zxvf cufflinks-2.2.1.Linux_x86_64.tar.gz
    mv cufflinks-2.2.1.Linux_x86_64/cuff* /usr/local/bin/
    mv cufflinks-2.2.1.Linux_x86_64/g* /usr/local/bin/
    rm cufflinks-2.2.1.Linux_x86_64.tar.gz
    rm -r cufflinks-2.2.1.Linux_x86_64
    rm "/etc/apk/keys/sgerrand.rsa.pub"
    rm -rf /usr/glibc-compat/bin
    apk del build-deps
```

## Collection

 - Name: [CompBio-TDU-Japan/containers](https://github.com/CompBio-TDU-Japan/containers)
 - License: None

