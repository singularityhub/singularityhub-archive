---
id: 10003
name: "kapsakcj/singularities"
branch: "master"
tag: "seqsero2.1.0.0"
commit: "889f9475d9b51af2aa302322d768a2b493691df2"
version: "e52cc8263724e464e6a1bcb1e145a20c"
build_date: "2019-08-29T18:40:02.301Z"
size_mb: 824
size: 314548255
sif: "https://datasets.datalad.org/shub/kapsakcj/singularities/seqsero2.1.0.0/2019-08-29-889f9475-e52cc826/e52cc8263724e464e6a1bcb1e145a20c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kapsakcj/singularities/seqsero2.1.0.0/2019-08-29-889f9475-e52cc826/
recipe: https://datasets.datalad.org/shub/kapsakcj/singularities/seqsero2.1.0.0/2019-08-29-889f9475-e52cc826/Singularity
collection: kapsakcj/singularities
---

# kapsakcj/singularities:seqsero2.1.0.0

```bash
$ singularity pull shub://kapsakcj/singularities:seqsero2.1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

%labels
  base.image="ubuntu:xenial"
  version="1"
  software="SeqSero2"
  software.version="1.0.0"
  description="Salmonella serotyping from genome sequencing data"
  website="https://github.com/denglab/SeqSero2"
  license="https://github.com/denglab/SeqSero2/blob/master/LICENSE"
  maintainer="Jake Garfin <jake.garfin@state.mn.us>"
  maintainer2="Curtis Kapsak <pjx8@cdc.gov>"
%post
apt-get update && apt-get install -y \
  python3\
  python3-pip\
  bwa\
  ncbi-blast+\
  sra-toolkit\
  bedtools\
  wget\
  zlib1g-dev\
  libbz2-dev\
  liblzma-dev\
  build-essential\
  libncurses5-dev

pip3 install biopython

# Install samtools (installing from apt breaks SeqSero2 version check)
wget 'https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2'
tar -xvf samtools-1.9.tar.bz2
rm samtools-1.9.tar.bz2
cd samtools-1.9
make

# Install salmID
cd /
wget https://github.com/hcdenbakker/SalmID/archive/0.122.tar.gz
tar -xzf 0.122.tar.gz
rm -rf 0.122.tar.gz

# Install SPAdes
cd /
wget https://github.com/ablab/spades/releases/download/v3.8.2/SPAdes-3.8.2-Linux.tar.gz
tar -xzf SPAdes-3.8.2-Linux.tar.gz
rm -rf SPAdes-3.8.2-Linux.tar.gz

# Install SeqSero2
cd /
wget https://github.com/denglab/SeqSero2/archive/v1.0.0.tar.gz
tar -xzf v1.0.0.tar.gz
rm -rf v1.0.0.tar.gz
mkdir /data

%environment
export PATH="${PATH}:/SeqSero2-1.0.0:/SPAdes-3.8.2-Linux/bin:/SalmID-0.122:/samtools-1.9"

%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [kapsakcj/singularities](https://github.com/kapsakcj/singularities)
 - License: [MIT License](https://api.github.com/licenses/mit)

