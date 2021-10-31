---
id: 3880
name: "IARCbioinfo/template-nf"
branch: "master"
tag: "latest"
commit: "6e61362f401117e0fa25f48ef301706d1ad8700a"
version: "f3fe934bba0accbcd1d7638f1c1d8d0c"
build_date: "2018-12-19T12:57:36.126Z"
size_mb: 657
size: 228634655
sif: "https://datasets.datalad.org/shub/IARCbioinfo/template-nf/latest/2018-12-19-6e61362f-f3fe934b/f3fe934bba0accbcd1d7638f1c1d8d0c.simg"
url: https://datasets.datalad.org/shub/IARCbioinfo/template-nf/latest/2018-12-19-6e61362f-f3fe934b/
recipe: https://datasets.datalad.org/shub/IARCbioinfo/template-nf/latest/2018-12-19-6e61362f-f3fe934b/Singularity
collection: IARCbioinfo/template-nf
---

# IARCbioinfo/template-nf:latest

```bash
$ singularity pull shub://IARCbioinfo/template-nf:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER **username** <**usermail**>
    DESCRIPTION Container image containing all requirements for **name of the pipeline**
    VERSION 1.0

%files
    environment.yml /

%post
    /opt/conda/bin/conda env update -n root -f /environment.yml
    /opt/conda/bin/conda clean -a






# environment.yml commit ID: c92804b
```

## Collection

 - Name: [IARCbioinfo/template-nf](https://github.com/IARCbioinfo/template-nf)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

