# hydra_dvc_minimal_example
Minimal example to explore workflows using hydra and DVC

## Setup

```
pyenv install 3.9.4
pyenv virtualenv 3.9.4 hydra_dvc_minimal_example
pyenv local hydra_dvc_minimal_example
pyenv activate hydra_dvc_minimal_example
python -m pip install -r requirements.txt
```

`dvc[s3]` installed on my machine straight from pyPI. If there are issues, refer to these [instructions](https://github.com/1QB-Information-Technologies/ml_allianz_dq).

## Examples

### General Structure
```
├── configs #hierarchical configuration directory
│   ├── main.yaml # main configuration, loads other config files
│   └── model
│       └── mymodel.yaml # default model configuration
├── hydra_instantiate.py
├── models
│   └── model.py # example class to test instantiation parameters
```

### Hydra Instantiation
Hydra provides the neat feature of steering instantiation through the configuration. This means, you can decide on config-level which object to instantiate in the code.
A use case would be using different models or training engines in ML experiments, without changing the code base.

The following script creates instances of `models.model.MyModel` dynamically. Note that no `import` statement is needed in the script. The first instance uses the parameter `name` as set in the `configs/model/mymodel.yaml` file. The second instance is created with an overwrite of this parameter in the code base itself.
The third way of creating this instance is by overwriting the option in the command line
```
python hydra_instantiate.py
python hydra_instantiate.py model.name=whatatool
```

