---
id: 2247
name: "CNC-UMCG/cnc_spm-fsl"
branch: "master"
tag: "latest"
commit: "aa596206b069778d42f35916fe60abd5633655fb"
version: "a73a19b6987c710def3b7273472c3492"
build_date: "2018-03-22T17:14:48.708Z"
size_mb: 4671
size: 1952059423
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_spm-fsl/latest/2018-03-22-aa596206-a73a19b6/a73a19b6987c710def3b7273472c3492.simg"
url: https://datasets.datalad.org/shub/CNC-UMCG/cnc_spm-fsl/latest/2018-03-22-aa596206-a73a19b6/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_spm-fsl/latest/2018-03-22-aa596206-a73a19b6/Singularity
collection: CNC-UMCG/cnc_spm-fsl
---

# CNC-UMCG/cnc_spm-fsl:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_spm-fsl:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: CNC-UMCG/cnc_spm


% post
apt-get install -y fsl fsl-5.0-core fsleyes
```

## Collection

 - Name: [CNC-UMCG/cnc_spm-fsl](https://github.com/CNC-UMCG/cnc_spm-fsl)
 - License: None

