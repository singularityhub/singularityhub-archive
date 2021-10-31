---
id: 4586
name: "BFL-lab/Mfannot"
branch: "master"
tag: "v1.0"
commit: "6472b973dcb814dfb9070e12b69c1277ad944766"
version: "379e7c764e3af3cd29f97acca1450c47"
build_date: "2019-03-19T15:51:57.344Z"
size_mb: 1439
size: 421740575
sif: "https://datasets.datalad.org/shub/BFL-lab/Mfannot/v1.0/2019-03-19-6472b973-379e7c76/379e7c764e3af3cd29f97acca1450c47.simg"
url: https://datasets.datalad.org/shub/BFL-lab/Mfannot/v1.0/2019-03-19-6472b973-379e7c76/
recipe: https://datasets.datalad.org/shub/BFL-lab/Mfannot/v1.0/2019-03-19-6472b973-379e7c76/Singularity
collection: BFL-lab/Mfannot
---

# BFL-lab/Mfannot:v1.0

```bash
$ singularity pull shub://BFL-lab/Mfannot:v1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nbeck/mfannot

%help
You are in the MFannot container. To see help run
singularity exec mfannot.simg -h

%labels
Author natabeck@gmail.com
Vendor Ubuntu
Version v1.0

%post
echo "For more information on MFannot, go to:"
echo "https://github.com/BFL-lab/Mfannot"
```

## Collection

 - Name: [BFL-lab/Mfannot](https://github.com/BFL-lab/Mfannot)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

