---
layout: post
title: Exploring Regional Wind Power Data in Sweden 1/3
plotly: true
tags: renewable-energy time-series visualization
live: true
---
Write a blog post about spot trading instead
This is the first of a series of three blog post where I will dive into and analyse a dataset. The dataset is the regional wind power production in Sweden from beginning of December 2014 until end of August 2017. As discussed in a previous [post](link), the Swedish electricity market is divided into four regions as illustrated in the picture below.

<p align="center">
  <img width="350" height="400" src="/images/areas-sweden.png">
</p>

Wind power producer (and every other producer and consumer of electricity) have to report production and consumption separately in all price areas. The reason for multiple areas is include physical constraints on the transmission capacity in the design of the electricity market. This allows for different prices (set by the supply and demand curves) in different regions depending on their specific production and consumption. Ideally, this design would incentivize investment of production plants in regions with high supply. In the Swedish electricity market prices are usually coupled between all areas. However, since most of the production of electricity is in the north and the consumption centres are in the south decoupling between Swedish area SE1 and SE2 do happen sometimes.

Write about the data providers: Nordpool and SVK

The wind power production time series for the full period is plotted below. It is a quite interesting graph because it can reveal the variability of the wind power production. The apparent variability changes a lot depending on the used time scale. For example, wind power production seem to vary like crazy on a yearly time scale but seen on daily or hourly time scale it seems to vary a lot less. Play around with the plot and see for yourself! From static plots, it is hard to appreciate this fact. For brevity, I only show the plot for SE1 in this blog post.  

<body> {% include _plots/windpower-ts-se1.html %} </body>



<body> {% include _plots/windpower-hist.html %} </body>

<body> {% include _plots/windpower-scatter-se1.html %} </body>
