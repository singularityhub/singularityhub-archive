---
id: 2911
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.1e"
commit: "3f724d5ebda37be2de287dee1bd4d5f57c1e3f0a"
version: "0208a0326f069243db023fc8ab2c55d4"
build_date: "2018-05-24T02:36:21.718Z"
size_mb: 4056
size: 1890566175
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1e/2018-05-24-3f724d5e-0208a032/0208a0326f069243db023fc8ab2c55d4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/prepT2space/v0.0.1e/2018-05-24-3f724d5e-0208a032/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1e/2018-05-24-3f724d5e-0208a032/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.1e

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.1e
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: khanlab/neuroglia-core-minc:v1.0.0


#########
%setup
#########
mkdir $SINGULARITY_ROOTFS/src
cp -Rv . $SINGULARITY_ROOTFS/src

#########
%post
#########
mkdir -p /opt/custom-templates
curl -L --retry 5 https://www.dropbox.com/s/zi4tidxnvhqa3w4/agile12i4_T2_space-0.3mm.nii.gz  -o /opt/custom-templates/agile12i4_T2_space-0.3mm.nii.gz

#########
%environment

%runscript
/src/prepT2space $@
```

## Collection

 - Name: [khanlab/prepT2space](https://github.com/khanlab/prepT2space)
 - License: None

