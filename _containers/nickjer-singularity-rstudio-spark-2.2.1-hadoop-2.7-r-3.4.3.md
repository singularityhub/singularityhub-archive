---
id: 1366
name: "nickjer/singularity-rstudio-spark"
branch: "master"
tag: "2.2.1-hadoop-2.7-r-3.4.3"
commit: "4cdff7648a01da1348ddef22f3e2cf0f53e7c5a2"
version: "85c240d6d6e3e0f8892745da2832a4f3"
build_date: "2018-03-11T21:43:45.230Z"
size_mb: 1717
size: 662728735
sif: "https://datasets.datalad.org/shub/nickjer/singularity-rstudio-spark/2.2.1-hadoop-2.7-r-3.4.3/2018-03-11-4cdff764-85c240d6/85c240d6d6e3e0f8892745da2832a4f3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nickjer/singularity-rstudio-spark/2.2.1-hadoop-2.7-r-3.4.3/2018-03-11-4cdff764-85c240d6/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-rstudio-spark/2.2.1-hadoop-2.7-r-3.4.3/2018-03-11-4cdff764-85c240d6/Singularity
collection: nickjer/singularity-rstudio-spark
---

# nickjer/singularity-rstudio-spark:2.2.1-hadoop-2.7-r-3.4.3

```bash
$ singularity pull shub://nickjer/singularity-rstudio-spark:2.2.1-hadoop-2.7-r-3.4.3
```

## Singularity Recipe

```singularity
BootStrap: shub
From: nickjer/singularity-rstudio:3.4.3

%labels
  Maintainer Jeremy Nicklas
  Spark_Version 2.2.1
  Hadoop_Version 2.7

%help
  This will run Apache Spark with an RStudio Server base

%apprun spark-class
  exec spark-class "${@}"

%apprun spark-master
  exec spark-class "org.apache.spark.deploy.master.Master" "${@}"

%apprun spark-worker
  exec spark-class "org.apache.spark.deploy.worker.Worker" "${@}"

%runscript
  exec spark-class "${@}"

%environment
  export SPARK_HOME=/opt/spark
  export PATH=${SPARK_HOME}/bin:${PATH}

%post
  # Software versions
  export SPARK_VERSION=2.2.1
  export HADOOP_VERSION=2.7

  # Install Spark
  apt-get update
  apt-get install -y --no-install-recommends \
    openjdk-8-jre
  mkdir -p /opt/spark
  wget \
      --no-verbose \
      -O - \
      "http://mirror.cc.columbia.edu/pub/software/apache/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" \
    | tar xz --strip-components=1 -C /opt/spark

  # Install sparklyr: R interface for Apache Spark
  Rscript -e " \
    withCallingHandlers( \
      install.packages( \
        c('tidyverse','sparklyr'), \
        lib='/usr/local/lib/R/site-library', \
        repo = 'https://cran.rstudio.com/', \
        clean = TRUE \
      ), \
      warning = function(w) stop(w) \
    ) \
  "

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [nickjer/singularity-rstudio-spark](https://github.com/nickjer/singularity-rstudio-spark)
 - License: [MIT License](https://api.github.com/licenses/mit)

