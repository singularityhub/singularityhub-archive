---
id: 7223
name: "motroy/singularity-mgmapper"
branch: "master"
tag: "latest"
commit: "df5682c9b0ccd09ccd50ebc35bde15d5bc5c1fce"
version: "112d00c7fe3507fc96cfbd495ca0e78a"
build_date: "2019-02-14T13:36:58.067Z"
size_mb: 1107
size: 428900383
sif: "https://datasets.datalad.org/shub/motroy/singularity-mgmapper/latest/2019-02-14-df5682c9-112d00c7/112d00c7fe3507fc96cfbd495ca0e78a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-mgmapper/latest/2019-02-14-df5682c9-112d00c7/
recipe: https://datasets.datalad.org/shub/motroy/singularity-mgmapper/latest/2019-02-14-df5682c9-112d00c7/Singularity
collection: motroy/singularity-mgmapper
---

# motroy/singularity-mgmapper:latest

```bash
$ singularity pull shub://motroy/singularity-mgmapper:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%files

%environment
export MGmap_MAKEBLASTDB="/MGMapper/dependences/ncbi-blast-2.2.31+/bin/makeblastdb"
export MGmap_BLASTDBCMD="/MGMapper/dependences/ncbi-blast-2.2.31+/bin/blastdbcmd"
export MGmap_HOME="/MGMapper/mgmapper"
export MGmap_PYTHON="/usr/bin/python"
export MGmap_BWA="/MGMapper/dependences/bwa/bwa"
export MGmap_SAMTOOLS="/MGMapper/dependences/samtools-1.9/samtools"
export MGmap_BEDTOOLS="/MGMapper/dependences/bedtools-2.17.0/bin/bedtools"
export MGmap_PIGZ="/MGMapper/dependences/pigz/pigz"
export MGmap_CUTADAPT="/usr/local/bin/cutadapt"
export MGmap_MAIN_DB="/MGMapper/mgmapper/db"
export PATH="/MGMapper/mgmapper:$PATH"


%post

apt update && apt install -y git curl wget less locate unzip build-essential python-dev python-pip zlib1g-dev libbz2-dev liblzma-dev cpanminus perl

mkdir /MGMapper && cd /MGMapper
git clone --recursive  https://bitbucket.org/genomicepidemiology/mgmapper.git
sed -i -e 's/MGmap_HOME  \/services\/tools\/mgmapper\/2.5/MGmap_HOME  \/MGMapper\/mgmapper/g' mgmapper/MGmapper.init

mkdir dependences && cd dependences

mkdir kyotocabinet && cd kyotocabinet
wget https://fallabs.com/kyotocabinet/perlpkg/kyotocabinet-perl-1.20.tar.gz
tar xvf kyotocabinet-perl-1.20.tar.gz

cd /MGMapper/dependences

wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.31/ncbi-blast-2.2.31+-x64-linux.tar.gz
tar xvf ncbi-blast-2.2.31+-x64-linux.tar.gz

sed -i -e 's/\/services\/tools\/ncbi-blast\//\/MGMapper\/dependences\/ncbi-blast-/g' /MGMapper/mgmapper/MGmapper.init

wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
bunzip2 samtools-1.9.tar.bz2
tar xvf samtools-1.9.tar
cd samtools-1.9
./configure --without-curses --prefix=$PWD
make
cd ..

sed -i -e 's/SAMTOOLS \/services\/tools\/samtools\/1.6\/bin\//SAMTOOLS \/MGMapper\/dependences\/samtools-1.9\//g' /MGMapper/mgmapper/MGmapper.init

wget https://github.com/arq5x/bedtools/archive/v2.17.0.tar.gz
tar xvf v2.17.0.tar.gz
cd bedtools-2.17.0/; make
cd ..

sed -i -e 's/BEDTOOLS \/services\/tools\/anaconda-2.2.0\//BEDTOOLS \/MGMapper\/dependences\/bedtools-2.17.0\//g' /MGMapper/mgmapper/MGmapper.init

git clone --recursive https://github.com/madler/pigz.git
cd pigz; make
cd ..

sed -i -e 's/PIGZ \/services\/tools\/pigz-2.3.3\/bin/PIGZ \/MGMapper\/dependences\/pigz\//g' /MGMapper/mgmapper/MGmapper.init

git clone https://github.com/lh3/bwa.git
cd bwa; make
cd ..

sed -i -e 's/BWA \/services\/tools\/bwa\/0.7.12\/bin/BWA \/MGMapper\/dependences\/bwa/g' /MGMapper/mgmapper/MGmapper.init

rm -f ncbi-blast-2.2.31+-x64-linux.tar.gz samtools-1.9.tar v2.17.0.tar.gz

pip install --upgrade cutadapt

sed -i -e 's/PYTHON \/services\/tools\/anaconda-2.2.0\//PYTHON \/usr\//g' /MGMapper/mgmapper/MGmapper.init
sed -i -e 's/MAIN_DB \/home\/databases\/metagenomics/MAIN_DB \/MGMapper\/mgmapper\/db/g' /MGMapper/mgmapper/MGmapper.init

export PATH="/MGMapper/mgmapper:$PATH"

#INSTALL MGMapper DB
#/MGMapper/mgmapper/MGmapper_makedb.pl -d 0,1 -r unix
```

## Collection

 - Name: [motroy/singularity-mgmapper](https://github.com/motroy/singularity-mgmapper)
 - License: [MIT License](https://api.github.com/licenses/mit)

