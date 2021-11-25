# Reconciliation methods
- Material flow in an industrial process can be represented as a directed graph with adjacency matrix $A$
- If path $j$ goes into node $i$ and path $k$ flows out of node $i$, then $A_{ij} = 1$ and $A_{ik} = -1$ to represent
steady state as input = output
- Mah et al. provide ways to do this when nodes are unmeasured; example: I can measure the flows into and out of the
water heater (boiler) by using the meter outside the house and measuring the volume out of the tap
    + The key is to aggregate nodes; I treat the tap + water heater as one unit for analysis; Mah et al. lay out the
    assumptions required to do this, to estimate measurement error accounting for unmeasured nodes, and to estimate flow
    through unmeasured nodes
    + [Original paper](https://gregstanleyandassociates.com/ReconciliationRectificationProcessData-1976.pdf)
    + [Less graph theory, more statistical tests](http://users.iems.northwestern.edu/~ajit/papers/64) Data Reconciliation-Technometrics Paper.pdf)
- [Himmelblau and Karjala (among others) propose using a recurrent neural network to do this](http://nn.cs.utexas.edu/downloads/papers/karjala.ijcnn92.pdf)
    + This paper also gives a simple model process--filling and draining a tank and reconciling measurements on input
    flow, output flow, and liquid height
# SHAP
- [SHAP](https://github.com/slundberg/shap) uses simple models as 'explainers' of neural network fits
- The importance of a feature, as assessed using SHAP, is an estimate of the difference in average prediction error between all
possible models _with_ the feature vs. the average prediction error in all models _without_ the feature

# The connection
- Mah, Stanley, and Downing propose an error detection algorithm that steps through all connected subgraphs of the
material flow graph and assesses a error statistic in each subgraph
- SHAP (applied to the training data) summarizes error statistics for all subgraphs
    + If we assume that SHAP values are most influenced by connected subgraphs it should be the case that SHAP values
    allow us to identify:
        i. the features with the largest error variances
        ii. the observations with the largest errors

# Plan
- Generate data from the tank model and apply errors as in Karjala, Himmelblau and Miikkulainen
- Fit WLS and RNN models to the tank model
- Apply SHAP to the resulting fits
- Compare measurement error variances to SHAP value variances (i)
- Use Spearman correlation of SHAP values and errors to assess their association (ii)

# Notes 

# Half-baked ideas 
- Improper RNN conjecture: there is some "closest" moving average to a(n equivalence class of) regularized RNN layer(s) that makes the layers understandable 
- Use `simpy` or `mesa` for something in this

# Other references
- [Elman finding structure in time](https://crl.ucsd.edu/~elman/Papers/fsit.pdf)
- [Shapley papers](https://www.rand.org/pubs/authors/s/shapley_lloyd_s.html)