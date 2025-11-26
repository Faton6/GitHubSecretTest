#!/usr/bin/env python3
"""
Validation script to compare tool results with ground truth
Measures: Precision, Recall, F1-score, False Positive Rate
"""

import json
import sys
from pathlib import Path
from typing import Set, Tuple, Dict

class ResultValidator:
    """Validates tool results against ground truth"""
    
    def __init__(self, ground_truth_file: str = "ground_truth.json"):
        self.ground_truth = self._load_ground_truth(ground_truth_file)
        self.true_secrets = self._extract_true_secrets()
    
    def _load_ground_truth(self, file_path: str) -> Dict:
        """Load ground truth from JSON"""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: {file_path} not found")
            sys.exit(1)
    
    def _extract_true_secrets(self) -> Set[Tuple]:
        """Extract set of true secrets as (file_path, line_number) tuples"""
        true_secrets = set()
        for secret in self.ground_truth.get("secrets", []):
            if secret.get("is_valid_secret"):
                key = (secret["file_path"], secret["start_line"])
                true_secrets.add(key)
        return true_secrets
    
    def validate_report(self, report_file: str, tool_name: str) -> Dict:
        """Validate tool report against ground truth"""
        
        try:
            with open(report_file, 'r') as f:
                if report_file.endswith('.json'):
                    report = json.load(f)
                else:
                    report = json.loads(f.read())
        except Exception as e:
            print(f"Error loading report: {e}")
            return {}
        
        # Extract detected secrets from report
        detected = self._parse_report(report, tool_name)
        
        # Calculate metrics
        metrics = self._calculate_metrics(detected, self.true_secrets)
  
