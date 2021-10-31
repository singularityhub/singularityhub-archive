---
id: 6986
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "minimap2"
commit: "277703bb17d3d079beb249830ce2f3ff58c2a1eb"
version: "283c967f6f1a9abeb4bf4d0ed79857eb"
build_date: "2019-02-07T15:45:22.828Z"
size_mb: 271
size: 115015711
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/minimap2/2019-02-07-277703bb-283c967f/283c967f6f1a9abeb4bf4d0ed79857eb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/minimap2/2019-02-07-277703bb-283c967f/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/minimap2/2019-02-07-277703bb-283c967f/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:minimap2

```bash
$ singularity pull shub://connor-lab/singularity-recipes:minimap2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%post
    apk update
    apk upgrade
    apk add git make
    apk add bash gcc bzip2-dev libc-dev ncurses-dev openjdk8-jre-base xz-dev zlib-dev
    
    git clone https://github.com/lh3/minimap2 /tmp/minimap2
    cd /tmp/minimap2
    make
    mv /tmp/minimap2/minimap2 /usr/local/bin/
    rm -rf /tmp/minimap2

    wget https://github.com/samtools/samtools/releases/download/1.8/samtools-1.8.tar.bz2 -O /tmp/samtools.tar.bz2
    cd /tmp
    tar xvjf samtools.tar.bz2
    cd samtools-1.8 && ./configure && make && make install

    wget https://github.com/broadinstitute/picard/releases/download/2.18.14/picard.jar -O /usr/local/bin/picard.jar

    wget https://raw.githubusercontent.com/connor-lab/singularity-recipes/master/scripts/picard -O /usr/local/bin/picard
    chmod 775 /usr/local/bin/picard

%labels
    Maintainer m-bull
    Version minimap2-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

