---
id: 5481
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "spades"
commit: "31bfb0f5d5af5a41bbd883bba963a15031f63c55"
version: "9a6111fe0232ac6bf01260212d4357e9"
build_date: "2019-08-15T05:25:58.602Z"
size_mb: 649
size: 238313503
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/spades/2019-08-15-31bfb0f5-9a6111fe/9a6111fe0232ac6bf01260212d4357e9.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/spades/2019-08-15-31bfb0f5-9a6111fe/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/spades/2019-08-15-31bfb0f5-9a6111fe/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:spades

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:spades
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

    # ========================
    # INSTALL spades
    # ========================
    VERSION="3.13.0"
	URL=https://github.com/ablab/spades/releases/download/v"$VERSION"/SPAdes-"$VERSION"-Linux.tar.gz
	ln -s /usr/bin/python3.6 /usr/bin/python
	apt install -y python3-distutils
	wget -O - "$URL" | tar xzf -
	cd SPAdes*/bin
	echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

