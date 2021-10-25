#!/usr/bin/python3
"""
Author: Eric Drechsler <eric_drechsler@1qbit.com>
"""

# external libraries
import os
import sys

import hydra
from hydra.utils import instantiate
from omegaconf import OmegaConf


@hydra.main(config_path="./configs/", config_name="main")
def main(cfg=None):

    print(OmegaConf.to_yaml(cfg))

    # instantiate a model using the parameters in the models/model.yaml file
    model = instantiate(cfg.model)
    print("Model from yaml: {0}".format(model))

    # instantiate model with new parameter
    model2 = instantiate(cfg.model, name="anothermodel")
    print("Model from script: {0}".format(model2))

    return


if __name__ == "__main__":
    main()
