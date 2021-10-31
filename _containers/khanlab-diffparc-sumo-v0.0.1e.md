---
id: 4722
name: "khanlab/diffparc-sumo"
branch: "master"
tag: "v0.0.1e"
commit: "5a6dbb1d95cd916068ade55ec7ecd7e095123e91"
version: "99f6840d75885d73a97c7bf82b156d87"
build_date: "2018-10-16T23:20:45.484Z"
size_mb: 11332
size: 5172973599
sif: "https://datasets.datalad.org/shub/khanlab/diffparc-sumo/v0.0.1e/2018-10-16-5a6dbb1d-99f6840d/99f6840d75885d73a97c7bf82b156d87.simg"
url: https://datasets.datalad.org/shub/khanlab/diffparc-sumo/v0.0.1e/2018-10-16-5a6dbb1d-99f6840d/
recipe: https://datasets.datalad.org/shub/khanlab/diffparc-sumo/v0.0.1e/2018-10-16-5a6dbb1d-99f6840d/Singularity
collection: khanlab/diffparc-sumo
---

# khanlab/diffparc-sumo:v0.0.1e

```bash
$ singularity pull shub://khanlab/diffparc-sumo:v0.0.1e
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: akhanf/vasst-dev:v0.0.4e


#########
%setup
#########
mkdir $SINGULARITY_ROOTFS/diffparcellate
cp -Rv . $SINGULARITY_ROOTFS/diffparcellate


cp -v matlab/*.m $SINGULARITY_ROOTFS/opt/vasst-dev/tools/matlab
cp -v processBedpostParcellateSeedfromPrepDWI $SINGULARITY_ROOTFS/opt/vasst-dev/pipeline/dwi
cp -v deps/mris_convert $SINGULARITY_ROOTFS/opt/freesurfer_minimal/bin

#remove older compiled version, superceded by script in matlab folder..
rm -vf $SINGULARITY_ROOTFS/opt/vasst-dev/mcr/v92/genBYUtoNiftiTransformFromCroppedAnalyze



%runscript
exec /diffparcellate/run.sh $@
```

## Collection

 - Name: [khanlab/diffparc-sumo](https://github.com/khanlab/diffparc-sumo)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

