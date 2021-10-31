---
id: 2504
name: "ShaopengLiu1/ATAC-seq_QC_analysis"
branch: "master"
tag: "mm10"
commit: "595bbd5f588939efb292fab1c6e08af5bd006f70"
version: "97e4daf4c99a86fbf42e34cdd9de4fce"
build_date: "2018-04-13T04:44:02.414Z"
size_mb: 10225
size: 5177458719
sif: "https://datasets.datalad.org/shub/ShaopengLiu1/ATAC-seq_QC_analysis/mm10/2018-04-13-595bbd5f-97e4daf4/97e4daf4c99a86fbf42e34cdd9de4fce.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ShaopengLiu1/ATAC-seq_QC_analysis/mm10/2018-04-13-595bbd5f-97e4daf4/
recipe: https://datasets.datalad.org/shub/ShaopengLiu1/ATAC-seq_QC_analysis/mm10/2018-04-13-595bbd5f-97e4daf4/Singularity
collection: ShaopengLiu1/ATAC-seq_QC_analysis
---

# ShaopengLiu1/ATAC-seq_QC_analysis:mm10

```bash
$ singularity pull shub://ShaopengLiu1/ATAC-seq_QC_analysis:mm10
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: zhanglab/atac-seq:mm10
IncludeCmd: yes



%runscript
cd /scratch \
	&& bash /atac_seq/pipe_code/atac_v1.1a.sh $@


%post
apt-get update && apt-get install -y locales
locale-gen en_US.UTF-8
apt-get install -y debconf
dpkg-reconfigure locales
```

## Collection

 - Name: [ShaopengLiu1/ATAC-seq_QC_analysis](https://github.com/ShaopengLiu1/ATAC-seq_QC_analysis)
 - License: None

