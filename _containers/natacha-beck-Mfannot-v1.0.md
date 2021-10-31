---
id: 2413
name: "natacha-beck/Mfannot"
branch: "master"
tag: "v1.0"
commit: "49d263320266d6239fdd8032447bbb7096db5ccb"
version: "99beccfae12fe46b5d4d3d8a61f503ad"
build_date: "2019-10-25T12:50:03.997Z"
size_mb: 1462
size: 425783327
sif: "https://datasets.datalad.org/shub/natacha-beck/Mfannot/v1.0/2019-10-25-49d26332-99beccfa/99beccfae12fe46b5d4d3d8a61f503ad.simg"
url: https://datasets.datalad.org/shub/natacha-beck/Mfannot/v1.0/2019-10-25-49d26332-99beccfa/
recipe: https://datasets.datalad.org/shub/natacha-beck/Mfannot/v1.0/2019-10-25-49d26332-99beccfa/Singularity
collection: natacha-beck/Mfannot
---

# natacha-beck/Mfannot:v1.0

```bash
$ singularity pull shub://natacha-beck/Mfannot:v1.0
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

 - Name: [natacha-beck/Mfannot](https://github.com/natacha-beck/Mfannot)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

