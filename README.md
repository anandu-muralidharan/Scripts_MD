# Scripts_MD
Here, I will be uploading scripts which I will be using to extract data from my MD simulation datafiles.

1. E0_T0_plot.py ---> Use this script to extract the plot between (energy and temperature) wrt the time-step of the MD simulation.
   - First run this program and then select the OSZICAR file from the GUI pop up menu.
   - The script will runa and output the (energy and temperature) wrt the timestep.
   - An example is given below -
   - ![image](https://github.com/user-attachments/assets/034876be-c65d-4fb5-ada8-fe4e7543644c)

2. distance_between_atoms.py ---> Use this script to plot how the distance between two different atoms changes wrt timestep. Use data from XDATACR
   - Change the index inside the code to which atoms you want to check (Check via XDATCAR file)
   - Run the code
   - Select the XDATCAR file
   - The plot will be obtained
   - An example is shown here -
   - ![image](https://github.com/user-attachments/assets/30b30060-4811-4a98-914d-2790b9175bcf)

3. Combine_oszicar.py ---> Use this code to concat more OSZICAR files.
   - First run the script.
   - Input the number of OSZICAR files you have.
   - Select the various OSZICAR files from the GUI pop up window.
   - The combined OSZICAR can be saved in any location in .txt format.
   
