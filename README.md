# Pygal Dice and Choice Simulations

This project contains a collection of Python scripts that use the `pygal` library to simulate and visualize random events, such as rolling dice and making random choices. The scripts generate interactive SVG charts to display the probability distributions of the outcomes.

## Visualizations

### 1. Dice Roll Simulations
* **Scripts:** `dice_visual.py`, `different_dice.py`
* **Description:** These scripts simulate rolling one or two dice with a variable number of sides. They calculate the frequency of each outcome and generate interactive bar charts (histograms) to visualize the results.

### 2. Random Walk/Choice Simulation
* **Scripts:** `choose.py`, `choose_visual.py`
* **Description:** This script simulates a series of random choices or steps, similar to a random walk. It then uses `pygal` to generate a line chart visualizing the path taken over the course of the simulation.

## Technologies Used
* **Python 3**
* **Pygal:** For generating interactive SVG charts.

## How to Run

### 1. Setup
Clone the repository and install the required libraries from the `requirements.txt` file:
```bash
git clone https://github.com/turganaliev/pygal.git
cd pygal
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# On Windows, use: .\venv\Scripts\activate
pip install -r requirements.txt
```
### 2. Execution
Run any of the visualization scripts from your terminal:
```bash
python dice_visual.py
python different_dice.py
python choose_visual.py
```
