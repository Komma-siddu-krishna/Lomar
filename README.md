# LOMAR: Lightweight Explainable Defense for Malicious Clients in Federated Learning

## Overview

LOMAR is a research-oriented Federated Learning (FL) simulation project that demonstrates how malicious client behavior can be identified using model-drift analysis, trust scoring, explainability techniques, and lightweight defense mechanisms.

The project simulates a federated environment where multiple clients contribute model updates. Some clients may behave maliciously by poisoning model parameters or generating abnormal updates. LOMAR analyzes the distance between global and client models, assigns trust scores, and provides interpretable explanations for suspicious behavior.

## Key Features

- Federated Learning simulation with multiple clients
- Detection of malicious model updates using layer-wise drift analysis
- Explainable AI (XAI) style reporting for client behavior
- Dynamic trust score management
- Model poisoning and gradient scaling attack simulation
- Lightweight model weight compression
- Modular and easy-to-extend architecture

## Project Structure

```text
Lomar-main/
│
├── main.py                 # Entry point
├── federated_learning.py   # Federated learning simulation
├── lomar_defence.py        # Drift analysis and defense logic
├── trust_manager.py        # Trust score updates
├── attack.py               # Attack simulation modules
├── compression.py          # Weight compression utilities
├── explainability.py       # Explainability functions
└── main_gui.py             # GUI version (if enabled)
```

## How It Works

### 1. Federated Training

The system simulates multiple clients participating in training rounds.

For every round:

- Clients generate local model updates
- Benign clients produce normal updates
- Malicious clients generate abnormal updates
- Model drift is measured against global weights

### 2. Drift-Based Detection

LOMAR calculates layer-wise drift:

```python
drift = np.linalg.norm(client_weights - global_weights)
```

Large drift values indicate potentially malicious behavior.

### 3. Explainability Layer

For each client update, the framework generates:

- Total drift score
- Layer-wise drift values
- Most impacted layer
- Benign/Malicious classification
- Human-readable explanation

### 4. Trust Management

Trust scores are updated dynamically.

- Suspicious clients lose trust
- Reliable clients gradually regain trust
- Trust can be used during aggregation decisions

## Attack Scenarios Supported

### Model Poisoning

Adds random noise to model parameters to simulate poisoned updates.

### Gradient Scaling Attack

Artificially scales model updates to dominate aggregation.

### Label Flipping

Generates incorrect labels to simulate data poisoning behavior.

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/lomar.git
cd lomar
```

### Create Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install numpy
```

Additional libraries may be required depending on visualization or GUI modules.

## Running the Project

```bash
python main.py
```

The simulation will:

1. Run federated training rounds
2. Simulate malicious clients
3. Measure model drift
4. Generate explanations
5. Update trust scores

## Example Output

```text
Client 2
Status: Malicious

Total Drift: 8.52
Most Impacted Layer: 3

Reason:
High model drift detected
```

## Research Motivation

Federated Learning improves privacy by keeping training data on client devices. However, malicious participants can still manipulate the global model through poisoned updates.

LOMAR focuses on:

- Lightweight defense mechanisms
- Explainable detection decisions
- Trust-aware federated systems
- Low computational overhead

## Future Improvements

- Real neural network integration (PyTorch/TensorFlow)
- Advanced aggregation methods
- Byzantine-resilient defenses
- SHAP/LIME-based explanations
- Real-world benchmark datasets
- Dashboard and monitoring tools

## Tech Stack

- Python
- NumPy
- Federated Learning Concepts
- Explainable AI (XAI)

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License

This project is intended for educational and research purposes. Add an appropriate open-source license before production use.

## Author

Developed as a Federated Learning security and explainability project focused on detecting malicious client behavior using lightweight drift-based analysis.
