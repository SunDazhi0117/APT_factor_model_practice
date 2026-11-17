# Note 22 — Learning Review and Independent Exercises

## What the code does

1. Create a random number generator with a fixed seed and simulate 120 months of three factors.
2. Generate stock excess returns using known alpha, betas and random noise.
3. Use the three factors as X and stock excess returns as y; add a column of ones to X to estimate alpha.
4. Use OLS to estimate all four coefficients jointly by minimising the sum of squared residuals across 120 months.
5. Compare the generating and estimated coefficients, then save the data, report and chart.

There is no real stock in this exercise: all observations are simulated. We know the generating coefficients, but the regression receives only X and y, not those preset values.

## Understanding beta

The estimated market beta is approximately 1.238. Holding SMB and HML fixed, a one-percentage-point increase in market excess return corresponds to an increase of approximately 1.238 percentage points in fitted stock excess return. This is not a guaranteed monthly gain; actual returns also reflect other factors and the error term.

In a multiple regression, each beta measures exposure conditional on the other factors. Calculating Cov(y, factor) / Var(factor) separately for each factor generally cannot replace the joint regression: those calculations produce three separate single-factor slopes.

## Three numbers that describe alpha

The fitted results are: alpha = 0.002577, standard error = 0.002775, and p-value = 0.355.

- **Estimate: approximately 0.258% per month.** This is the intercept estimated from this sample.
- **Standard error: approximately 0.278 percentage points.** This measures uncertainty in the intercept estimate. It is not the standard deviation of stock returns and does not guarantee that the true value lies within one standard error of the estimate.
- **t-statistic: approximately 0.929.** For a null hypothesis of zero alpha, divide the estimate by its standard error. The estimated alpha is about 0.929 standard errors away from zero.

Why is the sign alone insufficient? Imagine generating many new samples of 120 months. Different noise draws produce different alpha estimates. A positive estimate in one sample may reflect both a real signal and random variation.

The 95% confidence interval is approximately **-0.292% to +0.807% per month**, which includes zero. The interval is constructed using a procedure with 95% coverage under repeated sampling and the model assumptions. It does not mean that the fixed true alpha has a 95% probability of lying inside this particular realised interval.

## A p-value is not the probability that the null hypothesis is true

The null hypothesis is alpha = 0. A p-value of 0.355 means that, assuming the null hypothesis and the test's model assumptions hold, the probability of observing a t-statistic at least as large in absolute value as the observed one is approximately 35.5%.

At the chosen 5% significance level, we therefore do not reject the null hypothesis. This does not prove that true alpha is zero, assign a 35.5% probability to the model being correct, or describe the probability of making money.

In this simulation, we know that the generating alpha is 0.2% per month. Nevertheless, the estimate is not statistically significant: a finite sample and substantial noise can make a small genuine effect difficult to detect.

## Statistical versus economic significance

- **Statistical significance:** Does the evidence justify rejecting a specified null hypothesis? The answer depends on uncertainty, sample size and model assumptions.
- **Economic significance:** Is the effect large enough, persistent enough and valuable enough after costs to matter in practice?

A tiny effect can be statistically significant in a large sample. An economically meaningful effect may be statistically insignificant in a small sample. This exercise uses simulated data and cannot establish real investment value.

## R-squared

R-squared = 1 - residual sum of squares / total sum of squares of stock excess returns around their sample mean.

An R-squared of 0.776 means that the model explains approximately 77.6% of this variation within the sample. It is not 77.6% forecast accuracy and does not establish causation. Correct model specification, predictive performance and good in-sample fit are distinct questions.

## Independent assessment — not yet completed

Without consulting the notes above, answer these questions in your own words:

1. What is the difference between CAPM and the Fama–French Three-Factor Model?
2. What does a positive SMB beta and a negative HML beta suggest about a stock's factor exposure?
3. How should we interpret a positive estimated alpha with a p-value greater than 0.05?

Then independently write a **100–150-word Investment Research Commentary in English**. Identify the data as simulated and discuss the three factor exposures, the magnitude and statistical evidence for alpha, the meaning of R-squared, and at least one limitation. Do not claim to have studied a real company or demonstrated tradable abnormal returns.

The mentor's evaluation should prioritise:

- **Financial understanding:** Correct interpretation of conditional exposures, excess returns and differences between models.
- **Statistical inference:** Distinguishing estimates from true parameters and statistical from economic significance, without misinterpreting p-values.
- **Analytical reasoning:** Conclusions supported by the results, with appropriate acknowledgement of simulation and in-sample limitations.
- **Communication:** Accurate and concise English, assessed after the financial reasoning rather than as a substitute for it.

This document is a review guide, not a record that the learner has independently completed the exercises or passed the assessment.
