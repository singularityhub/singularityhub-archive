---
id: 10846
name: "mcw-rcc/apache-spark"
branch: "master"
tag: "latest"
commit: "eda86a031fc463dd3b49ebe59bdb36416941ffa1"
version: "026d5a2ca3641aa4940a322c0751e67f"
build_date: "2021-01-26T13:11:44.288Z"
size_mb: 2758.0
size: 1436528671
sif: "https://datasets.datalad.org/shub/mcw-rcc/apache-spark/latest/2021-01-26-eda86a03-026d5a2c/026d5a2ca3641aa4940a322c0751e67f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/apache-spark/latest/2021-01-26-eda86a03-026d5a2c/
recipe: https://datasets.datalad.org/shub/mcw-rcc/apache-spark/latest/2021-01-26-eda86a03-026d5a2c/Singularity
collection: mcw-rcc/apache-spark
---

# mcw-rcc/apache-spark:latest

```bash
$ singularity pull shub://mcw-rcc/apache-spark:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
  Maintainer Matthew Flister
  Spark 2.4.4
  Hadoop 2.7

%help
  This container will run Apache Spark.

%environment
  export SPARK_HOME=/opt/spark
  export PATH=${SPARK_HOME}/bin:${PATH}

%post
  export SPARK_VERSION=2.4.4
  export HADOOP_VERSION=2.7

  mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

  apt-get update
  apt-get install -y --no-install-recommends \
    openjdk-8-jre \
    python \
    python3 \
    python-dev \
    python3-dev \
    python-setuptools \
    python3-setuptools \
    python-pip \
    python3-pip \
    wget
  
  # install python packages
  pip install --no-binary --upgrade \
    wheel \
    numpy \
    scipy \
    jupyter \
    pandas \
    pyspark

  pip3 install --no-binary --upgrade \
    wheel \
    numpy \
    scipy \
    jupyter \
    jupyterhub \
    pandas \
    pyspark

  #install spark
  mkdir -p /opt/spark
  wget http://mirrors.sonic.net/apache/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
  tar -xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -C /opt/spark --strip-components=1

  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [mcw-rcc/apache-spark](https://github.com/mcw-rcc/apache-spark)
 - License: [MIT License](https://api.github.com/licenses/mit)

