---
id: 3197
name: "iqbal-lab-org/Mykrobe_tb_workflow"
branch: "master"
tag: "tb"
commit: "aa75d26ca06332aa85125b9c9010faf12d4910f7"
version: "8426a58819db4f0ce3de5f999c3843da"
build_date: "2019-10-21T08:55:43.194Z"
size_mb: 1228
size: 486961183
sif: "https://datasets.datalad.org/shub/iqbal-lab-org/Mykrobe_tb_workflow/tb/2019-10-21-aa75d26c-8426a588/8426a58819db4f0ce3de5f999c3843da.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/iqbal-lab-org/Mykrobe_tb_workflow/tb/2019-10-21-aa75d26c-8426a588/
recipe: https://datasets.datalad.org/shub/iqbal-lab-org/Mykrobe_tb_workflow/tb/2019-10-21-aa75d26c-8426a588/Singularity
collection: iqbal-lab-org/Mykrobe_tb_workflow
---

# iqbal-lab-org/Mykrobe_tb_workflow:tb

```bash
$ singularity pull shub://iqbal-lab-org/Mykrobe_tb_workflow:tb
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL:  http://us.archive.ubuntu.com/ubuntu/

%help
  A container to hold all the tools required for running Mykrobe predict.
  Run `singularity exec tb.simg` followed by any of the following:
    - pistis
    - porechop
    - mykrobe
    - minimap2
    - samtools
    - NanoStat

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y python3-pip git wget libncurses5-dev libbz2-dev liblzma-dev zlib1g-dev
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT


    # ========================
    # INSTALL Mykrobe
    # ========================
    COMMIT=8f7fd05b9b94fa3cc40df2845187fa35393b9c2a
    git clone https://github.com/Mykrobe-tools/mykrobe-atlas-cli.git mykrobe
    cd mykrobe
    git checkout "$COMMIT"
    wget https://goo.gl/DXb9hN -O - | tar -vxzf  -
    rm -fr src/mykrobe/data
    mv mykrobe-data src/mykrobe/data
    pip3 install .

    # ================================
    # INSTALL pistis
    # ================================
    pip3 install pistis==0.3.3

    # ================================
    # INSTALL porechop
    # ================================
    PORECHOP_VERSION=0.2.4
    PORECHOP_URL=https://github.com/rrwick/Porechop/archive/v${PORECHOP_VERSION}.tar.gz
    wget "$PORECHOP_URL"
    tar xzf v${PORECHOP_VERSION}.tar.gz
    rm v${PORECHOP_VERSION}.tar.gz
    cd Porechop-${PORECHOP_VERSION}
    python3 setup.py install
    cd ~

    # ================================
    # INSTALL minimap2
    # ================================
    MM2_VERSION=2.10
    MM2_URL=https://github.com/lh3/minimap2/releases/download/v${MM2_VERSION}/minimap2-${MM2_VERSION}_x64-linux.tar.bz2
    wget "$MM2_URL" -O - | tar -jxvf -
    cp ./minimap2-${MM2_VERSION}_x64-linux/minimap2 /usr/local/bin

    # ================================
    # INSTALL samtools
    # ================================
    SAMTOOLS_VERSION=1.7
    SAMTOOLS_URL=https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2
    wget "$SAMTOOLS_URL" -O - | tar -jxvf -
    cd samtools-${SAMTOOLS_VERSION}
    ./configure
    make
    make install
    cd ~

    # ================================
    # INSTALL nanostats
    # ================================
    pip3 install nanostat==1.1.2
```

## Collection

 - Name: [iqbal-lab-org/Mykrobe_tb_workflow](https://github.com/iqbal-lab-org/Mykrobe_tb_workflow)
 - License: None

