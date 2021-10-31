---
id: 5657
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "kraken2"
commit: "d76b3062b0eb29334c26e9e614e708c6cedf27d7"
version: "cc652db0ba5affecf17a9852599638b1"
build_date: "2019-01-09T15:39:53.462Z"
size_mb: 640
size: 232472607
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/kraken2/2019-01-09-d76b3062-cc652db0/cc652db0ba5affecf17a9852599638b1.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/kraken2/2019-01-09-d76b3062-cc652db0/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/kraken2/2019-01-09-d76b3062-cc652db0/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:kraken2

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:kraken2
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


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
    echo "export PATH=/usr/local:/usr/local/bin:$PATH" >> $SINGULARITY_ENVIRONMENT

    # ================================
    # INSTALL blast tools (dustmasker req. for kraken)
    # ================================
    apt install -y libidn11-dev
    VERSION="2.7.1"
    URL=ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/"$VERSION"/ncbi-blast-"$VERSION"+-x64-linux.tar.gz
    wget -O - "$URL" | tar xzf -
    cp ncbi*/bin/dustmasker /usr/local/bin/
    rm -rf ncbi-blast*
    cd ~

    # ================================
    # INSTALL kraken2
    # ================================
    apt install -y rsync
    VERSION="2.0.7-beta"
    URL=https://github.com/DerrickWood/kraken2/archive/v"$VERSION".tar.gz
    wget -O - "$URL" | tar xzf -
    cd kraken2*
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
    ./install_kraken2.sh $(pwd)
    cp kraken2 /usr/local/bin
    cp kraken2-build /usr/local/bin
    cp kraken2-inspect /usr/local/bin
    cd ~
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

