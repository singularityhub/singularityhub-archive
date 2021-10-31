---
id: 2928
name: "khanlab/prepT2space"
branch: "master"
tag: "v0.0.1f"
commit: "6387d99563253c8ffe726f5b310980a58b102cad"
version: "84baeec8413eaea6861e0b4fc8fcd821"
build_date: "2018-05-25T13:57:38.087Z"
size_mb: 4056
size: 1890566175
sif: "https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1f/2018-05-25-6387d995-84baeec8/84baeec8413eaea6861e0b4fc8fcd821.simg"
url: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1f/2018-05-25-6387d995-84baeec8/
recipe: https://datasets.datalad.org/shub/khanlab/prepT2space/v0.0.1f/2018-05-25-6387d995-84baeec8/Singularity
collection: khanlab/prepT2space
---

# khanlab/prepT2space:v0.0.1f

```bash
$ singularity pull shub://khanlab/prepT2space:v0.0.1f
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

