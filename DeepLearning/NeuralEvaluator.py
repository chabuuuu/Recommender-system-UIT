import numpy as np
import pandas as pd
from libreco.evaluation import evaluate

class NeuralEvaluator:
    def __init__(self, model, testing_set, data_info, products):
        self.model = model
        self.testing_set = testing_set
        self.data_info = data_info
        self.products = products

    def calculate_rmse(self):
        results = evaluate(self.model, self.testing_set, neg_sampling=False, metrics=["rmse"])
        return results["rmse"]

    def calculate_mae(self):
        results = evaluate(self.model, self.testing_set, neg_sampling=False, metrics=["mae"])
        return results["mae"]

    def calculate_hr(self, k=10):
        results = evaluate(self.model, self.testing_set, neg_sampling=True, metrics=[f"hit@{k}"])
        return results[f"hit@{k}"]

    def calculate_chr(self, k=10):
        results = evaluate(self.model, self.testing_set, neg_sampling=True, metrics=[f"chit@{k}"])
        return results[f"chit@{k}"]

    def calculate_arhr(self, k=10):
        results = evaluate(self.model, self.testing_set, neg_sampling=True, metrics=[f"arhr@{k}"])
        return results[f"arhr@{k}"]

    def calculate_coverage(self):
        results = evaluate(self.model, self.testing_set, neg_sampling=False, metrics=["coverage"])
        return results["coverage"]

    def calculate_diversity(self):
        results = evaluate(self.model, self.testing_set, neg_sampling=False, metrics=["diversity"])
        return results["diversity"]

    def calculate_novelty(self):
        results = evaluate(self.model, self.testing_set, neg_sampling=False, metrics=["novelty"])
        return results["novelty"]

    def evaluate_all(self):
        metrics = {
            "RMSE": self.calculate_rmse(),
            "MAE": self.calculate_mae(),
        # #    "HR@10": self.calculate_hr(k=10),
        # #    "cHR@10": self.calculate_chr(k=10),
        # #    "ARHR@10": self.calculate_arhr(k=10),
        #    "Coverage": self.calculate_coverage(),
        #    "Diversity": self.calculate_diversity(),
        #    "Novelty": self.calculate_novelty(),
        }
        return metrics
