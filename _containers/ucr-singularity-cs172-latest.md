---
id: 5795
name: "ucr-singularity/cs172"
branch: "master"
tag: "latest"
commit: "2d5771767948935389b53b01737b393035b90995"
version: "af0324026ce980018626d989034673a4"
build_date: "2018-12-04T16:31:44.394Z"
size_mb: 1027
size: 388698143
sif: "https://datasets.datalad.org/shub/ucr-singularity/cs172/latest/2018-12-04-2d577176-af032402/af0324026ce980018626d989034673a4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ucr-singularity/cs172/latest/2018-12-04-2d577176-af032402/
recipe: https://datasets.datalad.org/shub/ucr-singularity/cs172/latest/2018-12-04-2d577176-af032402/Singularity
collection: ucr-singularity/cs172
---

# ucr-singularity/cs172:latest

```bash
$ singularity pull shub://ucr-singularity/cs172:latest
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

# Set locale in Singularity environment
echo 'export LC_ALL=C' >>$SINGULARITY_ENVIRONMENT
echo 'export PATH=/opt/conda/bin:$PATH' >>$SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [ucr-singularity/cs172](https://github.com/ucr-singularity/cs172)
 - License: None

