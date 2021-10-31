---
id: 15812
name: "romxero/openfoam8_singularity"
branch: "main"
tag: "latest"
commit: "bf2aa41b9b42829b240228397755f3302f3633eb"
version: "ac48dd05ab4a987101c04d72892c28786f4c0109313a29df114af6a9423d3dd5"
build_date: "2021-04-02T17:58:24.274Z"
size_mb: 683.73046875
size: 716943360
sif: "https://datasets.datalad.org/shub/romxero/openfoam8_singularity/latest/2021-04-02-bf2aa41b-ac48dd05/ac48dd05ab4a987101c04d72892c28786f4c0109313a29df114af6a9423d3dd5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/openfoam8_singularity/latest/2021-04-02-bf2aa41b-ac48dd05/
recipe: https://datasets.datalad.org/shub/romxero/openfoam8_singularity/latest/2021-04-02-bf2aa41b-ac48dd05/Singularity
collection: romxero/openfoam8_singularity
---

# romxero/openfoam8_singularity:latest

```bash
$ singularity pull shub://romxero/openfoam8_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: openfoam/openfoam8-paraview56
%labels
Author "Randall Cab White - rcwhite@stanford.edu"


#########
#%setup
#########

#Downlaod packages
%post

%environment
export IMAGE_NAME="openfoam8"
export FOAM_INST_DIR=/opt
export WM_PROJECT_INST_DIR=$FOAM_INST_DIR
export WM_PROJECT_DIR=$WM_PROJECT_INST_DIR/openfoam8
. /opt/openfoam8/etc/bashrc
export PATH=/opt/ThirdParty-8/platforms/linux64Gcc/gperftools-svn/bin:/opt/paraviewopenfoam56/bin:/opt/site/8/platforms/linux64GccDPInt32Opt/bin:/opt/openfoam8/platforms/linux64GccDPInt32Opt/bin:/opt/openfoam8/bin:/opt/openfoam8/wmake:$PATH
export LD_LIBRARY_PATH=/opt/ThirdParty-8/platforms/linux64Gcc/gperftools-svn/lib:/opt/openfoam8/platforms/linux64GccDPInt32Opt/lib/paraview-5.6:/opt/paraviewopenfoam56/lib:/opt/openfoam8/platforms/linux64GccDPInt32Opt/lib/openmpi-system:/opt/ThirdParty-8/platforms/linux64GccDPInt32/lib/openmpi-system:/usr/lib/x86_64-linux-gnu/openmpi/lib:/opt/site/8/platforms/linux64GccDPInt32Opt/lib:/opt/openfoam8/platforms/linux64GccDPInt32Opt/lib:/opt/ThirdParty-8/platforms/linux64GccDPInt32/lib:/opt/openfoam8/platforms/linux64GccDPInt32Opt/lib/dummy:$LD_LIBRARY_PATH
%runscript
```

## Collection

 - Name: [romxero/openfoam8_singularity](https://github.com/romxero/openfoam8_singularity)
 - License: None

