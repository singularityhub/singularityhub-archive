---
id: 15178
name: "BrendelGroup/AllRice"
branch: "main"
tag: "latest"
commit: "a3bf4850c6277917bec452e2d896f8b48971fc2e"
version: "96b4640a198fda23d47ab4530a531a7ef1ab14615faeecc642932918e8a6363d"
build_date: "2020-12-25T12:56:44.487Z"
size_mb: 2920.37890625
size: 3062239232
sif: "https://datasets.datalad.org/shub/BrendelGroup/AllRice/latest/2020-12-25-a3bf4850-96b4640a/96b4640a198fda23d47ab4530a531a7ef1ab14615faeecc642932918e8a6363d.sif"
url: https://datasets.datalad.org/shub/BrendelGroup/AllRice/latest/2020-12-25-a3bf4850-96b4640a/
recipe: https://datasets.datalad.org/shub/BrendelGroup/AllRice/latest/2020-12-25-a3bf4850-96b4640a/Singularity
collection: BrendelGroup/AllRice
---

# BrendelGroup/AllRice:latest

```bash
$ singularity pull shub://BrendelGroup/AllRice:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
From: fedora:33

%help
    This container provides working software versions for the AllRice project.

%post
    dnf -y update
    dnf -y install bc bzip2 findutils git lftp mlocate tcsh unzip zip wget which
    dnf -y install gcc-c++ make automake ruby
    dnf -y install cairo-devel pango-devel zlib-devel
    dnf -y install libnsl
    dnf -y install python python-biopython python3-wheel python-wheel-wheel python3-virtualenv python3-pip
    dnf -y install python3-h5py
    dnf -y install pandoc
    dnf -y install java-11-openjdk java-11-openjdk-devel ant
    dnf -y install perl-App-cpanminus
    dnf -y install curl libcurl libcurl-devel ncurses ncurses-devel
    dnf -y install openssl openssl-devel


### Read quality control

    echo 'Installing FASTQC from http://www.bioinformatics.babraham.ac.uk/projects/fastqc/ '
    cd /opt
    wget http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip
    cpanm install FindBin
    unzip fastqc_v0.11.9.zip
    chmod +x FastQC/fastqc
    \rm fastqc_v0.11.9.zip

    echo 'Installing Trimmomatic from http://www.usadellab.org/cms/index.php?page=trimmomatic '
    cd /opt
    wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.39.zip
    unzip Trimmomatic-0.39.zip
#   Use:	java -jar /opt/Trimmomatic-0.39/trimmomatic-0.39.jar
    \rm Trimmomatic-0.39.zip


### Read manipulation

    echo 'Installing SRATOOLKIT from http://www.ncbi.nlm.nih.gov/books/NBK158900/ '
    cd /opt
    wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.10.5/sratoolkit.2.10.5-ubuntu64.tar.gz
    tar -xzf sratoolkit.2.10.5-ubuntu64.tar.gz
    \rm  sratoolkit.2.10.5-ubuntu64.tar.gz

    echo 'Installing UMI-tools from https://github.com/CGATOxford/UMI-tools '
    pip3 install --upgrade umi-tools

    echo 'Installing HTSLIB from http://www.htslib.org/ '
    cd /opt
    git clone git://github.com/samtools/htslib.git htslib
    cd htslib
    make && make install

    echo 'Installing SAMTOOLS from http://www.htslib.org/ '
    cd /opt
    git clone git://github.com/samtools/samtools.git samtools
    cd samtools
    make && make install


### Read mapping

    echo 'Installing BOWTIE2 version 2.4.2 '
    cd /opt
    wget https://github.com/BenLangmead/bowtie2/releases/download/v2.4.2/bowtie2-2.4.2-linux-x86_64.zip
    unzip bowtie2-2.4.2-linux-x86_64.zip 
    \rm bowtie2-2.4.2-linux-x86_64.zip

    echo 'Installing hisat2 '
    cd /opt
    wget https://cloud.biohpc.swmed.edu/index.php/s/oTtGWbWjaxsQ2Ho/download
    mv download hisat2.zip
    unzip hisat2.zip 
    \rm hisat2.zip 

    echo 'Installing STAR from https://github.com/alexdobin/STAR '
    cd /opt
    git clone https://github.com/alexdobin/STAR


### Repeat masking tools

    echo 'Installing rmblast from http://www.repeatmasker.org/ '
    cd /opt
    wget http://www.repeatmasker.org/rmblast-2.10.0+-x64-linux.tar.gz
    tar -xzf rmblast-2.10.0+-x64-linux.tar.gz
    \rm rmblast-2.10.0+-x64-linux.tar.gz

    echo 'Installing TRF '
    cd /opt
    git clone https://github.com/Benson-Genomics-Lab/TRF.git
    cd TRF
    mkdir build && cd build
    ../configure
    make
    make install
    make clean
    cd ../..

    echo 'Installing RepeatMasker from http://www.repeatmasker.org/ '
    cd /opt
    wget http://repeatmasker.org/RepeatMasker/RepeatMasker-4.1.1.tar.gz
    tar -xzf RepeatMasker-4.1.1.tar.gz 
    echo "/usr/local/bin/trf" > rmcnf
    echo "2" >> rmcnf
    echo "/opt/rmblast-2.10.0/bin" >> rmcnf
    echo "Y" >> rmcnf
    echo "5" >> rmcnf
    cd RepeatMasker
    perl ./configure < ../rmcnf
    cd Libraries
    wget https://github.com/BrendelGroup/AllRice/raw/main/data/RITE-12-10-2020.tgz
    tar -xzf RITE-12-10-2020.tgz
    \rm RITE-12-10-2020.tgz
# ... obtained by download from https://www.genome.arizona.edu/cgi-bin/rite/index.cgi (selecting all Oryza entries)
    cd ../..
    \rm RepeatMasker-4.1.1.tar.gz rmcnf


### RSEM, R, EBSeq

    echo 'Installing R '
    cd /opt
    dnf -y install R
    echo 'repo <- "http://ftp.ussg.iu.edu/CRAN"'                          > R2install
    echo 'install.packages("BiocManager", repos = repo)'                 >> R2install
    echo 'BiocManager::install(c("EBSeq","DESeq2","R2HTML"), ask=FALSE)' >> R2install
    Rscript R2install

    echo 'Installing RSEM '
    cd /opt
    git clone https://github.com/deweylab/RSEM
    cd RSEM/
    # ... we don't want the unaligned reads showing up in the BAM file when using bowtie2, thus:
    sed -i -e "s#--dpad 0#--no-unal --dpad 0#g" rsem-calculate-expression
    make
    make ebseq


### Alignment software

    echo 'Installing BLAST+ version 2.10.1 from NCBI '
    cd /opt
    wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.10.1/ncbi-blast-2.10.1+-x64-linux.tar.gz
    tar -xzf ncbi-blast-2.10.1+-x64-linux.tar.gz
    cd ncbi-blast-2.10.1+/bin
    cp * /usr/local/bin/
    cd ../..
    rm ncbi-blast-2.10.1+-x64-linux.tar.gz
    cd ..

    echo 'Installing MuSeqBox version 5.5 from BrendelGroup '
    cd /opt
    wget http://www.brendelgroup.org/bioinformatics2go/Download/MuSeqBox-3-4-2020.tar.gz
    tar -xzf MuSeqBox-3-4-2020.tar.gz
    cd MUSEQBOX5.5/src/
    make linux
    make install
    make clean
    cd ../..

    echo 'Installing GenomeThreader version 1.7.3 spliced aligner '
    cd /opt
    wget http://genomethreader.org/distributions/gth-1.7.3-Linux_x86_64-64bit.tar.gz
    tar -xzf gth-1.7.3-Linux_x86_64-64bit.tar.gz
    rm gth-1.7.3-Linux_x86_64-64bit.tar.gz
    ln -s gth-1.7.3-Linux_x86_64-64bit GENOMETHREADER


### Utilities

    echo 'Installing the GenomeTools package: '
    cd /opt
    git clone https://github.com/genometools/genometools.git
    cd genometools
    make
    make install
    make clean
    sh -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/genometools-x86_64.conf'
    ldconfig
    cd ..

    echo 'Installing ngsutilsj '
    cd /opt
    git clone https://github.com/compgen-io/ngsutilsj
    cd ngsutilsj
    ant jar
    ln -s /opt/ngsutilsj/dist/ngsutilsj /usr/local/bin/ngsutilsj
    cd ../..

    echo 'Installing the AllRice package: '
    cd /opt
    git clone https://github.com/BrendelGroup/AllRice
    cd ..


%environment
    export LC_ALL=C
    export PATH=$PATH:/opt/FastQC
    export PATH=$PATH:/opt/sratoolkit.2.10.5-ubuntu64/bin
    export PATH=$PATH:/opt/bowtie2-2.4.2-linux-x86_64
    export PATH=$PATH:/opt/hisat2-2.2.1
    export PATH=$PATH:/opt/STAR/bin/Linux_x86_64
    export PATH=$PATH:/opt/RSEM
    export PATH=$PATH:/opt/GENOMETHREADER/bin
    export PATH=$PATH:/opt/RepeatMasker
    export PATH=$PATH:/opt/AllRice/bin
    export BSSMDIR="/opt/GENOMETHREADER/bin/bssm"
    export GTHDATADIR="/opt/GENOMETHREADER/bin/gthdata"

%labels
    Maintainer vpbrendel
    Version v1.1
```

## Collection

 - Name: [BrendelGroup/AllRice](https://github.com/BrendelGroup/AllRice)
 - License: None

