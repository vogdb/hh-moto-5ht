### About

This project aims to implement a Nest model of Motor neuron from an existing [Neuron simulator implementation](https://senselab.med.yale.edu/ModelDB/showmodel.cshtml?model=189786) by Moraud EM, Capogrosso M.

#### Build
The below instructions are given for the **project's root.**
To build the model for Nest:
```
java -jar <path to nestml 'target' dir>nestml.jar research_team_models --target build
```

To install the built in Nest:
```
cd build
cmake -Dwith-nest=$NEST_INSTALL_DIR/bin/nest-config .
make all
make install
```

More details in the [Nestml repo](https://github.com/nest/nestml/#installing-and-running-nestml)

#### Verification

We use an existing Neuron implementation of the same model for verification.