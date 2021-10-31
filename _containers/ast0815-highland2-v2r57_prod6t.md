---
id: 15312
name: "ast0815/highland2"
branch: "master"
tag: "v2r57_prod6t"
commit: "47ec87f056974abca7f7d4731a14d6321e206dbd"
version: "ac6864c4abdfa86efed0ae53c4353e8b3ad80b776b9b11be5fb1e3253e56d891"
build_date: "2021-01-18T16:58:59.615Z"
size_mb: 1006.0
size: 2427428864
sif: "https://datasets.datalad.org/shub/ast0815/highland2/v2r57_prod6t/2021-01-18-47ec87f0-ac6864c4/ac6864c4abdfa86efed0ae53c4353e8b3ad80b776b9b11be5fb1e3253e56d891.sif"
url: https://datasets.datalad.org/shub/ast0815/highland2/v2r57_prod6t/2021-01-18-47ec87f0-ac6864c4/
recipe: https://datasets.datalad.org/shub/ast0815/highland2/v2r57_prod6t/2021-01-18-47ec87f0-ac6864c4/Singularity
collection: ast0815/highland2
---

# ast0815/highland2:v2r57_prod6t

```bash
$ singularity pull shub://ast0815/highland2:v2r57_prod6t
```

## Singularity Recipe

```singularity
Bootstrap: shub
#### Download base image from singularity hub
From: ast0815/t2k-base:latest

%post
  V='2.57.x'
  P='prod6T'

  mkdir -p /usr/local/t2k/current
  cd /usr/local/t2k/current
  export ND280_NJOBS=`nproc`
  git clone https://oauth2:BRTt3ecSv-8CCBeXWR37@git.t2k.org/nd280/pilot/nd280SoftwarePilot.git
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

