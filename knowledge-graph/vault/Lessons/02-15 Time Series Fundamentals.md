---
id: "lesson:02/15"
type: lesson
ref: 02/15
phase: 2
num: 15
title: Time Series Fundamentals
lesson_type: build
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 11
prereqs: 9
community: 4
libraries:
  - numpy
aliases:
  - 02/15
  - 02-15
tags:
  - phase/02
  - type/build
  - community/04
source: ai-engineering-from-scratch/phases/02-ml-fundamentals/15-time-series/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/15-time-series"
---

# 02/15 Time Series Fundamentals

> Past performance does predict future results -- if you check for stationarity first.

**Phase:** [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] · **Type:** Build · **Time:** 90 min · **Status:** —  
**Open:** [[Upstream/02-ml-fundamentals/15-time-series/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/02-ml-fundamentals/15-time-series) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/02-ml-fundamentals/15-time-series) · code: time_series.py  
**Community:** [[Communities/04 Overfitting · Underfitting · Data Leakage|04 Overfitting · Underfitting · Data Leakage]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 2, Lessons 01-09`

- **02/01-09**:
    - [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]]
    - [[Lessons/02-02 Linear Regression|02/02 Linear Regression]]
    - [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]]
    - [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]]
    - [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]]
    - [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]]
    - [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]]
    - [[Lessons/02-08 Feature Engineering & Selection|02/08 Feature Engineering & Selection]]
    - [[Lessons/02-09 Model Evaluation|02/09 Model Evaluation]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-08 Optimization|01/08 Optimization]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-14 Norms and Distances|01/14 Norms and Distances]], [[Lessons/01-18 Convex Optimization|01/18 Convex Optimization]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]]

## Concepts taught

- Stationarity `lesson term` — A series whose mean, variance, and autocorrelation structure are constant over time
- Differencing `lesson term` — Computing y[t] - y[t-1] to remove trends and achieve stationarity
- Autocorrelation (as *Autocorrelation (ACF)*) `lesson term` — The correlation between a time series and a lagged copy of itself, as a function of the lag
- Partial autocorrelation (as *Partial autocorrelation (PACF)*) `lesson term` — Autocorrelation at lag k after removing the effect of all shorter lags
- Lag features `lesson term` — Using y[t-1], y[t-2], ..., y[t-k] as features to predict y[t]
- Walk-forward validation `lesson term` — Evaluation where training data always precedes test data chronologically
- ARIMA `lesson term` — AutoRegressive Integrated Moving Average: combines past values (AR), differencing (I), and past errors (MA)
- Seasonality `lesson term` — Regular, predictable cycles in a time series tied to calendar periods (daily, weekly, yearly)
- Trend `lesson term` — A persistent increase or decrease in the series level over time
- Expanding window `lesson term` — Walk-forward validation where the training set grows with each fold
- [[Concepts/Sliding window|Sliding window]] `lesson term` — Walk-forward validation where the training set is a fixed-length window that slides forward

## Ships

- [[Artifacts/02-15 prompt-time-series-advisor|prompt-time-series-advisor]] `prompt` — Frame time series problems and recommend approaches

## Further reading

- Hyndman and Athanasopoulos, Forecasting: Principles and Practice (3rd ed.) ([link](https://otexts.com/fpp3/)) — the best free textbook on time series forecasting
- Makridakis et al., The M5 Competition (2022) ([link](https://www.sciencedirect.com/science/article/pii/S0169207021001874)) — large-scale forecasting competition showing ML methods vs statistical methods
- scikit-learn Time Series Split ([link](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html)) — sklearn's walk-forward splitter
- statsmodels ARIMA docs ([link](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html)) — ARIMA implementation with diagnostics


%% ── my notes ── %%
