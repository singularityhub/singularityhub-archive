---
id: 9182
name: "rgrandin/Singularity-QGIS"
branch: "master"
tag: "fedora29"
commit: "42c20da5d7a218fe2f177f417d83be22f971f19a"
version: "0fdf3011fc2b540381cefc3511404edf"
build_date: "2019-11-13T15:20:29.066Z"
size_mb: 1605
size: 611463199
sif: "https://datasets.datalad.org/shub/rgrandin/Singularity-QGIS/fedora29/2019-11-13-42c20da5-0fdf3011/0fdf3011fc2b540381cefc3511404edf.simg"
url: https://datasets.datalad.org/shub/rgrandin/Singularity-QGIS/fedora29/2019-11-13-42c20da5-0fdf3011/
recipe: https://datasets.datalad.org/shub/rgrandin/Singularity-QGIS/fedora29/2019-11-13-42c20da5-0fdf3011/Singularity
collection: rgrandin/Singularity-QGIS
---

# rgrandin/Singularity-QGIS:fedora29

```bash
$ singularity pull shub://rgrandin/Singularity-QGIS:fedora29
```

## Singularity Recipe

```singularity
BootStrap: docker 
From: fedora:29


%runscript
    exec qgis


%post
    dnf install -y qgis qgis-python qgis-grass qgis-server
```

## Collection

 - Name: [rgrandin/Singularity-QGIS](https://github.com/rgrandin/Singularity-QGIS)
 - License: None

