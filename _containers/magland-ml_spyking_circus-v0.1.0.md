---
id: 4698
name: "magland/ml_spyking_circus"
branch: "master"
tag: "v0.1.0"
commit: "7994b60f5b28c8d9255987f3ae3d69971e103830"
version: "db39780a6261ea649459d80703def513"
build_date: "2018-09-07T14:07:17.415Z"
size_mb: 1110
size: 425271327
sif: "https://datasets.datalad.org/shub/magland/ml_spyking_circus/v0.1.0/2018-09-07-7994b60f-db39780a/db39780a6261ea649459d80703def513.simg"
url: https://datasets.datalad.org/shub/magland/ml_spyking_circus/v0.1.0/2018-09-07-7994b60f-db39780a/
recipe: https://datasets.datalad.org/shub/magland/ml_spyking_circus/v0.1.0/2018-09-07-7994b60f-db39780a/Singularity
collection: magland/ml_spyking_circus
---

# magland/ml_spyking_circus:v0.1.0

```bash
$ singularity pull shub://magland/ml_spyking_circus:v0.1.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
FROM: magland/mlsing

%labels
    Maintainer Jeremy Magland

%setup
  mkdir ${SINGULARITY_ROOTFS}/working
  cp -r . ${SINGULARITY_ROOTFS}/working/src

%post
  echo "################################## Activating conda environment"
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab

  echo "################################## Installing ML package"
  pip install /working/src
  ml-link-python-module ml_spyking_circus `ml-config package_directory`/ml_spyking_circus

  echo "################################## Testing package"
  ml-list-processors

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab
```

## Collection

 - Name: [magland/ml_spyking_circus](https://github.com/magland/ml_spyking_circus)
 - License: [Other](None)

