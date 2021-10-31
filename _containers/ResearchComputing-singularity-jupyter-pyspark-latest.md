---
id: 1636
name: "ResearchComputing/singularity-jupyter-pyspark"
branch: "master"
tag: "latest"
commit: "395caae383f63294530a747ec17b295a74bbe20f"
version: "daea24d6b714a25e3a5cd69b3e89764b"
build_date: "2020-05-22T10:18:37.349Z"
size_mb: 2207
size: 1195200543
sif: "https://datasets.datalad.org/shub/ResearchComputing/singularity-jupyter-pyspark/latest/2020-05-22-395caae3-daea24d6/daea24d6b714a25e3a5cd69b3e89764b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ResearchComputing/singularity-jupyter-pyspark/latest/2020-05-22-395caae3-daea24d6/
recipe: https://datasets.datalad.org/shub/ResearchComputing/singularity-jupyter-pyspark/latest/2020-05-22-395caae3-daea24d6/Singularity
collection: ResearchComputing/singularity-jupyter-pyspark
---

# ResearchComputing/singularity-jupyter-pyspark:latest

```bash
$ singularity pull shub://ResearchComputing/singularity-jupyter-pyspark:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ResearchComputing/singularity-slurm-base

%labels
  AUTHOR sampedro@colorado.edu

%environment
  export SPARK_VERSION=2.2.1
  export SPARK_HOME=/opt/spark/spark-${SPARK_VERSION}-bin-hadoop2.7
  export PATH=$SPARK_HOME/bin:$PATH
  export PYTHONPATH=$SPARK_HOME/python/pyspark:$PYTHONPATH
  export PYSPARK_DRIVER_PYTHON=jupyter
  export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
  export JUPYTER_DATA_DIR=$HOME/.singularity-jupyter

%post
  SPARK_VERSION=2.2.1
  SPARK_HOME=/opt/spark
  yum -y update
  yum -y install epel-release
  yum -y groupinstall 'Development Tools'
  yum -y install wget python34-devel python34-pip
  # Install Java JDK 8
  mkdir --parents /opt/java && cd /opt/java
  wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.rpm"
  yum -y localinstall *.rpm
  # Install Jupyter
  pip3 install --upgrade pip
  pip3 install jupyterhub==0.7.2
  pip3 install --upgrade notebook
  pip3 install findspark
  # Install spark
  mkdir --parents $SPARK_HOME && cd $SPARK_HOME
  wget http://apache.claz.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop2.7.tgz
  tar -xzf spark-${SPARK_VERSION}-bin-hadoop2.7.tgz
```

## Collection

 - Name: [ResearchComputing/singularity-jupyter-pyspark](https://github.com/ResearchComputing/singularity-jupyter-pyspark)
 - License: [MIT License](https://api.github.com/licenses/mit)

