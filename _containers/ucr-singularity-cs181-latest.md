---
id: 5796
name: "ucr-singularity/cs181"
branch: "master"
tag: "latest"
commit: "44dcf557a173ac755c72a575ef74877be340fad1"
version: "36a05a40203b0f476c5434dce5fc31c8"
build_date: "2019-02-15T00:23:14.635Z"
size_mb: 1543
size: 625958943
sif: "https://datasets.datalad.org/shub/ucr-singularity/cs181/latest/2019-02-15-44dcf557-36a05a40/36a05a40203b0f476c5434dce5fc31c8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ucr-singularity/cs181/latest/2019-02-15-44dcf557-36a05a40/
recipe: https://datasets.datalad.org/shub/ucr-singularity/cs181/latest/2019-02-15-44dcf557-36a05a40/Singularity
collection: ucr-singularity/cs181
---

# ucr-singularity/cs181:latest

```bash
$ singularity pull shub://ucr-singularity/cs181:latest
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

# Install CS 181 specific stuff
apt-get install -y swi-prolog smlnj java11-sdk

# More cs181 specific stuff - for readline in interpreters
apt-get install -y rlwrap
# More cs181 specific stuff - for dot
apt-get install -y graphviz
# More cs181 specific stuff - for display
apt-get install -y graphicsmagick-imagemagick-compat

# Clean up
apt-get -y autoremove
rm -rvf /var/lib/apt/lists/*

# Install miniconda
cd /opt
curl -o /opt/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x /opt/miniconda.sh
/opt/miniconda.sh -b -p /opt/conda 
rm /opt/miniconda.sh

# Set locale in Singularity environment
echo 'export LC_ALL=C' >>$SINGULARITY_ENVIRONMENT
echo 'export PATH=/opt/conda/bin:$PATH' >>$SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [ucr-singularity/cs181](https://github.com/ucr-singularity/cs181)
 - License: None

