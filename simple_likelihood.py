from cobaya.likelihood import Likelihood
import numpy as np

# Example of a likelihood implementation for our simple example
class simple_likelihood(Likelihood):

    # In the initialization, we usually load the files and covariance
    def initialize(self):
        self.data = np.load("data_simple_model.npy")
        self.inv_covmat = np.load("inv_cov_simple_model.npy")
        self.x_data = self.data[0]
        self.y_data = self.data[1]
        
    def my_model(self, x, alpha, beta):
        return alpha * x + beta
    
    # In get_requirements, we tell cobaya what parameters we will need to compute the log-likelihood
    def get_requirements(self):
        return {'alpha': None, 'beta': None}
    
    # In case this class can compute some derived parameters, we return that list in the following function
    def get_can_provide_params(self):
        return ['gamma']

    # In logp, we compute and return the log-likelihood and compute the derived parameters
    def logp(self, _derived=None, **params_values):
        
        y_th = self.my_model(self.x_data, params_values['alpha'], params_values['beta'])
        loglike = -0.5*(y_th-self.y_data)@self.inv_covmat@(y_th-self.y_data)
        
        if _derived is not None:
            _derived["gamma"] = self.my_model(1., params_values['alpha'], params_values['beta'])
            
        return loglike                          