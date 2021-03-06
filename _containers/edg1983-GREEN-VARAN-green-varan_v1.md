---
id: 13853
name: "edg1983/GREEN-VARAN"
branch: "master"
tag: "green-varan_v1"
commit: "14c0ea3e30f6e9984cb83f550be2eac12d0027ef"
version: "8298b312dde04f9142eeca17b4d4ad334df47f77742fd79f131ba2e442045781"
build_date: "2021-03-23T13:05:51.073Z"
size_mb: 436.41015625
size: 457609216
sif: "https://datasets.datalad.org/shub/edg1983/GREEN-VARAN/green-varan_v1/2021-03-23-14c0ea3e-8298b312/8298b312dde04f9142eeca17b4d4ad334df47f77742fd79f131ba2e442045781.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/edg1983/GREEN-VARAN/green-varan_v1/2021-03-23-14c0ea3e-8298b312/
recipe: https://datasets.datalad.org/shub/edg1983/GREEN-VARAN/green-varan_v1/2021-03-23-14c0ea3e-8298b312/Singularity
collection: edg1983/GREEN-VARAN
---

# edg1983/GREEN-VARAN:green-varan_v1

```bash
$ singularity pull shub://edg1983/GREEN-VARAN:green-varan_v1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
    Author Edoardo Giacopuzzi
    Contact edoardo.giacopuzzi@well.ox.ac.uk
    Version v1.0

%environment
    SHELL=/bin/bash
    PATH=$PATH:/usr/local/bin:/opt/root/bin
    LC_ALL=C.UTF-8

%help
    GREEN-VARAN tools for annotation of regulatory variants
    The image contains the following tools:
    - GREEN-VARAN: annotation of small variants VCF
    - SV_annotation: annotation of SV VCF
    - GREEN-DB_query: query the GREEN-DB for detailed information 
    see https://github.com/edg1983/GREEN-VARAN 
  
    To get help on a specific tool use
    singularity run GREEN-VARAN.sif tool_name --help

    To run one of the tool use:
    singularity run --bind resources_folder:/opt/GREEN_VARAN/resources \
                    GREEN-VARAN.sif tool_name [arguments]
    
    NB. resources_folder must contain the standard subfolders and files expected by GREEN-VARAN
    
    By default you are expected to read/write from the present working directory
    - all input files are read from present working directory
    - output files and tmp folders are created in the present working directory

    You can change input/output/resource folders by creating additional folder binds 
    and then using the mounted paths accordingly in input/output arguments like:
    
    singularity run --bind input_folder:/input \
                    --bind output_folder:/output \
                    --bind bed_folder:/bed_files \
                    --bind scores_fodler:/scores \ 
                    GREEN-VARAN.sif \
                    GREEN-VARAN \
                    -i /input/input.vcf \
                    -o /output/output.vcf [arguments] \
                    --bed_dir /bed_files \
                    --scores_dir /scores \
                    [other arguments]

%runscript
    
    #!/usr/bin/bash
    echo "GREEN-VARAN tools image"
    exec bash /opt/runscript.sh "$@"
    
%post
    #Install system libraries
    apt-get update
    apt-get -y install apt-transport-https zlib1g-dev libcrypto++-dev libssl-dev libcurl4-openssl-dev liblzma-dev libbz2-dev build-essential wget cmake gcc language-pack-en-base python3 python3-pip make git autoconf
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    
    ## Install htslib 1.10
    cd /opt
    wget https://github.com/samtools/htslib/releases/download/1.10.2/htslib-1.10.2.tar.bz2
    tar -jxvf htslib-1.10.2.tar.bz2
    cd htslib-1.10.2
    ./configure
    make
    make install
    
    ## Install bedtools
    cd /opt
    mkdir bedtools && cd bedtools
    wget https://github.com/arq5x/bedtools2/releases/download/v2.29.2/bedtools.static.binary
    chmod a+x bedtools.static.binary
    ln --symbolic --force /opt/bedtools/bedtools.static.binary /usr/local/bin/bedtools
    
    ## Install python packages
    pip3 install --upgrade setuptools
    pip3 install Cython cytoolz toolz
    pip3 install pandas

    ## Install cyvcf2
    cd /opt
    git clone --recursive https://github.com/brentp/cyvcf2
    cd cyvcf2/htslib
    autoheader
    autoconf
    ./configure --enable-libcurl
    make

    cd ..
    pip3 install -r requirements.txt
    CYTHONIZE=1 pip3 install -e .

    ## Get GREEN-VARAN
    cd /opt
    git clone https://github.com/edg1983/GREEN-VARAN.git

    ## get vcfanno
    cd GREEN-VARAN
    wget https://github.com/brentp/vcfanno/releases/download/v0.3.2/vcfanno_linux64 -O vcfanno
    chmod a+x vcfanno

    ## made runscript
    echo 'case $1 in
        GREEN-VARAN|SV_annotation|GREEN-DB_query)
           echo "You are running tool $1"
           has_subfolder=$(ls /opt/GREEN_VARAN/resources/*/ &>/dev/null && echo 1 || echo 0)
           if [ $has_subfolder == 0 ]; then
               echo "## WARNING - No subfolders found in /opt/GREEN_VARAN/resources"
               echo "Did you forgot to bind your resources folder?"
               echo "This is OK if you mounted non-standard resource locations"
           fi
           python3 /opt/GREEN-VARAN/${1}.py ${@:2}
        ;;
        test)
           echo "run test OK"
           exit 0
        ;;
        *)
           echo "First argument must be one of the tool names: GREEN-VARAN, SV_annotation, GREEN-DB_query"
           exit 1
        ;; 
        esac' > /opt/runscript.sh
   
%test
    echo "## TEST 1: GREEN-VARAN ##"
    python3 /opt/GREEN-VARAN/GREEN-VARAN.py --help
    echo "## TEST 2: SV_annotation ##"
    python3 /opt/GREEN-VARAN/SV_annotation.py --help
    echo "## TEST 3: GREEN-DB_query ##"
    python3 /opt/GREEN-VARAN/GREEN-DB_query.py --help
    echo "## TEST 4: vcfanno"
    /opt/GREEN-VARAN/vcfanno
    echo "## TEST 5: bedtools ##"
    bedtools --version
    echo "## TEST 6: test runscript ##"
    bash /opt/runscript.sh test
```

## Collection

 - Name: [edg1983/GREEN-VARAN](https://github.com/edg1983/GREEN-VARAN)
 - License: None

