---
id: 15292
name: "ast0815/highland2"
branch: "master"
tag: "v2r58_prod6t"
commit: "9b4bba697130a61c299773dc3ae3ecb30a2f5314"
version: "25f00b6198837e7052411220135a8c4110b46fc5130be55ea79456cf4e105c7c"
build_date: "2021-01-19T14:19:59.915Z"
size_mb: 1006.0
size: 2427596800
sif: "https://datasets.datalad.org/shub/ast0815/highland2/v2r58_prod6t/2021-01-19-9b4bba69-25f00b61/25f00b6198837e7052411220135a8c4110b46fc5130be55ea79456cf4e105c7c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ast0815/highland2/v2r58_prod6t/2021-01-19-9b4bba69-25f00b61/
recipe: https://datasets.datalad.org/shub/ast0815/highland2/v2r58_prod6t/2021-01-19-9b4bba69-25f00b61/Singularity
collection: ast0815/highland2
---

# ast0815/highland2:v2r58_prod6t

```bash
$ singularity pull shub://ast0815/highland2:v2r58_prod6t
```

## Singularity Recipe

```singularity
Bootstrap: shub
#### Download base image from singularity hub
From: ast0815/t2k-base:latest

%post
  V='2.58.x'
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

