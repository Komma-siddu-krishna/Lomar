import tkinter as tk
import plotly.graph_objects as go
import numpy as np

from federated_learning import run_federated_training

NUM_CLIENTS = 5


# ==========================
# DRIFT GRAPH
# ==========================
def show_drift_graph(scenario):

    fig = go.Figure()

    rounds = len(scenario["all_drifts"])

    for client_id in range(NUM_CLIENTS):

        drift_values = []

        for r in range(rounds):
            drift = scenario["all_drifts"][r][client_id]
            drift_values.append(drift)

        color = "red" if client_id == 2 else "green"

        fig.add_trace(go.Scatter(
            x=list(range(1, rounds + 1)),
            y=drift_values,
            mode="lines+markers",
            name=f"Client {client_id}",
            line=dict(color=color)
        ))

    fig.update_layout(
        title="Client Drift Across Rounds",
        xaxis_title="Round",
        yaxis_title="Drift Value"
    )

    fig.show()


# ==========================
# 3D VISUALIZATION
# ==========================
def show_3d_visualization(scenario):

    fig = go.Figure()
    rounds = len(scenario["all_drifts"])

    for client_id in range(NUM_CLIENTS):

        acc_values = []
        drift_values = []
        trust_values = []

        for r in range(rounds):

            drift = scenario["all_drifts"][r][client_id]

            acc = scenario["results"][r * NUM_CLIENTS + client_id]["accuracy"]

            trust = acc / (1 + drift)

            acc_values.append(acc)
            drift_values.append(drift)
            trust_values.append(trust)

        color = "red" if client_id == 2 else "green"

        fig.add_trace(go.Scatter3d(
            x=acc_values,
            y=drift_values,
            z=trust_values,
            mode="markers+lines",
            marker=dict(size=6, color=color),
            name=f"Client {client_id}"
        ))

    fig.update_layout(
        title="3D Client Behaviour (Accuracy vs Drift vs Trust)",
        scene=dict(
            xaxis_title="Accuracy",
            yaxis_title="Drift",
            zaxis_title="Trust Score"
        )
    )

    fig.show()


# ==========================
# CLIENT DETAILS WINDOW
# ==========================
def show_client_details(scenario):

    window = tk.Toplevel()
    window.title("Client Details")
    window.geometry("700x400")

    text = tk.Text(window)
    text.pack(fill="both", expand=True)

    rounds = len(scenario["all_drifts"])

    for r in range(rounds):
        text.insert(tk.END, f"\n========== ROUND {r+1} ==========\n")

        for client_id in range(NUM_CLIENTS):

            drift = scenario["all_drifts"][r][client_id]
            acc = scenario["results"][r * NUM_CLIENTS + client_id]["accuracy"]
            trust = acc / (1 + drift)

            status = "MALICIOUS ❌" if client_id == 2 else "GENUINE ✅"

            text.insert(
                tk.END,
                f"Client {client_id} | "
                f"Accuracy: {acc:.4f} | "
                f"Drift: {drift:.4f} | "
                f"Trust: {trust:.4f} | "
                f"Status: {status}\n"
            )


# ==========================
# RUN SIMULATION
# ==========================
def run_simulation():

    scenario = run_federated_training()

    show_client_details(scenario)
    show_drift_graph(scenario)
    show_3d_visualization(scenario)


# ==========================
# MAIN WINDOW
# ==========================
root = tk.Tk()
root.title("LoMar Federated Learning Simulation")
root.geometry("400x250")

label = tk.Label(root, text="LoMar: Trust & Drift Detection",
                 font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root,
                   text="Run Simulation",
                   command=run_simulation,
                   bg="blue",
                   fg="white")
button.pack(pady=20)

root.mainloop()