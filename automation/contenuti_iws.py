# Testi home + chi siamo IT+EN per IWS (hosting gestito WooCommerce/PrestaShop). Rilanciabile. Nessun dato inventato.
# Poi: python automation/allinea_hash.py
import json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = [("vps","VPS e cloud","VPS and cloud","Server virtuali pronti all'uso, traffico incluso.","Ready-to-use virtual servers, traffic included."),
 ("web","Hosting gestito","Managed hosting","WooCommerce e PrestaShop gestiti: aggiornamenti, backup e assistenza.","Managed WooCommerce and PrestaShop: updates, backups and support."),
 ("ai","AI e LLM","AI and LLM","Modelli open source a consumo e GPU dedicate.","Open source models pay-as-you-go and dedicated GPUs."),
 ("game","Game server","Game servers","Server di gioco con risorse dedicate.","Game servers with dedicated resources.")]
T = {"it": dict(base="__BASEURL__", shop="/negozio/", cat="/negozio/categoria/", srv="/servizi/", con="/contatti/",
  eb="Hosting gestito per e-commerce", h1="Il tuo negozio online, <em>gestito da chi lo conosce.</em>",
  lead="Hosting gestito per WooCommerce e PrestaShop con migrazione, backup, aggiornamenti e assistenza in italiano. Traffico incluso, nessuna sorpresa in fattura.",
  b1="Vedi i piani", b2="Come funziona", ce="Prodotti", ch="Scegli cosa ti serve", cl="Dal server virtuale all'hosting gestito, fino ai modelli AI.", ccat_pre="Vedi i piani",
  mc="Come funziona", mh="Dalla scelta al sito online", steps=[("Scegli","Seleziona il piano adatto al tuo negozio."),("Migra","Spostiamo noi il tuo sito, senza fermarlo."),("Gestisci","Backup, aggiornamenti e sicurezza sono inclusi."),("Cresci","Passi a risorse maggiori quando serve.")],
  ct="Hai gia un negozio?", cs="Dicci dove e ospitato e ti proponiamo come migrarlo.", cb="Contattaci"),
 "en": dict(base="__BASEURL__", shop="/en/shop/", cat="/en/shop/category/", srv="/en/services/", con="/en/contact/",
  eb="Managed hosting for e-commerce", h1="Your online store, <em>run by people who know it.</em>",
  lead="Managed hosting for WooCommerce and PrestaShop with migration, backups, updates and support. Traffic included, no billing surprises.",
  b1="See the plans", b2="How it works", ce="Products", ch="Choose what you need", cl="From virtual servers to managed hosting and AI models.", ccat_pre="See the plans",
  mc="How it works", mh="From choice to live site", steps=[("Choose","Pick the plan that fits your store."),("Migrate","We move your site without downtime."),("Manage","Backups, updates and security included."),("Grow","Move to more resources when needed.")],
  ct="Already have a store?", cs="Tell us where it is hosted and we will propose how to migrate it.", cb="Contact us")}
def blocks(l):
    t = T[l]; i = 0 if l == "it" else 1
    cards = "".join('<div class="gc-pl"><b>%s</b><p>%s</p><p><a class="gc-link" href="%s%s%s/">%s</a></p></div>' % (c[1+i], c[3+i], t["base"], t["cat"], c[0], t["ccat_pre"]) for c in CATS)
    steps = "".join('<div class="gc-pl"><span class="n">0%d</span><b>%s</b><p>%s</p></div>' % (n+1, s[0], s[1]) for n, s in enumerate(t["steps"]))
    return [
     dict(id="hero", nome="Hero", enabled=True, html='<div class="gc"><section class="gc-sec"><div class="gc-wrap"><p class="gc-eyebrow">%s</p><h1 class="gc-h1">%s</h1><p class="gc-lead">%s</p><div class="gc-act"><a class="gc-btn gc-btn-a" href="%s%s">%s</a> <a class="gc-btn gc-btn-o" href="%s%s">%s</a></div></div></section></div>' % (t["eb"], t["h1"], t["lead"], t["base"], t["shop"], t["b1"], t["base"], t["srv"], t["b2"])),
     dict(id="categorie", nome=t["ce"], enabled=True, html='<div class="gc"><section class="gc-sec gc-soft" id="categorie"><div class="gc-wrap"><p class="gc-eyebrow">%s</p><h2 class="gc-h2">%s</h2><p class="gc-lead">%s</p><div class="gc-plat">%s</div></div></section></div>' % (t["ce"], t["ch"], t["cl"], cards)),
     dict(id="metodo", nome=t["mc"], enabled=True, html='<div class="gc"><section class="gc-sec" id="metodo"><div class="gc-wrap"><p class="gc-eyebrow">%s</p><h2 class="gc-h2">%s</h2><div class="gc-plat">%s</div></div></section></div>' % (t["mc"], t["mh"], steps)),
     dict(id="contatti", nome="Contatti" if l == "it" else "Contact", enabled=True, html='<div class="gc"><section class="gc-sec gc-dark" id="contatti"><div class="gc-wrap"><h2 class="gc-h2">%s</h2><p class="gc-lead">%s</p><a class="gc-btn" href="%s%s">%s</a></div></section></div>' % (t["ct"], t["cs"], t["base"], t["con"], t["cb"]))]
def azienda(l):
    if l == "it":
        a = ("Chi siamo","Hosting pensato per chi vende online","IWS offre server e hosting gestito per negozi WooCommerce e PrestaShop, con assistenza in italiano.","Ci occupiamo di migrazione, backup e aggiornamenti, cosi tu pensi a vendere.","Come lavoriamo",[("Chiarezza","Piani e prezzi leggibili, traffico incluso."),("Assistenza","Supporto in italiano da chi conosce i negozi online."),("Crescita graduale","Parti da un piano piccolo e scali quando serve.")])
    else:
        a = ("About us","Hosting built for online sellers","IWS provides servers and managed hosting for WooCommerce and PrestaShop stores, with support in Italian.","We handle migration, backups and updates so you can focus on selling.","How we work",[("Clarity","Readable plans and prices, traffic included."),("Support","Help from people who know online stores."),("Gradual growth","Start on a small plan and scale when needed.")])
    p = "".join('<div class="gc-pl"><span class="n">%d</span><b>%s</b><p>%s</p></div>' % (n+1, x[0], x[1]) for n, x in enumerate(a[5]))
    return [dict(id="chi", nome=a[0], enabled=True, html='<div class="gc"><section class="gc-sec" id="chi"><div class="gc-wrap"><p class="gc-eyebrow">%s</p><h2 class="gc-h2">%s</h2><p class="gc-lead">%s</p><p>%s</p></div></section></div>' % (a[0], a[1], a[2], a[3])),
            dict(id="principi", nome="Principi" if l == "it" else "Principles", enabled=True, html='<div class="gc"><section class="gc-sec gc-soft" id="principi"><div class="gc-wrap"><h2 class="gc-h2">%s</h2><div class="gc-plat">%s</div></div></section></div>' % (a[4], p))]
def wj(path, o):
    open(os.path.join(R, path), "w", encoding="utf-8", newline="\n").write(json.dumps(o, ensure_ascii=False, indent=2) + "\n")
wj("_data/blocks_home.json", blocks("it")); wj("_data/i18n/en/blocks_home.json", blocks("en"))
wj("_data/blocks_azienda.json", azienda("it")); wj("_data/i18n/en/blocks_azienda.json", azienda("en"))
print("ok")
