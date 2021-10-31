---
id: 3007
name: "bioinfo-dirty-jobs/oncotator_singularity"
branch: "master"
tag: "test"
commit: "be5e9c88dacaf4a4d3d1b84b79fd1087b1b507cb"
version: "e4b263d680fa466ab3c2b1ed109dd8a2"
build_date: "2018-06-01T15:01:20.916Z"
size_mb: 1601
size: 519987231
sif: "https://datasets.datalad.org/shub/bioinfo-dirty-jobs/oncotator_singularity/test/2018-06-01-be5e9c88-e4b263d6/e4b263d680fa466ab3c2b1ed109dd8a2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bioinfo-dirty-jobs/oncotator_singularity/test/2018-06-01-be5e9c88-e4b263d6/
recipe: https://datasets.datalad.org/shub/bioinfo-dirty-jobs/oncotator_singularity/test/2018-06-01-be5e9c88-e4b263d6/Singularity
collection: bioinfo-dirty-jobs/oncotator_singularity
---

# bioinfo-dirty-jobs/oncotator_singularity:test

```bash
$ singularity pull shub://bioinfo-dirty-jobs/oncotator_singularity:test
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: docker://broadinstitute/oncotator:1.9.9.0


%post
chmod 755 /root
```

## Collection

 - Name: [bioinfo-dirty-jobs/oncotator_singularity](https://github.com/bioinfo-dirty-jobs/oncotator_singularity)
 - License: None

