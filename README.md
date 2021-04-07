# PlotFalcon9

This is a quick python script made by RaSkk on twitch to extract the gps infos from the gps_debug file from a downlink capture and plot them on a map.

# Usage

## Prerequisite

On Ubuntu 20.10, you need to install python3-pyproj and python3-cartopy.
`sudo apt install python3-pyproj python3-cartopy`

You need to have a gps_debug.txt file from SatDump analysis.

## Running it

Put the gps_debug.txt in the same folder and launch 
`python3 PlotGPS.py`

the file `output.png` is created. 

# State of this project

This is a very preliminary project. It's more a proof of concept, and a lot is to be done. For example, the Zoom on the map is static on Europe and should be dynamic on the trajectory.
