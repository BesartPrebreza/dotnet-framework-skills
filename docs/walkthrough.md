# Warehouse stock report

Suppose a warehouse has five units at 45.00 and an item has two historical receipt records. Joining inventory to receipts before aggregation can double both the quantity and the value. Establish one current record per article and barcode per warehouse, then sum verified quantities or use the latest event according to the source data model.

Adapt the Web API 2 conventions, SQL Server query review, EF6 data access and resource authorization guidance to the project. Verify that an authorized warehouse returns an amount of 225.00, a second warehouse stays excluded, and an unauthorized caller is denied before the stock read. Use the same seeded data and assertions for both runs when comparing agent results with and without the skills. Record the model, prompt, changed files, and test output in the evaluation.
