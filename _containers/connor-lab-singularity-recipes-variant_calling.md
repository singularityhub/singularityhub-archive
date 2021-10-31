---
id: 7005
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "variant_calling"
commit: "df99279f62163633d6d5fb465bb1a7321fbfe67b"
version: "0b8a4a49fee524b9d825dad112af073a"
build_date: "2019-02-07T19:57:01.368Z"
size_mb: 261
size: 119250975
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/variant_calling/2019-02-07-df99279f-0b8a4a49/0b8a4a49fee524b9d825dad112af073a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/variant_calling/2019-02-07-df99279f-0b8a4a49/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/variant_calling/2019-02-07-df99279f-0b8a4a49/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:variant_calling

```bash
$ singularity pull shub://connor-lab/singularity-recipes:variant_calling
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%post
    apk update
    apk upgrade
    apk add git make
    apk add bash curl gcc bzip2-dev libc-dev ncurses-dev openjdk8-jre-base xz-dev zlib-dev
    apk add python2
    
    curl -fsSL 'https://github.com/dkoboldt/varscan/releases/download/2.4.2/VarScan.v2.4.2.jar' -o /usr/local/bin/varscan.jar

    curl -fsSL 'https://github.com/samtools/samtools/archive/1.1.tar.gz' | tar -xz -C /tmp/
    curl -fsSL 'https://github.com/samtools/htslib/archive/1.1.tar.gz' | tar -xz -C /tmp && mv /tmp/htslib-1.1 /tmp/htslib
    cd /tmp/htslib && make
    cd /tmp/samtools-1.1 && make

    curl -fsSL 'https://github.com/CSB5/lofreq/blob/master/dist/lofreq_star-2.1.3.1.tar.gz?raw=true' | tar -xz -C /tmp
    cd /tmp/lofreq_star-2.1.3.1 && ./configure SAMTOOLS=/tmp/samtools-1.1 HTSLIB=/tmp/htslib && make install

    curl -fsSL 'https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2' | tar -xj -C /tmp/
    cd /tmp/samtools-1.9 && ./configure && make && make install

    curl -fsSL 'https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2' | tar -xj -C /tmp/
    cd /tmp/bcftools-1.9 && ./configure && make && make install

    curl -fsSL 'https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2' | tar -xj -C /tmp/
    cd /tmp/htslib-1.9 && ./configure && make && make install

    rm -rf /tmp/samtools* /tmp/lofreq* /tmp/htslib* /tmp/bcftools*

%labels
    Maintainer m-bull
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

