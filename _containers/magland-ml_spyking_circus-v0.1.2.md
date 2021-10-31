---
id: 4701
name: "magland/ml_spyking_circus"
branch: "master"
tag: "v0.1.2"
commit: "9d381f888b163274730d07b85e535b99b271439a"
version: "20322b8568bd33f76335621642797ec6"
build_date: "2018-09-07T14:07:17.406Z"
size_mb: 1110
size: 425283615
sif: "https://datasets.datalad.org/shub/magland/ml_spyking_circus/v0.1.2/2018-09-07-9d381f88-20322b85/20322b8568bd33f76335621642797ec6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/magland/ml_spyking_circus/v0.1.2/2018-09-07-9d381f88-20322b85/
recipe: https://datasets.datalad.org/shub/magland/ml_spyking_circus/v0.1.2/2018-09-07-9d381f88-20322b85/Singularity
collection: magland/ml_spyking_circus
---

# magland/ml_spyking_circus:v0.1.2

```bash
$ singularity pull shub://magland/ml_spyking_circus:v0.1.2
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

