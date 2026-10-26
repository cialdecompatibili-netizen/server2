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
HERO = ('<style>.iws-hero{position:relative;overflow:hidden;background:radial-gradient(ellipse at 75% 0,#0b3a5c 0,#050b18 62%);color:#e6f1ff;padding:5rem 0}'
 '.iws-hero::before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(0,200,255,.09) 1px,transparent 1px),linear-gradient(90deg,rgba(0,200,255,.09) 1px,transparent 1px);background-size:48px 48px;animation:iwsg 16s linear infinite;-webkit-mask-image:linear-gradient(#000,transparent);mask-image:linear-gradient(#000,transparent)}'
 '@keyframes iwsg{to{background-position:0 48px}}@keyframes iwsd{to{stroke-dashoffset:-200}}@keyframes iwsb{50%{opacity:.15}}'
 '.iws-hero svg{position:absolute;inset:0;width:100%;height:100%;opacity:.6}.iws-hero .cp{fill:none;stroke:#19d3ff;stroke-width:1.5;stroke-dasharray:6 14;animation:iwsd 6s linear infinite}'
 '.iws-hero .led{fill:#19ffb4;animation:iwsb 1.8s ease-in-out infinite}.iws-hero .led:nth-child(2n){animation-delay:.6s;fill:#19d3ff}.iws-hero .led:nth-child(3n){animation-delay:1.1s}'
 '.iws-hero .gc-wrap{position:relative;z-index:1}.iws-hero .gc-h1,.iws-hero .gc-lead{color:#e6f1ff}.iws-hero .gc-eyebrow{color:#19d3ff}.iws-hero em{color:#19d3ff;font-style:normal}'
 '@media(prefers-reduced-motion:reduce){.iws-hero::before,.iws-hero .cp,.iws-hero .led{animation:none}}</style>')
SVG = ('<svg viewBox="0 0 1200 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
 '<path class="cp" d="M0 120H300L340 160H620"/><path class="cp" d="M1200 80H900L860 120H700V300"/><path class="cp" d="M0 380H200L240 340H480V460H800"/><path class="cp" d="M1200 400H1000L960 440H760"/>'
 '<rect x="900" y="190" width="150" height="150" rx="10" fill="rgba(5,20,40,.7)" stroke="#19d3ff"/><rect x="935" y="225" width="80" height="80" rx="6" fill="none" stroke="#19ffb4"/>'
 '<g stroke="#19d3ff" stroke-width="2"><path d="M930 190v-20M960 190v-20M990 190v-20M1020 190v-20M930 340v20M960 340v20M990 340v20M1020 340v20M900 230h-20M900 260h-20M900 290h-20M1050 230h20M1050 260h20M1050 290h20"/></g>'
 '<g><circle class="led" cx="975" cy="265" r="6"/><circle class="led" cx="60" cy="440" r="4"/><circle class="led" cx="90" cy="440" r="4"/><circle class="led" cx="120" cy="440" r="4"/><circle class="led" cx="340" cy="160" r="4"/><circle class="led" cx="700" cy="300" r="4"/><circle class="led" cx="480" cy="460" r="4"/></g></svg>')
def blocks(l):
    t = T[l]; i = 0 if l == "it" else 1
    cards = "".join('<div class="gc-pl"><b>%s</b><p>%s</p><p><a class="gc-link" href="%s%s%s/">%s</a></p></div>' % (c[1+i], c[3+i], t["base"], t["cat"], c[0], t["ccat_pre"]) for c in CATS)
    steps = "".join('<div class="gc-pl"><span class="n">0%d</span><b>%s</b><p>%s</p></div>' % (n+1, s[0], s[1]) for n, s in enumerate(t["steps"]))
    return [
     dict(id="hero", nome="Hero", enabled=True, html=HERO+'<div class="gc"><section class="gc-sec iws-hero">'+SVG+'<div class="gc-wrap"><p class="gc-eyebrow">%s</p><h1 class="gc-h1">%s</h1><p class="gc-lead">%s</p><div class="gc-act"><a class="gc-btn gc-btn-a" href="%s%s">%s</a> <a class="gc-btn gc-btn-o" href="%s%s">%s</a></div></div></section></div>' % (t["eb"], t["h1"], t["lead"], t["base"], t["shop"], t["b1"], t["base"], t["srv"], t["b2"])),
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
