# CAMB-Cobaya-Workshop

Welcome to the CAMB-Cobaya workshop! In this workshop, you will learn the basics of CAMB (how to compute CMB and matter power spectra for instance) and Cobaya (how to perform an MCMC analysis) as well as more advanced features.


## Softwares

In this workshop, you will need to have CAMB, Cobaya and Getdist installed. Those three codes can be installed with pip and it should only require to type:

> pip install camb

> pip install cobaya

> pip install getdist

You can find more information about those three codes on:  
https://camb.readthedocs.io/en/latest/  
https://cobaya.readthedocs.io/en/latest/  
https://github.com/cmbant/getdist  

Once Cobaya is installed, you will need to install the latest Planck likelihood using

> python -m cobaya install planck_NPIPE_highl_CamSpec.TTTEEE
