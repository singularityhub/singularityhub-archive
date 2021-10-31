---
id: 15518
name: "ast0815/highland2"
branch: "master"
tag: "v2r59_prod6t"
commit: "13c935370a9be9ea7b40fde4bdcb9f3e60d2e2f6"
version: "3b3bfed8c73a2b01d46afd3dcf3e0099e34c7f8a7d3277c1bb299e912e042755"
build_date: "2021-02-12T19:08:07.193Z"
size_mb: 1006.0
size: 1564323840
sif: "https://datasets.datalad.org/shub/ast0815/highland2/v2r59_prod6t/2021-02-12-13c93537-3b3bfed8/3b3bfed8c73a2b01d46afd3dcf3e0099e34c7f8a7d3277c1bb299e912e042755.sif"
url: https://datasets.datalad.org/shub/ast0815/highland2/v2r59_prod6t/2021-02-12-13c93537-3b3bfed8/
recipe: https://datasets.datalad.org/shub/ast0815/highland2/v2r59_prod6t/2021-02-12-13c93537-3b3bfed8/Singularity
collection: ast0815/highland2
---

# ast0815/highland2:v2r59_prod6t

```bash
$ singularity pull shub://ast0815/highland2:v2r59_prod6t
```

## Singularity Recipe

```singularity
Bootstrap: shub
#### Download base image from singularity hub
From: ast0815/t2k-base:latest

%post
  V='2.59.x'
  P='prod6T'

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

