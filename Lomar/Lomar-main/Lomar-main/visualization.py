import plotly.graph_objects as go

def plot_layer_drift_3d(all_client_drifts):

    clients = []
    layers = []
    drifts = []

    for client_id, layer_drifts in enumerate(all_client_drifts):
        for layer_id, drift in enumerate(layer_drifts):
            clients.append(client_id)
            layers.append(layer_id)
            drifts.append(drift)

    fig = go.Figure(data=[go.Scatter3d(
        x=clients,
        y=layers,
        z=drifts,
        mode='markers',
        marker=dict(
            size=6,
            color=drifts,
            colorscale='Viridis',
            colorbar=dict(title="Drift")
        )
    )])

    fig.update_layout(
        scene=dict(
            xaxis_title='Client ID',
            yaxis_title='Layer ID',
            zaxis_title='Drift Magnitude'
        ),
        title="Explainable LoMar - Layer Drift Visualization"
    )

    fig.show()
