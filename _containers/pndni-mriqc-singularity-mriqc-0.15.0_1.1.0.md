---
id: 8717
name: "pndni/mriqc-singularity"
branch: "master"
tag: "mriqc-0.15.0_1.1.0"
commit: "5df9b433f5cf8000e0be40b2dc7b386874c85435"
version: "c17884ed650f1fa22c0888f59cbda156"
build_date: "2019-04-30T08:10:39.705Z"
size_mb: 7589
size: 2928963615
sif: "https://datasets.datalad.org/shub/pndni/mriqc-singularity/mriqc-0.15.0_1.1.0/2019-04-30-5df9b433-c17884ed/c17884ed650f1fa22c0888f59cbda156.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/mriqc-singularity/mriqc-0.15.0_1.1.0/2019-04-30-5df9b433-c17884ed/
recipe: https://datasets.datalad.org/shub/pndni/mriqc-singularity/mriqc-0.15.0_1.1.0/2019-04-30-5df9b433-c17884ed/Singularity
collection: pndni/mriqc-singularity
---

# pndni/mriqc-singularity:mriqc-0.15.0_1.1.0

```bash
$ singularity pull shub://pndni/mriqc-singularity:mriqc-0.15.0_1.1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: poldracklab/mriqc:0.15.0

%post
    mkdir /data
    mkdir /out
    mkdir /work_dir
```

## Collection

 - Name: [pndni/mriqc-singularity](https://github.com/pndni/mriqc-singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

