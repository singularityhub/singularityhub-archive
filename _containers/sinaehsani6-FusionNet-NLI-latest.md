---
id: 5003
name: "sinaehsani6/FusionNet-NLI"
branch: "master"
tag: "latest"
commit: "8c6807d2479137c7aa716b9e7ebea202af954b4d"
version: "d3d17188e5d7135c531d7c9d1153ecc9"
build_date: "2018-09-28T07:34:32.473Z"
size_mb: 3510
size: 1554415647
sif: "https://datasets.datalad.org/shub/sinaehsani6/FusionNet-NLI/latest/2018-09-28-8c6807d2-d3d17188/d3d17188e5d7135c531d7c9d1153ecc9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sinaehsani6/FusionNet-NLI/latest/2018-09-28-8c6807d2-d3d17188/
recipe: https://datasets.datalad.org/shub/sinaehsani6/FusionNet-NLI/latest/2018-09-28-8c6807d2-d3d17188/Singularity
collection: sinaehsani6/FusionNet-NLI
---

# sinaehsani6/FusionNet-NLI:latest

```bash
$ singularity pull shub://sinaehsani6/FusionNet-NLI:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:momohuang/fusionnet-docker

%post
mkdir -p /extra/sinaehsani
git clone https://github.com/momohuang/FusionNet-NLI.git
cd FusionNet-NLI
```

## Collection

 - Name: [sinaehsani6/FusionNet-NLI](https://github.com/sinaehsani6/FusionNet-NLI)
 - License: None

