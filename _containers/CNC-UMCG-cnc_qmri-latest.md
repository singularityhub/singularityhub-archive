---
id: 2278
name: "CNC-UMCG/cnc_qmri"
branch: "master"
tag: "latest"
commit: "9e58ad35e5501e39efa9d51dd5ed2cddd0475dd5"
version: "9b65a9998c52935710b2c2ea78be3bf6"
build_date: "2018-03-29T09:26:05.819Z"
size_mb: 5184
size: 2155589663
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_qmri/latest/2018-03-29-9e58ad35-9b65a999/9b65a9998c52935710b2c2ea78be3bf6.simg"
url: https://datasets.datalad.org/shub/CNC-UMCG/cnc_qmri/latest/2018-03-29-9e58ad35-9b65a999/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_qmri/latest/2018-03-29-9e58ad35-9b65a999/Singularity
collection: CNC-UMCG/cnc_qmri
---

# CNC-UMCG/cnc_qmri:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_qmri:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: CNC-UMCG/cnc_spm-fsl

%environment


%post
    apt-get install -y ants
    
    #############################
    # mrQ package
    #############################
    
    git clone https://github.com/mezera/mrQ.git
```

## Collection

 - Name: [CNC-UMCG/cnc_qmri](https://github.com/CNC-UMCG/cnc_qmri)
 - License: [GNU Lesser General Public License v2.1](https://api.github.com/licenses/lgpl-2.1)

