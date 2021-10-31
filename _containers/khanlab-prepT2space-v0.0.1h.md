---
id: 3041
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.1h"
commit: "da231ca8d544b91826d9fd6fcfb8c157752439f5"
version: "837afb4d093a502b9042c20341a1a5d0"
build_date: "2018-06-07T10:20:38.223Z"
size_mb: 4245
size: 2089275423
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1h/2018-06-07-da231ca8-837afb4d/837afb4d093a502b9042c20341a1a5d0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/prepT2space/v0.0.1h/2018-06-07-da231ca8-837afb4d/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1h/2018-06-07-da231ca8-837afb4d/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.1h

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.1h
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
curl -L --retry 5 https://www.dropbox.com/s/rfzh9qvhxeq6g3y/snsx32_v0.1_i09_avg_T2w_inm.nii.gz  -o /opt/custom-templates/snsx32_v0.1_i09_avg_T2w_inm.nii.gz
#########
%environment

%runscript
/src/prepT2space $@
```

## Collection

 - Name: [khanlab/prepT2space](https://github.com/khanlab/prepT2space)
 - License: None

