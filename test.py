from pyledaq.adc import continuous_data
import h5py

task = continuous_data(100000,["Dev1/ai0","Dev1/ai1"],h5file=h5py.File("test.hdf5",'a'))

task.start()

input()


task.stop()
