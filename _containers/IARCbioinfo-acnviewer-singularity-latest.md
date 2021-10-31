---
id: 10299
name: "IARCbioinfo/acnviewer-singularity"
branch: "master"
tag: "latest"
commit: "97b1f28a7568e30b372e496e3e2facee140d32cf"
version: "83f69e52a0d874b8b3534c749252bb22"
build_date: "2020-11-05T08:52:30.717Z"
size_mb: 13722.0
size: 5311078431
sif: "https://datasets.datalad.org/shub/IARCbioinfo/acnviewer-singularity/latest/2020-11-05-97b1f28a-83f69e52/83f69e52a0d874b8b3534c749252bb22.sif"
url: https://datasets.datalad.org/shub/IARCbioinfo/acnviewer-singularity/latest/2020-11-05-97b1f28a-83f69e52/
recipe: https://datasets.datalad.org/shub/IARCbioinfo/acnviewer-singularity/latest/2020-11-05-97b1f28a-83f69e52/Singularity
collection: IARCbioinfo/acnviewer-singularity
---

# IARCbioinfo/acnviewer-singularity:latest

```bash
$ singularity pull shub://IARCbioinfo/acnviewer-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fjdceph/acnviewer
%post
    chmod -R o=u /data/
```

## Collection

 - Name: [IARCbioinfo/acnviewer-singularity](https://github.com/IARCbioinfo/acnviewer-singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

