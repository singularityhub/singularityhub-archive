---
id: 6983
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "kronatools"
commit: "5e322d4c80acb21db9d53649a55a0349c4378009"
version: "6cd73a18fb95e13da9f96a044cf50707"
build_date: "2019-02-07T15:45:22.849Z"
size_mb: 178
size: 49713183
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/kronatools/2019-02-07-5e322d4c-6cd73a18/6cd73a18fb95e13da9f96a044cf50707.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/kronatools/2019-02-07-5e322d4c-6cd73a18/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/kronatools/2019-02-07-5e322d4c-6cd73a18/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:kronatools

```bash
$ singularity pull shub://connor-lab/singularity-recipes:kronatools
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%post
    apk update
    apk upgrade
    apk add bash curl git make perl

    cd /usr/local/bin
    git clone https://github.com/marbl/Krona
    mkdir -p /usr/local/bin/Krona/KronaTools/taxonomy
    cd /usr/local/bin/Krona/KronaTools && ./install.pl 
    cd /usr/local/bin/Krona/KronaTools && ./updateTaxonomy.sh

%labels
    Maintainer m-bull
    Version KronaTools-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

