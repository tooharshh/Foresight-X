# Shakelytics

Web-based visualization platform for exploring Indian seismic activity using Kepler.gl and Flask.

## Motivation

I came across this blog [this Medium article](https://towardsdatascience.com/visualizing-indias-seismic-activity-4ed390de298c) and thought to try the Kepler.Gl tool out myself. I planned to create a simple and interactive dashboard for users to see earthquakes across the Indian Plate.

## What I Built

- **Flask Dashboard** with three interactive map views (All Events, Major Events ≥5.0, Timeline)
- **Data Cleaning** process to validate and format 10,000+ seismic events from NCS
- **Statistics Page** showing key metrics and top earthquakes

## Building Blocks

- **Kepler.gl** 
- **Flask**
- **Pandas**
- **Jupyter Notebook**

## Installation

**Steps:**

1. **Enable Long Paths**
   
   Run PowerShell as Administrator:
   ```powershell
   New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
   ```
   Restart your terminal after this.

2. **Create venv**
   ```powershell
   python3.11 -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Generate Maps**
   
   Open and run the Jupyter notebook:
   ```powershell
   jupyter notebook kepler_geoanalysis.ipynb
   ```
   Maps will be automatically saved to `static/maps/`.

5. **Run Dashboard**
   ```powershell
   python app.py
   ```
   Open browser to `http://localhost:5000`


## Dataset

- **Source**: [National Center of Seismology - Earthquake Archive](https://riseq.seismo.gov.in/riseq/earthquake/archive)
- **Time Period**: 2014-2025 (11 years)