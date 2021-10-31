---
id: 3974
name: "IARCbioinfo/platypus-nf"
branch: "master"
tag: "latest"
commit: "ccb7ad951204e0c384fc9fd20e9475755ed57c15"
version: "2284957f7e9b0d31e3acff6d64c7e9ad"
build_date: "2019-05-07T14:45:45.915Z"
size_mb: 667
size: 217423903
sif: "https://datasets.datalad.org/shub/IARCbioinfo/platypus-nf/latest/2019-05-07-ccb7ad95-2284957f/2284957f7e9b0d31e3acff6d64c7e9ad.simg"
url: https://datasets.datalad.org/shub/IARCbioinfo/platypus-nf/latest/2019-05-07-ccb7ad95-2284957f/
recipe: https://datasets.datalad.org/shub/IARCbioinfo/platypus-nf/latest/2019-05-07-ccb7ad95-2284957f/Singularity
collection: IARCbioinfo/platypus-nf
---

# IARCbioinfo/platypus-nf:latest

```bash
$ singularity pull shub://IARCbioinfo/platypus-nf:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Tiffany Delhomme <delhommet@students.iarc.fr>
    DESCRIPTION Container image containing requirements for iarcbioinfo/platypus-nf pipeline
    VERSION 1.0

%files
        environment.yml /

%post
        /opt/conda/bin/conda env update -n root -f /environment.yml
        /opt/conda/bin/conda clean -a








# environment.yml commit ID: 0818bf2
```

## Collection

 - Name: [IARCbioinfo/platypus-nf](https://github.com/IARCbioinfo/platypus-nf)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

