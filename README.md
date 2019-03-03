# mf6flopy2019_classrepo
Repository for the MODFLOW 6 / Flopy workshop

Delft, The Netherlands
March 26 - 28, 2019

## Location
* TBD

## Course Description
This workshop will cover new and enhanced capabilities for modeling groundwater flow with MODFLOW 6. The workshop will be taught using Flopy and Jupyter Notebooks.  In addition to lectures on the latest developments, most sessions will include in-class exercises to give attendees a better understanding of how to use the modeling tools.

## Overview
* Tuesday: 
* Wednesday: 
* Thursday: 

## Instructors
* Chris Langevin
* Joe Hughes 
* Mark Bakker
* Frans Schaars

## Agenda

The following tentative agenda is based on a start time each morning of 8:30 AM and an ending time each day of 4:30 PM.  The agenda may be adjusted during the week in response to student requests.

### Tuesday

* Introductions and class overview 
* Flopy introduction
* Flopy exercise fpex01: create, run, and post-process a 3-layer MODFLOW 2005 flow model and MODPATH 7 particle tracking model
* MODFLOW 6 overview (mf6-overview.pptx)

* Input and output (mf6-io.pptx)
* Exercise ex01: create a MODFLOW 6 flow model by hand
* MODFLOW 6 and Flopy
* Exercise ex02: create, run, and post-process a 3-layer regular grid flow model and MODPATH 7 particle tracking model using Flopy
* MODFLOW 6 discretization (mf6-discretization.pptx)

### Wednesday

* Exercise ex03: recreate flow problem using a 3-layer regular grid, but using the Discretization by Vertices (DISV) Package
* XT3D Overview (mf6-xt3d.pptx)
* Exercise ex04: recreate problem using a 3-layer quadtree grid created with the GRIDGEN program and DISV
* Exercise ex05: recreate flow problem using two tightly coupled regular grids using the flopy LGR utility and the GWF-GWF Exchange

* MODFLOW 6 observations and time series (mf6-obs-timeseries.pptx)
* Exercise ex06: adding observations to a model
* MODFLOW 6 Advanced Packages (mf6-advancedpackages.pptx)


### Thursday

* Exercise ex07: converting River (RIV) and Constant Head (CHD) Packages to the Stream Flow Routing (SFR) and Lake (LAK) Packages, with an emphasis on using time series
* Exercise ex08: using the Water Mover (MVR) package to connect streams and lakes

* Special Topics (with interactive demo if desired)
    * No more wetting and drying!  What’s up with the Newton-Raphson Formulation?
    * Status of MODFLOW 6 Subsidence Package
    * Status of MODFLOW 6 Groundwater Transport (GWT) Model 
    * Status of MODFLOW 6 Variable-Density Flow
    * Parameterizing a MODFLOW 6 model for PEST
    * Creating triangular meshes for MODFLOW 6 using the triangle program
* Recap and Adjourn



## Software

Required software: workshop participants will be required to have working copies of a relatively new version of Python capable of running Jupyter Notebooks.  The Anaconda Python distribution is STRONGLY recommended.  The class will rely heavily on the latest version of Flopy (and its dependencies: numpy, matplotlib, etc.), and so users will need to be able to install and update Python packages.  For those using Windows, we will be providing a version of the USGS ModelViewer program that works with MODFLOW 6.

