Nicholas Stryker - CSC718 - Final Project

# Dependencies, need to be installed prior to running NN.py and NN_MPI.py 
Python 3.9
pip3 install cython
pip3 install numpy
pip3 install mpi4py

# How to run the program
## data txt must be in the following directory from the Python.
./data/training_data/noaa51003
51003h1991.txt
51003h2010.txt
51003h2011.txt
51003h2012.txt
51003h2013.txt

python3.9 NN.py
mpirun -n 4 python3.9 NN_MPI.py

# Average run time and expected output

python3.9 NN.py

Version Information:
   Python: 3.8.6 (default, Sep 25 2020, 09:36:53) 
[GCC 10.2.0]
   numpy: 1.19.1
   Matplotlib: 3.2.2
[+] Ingesting file: 51003h2010.txt
Finished ingesting information:
[+] Instantiating Neural Network: 
[+] Building layers: 
[+] Finalizing model: 
[+] Ingesting evaluation data: 
[+] Ingesting file: 51003h2011.txt
Finished ingesting information:
[+] Begin training: 
epoch: 1000
step: 0, acc: 0.032, loss: 0.003 (data_loss: 0.003, reg_loss: 0.000), lr: 0.0002501250625312656
training, acc: 0.032, loss: 0.003 (data_loss: 0.003, reg_loss: 0.000), lr: 0.0002501250625312656
epoch: 2000
step: 0, acc: 0.428, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.00016672224074691563
training, acc: 0.428, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.00016672224074691563
epoch: 3000
step: 0, acc: 0.909, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.00012503125781445363
training, acc: 0.909, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.00012503125781445363
epoch: 4000
step: 0, acc: 0.991, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.00010002000400080015
training, acc: 0.991, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.00010002000400080015
epoch: 5000
step: 0, acc: 0.997, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 8.334722453742292e-05
training, acc: 0.997, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 8.334722453742292e-05
validation, acc: 0.914, loss: 0.017
Execution time in seconds: 532.5013997554779


mpirun -n 4 python3.9 NN_MPI.py

