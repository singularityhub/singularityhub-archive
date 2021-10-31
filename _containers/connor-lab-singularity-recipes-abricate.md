---
id: 6949
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "abricate"
commit: "a43cefa7f62c25a6726a49f5634f285ba75ea6a9"
version: "7b9f93a4c9cd9b6a5e37e06aa4f883d3"
build_date: "2019-02-07T11:31:15.368Z"
size_mb: 2403
size: 564142111
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/abricate/2019-02-07-a43cefa7-7b9f93a4/7b9f93a4c9cd9b6a5e37e06aa4f883d3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/abricate/2019-02-07-a43cefa7-7b9f93a4/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/abricate/2019-02-07-a43cefa7-7b9f93a4/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:abricate

```bash
$ singularity pull shub://connor-lab/singularity-recipes:abricate
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest


%post
    yum -y update

    yum install -y git make
    yum install -y bzip2 bzip2-devel gcc ncurses-devel perl-App-cpanminus unzip xz-devel zlib-devel

    cpanm LWP::Simple Text::CSV Bio::Perl JSON File::Slurp List::MoreUtils

    curl -fsSL 'https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.7.1/ncbi-blast-2.7.1+-x64-linux.tar.gz' | tar -xz -C /usr/local/bin
    find /usr/local/bin/ncbi-blast*/bin -maxdepth 1 -executable -type f -exec ln -s {} /usr/local/bin \;

    curl -fsSL 'ftp://emboss.open-bio.org/pub/EMBOSS/EMBOSS-6.6.0.tar.gz' | tar -xz -C /usr/local/bin
    cd /usr/local/bin/EMBOSS-6.6.0 && ./configure --without-x && make install

    git clone https://github.com/tseemann/abricate.git /usr/local/bin/abricate-latest
    ln -s /usr/local/bin/abricate-latest/bin/* /usr/local/bin

    abricate --setupdb
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

