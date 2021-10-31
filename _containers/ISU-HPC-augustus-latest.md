---
id: 5515
name: "ISU-HPC/augustus"
branch: "master"
tag: "latest"
commit: "8741a46b10e88883d2bec6aced3e4b0433002f25"
version: "d683fa481096f966ea654798b053dbd8"
build_date: "2021-03-22T04:33:19.679Z"
size_mb: 2861
size: 999796767
sif: "https://datasets.datalad.org/shub/ISU-HPC/augustus/latest/2021-03-22-8741a46b-d683fa48/d683fa481096f966ea654798b053dbd8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/augustus/latest/2021-03-22-8741a46b-d683fa48/
recipe: https://datasets.datalad.org/shub/ISU-HPC/augustus/latest/2021-03-22-8741a46b-d683fa48/Singularity
collection: ISU-HPC/augustus
---

# ISU-HPC/augustus:latest

```bash
$ singularity pull shub://ISU-HPC/augustus:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
FROM:ubuntu:18.04

%label
MAINTAINER ynanyam@iastate.edu

%post 

apt-get update
apt-get install build-essential wget git autoconf -y


# Install dependencies for AUGUSTUS
apt-get install -y libboost-iostreams-dev zlib1g-dev
apt-get install -y libgsl-dev libboost-graph-dev libsuitesparse-dev liblpsolve55-dev libsqlite3-dev libmysql++-dev
apt-get install -y libbamtools-dev
apt-get install -y libboost-all-dev

# Install additional dependencies for htslib and samtools
apt-get install -y libbz2-dev liblzma-dev
apt-get install -y libncurses5-dev

# Install additional dependencies for bam2wig
apt-get install -y libssl-dev libcurl3-dev

# Build bam2wig dependencies (htslib, bfctools, samtools)
git clone https://github.com/samtools/htslib.git /htslib
cd /htslib
autoheader
autoconf
./configure
make
make install
git clone https://github.com/samtools/bcftools.git /bcftools
cd /bcftools
autoheader
autoconf
./configure
make
make install
git clone https://github.com/samtools/samtools.git /samtools
cd /samtools
autoheader
autoconf -Wno-syntax
./configure
make
make install
export TOOLDIR="/"

#Clone Augustus
git clone https://github.com/Gaius-Augustus/Augustus.git  /augustus
cd /augustus
git checkout e789e51

# Build bam2wig
mkdir -p /augustus/bin
cd /augustus/auxprogs/bam2wig
make

# Build AUGUSTUS
cd /augustus
sed -i '/SQLITE/s/^#//' common.mk
make
make install

# Test AUGUSTUS
make test
```

## Collection

 - Name: [ISU-HPC/augustus](https://github.com/ISU-HPC/augustus)
 - License: None

