---
id: 3888
name: "cottersci/DIRT2_Workflows"
branch: "init"
tag: "dirt2d"
commit: "516fc04f967dfc27afb3731635dae3889ad24a8b"
version: "63411fb32e5a8ead769b412b8b48bc2e"
build_date: "2020-05-27T04:25:53.306Z"
size_mb: 1534
size: 606072863
sif: "https://datasets.datalad.org/shub/cottersci/DIRT2_Workflows/dirt2d/2020-05-27-516fc04f-63411fb3/63411fb32e5a8ead769b412b8b48bc2e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cottersci/DIRT2_Workflows/dirt2d/2020-05-27-516fc04f-63411fb3/
recipe: https://datasets.datalad.org/shub/cottersci/DIRT2_Workflows/dirt2d/2020-05-27-516fc04f-63411fb3/Singularity
collection: cottersci/DIRT2_Workflows
---

# cottersci/DIRT2_Workflows:dirt2d

```bash
$ singularity pull shub://cottersci/DIRT2_Workflows:dirt2d
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: Computational-Plant-Science/DIRT

%labels
  Maintainer Chris Cotter (cotter@uga.edu)
  Version v0.0

%setup
  mkdir -p ${SINGULARITY_ROOTFS}/workflow

%files
  dirt2D.nf /workflow/

%post
  #By default, nextflow writes cache and framework files to ~/.nextflow.
  # this variable is set to move that
  export NXF_HOME="/opt/.nextflow"

  apt-get update
  apt-get -y install openjdk-8-jre-headless wget

  cd /bin
  wget -qO- https://get.nextflow.io | bash
  chmod a+rx nextflow
  ./nextflow #Run nextflow to download and install remaining dependencies.
  chmod -R a+rwx $NXF_HOME

  apt-get -y install python3 python3-pip
  pip3 install git+https://github.com/cottersci/dirtweb_api.git#egg=dirtweb_api

  #cleanup
  apt-get purge
  apt-get clean

%environment
  export NXF_HOME="/opt/.nextflow"

%runscript
  /bin/nextflow run /workflow/dirt2D.nf  "$@"
```

## Collection

 - Name: [cottersci/DIRT2_Workflows](https://github.com/cottersci/DIRT2_Workflows)
 - License: None

