---
id: 5591
name: "khanlab/diffparc-sumo"
branch: "master"
tag: "v0.0.1g"
commit: "a7b99cccdcf5fdb16bbbe876aba5725b6d67d157"
version: "ccedd416b262e2a5d526bfbf2ed9e583"
build_date: "2018-11-13T19:58:13.646Z"
size_mb: 11332
size: 5172977695
sif: "https://datasets.datalad.org/shub/khanlab/diffparc-sumo/v0.0.1g/2018-11-13-a7b99ccc-ccedd416/ccedd416b262e2a5d526bfbf2ed9e583.simg"
url: https://datasets.datalad.org/shub/khanlab/diffparc-sumo/v0.0.1g/2018-11-13-a7b99ccc-ccedd416/
recipe: https://datasets.datalad.org/shub/khanlab/diffparc-sumo/v0.0.1g/2018-11-13-a7b99ccc-ccedd416/Singularity
collection: khanlab/diffparc-sumo
---

# khanlab/diffparc-sumo:v0.0.1g

```bash
$ singularity pull shub://khanlab/diffparc-sumo:v0.0.1g
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

