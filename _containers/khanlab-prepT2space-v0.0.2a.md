---
id: 3082
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.2a"
commit: "199c2018c122d48d45183e87aeb4fafdc725c9e5"
version: "39c1154cd50fe18ccbf4a4400b967ee4"
build_date: "2018-06-08T05:56:43.012Z"
size_mb: 4245
size: 2089279519
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.2a/2018-06-08-199c2018-39c1154c/39c1154cd50fe18ccbf4a4400b967ee4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/prepT2space/v0.0.2a/2018-06-08-199c2018-39c1154c/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.2a/2018-06-08-199c2018-39c1154c/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.2a

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.2a
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

