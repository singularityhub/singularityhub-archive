---
id: 6988
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "multiqc"
commit: "277703bb17d3d079beb249830ce2f3ff58c2a1eb"
version: "272827484a8e73aa8c501c76d704763a"
build_date: "2019-02-07T15:45:22.813Z"
size_mb: 516
size: 182480927
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/multiqc/2019-02-07-277703bb-27282748/272827484a8e73aa8c501c76d704763a.simg"
url: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/multiqc/2019-02-07-277703bb-27282748/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/multiqc/2019-02-07-277703bb-27282748/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:multiqc

```bash
$ singularity pull shub://connor-lab/singularity-recipes:multiqc
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8


%post
    apk update
    apk upgrade
    apk add bash bzip2-dev g++ gcc git libc-dev make ncurses-dev xz-dev zlib-dev
    apk add curl freetype-dev libpng-dev python2 python2-dev py2-pip
    
    cd /usr/local/bin
    curl -fsSL "https://github.com/jgm/pandoc/releases/download/2.3/pandoc-2.3-linux.tar.gz" | tar xz
    find /usr/local/bin/pandoc-2.3 -name "pandoc" -exec ln -s {} /usr/local/bin \;

    pip install git+https://github.com/ewels/MultiQC.git

%labels
    Maintainer m-bull
    Version multiqc-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

