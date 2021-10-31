---
id: 1861
name: "Wustl-Zhanglab/ATAC-seq_QC_analysis"
branch: "master"
tag: "mm10"
commit: "5d22c943d104ed5909c61f357da4825f1abce848"
version: "28fca78dee700bc735c30ea64993b12a"
build_date: "2018-03-03T01:06:30.189Z"
size_mb: 10215
size: 5175660575
sif: "https://datasets.datalad.org/shub/Wustl-Zhanglab/ATAC-seq_QC_analysis/mm10/2018-03-03-5d22c943-28fca78d/28fca78dee700bc735c30ea64993b12a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Wustl-Zhanglab/ATAC-seq_QC_analysis/mm10/2018-03-03-5d22c943-28fca78d/
recipe: https://datasets.datalad.org/shub/Wustl-Zhanglab/ATAC-seq_QC_analysis/mm10/2018-03-03-5d22c943-28fca78d/Singularity
collection: ShaopengLiu1/ATAC-seq_QC_analysis
---

# Wustl-Zhanglab/ATAC-seq_QC_analysis:mm10

```bash
$ singularity pull shub://Wustl-Zhanglab/ATAC-seq_QC_analysis:mm10
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

 - Name: [Wustl-Zhanglab/ATAC-seq_QC_analysis](https://github.com/Wustl-Zhanglab/ATAC-seq_QC_analysis)
 - License: None

