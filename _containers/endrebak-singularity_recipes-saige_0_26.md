---
id: 1778
name: "endrebak/singularity_recipes"
branch: "master"
tag: "saige_0_26"
commit: "8ffe4b0e6f50f6b430b91792dd9591d2404ef3cc"
version: "100003862d118f365624ae92adc8ebf5"
build_date: "2018-03-07T14:12:48.404Z"
size_mb: 3664
size: 1589268511
sif: "https://datasets.datalad.org/shub/endrebak/singularity_recipes/saige_0_26/2018-03-07-8ffe4b0e-10000386/100003862d118f365624ae92adc8ebf5.simg"
url: https://datasets.datalad.org/shub/endrebak/singularity_recipes/saige_0_26/2018-03-07-8ffe4b0e-10000386/
recipe: https://datasets.datalad.org/shub/endrebak/singularity_recipes/saige_0_26/2018-03-07-8ffe4b0e-10000386/Singularity
collection: endrebak/singularity_recipes
---

# endrebak/singularity_recipes:saige_0_26

```bash
$ singularity pull shub://endrebak/singularity_recipes:saige_0_26
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/anaconda3

%post
export PATH=/opt/conda/bin:${PATH}
echo 'export PATH=/opt/conda/bin:${PATH}' >> $SINGULARITY_ENVIRONMENT
conda config --add channels r
conda config --add channels bioconda
conda config --add channels conda-forge
conda install r r-matrix r-rcppeigen r-data.table r-rcppparallel r-rcpparmadillo r-rcpp lapack
wget https://cran.r-project.org/src/contrib/SPAtest_2.0.2.tar.gz
R CMD INSTALL SPAtest_2.0.2.tar.gz
wget 'https://zenodo.org/record/1181962/files/SAIGE_0.26_R_x86_64-pc-linux-gnu.tar.gz' -O SAIGE.tar.gz
R CMD INSTALL SAIGE.tar.gz
```

## Collection

 - Name: [endrebak/singularity_recipes](https://github.com/endrebak/singularity_recipes)
 - License: None

