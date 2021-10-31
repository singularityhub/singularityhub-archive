---
id: 2246
name: "CNC-UMCG/cnc_fsl"
branch: "master"
tag: "latest"
commit: "55dd92209aba8dcf85cd43b1138d3b7851b0b2fe"
version: "0d2407b6e2dd5c565b02ab94f8ce4dd3"
build_date: "2020-08-15T06:17:17.112Z"
size_mb: 2137
size: 658755615
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_fsl/latest/2020-08-15-55dd9220-0d2407b6/0d2407b6e2dd5c565b02ab94f8ce4dd3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CNC-UMCG/cnc_fsl/latest/2020-08-15-55dd9220-0d2407b6/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_fsl/latest/2020-08-15-55dd9220-0d2407b6/Singularity
collection: CNC-UMCG/cnc_fsl
---

# CNC-UMCG/cnc_fsl:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_fsl:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: CNC-UMCG/cnc_base


%post

apt-get install -y fsl fsl-5.0-core fsleyes
```

## Collection

 - Name: [CNC-UMCG/cnc_fsl](https://github.com/CNC-UMCG/cnc_fsl)
 - License: [GNU General Public License v2.0](https://api.github.com/licenses/gpl-2.0)

