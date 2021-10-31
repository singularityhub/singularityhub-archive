---
id: 10225
name: "sneuensc/singularity_KFMC"
branch: "master"
tag: "latest"
commit: "b9bca86f5b43eb7a7f9f7000f6998ab7ff71feba"
version: "70f6153c5f0ece722e2b59f85de7ddbe"
build_date: "2019-07-04T11:15:23.953Z"
size_mb: None
size: 875700255
sif: "https://datasets.datalad.org/shub/sneuensc/singularity_KFMC/latest/2019-07-04-b9bca86f-70f6153c/70f6153c5f0ece722e2b59f85de7ddbe.simg"
url: https://datasets.datalad.org/shub/sneuensc/singularity_KFMC/latest/2019-07-04-b9bca86f-70f6153c/
recipe: https://datasets.datalad.org/shub/sneuensc/singularity_KFMC/latest/2019-07-04-b9bca86f-70f6153c/Singularity
collection: sneuensc/singularity_KFMC
---

# sneuensc/singularity_KFMC:latest

```bash
$ singularity pull shub://sneuensc/singularity_KFMC:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest


%environment
# Section to define environment variables that will be available to the container at runtime.
# We use it to define the name, version and release of the container.
export CONTAINER_NAME="SV-Workflow"
export CONTAINER_VERSION="0.1"
export CONTAINER_RELEASE="centos"
export PATH="/usr/miniconda/bin/:$PATH"

%help
####################################################################################################
### Container metadata:
### ******************
### Name:    SV-Workflow
### Version: 0.1
### Release: centos
### Summary: Workflow to call SVs based on PacBio reads
### Group:   Container
### License: GPL
### URL:     ---
###
###
### Description:
### ***********
### A nextflow based workflow which has the following steps:
### - map PacBio reads against Chr22 using ngmlr
### - convert sam to bam and index
### - call structural variants with Sniffles
###
### Running the container:
### *********************
### Available commands: sniffles,ngmlr,samtools
###
### To run any command in the container, replace <command to run> in command below.:
###   singularity run KFMC_SVworkflow.simg  <options>
###
### To make a specific repository, such as "home/<yourDirectory>", available
### inside the container add the option "--bind <directory>". Here is an example:
###   singularity run --bind <directory>  KFMC_SVworkflow.simg <options>
###
### To run the default command for the container the command is the following. The default command
### generally displays the "help" section of the software installed in the container:
###   singularity run /software/singularity/containers/GEMTools-1.6.2-1.centos6.simg
####################################################################################################


%runscript
echo "### Displaying  help:"
exit 0


%files
# Section to copy files into the container from the host system at build time.
# /home/eschmid/Desktop/testFile.txt                          # copied to root of container.



%labels
# Section to set custom metadata to be added to the container.
AUTHOR emanuel.schmid@sib.swiss


%post
# Update base OS packages to latest version.
yum install deltarpm --assumeyes --quiet
yum update --assumeyes --quiet


# Install epel mirror (extra packages for enterprise linux).
yum install epel-release --assumeyes --quiet


# Install gcc and other development tools.
# yum groupinstall "Development Tools" --assumeyes
yum install gcc gcc-c++ gcc-gfortran glibc-devel binutils bzip2 which bzip2-devel zlib-devel libXext.x86_64 libXrender.x86_64 libXtst.x86_64 \
glib-networking-common  freetype libcanberra-gtk-module locales openjdk-8-jre \
make wget --assumeyes --quiet

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
bash miniconda3.sh -b -u -p /usr/miniconda
export PATH="/usr/miniconda/bin/:$PATH"
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda
conda install -y samtools ngmlr sniffles nextflow igv
```

## Collection

 - Name: [sneuensc/singularity_KFMC](https://github.com/sneuensc/singularity_KFMC)
 - License: None

