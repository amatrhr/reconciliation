# Reconciliation methods
- Material flow in an industrial process can be represented as a directed graph with adjacency matrix $A$
- If path $j$ goes into node $i$ and path $k$ flows out of node $i$, then $A_{ij} = 1$ and $A_{ik} = -1$ to represent
steady state as input = output
- Mah et al. provide ways to do this when nodes are unmeasured; example: I can measure the flows into and out of the
water heater (boiler) by using the meter outside the house and measuring the volume out of the tap
    + The key is to aggregate nodes; I treat the tap + water heater as one unit for analysis; Mah et al. lay out the
    assumptions required to do this, to estimate measurement error accounting for unmeasured nodes, and to estimate flow
    through unmeasured nodes
    + [https://gregstanleyandassociates.com/ReconciliationRectificationProcessData-1976.pdf](Original paper)
    + [http://users.iems.northwestern.edu/~ajit/papers/64)%20Data%20Reconciliation-Technometrics%20Paper.pdf](Less graph theory, more statistical tests)
- [http://nn.cs.utexas.edu/downloads/papers/karjala.ijcnn92.pdf]()Himmelblau and Karjala (among others) propose using a recurrent neural network to do this)

# SHAP
- [https://github.com/slundberg/shap](SHAP) uses simple models as 'explainers' of neural network fits
- The importance of a feature, as assessed using SHAP, is an estimate of the difference in average prediction error between all
possible models _with_ the feature vs. the average prediction error in all models _without_ the feature

# The connection
- Mah, Stanley, and Downing propose an error detection algorithm that steps through all connected subgraphs of the
material flow graph and assesses a error statistic in each subgraph
- SHAP (applied to the training data) summarizes error statistics for all subgraphs
    +
