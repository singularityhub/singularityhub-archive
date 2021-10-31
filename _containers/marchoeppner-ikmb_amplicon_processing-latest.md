---
id: 11857
name: "marchoeppner/ikmb_amplicon_processing"
branch: "master"
tag: "latest"
commit: "30a43651e3cdf50076256f405dd672e315b11e13"
version: "0aca19b7959f595814f0b3e71c7507616f9b6a13bd094d7a8485c383058b8287"
build_date: "2020-10-26T16:23:52.697Z"
size_mb: 749.30078125
size: 785698816
sif: "https://datasets.datalad.org/shub/marchoeppner/ikmb_amplicon_processing/latest/2020-10-26-30a43651-0aca19b7/0aca19b7959f595814f0b3e71c7507616f9b6a13bd094d7a8485c383058b8287.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/marchoeppner/ikmb_amplicon_processing/latest/2020-10-26-30a43651-0aca19b7/
recipe: https://datasets.datalad.org/shub/marchoeppner/ikmb_amplicon_processing/latest/2020-10-26-30a43651-0aca19b7/Singularity
collection: marchoeppner/ikmb_amplicon_processing
---

# marchoeppner/ikmb_amplicon_processing:latest

```bash
$ singularity pull shub://marchoeppner/ikmb_amplicon_processing:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:nfcore/base

%labels
    MAINTAINER Marc Hoeppner <m.hoeppner@ikmb.uni-kiel.de>
    DESCRIPTION Singularity image containing all requirements for the amplicon pipeline
    VERSION 1.0

%environment
    PATH=/opt/conda/envs/ikmb-amplicon-1.0/bin:/opt:$PATH
    export PATH

%files
    environment.yml /
    bin/dada2_16S_workflow.R /opt
    bin/dada2_16S_workflow_with_AR.R /opt
    bin/dada2_archaea_workflow.R /opt
    bin/dada2_fungi_workflow.R /opt
    bin/make_dada2_project.R /opt

    assets/rdp_species_assignment_16.fa.gz /opt 
    assets/RDP_v16-mod_March2018.RData /opt
    assets/sh_general_release_dynamic_10.10.2017_dev.fasta /opt
    assets/rdp_train_set_16.fa.gz /opt
    assets/sh_general_release_dynamic_02.02.2019.fasta /opt
    assets/silva_species_assignment_v132.fa.gz /opt
    assets/silva_nr_v132_train_set.fa.gz /opt

%post

    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

    mkdir -p /ifs
    apt-get -y install procps

    cd /opt
    chmod +x *.R
```

## Collection

 - Name: [marchoeppner/ikmb_amplicon_processing](https://github.com/marchoeppner/ikmb_amplicon_processing)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

