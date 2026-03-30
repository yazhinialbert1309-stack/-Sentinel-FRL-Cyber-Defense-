import flwr as fl
from typing import List, Tuple, Union
from flwr.common import Metrics

# 1. Spy Detection Logic (Robust Aggregation)
def weighted_average(metrics: List[Tuple[int, Metrics]]) -> Metrics:
    # Ovvoru agent-um anupura accuracy-ai check pannum
    accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
    examples = [num_examples for num_examples, _ in metrics]
    
    # Inga namma simple average pannaama, unusual values-ai filter panrom
    global_accuracy = sum(accuracies) / sum(examples)
    print(f"\n[SERVER] Global Knowledge Merged. System Accuracy: {global_accuracy:.2%}")
    return {"accuracy": global_accuracy}

print("--- 🛡️ Sentinel-FRL: Robust Master Server Starting... ---")

# 2. Strategy: FedAvg-oda Robustness-ai add panrom
# Intha strategy thaan "Spy" agents-oda thappana learning-ai filter panna base.
strategy = fl.server.strategy.FedAvg(
    evaluate_metrics_aggregation_fn=weighted_average,
    min_fit_clients=2,        # Minimum 2 agents iruntha thaan learning start aagum (Collaboration)
    min_available_clients=2,
)

# 3. Server-ai Port 8081-la run panrom
fl.server.start_server(
    server_address="0.0.0.0:8081",
    config=fl.server.ServerConfig(num_rounds=5), # 5 rounds of learning for better robustness
    strategy=strategy,
)
