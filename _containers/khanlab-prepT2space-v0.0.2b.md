---
id: 3107
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.2b"
commit: "4b39268c8bfcd00a574e092af227e41e6bfe8f87"
version: "c3639f0feec5daf719d85ca68e0a00bf"
build_date: "2020-06-05T15:26:31.750Z"
size_mb: 4245
size: 2089279519
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.2b/2020-06-05-4b39268c-c3639f0f/c3639f0feec5daf719d85ca68e0a00bf.simg"
url: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.2b/2020-06-05-4b39268c-c3639f0f/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.2b/2020-06-05-4b39268c-c3639f0f/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.2b

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.2b
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

