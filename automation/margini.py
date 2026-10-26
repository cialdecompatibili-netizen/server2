# Calcolatore margini IWS. Modifica PIANI (costo reale all'ingrosso) e lancia: python automation/margini.py
# Scrive MARGINI.md. Valori = SEGNAPOSTO da sostituire con i costi reali del fornitore.
import os
FEE = 0.015   # commissione pagamento (% del prezzo)
FEE_FISSA = 0.25  # EUR a transazione
IVA_ESCLUSA = True
# nome, costo_mensile_fornitore, prezzo_mensile_cliente, clienti_per_server (1 = dedicato), utilizzo_previsto
PIANI = [
    ("VPS Start (rivendita)",        4.5,   9.9, 1, 1.0),
    ("Hosting gestito WooCommerce",  30.0,  7.9, 8, 0.7),   # 1 server diviso tra 8 siti
    ("Hosting gestito PrestaShop",   30.0, 14.9, 6, 0.7),
    ("API LLM a consumo (GPU 1x)",  1100.0, 2400.0, 1, 0.5), # incasso mensile totale a util. 50%
    ("GPU dedicata Medium",        1100.0,  1590.0, 1, 1.0),
]
def riga(n, costo, prezzo, k, u):
    incasso = prezzo * k * u if "consumo" not in n else prezzo
    spesa = costo + incasso * FEE + FEE_FISSA * k
    m = incasso - spesa
    pct = 100 * m / incasso if incasso else 0
    be = costo / (prezzo * (1 - FEE)) if prezzo else 0
    return f"| {n} | {costo:.2f} | {incasso:.2f} | {m:.2f} | {pct:.0f}% | {be:.1f} |"
out = ["# Margini IWS (EUR/mese, IVA esclusa)", "",
       "Valori segnaposto: sostituire con costi reali. Margine = incasso - costo server - commissioni.", "",
       "| Piano | Costo server | Incasso | Margine | % | Clienti pareggio |", "|---|---|---|---|---|---|"]
out += [riga(*p) for p in PIANI]
out += ["", "Regola: non comprare hardware; affitta all'ingrosso e attiva il server solo dopo i primi ordini."]
p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "MARGINI.md")
open(p, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("\n".join(out))
