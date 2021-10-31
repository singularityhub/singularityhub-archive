---
id: 5466
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "pilon"
commit: "c45bed96c50e230a37fe94bda3d991b41c41620f"
version: "9cf480ad69bf29ca7ec846efef652765"
build_date: "2020-04-28T08:53:47.548Z"
size_mb: 1212
size: 630157343
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/pilon/2020-04-28-c45bed96-9cf480ad/9cf480ad69bf29ca7ec846efef652765.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/pilon/2020-04-28-c45bed96-9cf480ad/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/pilon/2020-04-28-c45bed96-9cf480ad/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:pilon

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:pilon
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y git wget build-essential
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    # ================================
    # INSTALL pilon 
    # ================================
    VERSION="1.22"
    URL=https://github.com/broadinstitute/pilon/releases/download/v"$VERSION"/pilon-"$VERSION".jar
    cd /usr/local/bin
    wget -O pilon.jar "$URL"
    # install java
    apt-get install -y debconf-utils
    add-apt-repository -y ppa:webupd8team/java
    apt-get update
    echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
    apt-get install -y oracle-java8-installer

    echo '#!/usr/bin/env sh\njava -Xmx16G -jar /usr/local/bin/pilon.jar $@' > pilon
    chmod +x pilon
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

