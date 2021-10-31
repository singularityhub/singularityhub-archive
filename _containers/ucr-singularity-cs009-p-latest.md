---
id: 6122
name: "ucr-singularity/cs009-p"
branch: "master"
tag: "latest"
commit: "869dadc13cc70b5a15a52b73f5e10c5d045c0136"
version: "84d0706e56d33d9058996a7bd0ec510e"
build_date: "2019-01-04T07:48:36.788Z"
size_mb: 3365
size: 1487708191
sif: "https://datasets.datalad.org/shub/ucr-singularity/cs009-p/latest/2019-01-04-869dadc1-84d0706e/84d0706e56d33d9058996a7bd0ec510e.simg"
url: https://datasets.datalad.org/shub/ucr-singularity/cs009-p/latest/2019-01-04-869dadc1-84d0706e/
recipe: https://datasets.datalad.org/shub/ucr-singularity/cs009-p/latest/2019-01-04-869dadc1-84d0706e/Singularity
collection: ucr-singularity/cs009-p
---

# ucr-singularity/cs009-p:latest

```bash
$ singularity pull shub://ucr-singularity/cs009-p:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%environment

PATH=/opt/conda/bin:$PATH
export PATH

%post
  
# Set up the PATH for other commands
export PATH=/opt/conda/bin:$PATH

# Update list of packages then upgrade them
apt-get update
apt-get install -y apt-utils 
DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade
    
# Install basic packages
apt-get install -y --no-install-recommends build-essential cmake git curl vim \
    ca-certificates 
apt-get install -y screen terminator tmux vim wget 
apt-get install -y aptitude build-essential cmake g++ gfortran git pkg-config software-properties-common
apt-get install -y unrar
apt-get install -y libzip-dev

# Clean up
apt-get -y autoremove
rm -rvf /var/lib/apt/lists/*

# Install miniconda
cd /opt
curl -o /opt/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x /opt/miniconda.sh
/opt/miniconda.sh -b -p /opt/conda 
rm /opt/miniconda.sh

# Install CS 009p related stuff
# Add packages that are also in system python via conda or pip
conda install -y -c anaconda scipy nose h5py scikit-image scikit-learn matplotlib pandas sympy virtualenv pygments sphinx

# Set to be used as a Jupyter kernel
pip install --no-cache-dir ipykernel

# Set locale and path in Singularity environment
echo 'export LC_ALL=C' >>$SINGULARITY_ENVIRONMENT
echo 'export PATH=/opt/conda/bin:$PATH' >>$SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [ucr-singularity/cs009-p](https://github.com/ucr-singularity/cs009-p)
 - License: None

