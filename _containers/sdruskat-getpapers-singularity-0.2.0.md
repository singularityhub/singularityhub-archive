---
id: 10505
name: "sdruskat/getpapers-singularity"
branch: "master"
tag: "0.2.0"
commit: "cc788b1bf326679532de2d457f8c5f17cba11382"
version: "96baaeac6614103063667836c37935fc7c9a2d3b8c29aa21d6b549834fef6089"
build_date: "2019-08-12T10:41:12.199Z"
size_mb: 115.42578125
size: 121032704
sif: "https://datasets.datalad.org/shub/sdruskat/getpapers-singularity/0.2.0/2019-08-12-cc788b1b-96baaeac/96baaeac6614103063667836c37935fc7c9a2d3b8c29aa21d6b549834fef6089.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sdruskat/getpapers-singularity/0.2.0/2019-08-12-cc788b1b-96baaeac/
recipe: https://datasets.datalad.org/shub/sdruskat/getpapers-singularity/0.2.0/2019-08-12-cc788b1b-96baaeac/Singularity
collection: sdruskat/getpapers-singularity
---

# sdruskat/getpapers-singularity:0.2.0

```bash
$ singularity pull shub://sdruskat/getpapers-singularity:0.2.0
```

## Singularity Recipe

```singularity
# Bootstrap a container from repo: library (https://cloud.sylabs.io/library)
Bootstrap: library
# Use this container (The library default Ubuntu 18.04 LTS container, 
# created at 2019-05-25 12:10:12 for amd64, with
# fingerprint 8883491F4268F173C6E5DC49EDECE4F3F38D871E)
From: library/default/ubuntu:sha256.80c52afadf3e7c3f9573de4fe79b7dca57fb3290df6c8dc46a75b02768a81146 

# After pulling this container, do the following:
%post
     # Update the apt repositories
     apt-get -y update
     # Install the cURL library for retrieving objects from a URL
     apt-get -y install curl
     # Retrieve and run the NodeJS setup script for versions 12.x
     curl -sL https://deb.nodesource.com/setup_12.x | bash -
     # Install NodeJS version 12
     apt-get install -y nodejs
     # Install ContentMine/getpapers node package version 0.4.17
     npm install -g getpapers@0.4.17

%runscript
    echo "To use getpapers from this Singularity container, run"
    echo "    singularity exec getpapers.sif getpapers ...\n"
    echo ""
    echo "The container also provides the following apps."
    echo "They can be run with"
    echo "    singularity run --app <app name>"
    echo ""
    echo "--app eupmc (Queries the European PubMed Central API for 'github.com')"
    echo "--app arxiv (Queries the arXiv API for 'all:github.com')"
    exec echo "$@"

%test
    # Test if the distribution pretty name is "Ubuntu 18.04 LTS"
    grep -q PRETTY_NAME=\"Ubuntu\ 18.04\ LTS\" /etc/os-release
    if [ $? -eq 0 ]; then
        echo "Container base is Ubuntu 18.04 LTS as expected."
    else
        echo "[ERROR] Container base is NOT Ubuntu 18.04 LTS!"
    fi

    # Test if the kernel version is 5.0.0-23-generic
    KERNEL_VER="$(uname -r)"
    if [ "$KERNEL_VER" = "5.0.0-23-generic" ]; then
        echo "Kernel version is 5.0.0-23-generic as expected."
    else
        echo "[ERROR] Kernel version is NOT 5.0.0-23-generic!"
    fi

    # Test if the Node version is 12.7.0
    NODE_VER="$(node --version)"
    if [ "$NODE_VER" = "v12.7.0" ]; then
        echo "Node version is 12.7.0 as expected."
    else
        echo "[ERROR] Node version is NOT 12.7.0!"
    fi

    # Test if the npm version is 6.10.0
    NPM_VER="$(npm --version)"
    if [ "$NPM_VER" = "6.10.0" ]; then
        echo "npm version is 6.10.0 as expected."
    else
        echo "[ERROR] npm version is NOT 6.10.0!"
    fi

    # Test if the getpapers version is 0.4.17
    GP_VER="$(getpapers --version)"
    if [ "$GP_VER" = "0.4.17" ]; then
        echo "getpapers version is 0.4.17 as expected."
    else
        echo "[ERROR] getpapers version is NOT 0.4.17!"
    fi

%labels
    Author Stephan Druskat (mail@sdruskat.net)
    Version v0.2.0

%help
    This container contains NodeJS version 12.7.0 (NPM 6.10.0) and the getpapers package v0.4.17 on Ubuntu 18.04 LTS.

##############################
# eupmc
##############################

%apprun eupmc
    echo "Querying EU PubMed Central and writing to ./eupmc.log"
    exec getpapers --query 'github.com' --outdir eupmc --xml | tee eupmc.log

%appinstall eupmc
   touch eupmc.exec

%apphelp eupmc
    Queries the European PubMed Central API with "github.com" and saves the resulting XML full texts to ./eupmc.

##############################
# arxiv
##############################

%apprun arxiv
    echo "Querying ArXiV and writing to ./arxiv.log."
    exec getpapers --query 'all:github.com' --api arxiv --pdf --outdir arxiv | tee arxiv.log

%appinstall arxiv
   touch arxiv.exec

%apphelp arxiv
    Queries the ArXiV API with "all:github.com" and saves the resulting PDF full texts to ./arxiv.
```

## Collection

 - Name: [sdruskat/getpapers-singularity](https://github.com/sdruskat/getpapers-singularity)
 - License: None

