---
id: 6987
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "mlst"
commit: "277703bb17d3d079beb249830ce2f3ff58c2a1eb"
version: "4e2c4581b09a0521fa22c568fd08ac18"
build_date: "2019-02-07T15:45:22.821Z"
size_mb: 1326
size: 466685983
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/mlst/2019-02-07-277703bb-4e2c4581/4e2c4581b09a0521fa22c568fd08ac18.simg"
url: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/mlst/2019-02-07-277703bb-4e2c4581/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/mlst/2019-02-07-277703bb-4e2c4581/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:mlst

```bash
$ singularity pull shub://connor-lab/singularity-recipes:mlst
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest


%post
    yum -y update

    yum install -y git make
    yum install -y bzip2 bzip2-devel gcc ncurses-devel perl-App-cpanminus unzip xz-devel zlib-devel

    cpanm Moo List::MoreUtils JSON Time::Piece

    curl -fsSL 'https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.7.1/ncbi-blast-2.7.1+-x64-linux.tar.gz' | tar -xz -C /usr/local/bin
    find /usr/local/bin/ncbi-blast*/bin -maxdepth 1 -executable -type f -exec ln -s {} /usr/local/bin \;

    git clone https://github.com/tseemann/mlst.git /usr/local/bin/mlst-latest
    ln -s /usr/local/bin/mlst-latest/bin/* /usr/local/bin

%labels
    Maintainer m-bull
    Version mlst-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

