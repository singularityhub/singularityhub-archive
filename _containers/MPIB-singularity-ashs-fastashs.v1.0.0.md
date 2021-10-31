---
id: 1958
name: "MPIB/singularity-ashs"
branch: "master"
tag: "fastashs.v1.0.0"
commit: "b9b41e3123dc53868d62b3891c1e35533180178e"
version: "45a1917ca3b3b0772e597bdbca3629e6"
build_date: "2020-07-14T10:07:07.030Z"
size_mb: 707
size: 232718367
sif: "https://datasets.datalad.org/shub/MPIB/singularity-ashs/fastashs.v1.0.0/2020-07-14-b9b41e31-45a1917c/45a1917ca3b3b0772e597bdbca3629e6.simg"
url: https://datasets.datalad.org/shub/MPIB/singularity-ashs/fastashs.v1.0.0/2020-07-14-b9b41e31-45a1917c/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-ashs/fastashs.v1.0.0/2020-07-14-b9b41e31-45a1917c/Singularity
collection: MPIB/singularity-ashs
---

# MPIB/singularity-ashs:fastashs.v1.0.0

```bash
$ singularity pull shub://MPIB/singularity-ashs:fastashs.v1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: debian:9.3-slim
# Debian Stretch without manpages and other files
# usually not needed in containers.

%help

Contains fastashes version v1.0.0

%post

# Set build specific variables
export BUILD_SOFTWARE="git"
export CONTAINER_SOFTWARE="parallel libxt6 libxext-dev libgl-gst"
export ASHS_VERSION="v1.0.0"
# Set paths to facilitate the build process.
export BUILDHOME="/opt"
export ASHS_HOME=${BUILDHOME}/ashs

# Install build requirements.
apt-get update
apt-get install $BUILD_SOFTWARE $CONTAINER_SOFTWARE -y

# Get ASHS from GitHub.
cd $BUILDHOME
git clone https://github.com/pyushkevich/ashs.git

# Select desired version.
cd $ASHS_HOME
git checkout $ASHS_VERSION

# Set the path environment variables for ASHS.

echo "export ASHS_ROOT=${ASHS_HOME}" >> $SINGULARITY_ENVIRONMENT
echo "export PATH=${ASHS_HOME}/bin:$PATH" >> $SINGULARITY_ENVIRONMENT


#cleanup
rm -rf $ASHS_HOME/.git*
apt-get purge $BUILD_SOFTWARE -y
apt-get autoclean -y
apt-get autoremove -y
rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [MPIB/singularity-ashs](https://github.com/MPIB/singularity-ashs)
 - License: None

