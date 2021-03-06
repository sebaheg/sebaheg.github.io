---
layout: post
title: Electric Power System
tags: [energy, power-system]
description: What is a power system? And what is necessary for it to function even in the event of external and internal disturbances? In this post we will find out.
mathjax: true
comments: true
live: true
---

Today, many of us take electricity for granted. Still, the benefits we get from the use of it are crucial for the functioning of our modern society. It is one of our highest prioritised national security issues. What seems so simple when plugging the charger into the power outlet at home, actually has a lot more to it. There is a whole machinery holding everything in place, from power transmission to production facilities and control system. In this blog post, we will dive into what the power system is and what is needed for it to function. Electric power engineering is not my core expertise, so feel free to correct me in the comments at any point along the way.

## What is the goal of the power system?
The goal of the power system is threefold:

* Consumer should get electricity whenever they want, no matter any external or internal disturbance to the power system such as weather or outages of production units.
* The consumer must have a realistic voltage (e.g. 230 V in Sweden) in the power outlet.
* The previous points should be obtained in an economic and sustainable way at a realistic reliability. This reliability is never 100 percent.

## What are the parts of the power system?
The power system can be divided into four parts: generation, transmission, distribution and utilization. An illustration of a modern, deregulated power system (the Nordic power system) is given in the figure below.

<p align="center">
  <img width="450" height="380" src="/images/power-system.jpeg">
</p>

Electricity is not a form of primary energy freely present in nature in large quantities. It must be produced by transforming energy in some other form to electrical energy. This is called generation and is carried out in power plants. The generation and utilization of electricity is typically not located in the same place. Therefore, it needs to be transported someone between these points. This is done using the transmission network (national grid), which is the highways of the power system. Electricity is flowing in a bulk movement from the generation site and onto the transmission network close to the speed of light.

