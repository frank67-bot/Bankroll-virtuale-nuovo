"""Funzioni base per analisi 1X2, senza puntate reali."""

def analyze(odds, probabilities):
    outcomes = ('1', 'X', '2')
    if set(odds) != set(outcomes) or set(probabilities) != set(outcomes):
        raise ValueError('Sono richiesti gli esiti 1, X e 2')
    if any(not 1 < float(odds[k]) < float('inf') for k in outcomes):
        raise ValueError('Quote non valide')
    if any(not 0 <= float(probabilities[k]) <= 1 for k in outcomes):
        raise ValueError('Probabilità non valide')
    if abs(sum(probabilities.values()) - 1) > 1e-8:
        raise ValueError('Le probabilità devono sommare a 1')
    implied = {k: 1 / odds[k] for k in outcomes}
    overround = sum(implied.values())
    return {k: {'quota': odds[k], 'mercato_senza_margine': implied[k] / overround,
                'probabilita_modello': probabilities[k], 'roi_atteso': odds[k] * probabilities[k] - 1,
                'kelly': max(0, (odds[k] * probabilities[k] - 1) / (odds[k] - 1))}
            for k in outcomes}
