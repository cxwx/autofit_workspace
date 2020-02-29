import autofit as af
import autoarray as aa


class Result(af.Result):
    def __init__(self, instance, figure_of_merit, analysis):
        """
        The result of a non-linear search.

        Parameters
        ----------
        instance: autofit.mapper.model.ModelInstance
            A model instance comprising the model instances that gave the highest likelihood fit.
        figure_of_merit: float
            A value indicating the figure of merit (e.g. the likelihood) given by the highest likelihood fit.
        """
        self.instance = instance
        self.figure_of_merit = figure_of_merit
        self.analysis = analysis

    @property
    def most_likely_model_image(self):
        return self.instance.gaussian.image_from_grid(
            grid=self.analysis.masked_imaging.grid
        )

    @property
    def most_likely_fit(self):
        return self.analysis.fit_from_model_image(
            model_image=self.most_likely_model_image
        )