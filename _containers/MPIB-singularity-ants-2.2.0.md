---
id: 1939
name: "MPIB/singularity-ants"
branch: "master"
tag: "2.2.0"
commit: "4f355c366e4a0442eb7cb25e5a5e8a8f5f8bafd3"
version: "fa56c3f572a711e607814caf1d60b90a"
build_date: "2021-01-01T13:54:47.017Z"
size_mb: 3520
size: 1041174559
sif: "https://datasets.datalad.org/shub/MPIB/singularity-ants/2.2.0/2021-01-01-4f355c36-fa56c3f5/fa56c3f572a711e607814caf1d60b90a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-ants/2.2.0/2021-01-01-4f355c36-fa56c3f5/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-ants/2.2.0/2021-01-01-4f355c36-fa56c3f5/Singularity
collection: MPIB/singularity-ants
---

# MPIB/singularity-ants:2.2.0

```bash
$ singularity pull shub://MPIB/singularity-ants:2.2.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: debian:9.3-slim 
# Debian Stretch without manpages and other files
# usually not needed in containers.

%help
Contains ANTs (Advanced Normalization Tools) version 2.2.0.
Installation is at /opt/bin/ants.

%post

# Set build specific variables
export BUILD_SOFTWARE="git cmake lib32z1-dev g++"
export CONTAINER_SOFTWARE=""
export ANTS_VERSION="v2.2.0"
# Set paths to facilitate the build process.
export BUILDHOME="/opt"
export CLONE_DIR=/opt
export ANTS_GIT_REPOSITORY=${CLONE_DIR}/ANTs
export ANTS_GIT_REMOTE="https://github.com/stnava/ANTs.git"
export ANTS_HOME=${BUILDHOME}/ants

# Install build requirements.
apt-get update -y
apt-get install $BUILD_SOFTWARE $CONTAINER_SOFTWARE -y 

# Get ANTs from GitHub.
cd $CLONE_DIR
git clone $ANTS_GIT_REMOTE

# Select desired version.
cd $ANTS_GIT_REPOSITORY
git checkout $ANTS_VERSION

# Build ANTs in $ANTS directory
mkdir -p $ANTS_HOME
cd $ANTS_HOME
# Move copyright notice into ANTs Home
cp ${ANTS_GIT_REPOSITORY}/ANTSCopyright.txt ${ANTS_HOME}/
cmake ${ANTS_GIT_REPOSITORY}
make

# Move scripts into the ANTs path.
mv ${ANTS_GIT_REPOSITORY}/Scripts/* $ANTS_HOME/bin/

# Set the path environment variables for ANTs.

echo "export ANTSPATH=${ANTS_HOME}/bin" >> $SINGULARITY_ENVIRONMENT
echo 'export PATH=${ANTSPATH}:$PATH' >> $SINGULARITY_ENVIRONMENT



#cleanup
cd
rm -rf ${ANTS_GIT_REPOSITORY}
apt-get purge $BUILD_SOFTWARE -y
apt-get autoclean -y
apt-get autoremove -y
rm -rf /var/lib/apt/lists/*


%test

# Is antsRegistration in its place and executable?
export ANTS_HOME=/opt/ants/bin/
if [ -d "$ANTS_HOME" ]; then
	/opt/ants/bin/antsRegistration -h
fi
```

## Collection

 - Name: [MPIB/singularity-ants](https://github.com/MPIB/singularity-ants)
 - License: None

