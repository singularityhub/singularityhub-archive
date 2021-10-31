---
id: 13112
name: "chenchen2015/Ergodic-Information-Harvesting-Staging"
branch: "master"
tag: "latest"
commit: "2a58fa6f25c28ba843950e99f09d4c37449bf724"
version: "2d689663f0f3081dbb2c64f12e56a2568e5a9778459140bc3a59555b186b1924"
build_date: "2020-06-07T22:31:14.462Z"
size_mb: 264.4140625
size: 277258240
sif: "https://datasets.datalad.org/shub/chenchen2015/Ergodic-Information-Harvesting-Staging/latest/2020-06-07-2a58fa6f-2d689663/2d689663f0f3081dbb2c64f12e56a2568e5a9778459140bc3a59555b186b1924.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/chenchen2015/Ergodic-Information-Harvesting-Staging/latest/2020-06-07-2a58fa6f-2d689663/
recipe: https://datasets.datalad.org/shub/chenchen2015/Ergodic-Information-Harvesting-Staging/latest/2020-06-07-2a58fa6f-2d689663/Singularity
collection: chenchen2015/Ergodic-Information-Harvesting-Staging
---

# chenchen2015/Ergodic-Information-Harvesting-Staging:latest

```bash
$ singularity pull shub://chenchen2015/Ergodic-Information-Harvesting-Staging:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: slayerchen/eih_staging:latest

%help
    This is a Singularity container for EIH simulations.
    It builds a minimal Python 3 environment running on Linux with all the libraries required for EIH simulations.

%labels
    Maintainer Chen Chen (chenchen.bme@gmail.com)
    Version v0.4
   
%environment
     conda=/opt/conda/bin/conda
     pip=/opt/conda/bin/pip
     python3=/opt/conda/bin/python
     python=python3
     export conda pip python3 python

%post 
     # create bind points for HPCC environment
     mkdir -p /EIH

%test  
     echo "Testing python..."
     /opt/conda/bin/python -V
```

## Collection

 - Name: [chenchen2015/Ergodic-Information-Harvesting-Staging](https://github.com/chenchen2015/Ergodic-Information-Harvesting-Staging)
 - License: [MIT License](https://api.github.com/licenses/mit)

