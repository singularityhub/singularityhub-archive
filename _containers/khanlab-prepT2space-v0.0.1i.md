---
id: 3079
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.1i"
commit: "59424a143afd038721760abee0fa61475d060e13"
version: "9e824e54f11f34761b2388a03607d9fb"
build_date: "2018-06-11T18:30:26.477Z"
size_mb: 4245
size: 2089279519
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1i/2018-06-11-59424a14-9e824e54/9e824e54f11f34761b2388a03607d9fb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/prepT2space/v0.0.1i/2018-06-11-59424a14-9e824e54/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1i/2018-06-11-59424a14-9e824e54/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.1i

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.1i
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

