# FinalFits standalone setup instructions

## Install the environment

```bash
micromamba create -f environment.yaml
micromamba activate flashggFinalFit
```

> [!IMPORTANT]
> This environment requires the `boost-cpp` package, which (at the time of writing) forces the use of an older version of `combine` (v10.0.2). This ships with an older version of `root_base` (v6.32.10), which contains a typo in the `ScalarWrapper.h` header from `root-project/VecCore` ([see here](https://github.com/root-project/veccore/commit/247b9c6bd48a26b298a73683bb6015b08829ca70)). As a temporary fix, run
>
> ```bash
> sed -i 's/fVal(s->val_ptr)/fVal(s->fVal)/' $CONDA_PREFIX/include/VecCore/Backend/ScalarWrapper.h
> ```
>
> after activating the environment to patch the header file.

## Setup FinalFits

```bash
mkdir src
cd src
FINALFIT_TAG=higgsdnafinalfit
git clone -b $FINALFIT_TAG https://github.com/cms-analysis/flashggFinalFit.git
cd flashggFinalFit
source setup_standalone.sh
```

## Build the Background modelling code

```bash
cd Background
make clean
make -j 8
cd -
```

## Download data from the lhc-hxswg (optional, needed for the tutorial's physics model)

```bash
mkdir -p $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/data/lhc-hxswg
cd $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/data/lhc-hxswg
curl -L -o lhc-hxswg.tar.gz "https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit/archive/refs/heads/main.tar.gz"
tar -xzf lhc-hxswg.tar.gz --strip-components=3 HiggsAnalysis-CombinedLimit-main/data/lhc-hxswg
rm lhc-hxswg.tar.gz
cd -
```
