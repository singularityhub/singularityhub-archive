---
id: 15712
name: "jesus-gorronogoitia/easy"
branch: "main"
tag: "latest"
commit: "590a6330cc3466895870868ded3430b9d2afe1f6"
version: "b91eb44caf9f6007fe3f3291be6d0084"
build_date: "2021-03-17T09:28:42.368Z"
size_mb: 6089.0
size: 3205144607
sif: "https://datasets.datalad.org/shub/jesus-gorronogoitia/easy/latest/2021-03-17-590a6330-b91eb44c/b91eb44caf9f6007fe3f3291be6d0084.sif"
url: https://datasets.datalad.org/shub/jesus-gorronogoitia/easy/latest/2021-03-17-590a6330-b91eb44c/
recipe: https://datasets.datalad.org/shub/jesus-gorronogoitia/easy/latest/2021-03-17-590a6330-b91eb44c/Singularity
collection: jesus-gorronogoitia/easy
---

# jesus-gorronogoitia/easy:latest

```bash
$ singularity pull shub://jesus-gorronogoitia/easy:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: conda/miniconda3

%files
	./Next_trials_ITAINNOVA.zip /root
	./easy.sh /usr/local/bin

%post
	apt-get -y update && apt-get install -y unzip
	conda config --set auto_activate_base false
	conda update -n base -c defaults conda
	conda create -n tf_test tensorflow=2.2.0=gpu_py37h1a511ff_0
	conda init bash
	. ~/.bashrc
	conda activate tf_test
	pip install optuna keras scikit-learn pandas
	unzip /root/Next_trials_ITAINNOVA.zip -d /usr/local/
	chmod +x /usr/local/bin/easy.sh
%runscript
	/usr/local/bin/easy.sh
```

## Collection

 - Name: [jesus-gorronogoitia/easy](https://github.com/jesus-gorronogoitia/easy)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

