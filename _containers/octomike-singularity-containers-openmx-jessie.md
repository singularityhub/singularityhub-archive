---
id: 1478
name: "octomike/singularity-containers"
branch: "master"
tag: "openmx-jessie"
commit: "6999e6b5485bf94419436f73ba12d7d8e20043e5"
version: "2f3196f7d3a44783e523019e21d5aadf"
build_date: "2018-01-26T02:08:37.344Z"
size_mb: 1066
size: 351629343
sif: "https://datasets.datalad.org/shub/octomike/singularity-containers/openmx-jessie/2018-01-26-6999e6b5-2f3196f7/2f3196f7d3a44783e523019e21d5aadf.simg"
url: https://datasets.datalad.org/shub/octomike/singularity-containers/openmx-jessie/2018-01-26-6999e6b5-2f3196f7/
recipe: https://datasets.datalad.org/shub/octomike/singularity-containers/openmx-jessie/2018-01-26-6999e6b5-2f3196f7/Singularity
collection: octomike/singularity-containers
---

# octomike/singularity-containers:openmx-jessie

```bash
$ singularity pull shub://octomike/singularity-containers:openmx-jessie
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:jessie

%labels
   AUTHOR krause@mpib-berlin.mpg.de

%post
echo "deb http://ftp5.gwdg.de/pub/misc/cran/bin/linux/debian jessie-cran3/" > /etc/apt/sources.list.d/cran.list
apt-key adv --keyserver keys.gnupg.net --recv-key '6212B7B7931C4BB16280BA1306F90DE5381BA480'
apt-get update
apt-get -y install libopenblas-base libxml2-dev wget locales
apt-get install -y r-recommended -t jessie-cran3
cat <<EOF > /etc/locale.gen
de_DE ISO-8859-1
de_DE.UTF-8 UTF-8
de_DE@euro ISO-8859-15
en_US ISO-8859-1
en_US.ISO-8859-15 ISO-8859-15
en_US.UTF-8 UTF-8
EOF
locale-gen -a
cat <<EOF > /tmp/install.R
chooseCRANmirror(ind=30)
source('http://openmx.psyc.virginia.edu/getOpenMx.R')
EOF
Rscript /tmp/install.R
```

## Collection

 - Name: [octomike/singularity-containers](https://github.com/octomike/singularity-containers)
 - License: None

