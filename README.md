# My Blog
In this blog, I am writing about how algorithms can help in the fight against climate change.

## Planned Blog Posts
As always, I have way more ideas than I have time to realise. These are the blog posts I have planned for at the moment:

1. Existential risk
1. Climate Change (history and joseph fourier)
1. Big World, Small Planet
1. The Bill Gates Equation
1. The Rise of Renewable Energy (Reference IEA report) and exponential growth. It is possible to do something about climate change.
here is about the optimism in climate change (al gore) https://www.ted.com/talks/al_gore_the_case_for_optimism_on_climate_change
1. The Energy Transformation (structural change of energy system)
1. The Grid Stability Problem (TSO - SVK)
1. System integration problem https://www.iea.org/topics/renewables/systemintegration/
1. Flexibility is Key (key for allowing for transformation, what are the sources of flexibility?)
1. Day-Ahead Electricity Market (from physical problem to market design)
1. Intraday Electricity Market (not really a market more a horizon)
1. Artificial Intelligence (what is artificial intelligence)
1. Artificial Intelligence in Energy (include MIT Review)
1. The Electricity Forecast Problem (what is the problem and how can it be defined)
1. Uncertainty in Electricity Forecasts (why is it needed? refer to paper)
1. Regional windpower data in sweden
1. Intraday trading
1. Meteorology - wind profile
1. knapsack problem
1. Climate models and WRF https://www.ted.com/talks/gavin_schmidt_the_emergent_patterns_of_climate_change#t-691522
1. autocorrelation
1. multiple weather
1. SHMI API (multigrid) (try geoviews by bokeh)
1. Navier stokes
1. IEA insights
1. Algorithmic trading
1. Bayesian statistics
1. Computational fluid dynamics

## Mathjax

## Interactive Plots
This blog is capable of handing interactive plots with [plotly](https://plot.ly/). To add an interactive plot, first one has to get the ```div``` using a plotly function according to:

```
import plotly
div = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
```

Using ```python```, the ```div``` can be saved to a file:

```
text_file = open("example_plot.html", "w")
text_file.write(div)
text_file.close()
```

This this file should be placed on the following path. ```_includes/_plots/```. Finally, in order to include it in a ```.md``` blog post, the following code can be used:

```
<body> {% include _plots/example_plot.html %} </body>
```

## Planned Changes to the Blog
There are wanted changes to the blog that still are not implemented in the jekyll tempelate. These are:
* Make the tags look nicer.
* Better filtering of blog post based on tags.

I want to have the following tags:

* Math
* Data
* Visualization
* Meteorology
* Machine learning
* Electricity market
* Python
* Time Series
* computing
* CFD
* Game Theory
* Forecasting

## On Writing blog posts
General advice on writing blog posts:

* Start by sketching out what you want to include in the post.
* Write about stuff that you, yourself want to learn more about.
