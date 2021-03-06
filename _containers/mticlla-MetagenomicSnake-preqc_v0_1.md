---
id: 9441
name: "mticlla/MetagenomicSnake"
branch: "master"
tag: "preqc_v0_1"
commit: "17e16c0bc368a90cc4ba7ff48936e98e48011b53"
version: "df60be93049594cb84c1b815595f2ac4"
build_date: "2021-02-03T10:46:21.130Z"
size_mb: 2162
size: 859787295
sif: "https://datasets.datalad.org/shub/mticlla/MetagenomicSnake/preqc_v0_1/2021-02-03-17e16c0b-df60be93/df60be93049594cb84c1b815595f2ac4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mticlla/MetagenomicSnake/preqc_v0_1/2021-02-03-17e16c0b-df60be93/
recipe: https://datasets.datalad.org/shub/mticlla/MetagenomicSnake/preqc_v0_1/2021-02-03-17e16c0b-df60be93/Singularity
collection: mticlla/MetagenomicSnake
---

# mticlla/MetagenomicSnake:preqc_v0_1

```bash
$ singularity pull shub://mticlla/MetagenomicSnake:preqc_v0_1
```

## Singularity Recipe

```singularity
# Author(s): Monica R. Ticlla
# Afiliation(s):
#  - Swiss Institute of Bioinformatics (SIB)
#  - Swiss Tropical and Public Health Institute (SwissTPH)
#  - University of Basel (UNIBAS)

Bootstrap: docker
From: centos:7

# ==============================================================================
# Global Help
# ==============================================================================
%help
This image contains software for quality control and preprocessing of sequencing
data. It was built with CentOS 7 as base OS and Python 3.6. Although this is a
companion container of the MetagenomicSnake workflow, it can also be used separately.

Usage:
- To list available Apps:
singularity apps <CONTAINER_PATH>
- To get help for a particular APP:
singularity help --app <APP_NAME> <CONTAINER_PATH>
- To run a particular APP:
singularity run --app <APP_NAME> <CONTAINER_PATH>

%labels
# ==============================================================================
# Labels
# ==============================================================================
  AUTHOR mticlla@gmail.com
  MAINTAINER mticlla@gmail.com
  BUILD_VERSION v0.1

# ==============================================================================
# Global Environment
# ==============================================================================
%environment
  export LANG=en_US.UTF-8
  export LANGUAGE=en_US:en
  export LC_ALL=en_US.UTF-8

# ==============================================================================
# Global installation
# ==============================================================================
%post
  # set environment variables for build time
  echo "Setting environment variables for build time ..."
  export LANG=en_US.UTF-8
  export LANGUAGE=en_US:en
  export LC_ALL=en_US.UTF-8

  # Install core packages
  yum -y update
  echo "Installing development tools ..."
  yum -y groupinstall "Development tools"
  yum -y makecache
  yum -y install unzip
  yum -y install which
  yum -y install hg
  yum -y install gcc
  yum -y install gcc-c++
  yum -y install zlib-devel
  yum -y install libstdc++-static
  yum -y install wget
  yum -y install bzip2
  yum -y install git
  yum -y install make
  yum -y install nano
  yum -y install perl

  # Install Java
  yum -y install java-1.8.0-openjdk-devel

  # Install pigz
  yum -y install pigz

  # Install conda
  curl -sSL -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
  bash Miniconda3-latest-Linux-x86_64.sh -p /opt/miniconda3 -b
  rm -fr Miniconda3-latest-Linux-x86_64.sh
  export PATH=/opt/miniconda3/bin:$PATH
  echo "export PATH=/opt/miniconda3/bin:\$PATH" >> $SINGULARITY_ENVIRONMENT
  conda update --yes -n base conda
  conda install --yes gcc_linux-64
  conda install --yes gxx_linux-64
  conda install --yes python==3.6

%runscript
  echo "This image has the following software installed:"
  fastqc --version
  echo "BBTools $(tail -n1 /scif/apps/BBTools/bbmap/README.md | cut -d' ' -f 2,3)"
  multiqc --version
  cutadapt --help| head -n1
  fastp --version

  echo -e "\nHow to use these programs?:"
  echo "Example: singularity exec <CONTAINER_PATH> fastp --help"

  echo -e "\nThese programs are also available as SCIF applications:"
  ls /scif/apps | sort -u
  echo -e "\nHow to use a SCIF APP?:"
  echo "Example: singularity run --app FastQC <CONTAINER_PATH>\n"

# ==============================================================================
# SCIF Apps
# ==============================================================================

# FastQC
# ==============================================================================
%applabels FastQC
  VERSION v0.11.8
%appenv FastQC
  FASTQC_VERSION='0.11.8'
  export FASTQC_VERSION
%appinstall FastQC
  FASTQC_VERSION='0.11.8'
  yum -y install java-1.8.0-openjdk-devel
  wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v${FASTQC_VERSION}.zip
  unzip fastqc_v${FASTQC_VERSION}.zip
  rm fastqc_v${FASTQC_VERSION}.zip
  cd FastQC/
  chmod 755 fastqc
  ln -s /scif/apps/FastQC/FastQC/fastqc /usr/local/bin/fastqc
%apphelp FastQC
  From [FastQC website](http://www.bioinformatics.babraham.ac.uk/projects/fastqc):

  FastQC aims to provide a simple way to do some quality control checks on raw
  sequence data coming from high throughput sequencing pipelines. It provides a
  modular set of analyses which you can use to give a quick impression of whether
  your data has any problems of which you should be aware before doing any further
  analysis.
%apprun FastQC
  exec fastqc "$@"
%apptest FastQC
  fastqc --version
  if [ $? -ne 0 ] ; then
    echo "FastQC installation failed!"
  else
    echo "FastQC installed successfully!"
  fi

# BBTools
# ==============================================================================
%applabels BBTools
  VERSION v38.39
%appenv BBTools
  BBTOOLS_VERSION='38.39'
  export BBTOOLS_VERSION
  BBTOOLS=/scif/apps/BBTools/bbmap
  export BBTOOLS
%appinstall BBTools
  BBTOOLS_VS='38.39'
  yum -y install java-1.8.0-openjdk-devel
  wget https://sourceforge.net/projects/bbmap/files/BBMap_${BBTOOLS_VS}.tar.gz
  tar -xzf BBMap_${BBTOOLS_VS}.tar.gz
  rm BBMap_${BBTOOLS_VS}.tar.gz
  ln -s /scif/apps/BBTools/bbmap /scif/apps/BBTools/bin
  echo "export PATH=/scif/apps/BBTools/bbmap:\$PATH" >> $SINGULARITY_ENVIRONMENT
%apphelp BBTools
  From [BBTools website](https://jgi.doe.gov/data-and-tools/bbtools/):

  BBTools is a suite of fast, multithreaded bioinformatics tools designed for
  analysis of DNA and RNA sequence data. BBTools can handle common sequencing
  file formats such as fastq, fasta, sam, scarf, fasta+qual, compressed or raw,
  with autodetection of quality encoding and interleaving. It is written in Java
  and works on any platform supporting Java, including Linux, MacOS, and Microsoft
  Windows and Linux; there are no dependencies other than Java (version 7 or higher).
  Program descriptions and options are shown when running the shell scripts with
  no parameters.

  BBTools is open source and free for unlimited use, and is used regularly by
  DOE JGI and other institutions around the world.

  USAGE:
  Once the container has been built, BBTools tools (e.g reformat.sh) can be used
  in any of the following ways:
  - Option 1:
  singularity exec --app BBTools <SINGULARITY_CONTAINER_PATH> reformat.sh --help

  - Option 2:
  singularity exec <SINGULARITY_CONTAINER_PATH> reformat.sh --help

  - Option 3 :from inside the container
  reformat.sh --help
%apprun BBTools
  echo -e "
  BBTools v${BBTOOLS_VERSION} is a suite of tools designed for analysis of DNA
  and RNA sequence data.For help, run:
  singularity help --app BBTools <CONTAINER_PATH>
  "
%apptest BBTools
  export BBTOOLS=/scif/apps/BBTools/bbmap
  ${BBTOOLS}/stats.sh in=${BBTOOLS}/resources/phix174_ill.ref.fa.gz
  if [ $? -ne 0 ] ; then
    echo "BBTools installation failed!"
  else
    echo "BBTools installed successfully!"
  fi

# MultiQC
# ==============================================================================
%appinstall MultiQC
  export LANG=en_US.UTF-8
  export LANGUAGE=en_US:en
  export LC_ALL=en_US.UTF-8
  export PATH=/opt/miniconda3/bin:$PATH
  git clone https://github.com/ewels/MultiQC.git
  cd MultiQC/
  pip install setuptools
  python setup.py install
%apphelp MultiQC
  From [MultiQC website](https://multiqc.info/docs/)

  MultiQC is a reporting tool that parses summary statistics from results and log
  files generated by other bioinformatics tools. MultiQC doesn't run other tools
  for you - it's designed to be placed at the end of analysis pipelines or to be
  run manually when you've finished running your tools.

  When you launch MultiQC, it recursively searches through any provided file paths
  and finds files that it recognizes. It parses relevant information from these
  and generates a single stand-alone HTML report file. It also saves a directory
  of data files with all parsed data for further downstream use.
%apprun MultiQC
  exec multiqc "$@"
%apptest MultiQC
  multiqc --version
  if [ $? -ne 0 ] ; then
    echo "MultiQC installation failed!"
  else
    echo "MultiQC installed successfully!"
  fi

# cutadapt
# ==============================================================================
%applabel cutadapt
  VERSION v2.3
%appinstall cutadapt
  export PATH=/opt/miniconda3/bin:$PATH
  pip install "cutadapt==2.3"
%apphelp cutadapt
  From [Cuatadapt website](https://cutadapt.readthedocs.io/en/stable/index.html)

  Cutadapt finds and removes adapter sequences, primers, poly-A tails and other
  types of unwanted sequence from your high-throughput sequencing reads.
%apprun cutadapt
  exec cutadapt "$@"
%apptest cutadapt
  cutadapt --help| head -n1
  if [ $? -ne 0 ] ; then
    echo "cutadapt installation failed!"
  else
    echo "cutadapt installed successfully!"
  fi

# fastp
# ==============================================================================
%appinstall fastp
  git clone https://github.com/OpenGene/fastp.git
  cd fastp
  make
  make install
%apphelp fastp
  From [fastp website](https://github.com/OpenGene/fastp)

  A tool designed to provide fast all-in-one preprocessing for FastQ files.
  This tool is developed in C++ with multithreading supported to afford high
  performance.
%apprun fastp
  exec fastp "$@"
%apptest fastp
  fastp --version
  if [ $? -ne 0 ] ; then
    echo "fastp installation failed!"
  else
    echo "fastp installed successfully!"
  fi
```

## Collection

 - Name: [mticlla/MetagenomicSnake](https://github.com/mticlla/MetagenomicSnake)
 - License: None

