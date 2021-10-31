---
id: 5275
name: "IARCbioinfo/qualimap-nf"
branch: "master"
tag: "latest"
commit: "f1055316535f837e9eaec110f9f31a291640fc20"
version: "b3d13256e3a0111163b78e6f8d16371f"
build_date: "2018-10-25T18:55:05.207Z"
size_mb: 2694
size: 870916127
sif: "https://datasets.datalad.org/shub/IARCbioinfo/qualimap-nf/latest/2018-10-25-f1055316-b3d13256/b3d13256e3a0111163b78e6f8d16371f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/IARCbioinfo/qualimap-nf/latest/2018-10-25-f1055316-b3d13256/
recipe: https://datasets.datalad.org/shub/IARCbioinfo/qualimap-nf/latest/2018-10-25-f1055316-b3d13256/Singularity
collection: IARCbioinfo/Qualimap-nf
---

# IARCbioinfo/qualimap-nf:latest

```bash
$ singularity pull shub://IARCbioinfo/qualimap-nf:latest
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









# environment.yml commit ID: d93b0a3
```

## Collection

 - Name: [IARCbioinfo/qualimap-nf](https://github.com/IARCbioinfo/qualimap-nf)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

