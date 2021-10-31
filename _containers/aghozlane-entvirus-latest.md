---
id: 4551
name: "aghozlane/entvirus"
branch: "master"
tag: "latest"
commit: "a7f0decd462db5609d8f45f4efebe9f8c4cf0c98"
version: "c930dc5ca8263bea9a194172c5a238c0"
build_date: "2018-08-30T14:39:44.246Z"
size_mb: 1969
size: 738123807
sif: "https://datasets.datalad.org/shub/aghozlane/entvirus/latest/2018-08-30-a7f0decd-c930dc5c/c930dc5ca8263bea9a194172c5a238c0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aghozlane/entvirus/latest/2018-08-30-a7f0decd-c930dc5c/
recipe: https://datasets.datalad.org/shub/aghozlane/entvirus/latest/2018-08-30-a7f0decd-c930dc5c/Singularity
collection: aghozlane/entvirus
---

# aghozlane/entvirus:latest

```bash
$ singularity pull shub://aghozlane/entvirus:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04
%help
Entvirus workflow

%environment
    export LC_ALL=C

%files
    ./bin/*.py /usr/local/bin

%post
    apt -y update && apt -y install python-pip gcc g++ wget unzip gcj-jdk python3-pip git pigz
    # Bowtie2
    wget https://github.com/BenLangmead/bowtie2/releases/download/v2.3.4.1/bowtie2-2.3.4.1-linux-x86_64.zip
    unzip bowtie2-2.3.4.1-linux-x86_64.zip
    mv bowtie2-2.3.4.1-linux-x86_64/bowtie2* /usr/local/bin/
    rm -rf bowtie2-2.3.4.1-linux-x86_64.zip bowtie2-2.3.4.1-linux-x86_64
    # Alientrimmer
    wget ftp://ftp.pasteur.fr/pub/gensoft/projects/AlienTrimmer/AlienTrimmer_0.4.0.tar.gz
    tar -zxf AlienTrimmer_0.4.0.tar.gz
    cd AlienTrimmer_0.4.0/src && sed "s:-march=native::g" -i Makefile && make && mv AlienTrimmer /usr/local/bin/ && cd
    # Khmer
    pip2 install khmer
    # Megahit
    wget https://github.com/voutcn/megahit/releases/download/v1.1.3/megahit_v1.1.3_LINUX_CPUONLY_x86_64-bin.tar.gz
    tar -zxf megahit_v1.1.3_LINUX_CPUONLY_x86_64-bin.tar.gz
    mv megahit_v1.1.3_LINUX_CPUONLY_x86_64-bin/megahit* /usr/local/bin/
    rm -rf megahit_v1.1.3_LINUX_CPUONLY_x86_64-bin megahit_v1.1.3_LINUX_CPUONLY_x86_64-bin.tar.gz
    # Spades
    wget http://cab.spbu.ru/files/release3.12.0/SPAdes-3.12.0-Linux.tar.gz
    tar -zxf SPAdes-3.12.0-Linux.tar.gz
    mv SPAdes-3.12.0-Linux/bin/* /usr/local/bin/
    # pysam pandas
    pip install pysam pandas
    # taxadb
    pip3 install taxadb
    # blast
    wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.7.1/ncbi-blast-2.7.1+-x64-linux.tar.gz
    tar -zxf ncbi-blast-2.7.1+-x64-linux.tar.gz
    mv ncbi-blast-2.7.1+/bin/* /usr/local/bin/
    rm -rf ncbi-blast-2.7.1+-x64-linux.tar.gz ncbi-blast-2.7.1+/
    # BMGE
    wget ftp://ftp.pasteur.fr/pub/gensoft/projects/BMGE/BMGE-1.12.tar.gz
    tar -zxf BMGE-1.12.tar.gz
    mv BMGE-1.12/BMGE.jar /usr/local/bin/
    # gotree
    wget https://github.com/fredericlemoine/gotree/releases/download/v0.2.10/gotree_amd64_linux
    mv gotree_amd64_linux /usr/local/bin/gotree
    # iqtree
    wget https://github.com/Cibiv/IQ-TREE/releases/download/v1.6.6/iqtree-1.6.6-Linux.tar.gz
    tar -zxf iqtree-1.6.6-Linux.tar.gz
    mv iqtree-1.6.6-Linux/bin/* /usr/local/bin/
    # mafft
    wget https://mafft.cbrc.jp/alignment/software/mafft-7.402-linux.tgz
    tar -zxf mafft-7.402-linux.tgz
    mv mafft-linux64/mafftdir/bin/* /usr/local/bin/
    # MBMA
    #git clone https://gitlab.pasteur.fr/aghozlan/mbma_singularity.git
    #mv mbma_singularity/* /usr/local/bin/
    # clean
    rm -rf .cache/
    # execute python
    chmod +x /usr/local/bin/*.py
    # pasteur dir
    mkdir -p /pasteur /local
```

## Collection

 - Name: [aghozlane/entvirus](https://github.com/aghozlane/entvirus)
 - License: None

