
# DeepTrust^RT: Confidential Deep Neural Inference Meets Real-Time!

This repository have necessary code and instruction to implement our DeepTrust^RT project.

## Testing Platform

We use the following environment to perform the test:
1. 4x ARM Cortex A53, 1 GB RAM (Raspberry Pi 3 B)

3. Linux 6.2.0

3. OP-TEE 3.19.0

## OP-TEE installation

Install OP-TEE by following instruction from here [OP-TEE Documentation](https://optee.readthedocs.io/en/latest/building/index.html)

To install optee in Raspebrry Pi, follow this instruction: [install OP-TEE on Raspberry Pi](https://optee.readthedocs.io/en/latest/building/devices/rpi3.html)

## Building DeepTrust^RT 

Clone Darkentz from this repo to `<optee_dir>/optee_examples` folder

Download necessary weight, cfg, dataset file from here [Darknet Site](https://pjreddie.com/darknet/) and put those files in `$optee_dir$/out-br/target/root/` directory

Flash the device following OP-TEE documentation.

## Running the Code

Login with password root

Run the command to get the layerwise execution time na dlayer-size using the following command: `darknetp classifier predict -pp_start 2 -pp_end 3 <path to dataset> <path to cfg> <path to weights> <path to test image>`

Run this command to get the necessary data and use those data in `task_sched_response.py` to get the response time. we use those data in `subplot_res.py` and `subplot_sched.py` to get the plot.




