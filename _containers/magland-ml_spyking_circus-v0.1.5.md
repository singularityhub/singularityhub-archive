---
id: 4726
name: "magland/ml_spyking_circus"
branch: "master"
tag: "v0.1.5"
commit: "1116d21b7803057306888fa2713e4d761bc94d37"
version: "3097572d7e0618203f52bf26af0e367f"
build_date: "2018-09-08T21:55:12.947Z"
size_mb: 1111
size: 425373727
sif: "https://datasets.datalad.org/shub/magland/ml_spyking_circus/v0.1.5/2018-09-08-1116d21b-3097572d/3097572d7e0618203f52bf26af0e367f.simg"
url: https://datasets.datalad.org/shub/magland/ml_spyking_circus/v0.1.5/2018-09-08-1116d21b-3097572d/
recipe: https://datasets.datalad.org/shub/magland/ml_spyking_circus/v0.1.5/2018-09-08-1116d21b-3097572d/Singularity
collection: magland/ml_spyking_circus
---

# magland/ml_spyking_circus:v0.1.5

```bash
$ singularity pull shub://magland/ml_spyking_circus:v0.1.5
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

