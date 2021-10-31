---
id: 3004
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.1g"
commit: "2cf95e274a7614fc8c6a177cf178742ba7645254"
version: "ae417b3930a549024314ca512d75b6dc"
build_date: "2018-06-01T09:59:29.467Z"
size_mb: 4056
size: 1890566175
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1g/2018-06-01-2cf95e27-ae417b39/ae417b3930a549024314ca512d75b6dc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/prepT2space/v0.0.1g/2018-06-01-2cf95e27-ae417b39/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1g/2018-06-01-2cf95e27-ae417b39/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.1g

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.1g
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

