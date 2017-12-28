### About

This project aims to implement a Nest model of Motor neuron from an article [Compartmental model of vertebrate motoneurons for Ca2+-dependent spiking and plateau potentials under pharmacological treatment.](https://www.ncbi.nlm.nih.gov/pubmed/9405551) by Booth V, Rinzel J, Kiehn O. By the time of writing this README the article was accessible [here](https://www.researchgate.net/profile/Ole_Kiehn2/publication/13823785_Compartmental_Model_of_Vertebrate_Motoneurons_for_Ca2-dependent_Spiking_and_plateau_potentials_under_pharmacological_treatment/links/0deec53301bfc0a436000000.pdf?origin=publication_detail).

#### Build
To build the model for Nest:
```
java -jar <path to nestml 'target' dir>nestml.jar <hh-moto-booth-1997 path> --target <build_dir>
```

More details in the [Nestml repo](https://github.com/nest/nestml/#installing-and-running-nestml)

#### Verification

We use an existing [Neuron implementation](https://senselab.med.yale.edu/ModelDB/showmodel.cshtml?model=189786) of the same model for verification.