### About

This project aims to implement a Nest model of Motor neuron from an existing [Neuron simulator implementation](https://senselab.med.yale.edu/ModelDB/showmodel.cshtml?model=189786) by Moraud EM, Capogrosso M.

#### Build
To build the model for Nest:
```
java -jar <path to nestml 'target' dir>nestml.jar hh-moto-5ht --target <build_dir>
```

More details in the [Nestml repo](https://github.com/nest/nestml/#installing-and-running-nestml)

#### Verification

We use an existing Neuron implementation of the same model for verification.