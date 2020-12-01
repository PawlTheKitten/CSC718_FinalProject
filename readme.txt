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

[+] Ingesting file: 51003h2010.txt
Finished ingesting information:
[+] P0 Ingesting evaluation data: 
[+] Ingesting file: 51003h1991.txt
Finished ingesting information:
[+] P0 Instantiating NN learning_rate = 0.005 decay = 0.01
[+] P0 Building layers: 
[+] P0 training: 
epoch: 1000
Results for process 0 of 4 on kali for epoch 1000
P 0 training, acc: 0.549, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.0004549590536851683
epoch: 2000
Results for process 0 of 4 on kali for epoch 2000
P 0 training, acc: 0.945, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.00023820867079561695
epoch: 3000
Results for process 0 of 4 on kali for epoch 3000
P 0 training, acc: 0.988, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.00016134236850596964
epoch: 4000
Results for process 0 of 4 on kali for epoch 4000
P 0 training, acc: 0.998, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.00012198097096852891
epoch: 5000
Results for process 0 of 4 on kali for epoch 5000
P 0 training, acc: 0.998, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 9.805844283192783e-05
============================================================================
Validation results for process 0 of 4 on kali
P 0 validation, acc: 0.994, loss: 0.000
============================================================================
P:0 Execution time in seconds: 690.0434861183167
[+] Ingesting file: 51003h2011.txt
Finished ingesting information:
[+] P1 Ingesting evaluation data: 
[+] Ingesting file: 51003h1991.txt
Finished ingesting information:
[+] P1 Instantiating NN learning_rate = 0.09 decay = 0.02
[+] P1 Building layers: 
[+] P1 training: 
epoch: 1000
Results for process 1 of 4 on kali for epoch 1000
P 1 training, acc: 0.007, loss: 0.573 (data_loss: 0.573, reg_loss: 0.000), lr: 0.004289799809342231
epoch: 2000
Results for process 1 of 4 on kali for epoch 2000
P 1 training, acc: 0.007, loss: 0.573 (data_loss: 0.573, reg_loss: 0.000), lr: 0.0021961932650073203
epoch: 3000
Results for process 1 of 4 on kali for epoch 3000
P 1 training, acc: 0.007, loss: 0.573 (data_loss: 0.573, reg_loss: 0.000), lr: 0.001475893735651033
epoch: 4000
Results for process 1 of 4 on kali for epoch 4000
P 1 training, acc: 0.007, loss: 0.573 (data_loss: 0.573, reg_loss: 0.000), lr: 0.0011113855272906889
epoch: 5000
Results for process 1 of 4 on kali for epoch 5000
P 1 training, acc: 0.007, loss: 0.573 (data_loss: 0.573, reg_loss: 0.000), lr: 0.00089126559714795
============================================================================
Validation results for process 1 of 4 on kali
P 1 validation, acc: 0.000, loss: 0.580
============================================================================
P:1 Execution time in seconds: 745.696825504303
[+] Ingesting file: 51003h2013.txt
Finished ingesting information:
[+] P3 Ingesting evaluation data: 
[+] Ingesting file: 51003h1991.txt
Finished ingesting information:
[+] P3 Instantiating NN learning_rate = 0.0009 decay = 1e-06
[+] P3 Building layers: 
[+] P3 training: 
epoch: 1000
Results for process 3 of 4 on kali for epoch 1000
P 3 training, acc: 0.008, loss: 0.001 (data_loss: 0.001, reg_loss: 0.000), lr: 0.0008991017973044929
epoch: 2000
Results for process 3 of 4 on kali for epoch 2000
P 3 training, acc: 0.818, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.0008982044892260371
epoch: 3000
Results for process 3 of 4 on kali for epoch 3000
P 3 training, acc: 0.976, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.0008973089703977771
epoch: 4000
Results for process 3 of 4 on kali for epoch 4000
P 3 training, acc: 0.262, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.000896415235473342
epoch: 5000
Results for process 3 of 4 on kali for epoch 5000
P 3 training, acc: 0.674, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.0008955232791276409
============================================================================
Validation results for process 3 of 4 on kali
P 3 validation, acc: 0.008, loss: 0.000
============================================================================
P:3 Execution time in seconds: 779.340368270874
[+] Ingesting file: 51003h2012.txt
Finished ingesting information:
[+] P2 Ingesting evaluation data: 
[+] Ingesting file: 51003h1991.txt
Finished ingesting information:
[+] P2 Instantiating NN learning_rate = 0.001 decay = 1e-05
[+] P2 Building layers: 
[+] P2 training: 
epoch: 1000
Results for process 2 of 4 on kali for epoch 1000
P 2 training, acc: 0.156, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.0009901088129585442
epoch: 2000
Results for process 2 of 4 on kali for epoch 2000
P 2 training, acc: 0.001, loss: 0.001 (data_loss: 0.001, reg_loss: 0.000), lr: 0.0009804017686447907
epoch: 3000
Results for process 2 of 4 on kali for epoch 3000
P 2 training, acc: 0.991, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.0009708832124583735
epoch: 4000
Results for process 2 of 4 on kali for epoch 4000
P 2 training, acc: 0.994, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.0009615477071894923
epoch: 5000
Results for process 2 of 4 on kali for epoch 5000
P 2 training, acc: 0.997, loss: 0.000 (data_loss: 0.000, reg_loss: 0.000), lr: 0.0009523900227621216
============================================================================
Validation results for process 2 of 4 on kali
P 2 validation, acc: 0.991, loss: 0.000
============================================================================
P:2 Execution time in seconds: 786.5464541912079