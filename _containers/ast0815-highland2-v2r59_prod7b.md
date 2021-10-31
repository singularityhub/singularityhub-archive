---
id: 15519
name: "ast0815/highland2"
branch: "master"
tag: "v2r59_prod7b"
commit: "13c935370a9be9ea7b40fde4bdcb9f3e60d2e2f6"
version: "5372fc9c8d873779a84afcac795162b2cd349423ff805a4c63e93e9e9e708c8f"
build_date: "2021-02-13T12:01:34.191Z"
size_mb: 1006.0
size: 1564155904
sif: "https://datasets.datalad.org/shub/ast0815/highland2/v2r59_prod7b/2021-02-13-13c93537-5372fc9c/5372fc9c8d873779a84afcac795162b2cd349423ff805a4c63e93e9e9e708c8f.sif"
url: https://datasets.datalad.org/shub/ast0815/highland2/v2r59_prod7b/2021-02-13-13c93537-5372fc9c/
recipe: https://datasets.datalad.org/shub/ast0815/highland2/v2r59_prod7b/2021-02-13-13c93537-5372fc9c/Singularity
collection: ast0815/highland2
---

# ast0815/highland2:v2r59_prod7b

```bash
$ singularity pull shub://ast0815/highland2:v2r59_prod7b
```

## Singularity Recipe

```singularity
Bootstrap: shub
#### Download base image from singularity hub
From: ast0815/t2k-base:latest

%post
  V='2.59.x'
  P='prod7B'

  mkdir -p /usr/local/t2k/current
  cd /usr/local/t2k/current
  export ND280_NJOBS=`nproc`
  git clone -b feature/shallow https://oauth2:BRTt3ecSv-8CCBeXWR37@git.t2k.org/nd280/pilot/nd280SoftwarePilot.git
  cd nd280SoftwarePilot
  ./configure.sh
  source ./nd280SoftwarePilot.profile
  cd ../
  git clone https://oauth2:BRTt3ecSv-8CCBeXWR37@git.t2k.org/nd280/highland2Software/highland2SoftwarePilot.git
  cd ./highland2SoftwarePilot
  source ./highland2SoftwarePilot.profile
  highland-install -j ${ND280_NJOBS} -r -p ${P} ${V}
  cd ../
  source ./highland2Master_${V}/bin/setup.sh

  # Create setup script
  echo '#!/bin/bash' > setup.sh
  echo 'source /usr/local/t2k/current/nd280SoftwarePilot/nd280SoftwarePilot.profile' >> setup.sh
  echo 'source /usr/local/t2k/current/highland2SoftwarePilot/highland2SoftwarePilot.profile' >> setup.sh
  echo "source /usr/local/t2k/current/highland2Master_${V}/bin/setup.sh" >> setup.sh

%environment
    echo "# Use the following command to setup the software:"
    echo ""
    echo "source /usr/local/t2k/current/setup.sh"
    echo ""
    echo "# Please ignore any errors about checks for pdf files or geometries."
```

## Collection

 - Name: [ast0815/highland2](https://github.com/ast0815/highland2)
 - License: None

