---
layout: post
title: Exploring Regional Wind Power Data in Sweden
tags: [data, python, renewable-energy, time-series, visualization]
description: The Swedish wind power industry has been growing rapidly in the last decade. Raw data regarding power production has been public since late 2014. However, there is not much visualization and exploration of the data. The goal of this blog post is to fill this hole and turn the raw data into insights and understanding. 
plotly: true
live: true
---

## Introduction
In this blog post, we will dive into and explore regional wind power production data in Sweden. The Swedish electricity market ([Nord Pool](http://www.nordpoolspot.com/)) is divided into four price areas as illustrated in the figure below. For these areas, public data regarding the active power of the aggregated wind power is available with an hourly resolution. The time span of the data is from beginning of December 2014 until end of August 2017. The full analysis together with the ```python``` code can be found in [this](https://github.com/sebaheg/windpower-data) GitHub repository.

<p align="center">
  <img width="320" height="360" src="/images/areas-sweden.png">
</p>

## Data provider
There are two different data providers given in the table below.

<table>
  <thead>
    <tr>
      <th>Provider</th>
      <th>Data Access</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Nord Pool</td>
      <td>[nordpoolspot.com/historical-market-data/](nordpoolspot.com/historical-market-data/)</td>
    </tr>
    <tr>
      <td>SVK</td>
      <td>[mimer.svk.se/ProductionConsumption/ProductionIndex](mimer.svk.se/ProductionConsumption/ProductionIndex)</td>
    </tr>
  </tbody>
</table>

## Comparison
The wind power production time series for the full period is plotted below. It is a quite interesting graph because it reveal the variability of the wind power production. The apparent variability changes a lot depending on the used time scale. For example, wind power production seem to vary like crazy on a yearly time scale but seen on daily or hourly time scale it seems to vary a lot less. Play around with the interactive plot and see for yourself! By using static plots, it is hard to appreciate this fact. For brevity, only the plot for SE1 is shown here.

<body> {% include _plots/_windpower/windpower-ts-se1.html %} </body>

As can be seen in the plot above, the two datasets (Nord Pool and SVK) seem to agree. But using only a time series plot it is hard to say if they are indeed identical. For this reason, we calculate the residual between the datasets and make use of a histogram plot to explore its distribution. From the histogram plot, it is clear that the datasets are not identical. But there is no bias between them either.

<body> {% include _plots/_windpower/windpower-hist.html %} </body>

A similar comparison can be made by plotting a scatter plot of the two datasets. By zooming the scatter plot in it is revealed that the Nord Pool dataset is rounded to whole numbers in MW. Because of this fact and because the SVK data is available for a longer period in time, only the SVK dataset is considered from now on.

<body> {% include _plots/_windpower/windpower-scatter-se1.html %} </body>

## Distribution
It has been found that wind speed at a given location follows the [Weibull distribution](https://en.wikipedia.org/wiki/Weibull_distribution) quite well. There is a quite well-defined dependence (called power curve) between wind speed and power for a given wind turbine. Therefore, the distribution of power from a wind turbine should be the roughly a Weibull distribution propagated through the power curve. This means for example that the resulting distribution should be amplified around zero (since wind power is damped before cut-in) and that the tail of the Weibull distribution should be truncated at cut-out power. By aggregating several wind farms in a region, this smooths out the resulting distribution. In the plot below, the distribution of wind power production in the different price areas is shown (for the whole time span).

<body> {% include _plots/_windpower/windpower-dist.html %} </body>

The distribution above can be made using only an interval of the full time span and represented as a [box plot](https://en.wikipedia.org/wiki/Box_plot). This way, the change in distribution over time can be revealed. In the plots below, the temporal variation are shown over different time scales: yearly, monthly and hourly. In the yearly time scale is can be seen that the mean wind power production is decreasing but the maximum produced is increasing. This is probably related to the increased installed capacity and inter-yearly variability of the wind resource. On the monthly time scale, we see that wind power production in Sweden is strongest during the winter months. Lastly, on the hourly time scale, there a slight but clear decrease of the power production during daytime.

<body> {% include _plots/_windpower/windpower-box-yearly-se1.html %} </body>

<body> {% include _plots/_windpower/windpower-box-monthly-se1.html %} </body>

<body> {% include _plots/_windpower/windpower-box-hourly-se1.html %} </body>

## Density distribution
Up until now, we have considered the price areas independently from each other. But since the price areas are located close to each other in space, it is likely that there will be a correlation between them. A first step towards finding this covariance is to plot the power production of two neighbouring price areas in a scatter plot. However, since there are so many data points, points in the scatter plot will overlap and any pattern will not be clear. For this reason, it is more informative to plot the density distribution calculated by using [Kernel density estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation). To explore all possible combinations of price areas, matrix of density distributions (or density distribution matrix similarly to scatter matrix) can be adopted. The [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) is reported above each graph to give a summary metric. On the diagonal there is only one price area, therefore only the distribution is shown. Considering the map of the price areas in the beginning of this blog post, it is clear that the data suggest that regions that are geographically closer tend to have a stronger correlation.

<body> {% include _plots/_windpower/windpower-scatter-matrix.html %} </body>

## Conclusion
From the analysis presented in this blog post, it is clear that Nord Pool and SVK are providing similar data however not equivalent. The difference between the datasets is exceeding the round-off error, and is thus not the only reason for the discrepancy. It is found that the wind power production in Sweden follows yearly, monthly and daily patterns. Finally, by looking at the correlations between the different price areas, it is seen that there is a positive dependency between many areas. This dependancy is especially strong between SE1-SE2 and SE3-SE4, which is reasonable considering their geographical location.

## Future work
Inspired by the correlations found between the price areas, it is probably possible to find more and also time dependent patterns between the areas. A next step could therefore be to extend the density distribution matrix with a slide bar that controls the considered time period. Furthermore, to explore the temporal correlation of time series for the different price areas with itself and with each other, auto-correlation and cross-correlation plots can be made. Lastly, it is also possible to leverage Fourier analysis to explore the frequency content in a more rigorous way.

### References
* Nord Pool, [Historical Market Data]([nordpoolspot.com/historical-market-data/](nordpoolspot.com/historical-market-data/))
* SVK, [Mimer](mimer.svk.se/ProductionConsumption/ProductionIndex)
