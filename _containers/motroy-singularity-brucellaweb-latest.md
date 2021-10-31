---
id: 10583
name: "motroy/singularity-brucellaweb"
branch: "master"
tag: "latest"
commit: "9ea784b8e0126501eaeade87533d275ae3ca2452"
version: "cc79efd68de521621efc088a34f502e4"
build_date: "2020-08-11T11:37:05.767Z"
size_mb: 6131.0
size: 2364715039
sif: "https://datasets.datalad.org/shub/motroy/singularity-brucellaweb/latest/2020-08-11-9ea784b8-cc79efd6/cc79efd68de521621efc088a34f502e4.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-brucellaweb/latest/2020-08-11-9ea784b8-cc79efd6/
recipe: https://datasets.datalad.org/shub/motroy/singularity-brucellaweb/latest/2020-08-11-9ea784b8-cc79efd6/Singularity
collection: motroy/singularity-brucellaweb
---

# motroy/singularity-brucellaweb:latest

```bash
$ singularity pull shub://motroy/singularity-brucellaweb:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
export PATH="/miniconda/miniconda3/:/miniconda/miniconda3/bin:/minimap2:/minimap2/misc:/ekidna/bin:/quast/quast-5.0.2:$PATH"
export PERL5LIB="/miniconda/miniconda3/lib:$PERL5LIB"
export CONDARC=/.condarc
export LC_ALL=C

%post
#install miniconda3
export CONDARC=/.condarc
mkdir /miniconda && cd /miniconda
apt update && apt install -y git curl wget less locate build-essential openssh-server zlib1g-dev libboost-all-dev perl libmoo-perl liblist-moreutils-perl libjson-perl fastqc pkg-config libfreetype6-dev libpng-dev python-matplotlib #python3 python3-numpy python3-scipy python3-pip
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda/miniconda3
/miniconda/miniconda3/bin/conda config --file /.condarc --add channels defaults && /miniconda/miniconda3/bin/conda config --file /.condarc --add channels conda-forge && /miniconda/miniconda3/bin/conda config --file /.condarc --add channels bioconda
/miniconda/miniconda3/bin/conda install -c bioconda shovill abricate mlst skesa iqtree samtools bcftools seqtk bedtools snp-sites any2fasta multiqc
/miniconda/miniconda3/bin/conda install -c conda-forge -c bioconda -c defaults prokka
export PATH="/miniconda/miniconda3/:/miniconda/miniconda3/bin:$PATH"
export PERL5LIB="/miniconda/miniconda3/lib:$PERL5LIB"
# install minimap2
cd /
git clone https://github.com/lh3/minimap2
cd minimap2 && make
cp /minimap2/misc/paftools.js /minimap2/misc/paftools
# install the k8 javascript shell
curl -L https://github.com/attractivechaos/k8/releases/download/v0.2.4/k8-0.2.4.tar.bz2 | tar -jxf -
cp k8-0.2.4/k8-`uname -s` k8              # or copy it to a directory on your $PATH
export PATH="$PATH:`pwd`:`pwd`/misc"    # run this if k8, minimap2 or paftools.js not on your $PATH
cd /
git clone https://github.com/tseemann/ekidna.git
#sed -i -e 's|#!/usr/bin/env perl|#!/miniconda/miniconda3/bin/perl|g' /ekidna/bin/ekidna
export PATH="/ekidna/bin:$PATH"
mkdir /quast && cd /quast
wget https://downloads.sourceforge.net/project/quast/quast-5.0.2.tar.gz
tar -xzf quast-5.0.2.tar.gz && rm -f quast-5.0.2.tar.gz
cd quast-5.0.2
./setup.py install
export PATH="/quast/quast-5.0.2:$PATH"
abricate --setupdb
mlst --longlist
prokka --setupdb
```

## Collection

 - Name: [motroy/singularity-brucellaweb](https://github.com/motroy/singularity-brucellaweb)
 - License: [MIT License](https://api.github.com/licenses/mit)

