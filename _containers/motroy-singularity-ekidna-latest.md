---
id: 11810
name: "motroy/singularity-ekidna"
branch: "master"
tag: "latest"
commit: "b49ab5d83b455945431260a28918bb66ce5be537"
version: "6ba4d46473c6c3f3b1de1c612f61d355"
build_date: "2019-12-13T07:25:50.979Z"
size_mb: 5830.0
size: 2248794143
sif: "https://datasets.datalad.org/shub/motroy/singularity-ekidna/latest/2019-12-13-b49ab5d8-6ba4d464/6ba4d46473c6c3f3b1de1c612f61d355.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-ekidna/latest/2019-12-13-b49ab5d8-6ba4d464/
recipe: https://datasets.datalad.org/shub/motroy/singularity-ekidna/latest/2019-12-13-b49ab5d8-6ba4d464/Singularity
collection: motroy/singularity-ekidna
---

# motroy/singularity-ekidna:latest

```bash
$ singularity pull shub://motroy/singularity-ekidna:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/miniconda/miniconda3/:/miniconda/miniconda3/bin:/minimap2:/minimap2/misc:/ekidna/bin:$PATH"
export PERL5LIB="/miniconda/miniconda3/lib:$PERL5LIB"
export CONDARC=/.condarc
export LC_ALL=C

%post
#install miniconda3
export CONDARC=/.condarc
mkdir /miniconda && cd /miniconda
apt update && apt install -y git curl wget less locate build-essential openssh-server zlib1g-dev libboost-all-dev perl libmoo-perl liblist-moreutils-perl libjson-perl #python3 python3-numpy python3-scipy python3-pip
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda/miniconda3
/miniconda/miniconda3/bin/conda config --file /.condarc --add channels defaults && /miniconda/miniconda3/bin/conda config --file /.condarc --add channels conda-forge && /miniconda/miniconda3/bin/conda config --file /.condarc --add channels bioconda
/miniconda/miniconda3/bin/conda install -c bioconda shovill abricate mlst skesa iqtree samtools bcftools seqtk bedtools snp-sites any2fasta prokka snippy gubbins
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
abricate --setupdb
mlst --longlist
prokka --setupdb
```

## Collection

 - Name: [motroy/singularity-ekidna](https://github.com/motroy/singularity-ekidna)
 - License: [MIT License](https://api.github.com/licenses/mit)

