---
id: 4625
name: "IARCbioinfo/Qualimap-nf"
branch: "master"
tag: "latest"
commit: "87da027c7fafd440fe4837d06a81a65b2b8a1f1c"
version: "be1a25fd1dd330114a1ed2195a33e7ec"
build_date: "2018-10-12T16:28:13.499Z"
size_mb: 2427
size: 830570527
sif: "https://datasets.datalad.org/shub/IARCbioinfo/Qualimap-nf/latest/2018-10-12-87da027c-be1a25fd/be1a25fd1dd330114a1ed2195a33e7ec.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/IARCbioinfo/Qualimap-nf/latest/2018-10-12-87da027c-be1a25fd/
recipe: https://datasets.datalad.org/shub/IARCbioinfo/Qualimap-nf/latest/2018-10-12-87da027c-be1a25fd/Singularity
collection: IARCbioinfo/Qualimap-nf
---

# IARCbioinfo/Qualimap-nf:latest

```bash
$ singularity pull shub://IARCbioinfo/Qualimap-nf:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Tiffany Delhomme <delhommet@students.iarc.fr>
    DESCRIPTION Container image containing all requirements for qualimap-nf
    VERSION 1.0

%files
    environment.yml /

%post
    /opt/conda/bin/conda env update -n root -f /environment.yml
    /opt/conda/bin/conda clean -a

# environment.yml commit ID: 4da4ea9
```

## Collection

 - Name: [IARCbioinfo/Qualimap-nf](https://github.com/IARCbioinfo/Qualimap-nf)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

