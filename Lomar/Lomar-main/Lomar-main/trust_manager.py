def update_trust_scores(current_trust, malicious_idx, decay=0.8):
    new_trust = current_trust.copy()
    for i in range(len(new_trust)):
        if i in malicious_idx:
            new_trust[i] *= decay
        else:
            new_trust[i] = min(1.0, new_trust[i] + 0.05)
    return new_trust
