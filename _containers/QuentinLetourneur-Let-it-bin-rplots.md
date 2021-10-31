---
id: 4643
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "rplots"
commit: "4cc6a9b6e06fa4cbb5de17ff93e84391ced89c95"
version: "944c4f2094d8a9f818369b24693eb2a0"
build_date: "2019-12-06T16:44:17.156Z"
size_mb: 675
size: 276512799
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/rplots/2019-12-06-4cc6a9b6-944c4f20/944c4f2094d8a9f818369b24693eb2a0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/QuentinLetourneur/Let-it-bin/rplots/2019-12-06-4cc6a9b6-944c4f20/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/rplots/2019-12-06-4cc6a9b6-944c4f20/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:rplots

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:rplots
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%setup
    export LC_ALL=C

%files
	bin/binning_stats.R
	bin/nb_bin_per_threshold.R
	bin/binning_heatmap.R

%post
    mkdir /pasteur
	apt -y update
    apt -y install wget build-essential
    
	cd /home
    wget https://cran.r-project.org/bin/linux/ubuntu/xenial/r-base-core_3.4.1-2xenial0_amd64.deb
    apt -y install ./r-base-core_3.4.1-2xenial0_amd64.deb
    rm r-base-core_3.4.1-2xenial0_amd64.deb
    
    R --vanilla -e'install.packages("cowplot", repo="http://cran.univ-paris1.fr/")'
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

