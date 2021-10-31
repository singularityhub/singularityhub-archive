---
id: 8240
name: "BFL-lab/Mfannot"
branch: "issue_16"
tag: "v1.1"
commit: "4ba0453b2b02a004497a48d332c206ea42504232"
version: "c0fb036c2d72b6f8a808b950608f717e"
build_date: "2020-10-29T21:39:53.001Z"
size_mb: 1439
size: 421740575
sif: "https://datasets.datalad.org/shub/BFL-lab/Mfannot/v1.1/2020-10-29-4ba0453b-c0fb036c/c0fb036c2d72b6f8a808b950608f717e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/BFL-lab/Mfannot/v1.1/2020-10-29-4ba0453b-c0fb036c/
recipe: https://datasets.datalad.org/shub/BFL-lab/Mfannot/v1.1/2020-10-29-4ba0453b-c0fb036c/Singularity
collection: BFL-lab/Mfannot
---

# BFL-lab/Mfannot:v1.1

```bash
$ singularity pull shub://BFL-lab/Mfannot:v1.1
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

