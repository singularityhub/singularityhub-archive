---
id: 2013
name: "pescobar/STPH-course-soft"
branch: "master"
tag: "latest"
commit: "63cbb15efa08c2df3916e067a7abc083198d90e5"
version: "177b15836d5fa842470346c4a0ade338"
build_date: "2020-08-15T07:05:10.379Z"
size_mb: 5152
size: 2762510367
sif: "https://datasets.datalad.org/shub/pescobar/STPH-course-soft/latest/2020-08-15-63cbb15e-177b1583/177b15836d5fa842470346c4a0ade338.simg"
url: https://datasets.datalad.org/shub/pescobar/STPH-course-soft/latest/2020-08-15-63cbb15e-177b1583/
recipe: https://datasets.datalad.org/shub/pescobar/STPH-course-soft/latest/2020-08-15-63cbb15e-177b1583/Singularity
collection: pescobar/STPH-course-soft
---

# pescobar/STPH-course-soft:latest

```bash
$ singularity pull shub://pescobar/STPH-course-soft:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post

    # install some system deps
    apt-get -y update
    apt-get -y install locales curl bzip2 less unzip
    # this is a X11 dep for IGV
    apt-get -y install libxext6
    # tools to open PDF and HTML files
    apt-get -y install firefox xpdf
    # some extra devel libs
    apt-get -y install zlib1g-dev libssl-dev
    locale-gen en_US.UTF-8
    apt-get clean

    # download and install miniconda3
    curl -sSL -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -p /opt/miniconda3 -b
    rm -fr Miniconda3-latest-Linux-x86_64.sh
    export PATH=/opt/miniconda3/bin:$PATH
    conda update -n base conda
    conda config --add channels conda-forge
    conda config --add channels bioconda

    # install some bioinfo tools from Bioconda
    conda install --yes -c bioconda samtools==1.7
    conda install --yes -c bioconda bwa==0.7.17
    conda install --yes -c bioconda trimmomatic==0.36
    conda install --yes -c bioconda perl-findbin==1.51
    conda install --yes -c bioconda fastqc==0.11.7
    conda install --yes -c bioconda seqprep==1.2
    conda install --yes -c bioconda gatk4==4.0.1.1
    conda install --yes -c bioconda igv=2.3.98
    conda install --yes -c bioconda vcftools==0.1.15
    conda install --yes -c bioconda snpeff=4.3.1t-0
    conda install --yes -c bioconda varscan==2.4.3
    conda install --yes -c bioconda muscle==3.8.1551
    conda install --yes -c bioconda mafft==7.313
    conda install --yes -c bioconda raxml==8.2.10
    conda install --yes -c bioconda beast==1.8.4
    conda install --yes -c bioconda phylip==3.696
    conda install --yes -c bioconda paml==4.9
    conda install --yes -c bioconda qualimap==2.2.2a
    conda install --yes -c bioconda picard==2.18.3
    conda install --yes -c bioconda biopython==1.71

    # install the R programming language
    conda install --yes -c conda-forge r-base==3.4.1

    # install some dependencies to build R packages
    apt-get -y install build-essential gfortran
    #conda install --yes -c conda-forge make
    #conda install --yes gfortran_linux-64
    #conda install --yes gxx_linux-64
    #conda install --yes gcc_linux-64

    # install some extra R packages
    Rscript -e "source ('https://bioconductor.org/biocLite.R'); biocLite(c('ape', 'pegas', 'adegenet', 'phangorn', 'sqldf', 'ggtree', 'ggplot2', 'phytools'))"

    # install the jupyter notebook
    conda install --yes jupyter

    # install R kernel for jupyter
    Rscript -e "source ('https://bioconductor.org/biocLite.R'); biocLite(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'git2r', 'devtools', 'uuid', 'digest'))"
    ln -s /bin/tar /bin/gtar
    Rscript -e "devtools::install_url('https://github.com/IRkernel/IRkernel/archive/0.8.11.tar.gz')"
    #Rscript -e "devtools::install_github('IRkernel/IRkernel')" # this one doesnt work
    Rscript -e "IRkernel::installspec(user = FALSE)"

    # install TNT 
    curl -sSL -O http://www.lillo.org.ar/phylogeny/tnt/tnt64.zip
    unzip -p tnt64.zip tnt > /usr/local/bin/tnt
    chmod +x /usr/local/bin/tnt

    # donwload and uncompress figtree to /opt/FigTree_v1.4.3/
    # also create a wrapper script in /usr/local/bin
    curl -sSL -o /opt/figtree.tgz "http://tree.bio.ed.ac.uk/download.php?id=96&num=3"
    tar -xvf /opt/figtree.tgz -C /opt/
    chmod +x /opt/FigTree_v1.4.3/bin/figtree
    cat <<EOF >>/usr/local/bin/figtree
#!/bin/sh
cd /opt/FigTree_v1.4.3/
java -Xms64m -Xmx512m -jar lib/figtree.jar $*
EOF
    chmod +x /usr/local/bin/figtree

%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export PATH=/opt/miniconda3/bin:$PATH
    export XDG_RUNTIME_DIR=""

%apprun samtools
    samtools "$@"

%apprun bwa
    bwa "$@"

%apprun trimmomatic
    trimmomatic "$@"

%apprun fastqc
    fastqc "$@"

%apprun seqprep
    seqprep "$@"

%apprun gatk4
    gatk-launch "$@"

%apprun vcftools
    vcftools "$@"

%apprun snpeff
    snpeff "$@"

%apprun varscan
    varscan "$@"

%apprun muscle
    varscan "$@"

%apprun mafft
    mafft "$@"

%apprun raxml
    raxmlHPC-PTHREADS "$@"

%apprun beast
    beast "$@"

%apprun phylip
    phylip "$@"

%apprun paml
    codeml "$@"

%apprun picard
    picard "$@"

%apprun qualimap
    qualimap "$@"

%apprun R
    R "$@"

%apprun jupyter
    jupyter "$@"

%apprun tnt
    tnt "$@"

%apprun figtree
    /usr/local/bin/figtree
```

## Collection

 - Name: [pescobar/STPH-course-soft](https://github.com/pescobar/STPH-course-soft)
 - License: None

