# Warehouse stock evaluation

Prompt an agent to add a warehouse-scoped stock report with article, barcode, quantity, unit price and total. Use one warehouse with five units at 45.00, a second with a separate stock item and two historical receipts for the first item. Check that the response reports 225.00, preserves the row grain and denies unassigned users. Compare runs with the same source state, model and task. Save diffs, executed checks and scores for authorization, coverage, cardinality and monetary precision.
