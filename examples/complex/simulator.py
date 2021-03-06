# %%
"""
This script simulates the 1D Gaussians + Exponential profile dataset used throughout the example scripts.
"""

# %%
#%matplotlib inline

from autofit_workspace.examples.complex import model as m
import numpy as np

# %%
"""
__Gaussian x1 + Expoonential x1__

Create a model instance of the Gaussian and Exponential.
"""

# %%
gaussian = m.Gaussian(centre=50.0, intensity=25.0, sigma=10.0)
exponential = m.Exponential(centre=30.0, intensity=10.0, rate=0.1)

# %%
"""
Specify the number of pixels used to create the xvalues on which the 1D line of the profile is generated using and
thus defining the number of data-points in our data.
"""

# %%
pixels = 100
xvalues = np.arange(pixels)

# %%
"""
Evaluate this Gaussian and Exponential model instances at every xvalues to create their model profiles and add 
them together.
"""

# %%
model_line = gaussian.profile_from_xvalues(
    xvalues=xvalues
) + exponential.profile_from_xvalues(xvalues=xvalues)

# %%
"""
Determine the noise (at a specified signal to noise level) in every pixel of our model profile.
"""

# %%
signal_to_noise_ratio = 25.0
noise = np.random.normal(0.0, 1.0 / signal_to_noise_ratio, pixels)

# %%
"""
Add this noise to the model line to create the line data that is fitted, using the signal-to-noise ratio to compute
noise-map of our data which is required when evaluating the chi-squared value of the likelihood.
"""

# %%
data = model_line + noise
noise_map = (1.0 / signal_to_noise_ratio) * np.ones(pixels)


# %%
"""
__Gaussian X1 (0)__

Create a model instance of the Gaussians.
"""

# %%
gaussian = m.Gaussian(centre=50.0, intensity=25.0, sigma=1.0)

# %%
"""
Specify the number of pixels used to create the xvalues on which the 1D line of the profile is generated using and
thus defining the number of data-points in our data.
"""

# %%
pixels = 100
xvalues = np.arange(pixels)

# %%
"""
Evaluate this Gaussian model instance at every xvalues to create its model profile.
"""

# %%
model_line = gaussian.profile_from_xvalues(xvalues=xvalues)

# %%
"""
Determine the noise (at a specified signal to noise level) in every pixel of our model profile.
"""

# %%
signal_to_noise_ratio = 25.0
noise = np.random.normal(0.0, 1.0 / signal_to_noise_ratio, pixels)

# %%
"""
Add this noise to the model line to create the line data that is fitted, using the signal-to-noise ratio to compute
noise-map of our data which is required when evaluating the chi-squared value of the likelihood.
"""

# %%
data_0 = model_line + noise
noise_map_0 = (1.0 / signal_to_noise_ratio) * np.ones(pixels)

# %%
"""
__Gaussian X1 (1)__

Create a model instance of the Gaussian.
"""

# %%
gaussian = m.Gaussian(centre=50.0, intensity=25.0, sigma=5.0)

# %%
"""
Specify the number of pixels used to create the xvalues on which the 1D line of the profile is generated using and
thus defining the number of data-points in our data.
"""

# %%
pixels = 100
xvalues = np.arange(pixels)

# %%
"""
Evaluate this Gaussian model instance at every xvalues to create its model profile.
"""

# %%
model_line = gaussian.profile_from_xvalues(xvalues=xvalues)

# %%
"""
Determine the noise (at a specified signal to noise level) in every pixel of our model profile.
"""

# %%
signal_to_noise_ratio = 25.0
noise = np.random.normal(0.0, 1.0 / signal_to_noise_ratio, pixels)

# %%
"""
Add this noise to the model line to create the line data that is fitted, using the signal-to-noise ratio to compute
noise-map of our data which is required when evaluating the chi-squared value of the likelihood.
"""

# %%
data_1 = model_line + noise
noise_map_1 = (1.0 / signal_to_noise_ratio) * np.ones(pixels)

# %%
"""
__Gaussian X1 (2)__

Create a model instance of the Gaussian.
"""

# %%
gaussian = m.Gaussian(centre=50.0, intensity=25.0, sigma=10.0)

# %%
"""
Specify the number of pixels used to create the xvalues on which the 1D line of the profile is generated using and
thus defining the number of data-points in our data.
"""

# %%
pixels = 100
xvalues = np.arange(pixels)

# %%
"""
Evaluate this Gaussian model instance at every xvalues to create its model profile.
"""

# %%
model_line = gaussian.profile_from_xvalues(xvalues=xvalues)

# %%
"""
Determine the noise (at a specified signal to noise level) in every pixel of our model profile.
"""

signal_to_noise_ratio = 25.0
noise = np.random.normal(0.0, 1.0 / signal_to_noise_ratio, pixels)

# %%
"""
Add this noise to the model line to create the line data that is fitted, using the signal-to-noise ratio to compute
noise-map of our data which is required when evaluating the chi-squared value of the likelihood.
"""

# %%
data_2 = model_line + noise
noise_map_2 = (1.0 / signal_to_noise_ratio) * np.ones(pixels)
