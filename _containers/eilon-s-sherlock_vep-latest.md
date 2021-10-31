---
id: 2075
name: "eilon-s/sherlock_vep"
branch: "master"
tag: "latest"
commit: "69bd4e7a9fcd278546ff9daa55861cb531c9d5e4"
version: "a9932f2459a8efcf212a81f8d5557c9c"
build_date: "2021-01-19T22:24:02.715Z"
size_mb: 1621
size: 616017951
sif: "https://datasets.datalad.org/shub/eilon-s/sherlock_vep/latest/2021-01-19-69bd4e7a-a9932f24/a9932f2459a8efcf212a81f8d5557c9c.simg"
url: https://datasets.datalad.org/shub/eilon-s/sherlock_vep/latest/2021-01-19-69bd4e7a-a9932f24/
recipe: https://datasets.datalad.org/shub/eilon-s/sherlock_vep/latest/2021-01-19-69bd4e7a-a9932f24/Singularity
collection: eilon-s/sherlock_vep
---

# eilon-s/sherlock_vep:latest

```bash
$ singularity pull shub://eilon-s/sherlock_vep:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: willmclaren/ensembl-vep

# sudo singularity build ensembl-vep Singularity

%help
	This is a singularity file for VEP docker.
	run example: singularity run --bind $PWD:$PWD ensembl-vep -i ./inputfilename.vcf -o ./outputfilename --cache --assembly GRCh37 --dir_cache /home/vep/.vep --dir_plugins /home/vep/.plugins --offline --format vcf --vcf --symbol --plugin Downstream --plugin Wildtype --terms SO

%environment
    LANGUAGE=en_US
    LANG="en_US.UTF-8"
    LC_ALL=C
    export LANGUAGE LANG LC_ALL

%post
    mkdir -p /home/vep/.vep;
    # install data for yeast BY
    #perl /home/vep/src/ensembl-vep/INSTALL.pl -a acf -s Saccharomyces_cerevisiae -y R64-1-1 -c /home/vep/.vep;
    # install data for human hg19
    #perl /home/vep/src/ensembl-vep/INSTALL.pl -a acf -s homo_sapiens -y GRCh37 -c /home/vep/.vep
    
    # get plugins
    #rm -fr /home/vep/.plugins;
    mkdir -p /home/vep/.plugins;
    
    rm -f -r /VEP_plugins;
    git clone https://github.com/Ensembl/VEP_plugins.git;
    cp -r -f /VEP_plugins/* /home/vep/.plugins;
    rm -f -r /VEP_plugins;
    
    # get pVACseq plugin
    rm -f -r /pVAC-Seq;
    git clone https://github.com/griffithlab/pVAC-Seq.git;
    cp -f /pVAC-Seq/pvacseq/VEP_plugins/Wildtype.pm /home/vep/.plugins;
    rm -f -r /pVAC-Seq;
    
%runscript
    exec /home/vep/src/ensembl-vep/vep "$@"

%apprun vep
	exec /home/vep/src/ensembl-vep/vep "$@"

%apprun install_vep
	exec perl /home/vep/src/ensembl-vep/INSTALL.pl "$@"
```

## Collection

 - Name: [eilon-s/sherlock_vep](https://github.com/eilon-s/sherlock_vep)
 - License: None

