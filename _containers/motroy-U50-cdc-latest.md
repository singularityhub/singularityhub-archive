---
id: 11925
name: "motroy/U50-cdc"
branch: "master"
tag: "latest"
commit: "e506ba8990edabc6fcb25b229abde269d8a24d9b"
version: "132a0d2343dc6d263cb2e7c2317f378d"
build_date: "2020-01-01T15:41:00.041Z"
size_mb: 5435.0
size: 2544738335
sif: "https://datasets.datalad.org/shub/motroy/U50-cdc/latest/2020-01-01-e506ba89-132a0d23/132a0d2343dc6d263cb2e7c2317f378d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/U50-cdc/latest/2020-01-01-e506ba89-132a0d23/
recipe: https://datasets.datalad.org/shub/motroy/U50-cdc/latest/2020-01-01-e506ba89-132a0d23/Singularity
collection: motroy/U50-cdc
---

# motroy/U50-cdc:latest

```bash
$ singularity pull shub://motroy/U50-cdc:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/miniconda/miniconda3/:/miniconda/miniconda3/bin:/U50_tool/U50/:$PATH"
export PERL5LIB="/miniconda/miniconda3/lib:$PERL5LIB"
export CONDARC=/.condarc
export LC_ALL=C

%post
#install miniconda3
export CONDARC=/.condarc
mkdir /miniconda && cd /miniconda
apt update && apt install -y git curl wget less locate openssh-server locales #build-essential zlib1g-dev libboost-all-dev
locale-gen en_US.UTF-8
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda/miniconda3
/miniconda/miniconda3/bin/conda config --file /.condarc --add channels defaults && /miniconda/miniconda3/bin/conda config --file /.condarc --add channels conda-forge && /miniconda/miniconda3/bin/conda config --file /.condarc --add channels bioconda
/miniconda/miniconda3/bin/conda install -c bioconda mummer=3.23 bwa=0.7.17 samtools=1.8 bedtools=2.29.2 quast=5.0.2 python=3.6 #bowtie2=2.3.5
/miniconda/miniconda3/bin/conda install -c conda-forge biopython=1.76
export PATH="/miniconda/miniconda3/:/miniconda/miniconda3/bin:$PATH"
export PERL5LIB="/miniconda/miniconda3/lib:$PERL5LIB"

mkdir /U50_tool && cd /U50_tool
git clone https://github.com/CDCgov/U50.git
export PATH="/U50_tool/U50/:$PATH"
export LC_ALL=C
```

## Collection

 - Name: [motroy/U50-cdc](https://github.com/motroy/U50-cdc)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

