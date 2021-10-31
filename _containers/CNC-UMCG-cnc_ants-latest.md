---
id: 2313
name: "CNC-UMCG/cnc_ants"
branch: "master"
tag: "latest"
commit: "104c31dac13548d86a921f5394625a5c963551ad"
version: "91fa458d0496a7e7e7d8e3e1f71a044b"
build_date: "2018-03-29T09:26:06.160Z"
size_mb: 5075
size: 2042785823
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_ants/latest/2018-03-29-104c31da-91fa458d/91fa458d0496a7e7e7d8e3e1f71a044b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CNC-UMCG/cnc_ants/latest/2018-03-29-104c31da-91fa458d/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_ants/latest/2018-03-29-104c31da-91fa458d/Singularity
collection: CNC-UMCG/cnc_ants
---

# CNC-UMCG/cnc_ants:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_ants:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: CNC-UMCG/cnc_spm-fsl

%environment


%post
   apt-get install -y libstdc++6
   apt-get install -y ants
```

## Collection

 - Name: [CNC-UMCG/cnc_ants](https://github.com/CNC-UMCG/cnc_ants)
 - License: None