The voltage on the transmission network is high in order to limit the current and thus also the electrical losses (see [Joule heating](https://en.wikipedia.org/wiki/Joule_heating)). Customers, on the other side, need realistic voltage levels (e.g. 230 V in Sweden) for their appliances. For this reason, the voltage is transformed down on the distribution network (local grid) which carries electricity to the individual consumers. Some power systems have an intermediary voltage level (regional grid) between the transmission and distribution networks. The utilization of electricity ranges from large industries like steel manufacturing and railway transport to our our appliances for cooking and entertainment at home

## Alternating vs direct current
The majority of electrical power systems are based on three-phase alternating current (AC), which has become the standard for large-scale power transmission and distribution. Three-phase current is ideal in the sense that the sum of the power output from all phases is constant. This lets synchronous motors be driven with constant torque. Historically, it was easier to convert AC than direct current (DC) between different voltage levels. However, nowadays it is possible to do change the voltage level also with DC. In fact, it might even be better alternative since most appliances are DC powered, like our computers and phones. But because of the immense economic investment already made in the current system it is not likely that this would happen anytime in the near future.

## Synchronous power system
In a synchronous power system, all producers and consumers are connected to each other through the transmission and distribution network together with transformers. The speed at which rotors spin, in combination with the number of generator poles, determines the frequency of the alternating current produced by the generators. The frequency in a synchronous power system is the same everywhere in the system. This means that all generators must rotate at sub-multiples of the same speed. However, an exception to this is generators that are connected through power electronics (such as gear-less wind turbines) or that are linked to a grid through an asynchronous tie (such as a HVDC link). These generators can operate at frequencies completely independent of the power system frequency. The synchronous power systems in Europe are shown below.

<p align="center">
  <img width="300" height="300" src="/images/synchronous-system.png">
</p>

## Balancing the power system
One peculiarity with electricity is that it must be produced and consumed at the same time. The amount of active power consumed plus the losses always equals the active power produced. In a situation where there is more consumption than production of active power, the remaining active power is provided by the inertia of the rotating machinery. This lowers the frequency of the AC on the grid. In Europe, the predetermined nominal frequency is 50 Hz (in North America this is 60 Hz). Even small deviations from the nominal frequency value could damage synchronous machines and other appliances. It is normal that the frequency varies around 50 \\( \pm \\) 0.1 Hz. The Swedish transmission system operator (TSO) publishes data regarding the instantaneous frequency in real time [here](http://www.svk.se/en/national-grid/the-control-room/). You can learn a lot about the power system just by observing the frequency, power flows and generation on that site. To make the physics of the power system more tangible, we can draw an analogy with a long bike as shown below.

<p align="center">
  <img width="400" height="300" src="/images/bike.jpeg">
</p>

The speed of the bike is given by the balance between the air and rolling resistance and the summed peddling forces by all riders (Newton's second law of motion). If these opposite forces are equal, then the speed is constant. This is exactly the same as how the power system works. The speed and inertia of the bike represents the frequency in the power system and inertia of the rotating machinery respectively. Just as the frequency of a synchronous power system is the same wherever you measure it, the speed of the bike is the same everywhere on the bike. The one responsible for the speed of the bike corresponds to the TSO in the power system. Every rider is a generating unit and the air and rolling resistance represent the electrical load. If one of the riders would stop pedaling (corresponding to an outage of a power plant), then the speed would decrease (frequency would drop). As the speed decreases, the air resistance also decrease. This is similar to a power system where an outage would lead to lower voltage and frequency, which in turn lowers the load. In the Nordic power system an outage of 1200 MW would lead to approximately 200 MW decrease in load.

In addition to the power used by a load to do useful work (active power), many AC devices also use an additional amount of power since they cause the AC voltage and current to become out-of-sync (reactive power). When the voltage and current is not perfectly aligned, the electrical power is not given by product of current and voltage as is the case for DC. Instead the total power (apparent power) can be decomposed into active and reactive power. Reactive power does not do any real work but is transmitted back and forth between the reactive power source and load every cycle. This extra current on the power lines leads to thermal losses. Therefore, too much reactive power is undesirable. However, some reactive power is needed to maintain the voltage levels on the grid. The reactive power, just like the active power, must be balanced. There must be as much reactive generation (capacitance) as load (reactance). This is equivalent to keeping the bike in an upright position, having the same forcing on left and right hand side. However, the voltage is not the same in the whole power system, it is provided locally.

## Control system
The active power balance between power generation and demand in the power system can be disturbed by several different factors. These can for instance be variations of weather dependent power generation and demand or outages of generation units or transmission lines. Therefore, a sophisticated control system is required in order to maintain the required balance. In the event of a large generating unit outage, standby regulating capacity must fill its place. Three such examples of large nuclear outages in Sweden are shown below.

<p align="center">
  <img width="480" height="300" src="/images/outages.jpeg">
</p>

In all examples, the frequency fell initially and then recovered back to normal levels. This is thanks to several stabilising mechanisms that are used to control the frequency. These mechanisms operate on different time scales given in the table presented below.

<table>
  <thead>
    <tr>
      <th>Mechanism</th>
      <th>Time scale</th>
      <th>Activation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Inertia</td>
      <td>Instantaneous</td>
      <td>Physical</td>
    </tr>
    <tr>
      <td>Primary regulation</td>
      <td>Seconds to minutes</td>
      <td>Automatic</td>
    </tr>
    <tr>
      <td>Secondary regulation</td>
      <td>Minutes to hours</td>
      <td>Automatic</td>
    </tr>
    <tr>
      <td>Tertiary regulation</td>
      <td>Minutes to hours</td>
      <td>Manual</td>
    </tr>
  </tbody>
</table>

We already discussed the inertia of rotating machinery and its analogy to the bike. The other mechanisms are regulating power on different time scales. The primary regulation is specific power units (often hydro power in Sweden) that have frequency sensitive equipment attached to them. This equipment controls the unit to increase production as frequency falls and decrease production as it rises. The goal of the primary regulation is to stop the frequency from changing. In the Nordic power system there is about 600 MW of primary regulation (of which 250 MW in Sweden) available within 50 \\( \pm \\) 0.1 Hz. To take the frequency back to 50 Hz, the tertiary regulation is used. The existence and role of secondary regulation changes somewhat from different countries. An example of how the different variables interplay in the case of an outage (and redeployment) of a 30 MW production unit is illustrated below.

<p align="center">
  <img width="520" height="350" src="/images/power-system-control.jpeg">
</p>

Most regulating power is part of the spinning reserve. This means that they are already connected to the power system and just need to ramp their power output to contribute to balancing the grid. There is also regulating power in form of non-spinning reserve. These are not already connected to the power system but can be brought online after a short delay (start-up time). The spinning reserve is generally more reliable than the non-spinning reserve.  

As mentioned, the TSO has the responsible of keeping the frequency at nominal level. In order to achieve that, they have several tools at their disposal that all together constitutes the full control system. The full strategy of the Swedish TSO for keeping the balance in the power system is given by the table below. Notice that frequencies are approximate.

<table>
  <thead>
    <tr>
      <th>Frequency [Hz]</th>
      <th>Measure</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Always</td>
      <td>Export/import of electricity to/from neighbouring areas</td>
    </tr>
    <tr>
      <td>49.9-50.1</td>
      <td>Activation of primary and secondary regulation</td>
    </tr>
    <tr>
      <td>49.8-49.9</td>
      <td>Activation of tertiary regulation and pumping stop</td>
    </tr>
    <tr>
      <td>49.5-49.7</td>
      <td>Activation of gas turbines and automatic load shedding of heat pumps and boilers</td>
    </tr>
    <tr>
      <td>49.0-49.7</td>
      <td>Power reserve and emergency power DC-links</td>
    </tr>
    <tr>
      <td>Below 49.0</td>
      <td>Manual load shedding of specific regions</td>
    </tr>
  </tbody>
</table>

## Power quality
A part from voltage and frequency regulation issues, the loads in a power system can be adversely affected by a range of temporal issues. This can for example be voltage sags, dips and swells, transient overvoltages, flicker and high frequency noise (also called harmonics). All these are basically deviations from an AC perfect sine wave with current and voltage in-sync at a prescribed frequency and voltage. Power quality issues is a complete topic by itself. However, it is good to know that it exists and the some specialist in specialist industrial machinery or hospital equipment might be sensitive to it.

## Conclusion
This post gives a glance into how power system works. There is of course a lot more to it. But with this basic understanding, it is possible to make qualitative arguments on how different changes or events would affect the system. For example, what would be the implications of more intermittent wind power in the power system? Or what happens if a large production unit goes down? The next step is to link the physical constraints of the power system with market design, but that is the topic for another post.

### References
* Lennart Söder, På väg mot en elförsörjning baserad på enbart förnybar el i Sverige, 2014
* Svenska Kraftnät, [www.svk.se](http://www.svk.se/en)
* Wikipedia, [Ancillary services](https://en.wikipedia.org/wiki/Ancillary_services_(electric_power))
* Wikipedia, [Electrical power system](https://en.wikipedia.org/wiki/Electric_power_system)
