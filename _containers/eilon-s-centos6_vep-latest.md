---
id: 2771
name: "eilon-s/centos6_vep"
branch: "master"
tag: "latest"
commit: "ddb130ab869066051c2e5c3a41f89ec0191160b2"
version: "8af692060443e6c221ed69e92c2544ba"
build_date: "2018-05-13T10:34:44.154Z"
size_mb: 1637
size: 620933151
sif: "https://datasets.datalad.org/shub/eilon-s/centos6_vep/latest/2018-05-13-ddb130ab-8af69206/8af692060443e6c221ed69e92c2544ba.simg"
url: https://datasets.datalad.org/shub/eilon-s/centos6_vep/latest/2018-05-13-ddb130ab-8af69206/
recipe: https://datasets.datalad.org/shub/eilon-s/centos6_vep/latest/2018-05-13-ddb130ab-8af69206/Singularity
collection: eilon-s/centos6_vep
---

# eilon-s/centos6_vep:latest

```bash
$ singularity pull shub://eilon-s/centos6_vep:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: willmclaren/ensembl-vep

# sudo singularity build ensembl-vep Singularity

%help
	This is a singularity file for VEP docker.
	run example: singularity run --bind $PWD:$PWD ensembl-vep -i ./inputfilename.vcf -o ./outputfilename --cache --assembly GRCh37 --dir_cache /opt/vep/.vep --dir_plugins /opt/vep/.plugins --offline --format vcf --vcf --symbol --plugin Downstream --plugin Wildtype --terms SO

%environment
    LANGUAGE=en_US
    LANG="en_US.UTF-8"
    LC_ALL=C
    export LANGUAGE LANG LC_ALL

%post
    
    mkdir -p /opt/vep/.vep;
    # install data for yeast BY
    #perl /opt/vep/src/ensembl-vep/INSTALL.pl -a acf -s Saccharomyces_cerevisiae -y R64-1-1 -c /opt/vep/.vep;
    # install data for human hg19
    #perl /opt/vep/src/ensembl-vep/INSTALL.pl -a acf -s homo_sapiens -y GRCh37 -c /opt/vep/.vep
    
    # get plugins
    #rm -fr /opt/vep/.plugins;
    mkdir -p /opt/vep/.plugins;
    
    rm -f -r /VEP_plugins;
    git clone https://github.com/Ensembl/VEP_plugins.git;
    cp -r -f /VEP_plugins/* /opt/vep/.plugins;
    rm -f -r /VEP_plugins;
    
    # get pVACseq plugin
    rm -f -r /pVAC-Seq;
    git clone https://github.com/griffithlab/pVAC-Seq.git;
    cp -f /pVAC-Seq/pvacseq/VEP_plugins/Wildtype.pm /opt/vep/.plugins;
    rm -f -r /pVAC-Seq;
    
%runscript
    exec /opt/vep/src/ensembl-vep/vep "$@"

%apprun vep
	exec /opt/vep/src/ensembl-vep/vep "$@"

%apprun install_vep
	exec perl /opt/vep/src/ensembl-vep/INSTALL.pl "$@"
```

## Collection

 - Name: [eilon-s/centos6_vep](https://github.com/eilon-s/centos6_vep)
 - License: None

