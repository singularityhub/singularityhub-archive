---
id: 10179
name: "bioinformatics-group/bioinformatics-singularity"
branch: "master"
tag: "latest"
commit: "85a63f16e0a24bf24086dd46229de794a23218ed"
version: "6c1206f74984a4c3212fa447087e6dd6"
build_date: "2019-07-24T16:07:27.370Z"
size_mb: 2416
size: 1007812639
sif: "https://datasets.datalad.org/shub/bioinformatics-group/bioinformatics-singularity/latest/2019-07-24-85a63f16-6c1206f7/6c1206f74984a4c3212fa447087e6dd6.simg"
url: https://datasets.datalad.org/shub/bioinformatics-group/bioinformatics-singularity/latest/2019-07-24-85a63f16-6c1206f7/
recipe: https://datasets.datalad.org/shub/bioinformatics-group/bioinformatics-singularity/latest/2019-07-24-85a63f16-6c1206f7/Singularity
collection: bioinformatics-group/bioinformatics-singularity
---

# bioinformatics-group/bioinformatics-singularity:latest

```bash
$ singularity pull shub://bioinformatics-group/bioinformatics-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: stretch
MirrorURL: http://ftp.ca.debian.org/debian/

%files
    setup.R

%post
    export DEBIAN_FRONTEND=noninteractive
    apt-get update
    apt-get install -y curl gnupg2
    apt-get install -y ca-certificates lsb-release apt-transport-https dirmngr
    curl --silent -o apt.gpg https://packages.sury.org/php/apt.gpg
    echo "deb http://cran.rstudio.com/bin/linux/debian stretch-cran35/" >> /etc/apt/sources.list
    apt-key add /apt.gpg
    apt-key adv --keyserver keys.gnupg.net --recv-key 'E19F5F87128899B192B1A2C2AD5F960A256A04AF'
    apt-get -qqq update
    apt-get -qqq upgrade
    ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
    dpkg-reconfigure --frontend noninteractive tzdata
    apt-get -y install gfortran g++ perl alien git r-base libcurl4-openssl-dev libxml2-dev
    Rscript setup.R
    curl -s ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.3.0/ncbi-blast-2.3.0+-1.x86_64.rpm --output ncbi-blast-2.3.0+-1.x86_64.rpm
    alien -i ncbi-blast-2.3.0+-1.x86_64.rpm
    git clone https://github.com/cbcrg/tcoffee.git tcoffee
    cd tcoffee/compile
    make t_coffee
    cp t_coffee /usr/bin/
    cd ../..
    rm -r tcoffee
    apt-get update && apt-get install -y && \
           apt-get install -y locales locales-all && \
            export LANGUAGE=en_US.UTF-8 && \
            export LANG=en_US.UTF-8 && \
            export LC_ALL=en_US.UTF-8 && \
            locale-gen en_US.UTF-8 && \
            dpkg-reconfigure locales
    rm ncbi-blast-2.3.0+-1.x86_64.rpm
    rm -r /var/lib/apt/lists/*
```

## Collection

 - Name: [bioinformatics-group/bioinformatics-singularity](https://github.com/bioinformatics-group/bioinformatics-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

