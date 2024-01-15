# Fire_Dynamics
Simulation and Prediction system to identify how fire will spread in a given controlled environment using point cloud.
## System Requirements
* Intel i5 9th Generation
* NVIDIA GeForce FTX 1650 (4GB)
* Windows 10 | 11 | Debian
* 16 GB RAM
## Software Requirements
* Python 3.10.x
* Pandas
* Matplotlib
* NumPy
* Cloud compare
## Procedure
### FDM 2D Sim
* Run <code>pip install -r requirements.txt</code>
* Adjust fuel addition probability, fuel distribution probability, wind direction,ignition points etc in the FDM parameters.
* Open new terminal in the project location.
* Run <code>python FDM_2D_Sim.py</code>