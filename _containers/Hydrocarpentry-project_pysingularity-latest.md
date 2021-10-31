---
id: 3706
name: "Hydrocarpentry/project_pysingularity"
branch: "master"
tag: "latest"
commit: "1c574d3ee1b60ca7dba45e98d1c40f7509a7f963"
version: "46daa01a4cdd14aeb6be969209711f58"
build_date: "2018-07-27T11:59:51.499Z"
size_mb: 2332
size: 585093151
sif: "https://datasets.datalad.org/shub/Hydrocarpentry/project_pysingularity/latest/2018-07-27-1c574d3e-46daa01a/46daa01a4cdd14aeb6be969209711f58.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Hydrocarpentry/project_pysingularity/latest/2018-07-27-1c574d3e-46daa01a/
recipe: https://datasets.datalad.org/shub/Hydrocarpentry/project_pysingularity/latest/2018-07-27-1c574d3e-46daa01a/Singularity
collection: Hydrocarpentry/project_pysingularity
---

# Hydrocarpentry/project_pysingularity:latest

```bash
$ singularity pull shub://Hydrocarpentry/project_pysingularity:latest
```

## Singularity Recipe

```singularity
# Singularity
Bootstrap: docker
From: ubuntu:18.04
%post
    apt-get update && apt-get install -y python-pandas r-base
	apt-get install wget
	wget -O /hampt_rd_data.sqlite https://osf.io/mr7jx/?action=download 
	wget -O /STORM_data_flooded_streets_2010-2016.csv https://github.com/Hydrocarpentry/reproduced_data/blob/master/STORM_data_flooded_streets_2010-2016.csv
    echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile
    R --slave -e "install.packages('caret')"
    R --slave -e "install.packages('randomForest')"
    R --slave -e "install.packages('getopt')"
%files
    prepare_flood_events_table.py /tmp
    make_dly_obs_table_standalone.py /tmp
    by_event_for_model.py /tmp
    model_flood_counts_rf_ps_cln.r /tmp
    plot_count_model_results.py /tmp
    test.sh /tmp
%runscript
    bash /tmp/test.sh
```

## Collection

 - Name: [Hydrocarpentry/project_pysingularity](https://github.com/Hydrocarpentry/project_pysingularity)
 - License: None

