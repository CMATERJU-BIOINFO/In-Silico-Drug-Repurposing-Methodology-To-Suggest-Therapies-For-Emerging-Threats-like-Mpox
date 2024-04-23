# Insilico_drug_repurposing_for_viral_threats
![Slide1](https://github.com/CMATERJU-BIOINFO/Insilico_drug_repurposing_for_viral_threats/assets/132830310/53c553bc-44a2-4e8b-9bd9-bc8eb08eea58)

![Slide2](https://github.com/CMATERJU-BIOINFO/Insilico_drug_repurposing_for_viral_threats/assets/132830310/cbce3f1b-5eeb-4821-b25e-29e09fc4d90c)

Monkeypox (Mpox), a zoonotic illness triggered by the monkeypox virus (MPXV), poses a significant threat since it may be transmitted and has no cure. This work introduces a computational method to predict protein-protein interactions (PPIs) during MPXV infection. The objective is to discover prospective drug targets and repurpose current potential Food and Drug Administration (FDA) drugs for therapeutic purposes. In this work, ensemble features, comprising 2-5 node graphlet attributes and protein composition-based features are utilized for deep learning (DL) models to predict PPIs. The technique that is used here demonstrated an excellent prediction performance for PPI on both the Human Integrated Protein-Protein Interaction Reference (HIPPIE) and MPXV-Human PPI datasets. In addition, the human protein targets for MPXV have been identified accurately along with the detection of possible therapeutic targets. Furthermore, the validation process included conducting docking research studies on potential FDA drugs like NADH, Fostamatinib, Glutamic acid, Cannabidiol, Copper, and Zinc in DrugBank identified via research on drug repurposing and the drug consensus score (DCS) for MPXV. This has been achieved by employing the primary crystal structures of MPXV, which are now accessible. The results of our study emphasize the effectiveness of using ensemble feature-based PPI prediction to understand the molecular processes involved in viral infection and to aid in the development of repurposed drugs for emerging infectious diseases such as, but not limited to, Mpox.

## Repository Contents

The **Data directory** contains all the data files referred to by our code to run our proposed model and conduct the experiments.

a) Edge.csv - The protein interaction pairs of the HIPPIE dataset.

b) Edge_combined.csv - The protein interaction pairs of the MPXV-Human dataset.

c) train_edge_pos_data.csv - positive edge index file (HIPPIE dataset) to train the model. 

d) train_edge_neg_data.csv - negative edge index file (HIPPIE dataset) to train the model.

e) test_edge_pos_data.csv - positive edge index file (HIPPIE dataset) to test the model.

f) test_edge_neg_data.csv - negative edge index file (HIPPIE dataset) to test the model.

g) combined_train_edge_pos_data.csv - positive edge index file (MPXV-Human dataset) to train the model. 

h) combined_train_edge_neg_data.csv - negative edge index file (MPXV-Human dataset) to train the model.

i) combined_test_edge_pos_data.csv - positive edge index file (MPXV-Human dataset) to test the model.

j) combined_test_edge_neg_data.csv - negative edge index file (MPXV-Human dataset) to test the model.

k) prot_id_data - file containing protein id to index mapping for HIPPIE dataset.

l) MP_Hippie_combined - file containing protein id to index mapping for MPXV-Human dataset.

The **code directory** contains all the code files.

The **Drug_repurposing_analysis directory** contains all the input required for computing the Drug consensus score as well as the generated output files.

Executable file:- DCSS.py

**Input Files:-**

a) DrugBank.txt - contains mapping of human protein and their drug targets.

b) trgts dbrti.txt - contains the human protein ids succesfully identified as interacting with MPXV by our proposed model. 

c) drugbank idnamemapping.txt - contains mapping of Drugbank Id and their corresponding drug name.

**Output Files:-**

d) Spreaders_drug_map.txt - returns the drugbank Id of the matched drugs of our MPXV targetted Human proteins(mentioned in trgts dbrti.txt)

e) Spreader_drug_name.txt - returns the drug name of the corresponding drug Ids of Output file Spreaders_drug_map.txt.

f) Spreader_drug_frequency.txt (final output) - returns the frequency of occurence of each drug in Spreader_drug_name.txt. 

The **Molecular_docking_results directory** contains all the output files generated by conducting molecular docking of the top four Level I drugs using AutoDockVina suite. Each file contains the docking results like the affinity (kcal/mol) and dist from best mode for 9 binding poses. 

a) Cannabidiol_DB09061_log.txt - contains docking result of Cannabidiol

b) Fostamatinib_log.txt - contains docking result of Fostamatinib

c) Glutamic_Acid__DB00142_log.txt - contains docking result of Glutamic_Acid

d) NADH_log.txt - contains docking result of NADH

## Usage

Step 1- to be added





