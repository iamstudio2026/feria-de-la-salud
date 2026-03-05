#!/usr/bin/env python3
"""Build casaxcasa-barreras.html with embedded logos from dashboard."""
import os

DIR = os.path.dirname(os.path.abspath(__file__))

def read(f):
    with open(os.path.join(DIR, f), 'r', encoding='utf-8') as fh:
        return fh.read().strip()

logo_salud = read('logo_base64_1.txt')
logo_snsp = read('logo_base64_2.txt')
logo_maza = read('logo_base64_3.txt')
logo_cxc = read('logo_casaxcasa_b64.txt')
logo_birmex = read('logo_birmex_b64.txt')
logo_alimentacion = read('logo_alimentacion_b64.txt')

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Casa x Casa — Barreras al Surtimiento de Recetas | CeCoSaBi</title>
<meta name="description" content="Identificacion de barreras para el surtimiento correcto de recetas del programa Salud Casa por Casa - CeCoSaBi">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<style>
:root {{
    --guinda: #9b2247;
    --guinda-dark: #611232;
    --dorado: #a57f2c;
    --verde: #1e5b4f;
    --gris: #98989A;
    --negro: #161a1d;
}}
body {{ font-family: 'Montserrat', sans-serif; background: #f0f2f5; margin: 0; }}
.font-patria {{ font-family: 'Playfair Display', serif; }}
.glass {{ background: rgba(255,255,255,.85); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,.3); }}
@keyframes fadeUp {{ from {{ opacity:0; transform:translateY(30px) }} to {{ opacity:1; transform:translateY(0) }} }}
.fade-up {{ animation: fadeUp .6s ease forwards; opacity:0; }}
.fade-up:nth-child(1){{animation-delay:.1s}} .fade-up:nth-child(2){{animation-delay:.2s}}
.fade-up:nth-child(3){{animation-delay:.3s}} .fade-up:nth-child(4){{animation-delay:.4s}}
.fade-up:nth-child(5){{animation-delay:.5s}} .fade-up:nth-child(6){{animation-delay:.6s}}
@keyframes pulse-glow {{ 0%,100%{{box-shadow:0 0 5px rgba(155,34,71,.3)}} 50%{{box-shadow:0 0 20px rgba(155,34,71,.6)}} }}
.pulse-glow {{ animation: pulse-glow 2s infinite; }}
.barrier-card {{ transition: all .3s ease; cursor:pointer; }}
.barrier-card:hover {{ transform: translateY(-6px); box-shadow: 0 20px 40px rgba(0,0,0,.15); }}
.flow-node {{ transition: all .3s ease; cursor:pointer; }}
.flow-node:hover {{ transform: scale(1.05); box-shadow: 0 8px 25px rgba(0,0,0,.2); }}
.flow-node.active {{ ring: 3px solid var(--guinda); transform: scale(1.08); }}
.section-title {{ position:relative; display:inline-block; }}
.section-title::after {{ content:''; position:absolute; bottom:-8px; left:0; width:60px; height:4px; background:linear-gradient(90deg,var(--guinda),var(--dorado)); border-radius:2px; }}
.tab-btn {{ transition: all .3s; border-bottom: 3px solid transparent; }}
.tab-btn.active {{ border-color: var(--guinda); color: var(--guinda); font-weight:600; }}
.tab-btn:hover {{ color: var(--guinda); }}
.cedula-field {{ transition: all .2s; }}
.cedula-field:hover {{ background: rgba(155,34,71,.05); }}
.timeline-dot {{ width:16px; height:16px; border-radius:50%; border:3px solid var(--guinda); background:#fff; position:relative; z-index:2; }}
.timeline-dot.completed {{ background: var(--guinda); }}
.actor-icon {{ width:48px; height:48px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:1.2rem; color:#fff; }}
@keyframes slideIn {{ from{{opacity:0;transform:translateX(-20px)}} to{{opacity:1;transform:translateX(0)}} }}
.slide-in {{ animation: slideIn .4s ease forwards; }}
.methodology-card {{ transition: all .3s; border-left: 4px solid transparent; }}
.methodology-card:hover {{ border-left-color: var(--guinda); transform: translateX(4px); }}
@media print {{ .no-print {{ display:none!important; }} }}
.gantt-bar {{ transition: all .3s ease; border-radius: 6px; position: relative; overflow: hidden; }}
.gantt-bar::after {{ content:''; position:absolute; top:0; left:0; right:0; bottom:0; background:linear-gradient(90deg,rgba(255,255,255,.15),transparent); }}
.gantt-bar:hover {{ transform: scaleX(1.02); box-shadow: 0 4px 12px rgba(0,0,0,.2); }}
</style>
</head>
<body>
<!-- HEADER -->
<header class="bg-white shadow-md sticky top-0 z-50">
    <div class="bg-[#002f2a] text-white text-xs py-1 px-4 flex justify-center items-center gap-4">
        <span>Secretaria de Salud Tamaulipas</span><span class="opacity-50">&bull;</span>
        <span>Servicio Nacional de Salud Publica</span><span class="opacity-50">&bull;</span>
        <span>BIRMEX</span><span class="opacity-50">&bull;</span>
        <span>Alimentacion para el Bienestar</span>
    </div>
    <div class="container mx-auto px-4 py-3 flex flex-col md:flex-row justify-between items-center gap-3">
        <div class="flex items-center gap-3 flex-wrap justify-center md:justify-start">
            <img src="{logo_salud}" alt="Secretaria de Salud" class="h-10 md:h-14 object-contain">
            <div class="h-8 w-px bg-gray-300 hidden md:block"></div>
            <img src="{logo_snsp}" alt="SNSP" class="h-8 md:h-12 object-contain">
            <div class="h-8 w-px bg-gray-300 hidden md:block"></div>
            <img src="{logo_cxc}" alt="Casa x Casa" class="h-8 md:h-12 object-contain">
            <div class="h-8 w-px bg-gray-300 hidden md:block"></div>
            <img src="{logo_birmex}" alt="BIRMEX" class="h-8 md:h-12 object-contain">
            <div class="h-8 w-px bg-gray-300 hidden md:block"></div>
            <img src="{logo_alimentacion}" alt="Alimentacion para el Bienestar" class="h-8 md:h-12 object-contain">
        </div>
        <img src="{logo_maza}" alt="2026 Ano de Margarita Maza" class="h-12 md:h-16 object-contain">
    </div>
    <div class="flex h-1 w-full">
        <div class="w-1/3 bg-[#1e5b4f]"></div>
        <div class="w-1/3 bg-[#9b2247]"></div>
        <div class="w-1/3 bg-[#a57f2c]"></div>
    </div>
</header>

<!-- HERO -->
<section id="hero" class="relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-br from-[#1e5b4f] via-[#9b2247] to-[#611232]"></div>
    <div class="absolute inset-0 opacity-10" style="background-image:url('data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2260%22 height=%2260%22><circle cx=%2230%22 cy=%2230%22 r=%222%22 fill=%22white%22/></svg>');"></div>
    <div class="relative container mx-auto px-4 py-16 md:py-24 text-center text-white">
        <div class="fade-up mb-6"><span class="inline-block bg-white/20 backdrop-blur-sm rounded-full px-6 py-2 text-sm font-medium tracking-wide">CeCoSaBi &mdash; Centro Coordinador de Salud para el Bienestar</span></div>
        <h1 class="fade-up font-patria text-3xl md:text-5xl lg:text-6xl font-bold mb-6 leading-tight">Barreras al Surtimiento<br>de Recetas</h1>
        <p class="fade-up text-lg md:text-xl max-w-3xl mx-auto opacity-90 mb-8">Identificar las barreras para el surtimiento correcto de recetas basandonos en el analisis causa-raiz (DGPLADES), definiendo una metodologia clara e instrumentos de medicion aplicables en campo.</p>
        <div class="fade-up flex flex-wrap justify-center gap-4">
            <a href="#barreras" class="bg-white text-[#9b2247] font-semibold px-8 py-3 rounded-full hover:bg-opacity-90 transition shadow-lg hover:shadow-xl"><i class="fas fa-search mr-2"></i>Ver Barreras</a>
            <a href="#cedula" class="border-2 border-white text-white font-semibold px-8 py-3 rounded-full hover:bg-white/10 transition"><i class="fas fa-file-alt mr-2"></i>Constructor de Cedulas</a>
        </div>

    </div>
</section>

<!-- NAV TABS -->
<nav id="section-nav" class="sticky top-[72px] z-40 bg-white/95 backdrop-blur-md shadow-sm no-print">
    <div class="container mx-auto px-4 flex gap-1 overflow-x-auto py-2 text-sm">
        <a href="#ruta" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-route mr-1"></i>Ruta Critica</a>
        <a href="#marco" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-bullseye mr-1"></i>Marco Operativo</a>
        <a href="#barreras" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-exclamation-triangle mr-1"></i>Barreras</a>
        <a href="#metodologia" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-flask mr-1"></i>Metodologia</a>
        <a href="#cedula" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-clipboard-list mr-1"></i>Cedulas</a>
        <a href="#resumen" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-chart-pie mr-1"></i>Proximos Pasos</a>
    </div>
</nav>

<!-- SECTION 1: RUTA CRITICA -->
<section id="ruta" class="container mx-auto px-4 py-12">
    <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-10"><i class="fas fa-route text-[#9b2247] mr-2"></i>Ruta Critica del Proceso</h2>
    <p class="text-gray-600 mb-8 max-w-3xl">Flujo del proceso de reporte nacional para el surtimiento de recetas, desde la emision hasta la entrega al derechohabiente.</p>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" id="flowContainer">
    </div>
    <div id="flowDetail" class="mt-8 glass rounded-2xl p-6 hidden transition-all">
        <h3 id="flowDetailTitle" class="font-bold text-lg text-[#9b2247] mb-3"></h3>
        <p id="flowDetailDesc" class="text-gray-600"></p>
    </div>
</section>

<!-- SECTION: MARCO OPERATIVO -->
<section id="marco" class="bg-gradient-to-b from-white to-gray-50 py-12">
    <div class="container mx-auto px-4">
        <!-- Paso Cero: Folio Unico -->
        <div class="glass rounded-2xl p-6 mb-10 border-l-4 border-[#9b2247] relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-[#9b2247]/5 rounded-full -translate-y-1/2 translate-x-1/2"></div>
            <div class="flex items-start gap-4">
                <div class="w-14 h-14 rounded-xl bg-gradient-to-br from-[#9b2247] to-[#611232] flex items-center justify-center text-white text-xl flex-shrink-0 shadow-lg">
                    <i class="fas fa-fingerprint"></i>
                </div>
                <div>
                    <div class="flex items-center gap-2 mb-2"><span class="text-xs bg-[#9b2247]/10 text-[#9b2247] px-3 py-1 rounded-full font-bold uppercase tracking-wide">Paso Cero</span><span class="text-xs text-gray-400">Condicion Innegociable</span></div>
                    <h3 class="font-bold text-xl text-gray-800 mb-2">Folio Unico de Receta</h3>
                    <p class="text-gray-600 text-sm mb-3">Antes de medir cualquier barrera, cada receta debe tener un identificador unico que la acompane desde su emision hasta su entrega. Sin esto, no hay trazabilidad posible.</p>
                    <div class="bg-gray-50 rounded-lg p-3 border border-gray-200">
                        <span class="text-xs font-semibold text-gray-500 block mb-1">Formato propuesto:</span>
                        <code class="text-sm font-mono text-[#9b2247] font-bold">ENTIDAD-DSB-UNIDAD-FECHA-CONSECUTIVO</code>
                        <span class="text-xs text-gray-400 block mt-1">Ejemplo: EDM-DSB03-CS12-20260303-001</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- 4 Dimensiones -->
        <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-4"><i class="fas fa-bullseye text-[#1e5b4f] mr-2"></i>Definicion Operativa de Surtimiento Correcto</h2>
        <p class="text-gray-600 mb-8 max-w-3xl">Para evitar que el diagnostico se base en opiniones, estructuramos el problema en 4 dimensiones medibles.</p>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" id="dimensionesGrid"></div>
    </div>
</section>

<!-- SECTION 2: BARRERAS -->
<section id="barreras" class="bg-gradient-to-b from-gray-50 to-white py-12">
    <div class="container mx-auto px-4">
        <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-4"><i class="fas fa-exclamation-triangle text-[#a57f2c] mr-2"></i>Analisis de Barreras por Actor</h2>
        <p class="text-gray-600 mb-8 max-w-3xl">Problematicas organizadas por cada actor involucrado en el proceso de surtimiento de recetas.</p>
        <div class="flex flex-wrap gap-2 mb-8 no-print" id="actorFilters"></div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="barrerasGrid"></div>
    </div>
</section>

<!-- SECTION 3: METODOLOGIA -->
<section id="metodologia" class="container mx-auto px-4 py-12">
    <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-4"><i class="fas fa-flask text-[#1e5b4f] mr-2"></i>Metodologia: Diseno Mixto en 3 Capas</h2>
    <p class="text-gray-600 mb-10 max-w-3xl">Para pasar del arbol de problemas a las soluciones, proponemos un despliegue rapido, defendible y accionable.</p>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12" id="fasesGrid"></div>
    <h3 class="font-bold text-lg mb-6 text-gray-800"><i class="fas fa-tools text-[#9b2247] mr-2"></i>Instrumentos de Medicion (Listos para Piloto)</h3>
    <p class="text-gray-500 text-sm mb-6">Pueden montarse en Google Forms y Excel para agilidad en campo.</p>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" id="instrumentosGrid"></div>
</section>

<!-- SECTION 4: CEDULA BUILDER -->
<section id="cedula" class="bg-gradient-to-b from-white to-gray-50 py-12">
    <div class="container mx-auto px-4">
        <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-4"><i class="fas fa-clipboard-list text-[#9b2247] mr-2"></i>Constructor de Cedulas</h2>
        <p class="text-gray-600 mb-8 max-w-3xl">Genera cedulas de evaluacion personalizadas para cada actor. Selecciona las barreras a evaluar y exporta a PDF.</p>
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div class="lg:col-span-1 space-y-4">
                <div class="glass rounded-xl p-4">
                    <label class="block font-semibold text-sm mb-2 text-gray-700">Actor a Evaluar</label>
                    <select id="cedulaActor" class="w-full border rounded-lg px-3 py-2 text-sm focus:ring-2 focus:ring-[#9b2247] focus:border-transparent outline-none"></select>
                </div>
                <div class="glass rounded-xl p-4">
                    <label class="block font-semibold text-sm mb-2 text-gray-700">Tipo de Instrumento</label>
                    <select id="cedulaTipo" class="w-full border rounded-lg px-3 py-2 text-sm focus:ring-2 focus:ring-[#9b2247] focus:border-transparent outline-none">
                        <option value="encuesta">Encuesta a Personal CxC</option>
                        <option value="farmacia">Encuesta a Farmacia/Operador</option>
                        <option value="auditoria">Cedula de Auditoria de Recetas</option>
                        <option value="beneficiario">Mini-encuesta a Beneficiarios</option>
                    </select>
                </div>
                <div class="glass rounded-xl p-4" id="barreraCheckboxes">
                    <label class="block font-semibold text-sm mb-2 text-gray-700">Barreras a Incluir</label>
                </div>
                <button onclick="generateCedula()" class="w-full bg-gradient-to-r from-[#9b2247] to-[#611232] text-white font-semibold py-3 rounded-xl hover:opacity-90 transition shadow-lg"><i class="fas fa-magic mr-2"></i>Generar Cedula</button>
                <button onclick="exportPDF()" class="w-full border-2 border-[#9b2247] text-[#9b2247] font-semibold py-3 rounded-xl hover:bg-[#9b2247]/5 transition"><i class="fas fa-file-pdf mr-2"></i>Exportar PDF</button>
            </div>
            <div class="lg:col-span-2">
                <div id="cedulaPreview" class="bg-white rounded-2xl shadow-lg p-8 min-h-[500px]">
                    <div class="text-center text-gray-400 py-20"><i class="fas fa-file-alt text-5xl mb-4 block opacity-30"></i><p>Selecciona un actor y genera la cedula</p></div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- SECTION 5: PROXIMOS PASOS -->
<section id="resumen" class="container mx-auto px-4 py-12">
    <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-10"><i class="fas fa-chart-pie text-[#a57f2c] mr-2"></i>Proximos Pasos</h2>
    <div class="glass rounded-2xl p-6 mb-8">
        <h3 class="font-bold text-lg mb-6 text-[#a57f2c]"><i class="fas fa-tasks mr-2"></i>Fases del Proyecto</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6" id="nextSteps"></div>
    </div>
    <div class="glass rounded-2xl p-6">
        <h3 class="font-bold text-lg mb-6 text-[#9b2247]"><i class="fas fa-calendar-alt mr-2"></i>Cronograma de Actividades</h3>
        <div id="ganttChart"></div>
    </div>
</section>

<!-- FOOTER -->
<footer class="bg-[#161a1d] text-white py-8">
    <div class="container mx-auto px-4 text-center">
        <div class="flex justify-center items-center gap-6 mb-6 flex-wrap">
            <img src="{logo_salud}" alt="Gobierno de Mexico - Secretaria de Salud" class="h-14 object-contain" style="mix-blend-mode:screen; filter:invert(1) grayscale(1) brightness(2);">
        </div>
        <p class="text-gray-400 text-sm">CeCoSaBi &mdash; Centro Coordinador de Salud para el Bienestar</p>
        <p class="text-gray-500 text-xs mt-2">Servicio Nacional de Salud Publica | Tamaulipas 2026</p>
    </div>
</footer>

<script>
// ===== DATA =====
const flowSteps = [
    {{ id:1, title:"Emision de Receta", icon:"fa-prescription", color:"#9b2247", desc:"La Secretaria de Salud emite la receta medica para el derechohabiente del programa.", actors:["Secretaria de Salud"] }},
    {{ id:2, title:"Generacion de Pedido", icon:"fa-clipboard-check", color:"#a57f2c", desc:"Se genera el pedido y se envia a BIRMEX para la conformacion de paquetes individualizados.", actors:["BIRMEX","DGPLADES"] }},
    {{ id:3, title:"Distribucion a Almacenes", icon:"fa-warehouse", color:"#1e5b4f", desc:"La Secretaria de Alimentacion para el Bienestar distribuye paquetes a almacenes regionales.", actors:["Sec. Alimentacion","Almacenes"] }},
    {{ id:4, title:"Almacen Central", icon:"fa-boxes-stacked", color:"#0369a1", desc:"El almacen central concentra la informacion fisica y la distribuye a farmacias.", actors:["Almacen Central"] }},
    {{ id:5, title:"Farmacias del Bienestar", icon:"fa-store", color:"#6b21a8", desc:"Las farmacias del bienestar reciben los paquetes y preparan la entrega.", actors:["Farmacias"] }},
    {{ id:6, title:"Entrega Casa por Casa", icon:"fa-house-medical", color:"#db2777", desc:"El personal de Casa por Casa entrega los medicamentos a domicilio.", actors:["Personal CxC"] }},
    {{ id:7, title:"Reporte y Seguimiento", icon:"fa-chart-line", color:"#ea580c", desc:"Se concentra la informacion en formularios, se procesan reportes en Excel y se genera el reporte nacional.", actors:["DGPLADES","Sec. Bienestar"] }},
    {{ id:8, title:"Analisis Nacional", icon:"fa-globe-americas", color:"#0d9488", desc:"DGPLADES analiza y genera el reporte nacional consolidado del programa.", actors:["DGPLADES"] }}
];

const actors = [
    {{ name:"Personal Casa por Casa", icon:"fa-people-carry-box", color:"#9b2247",
       barriers:["Falta de Capacitacion","Rotacion frecuente del personal joven","Falta de conocimiento del Proceso","Falta de capacitacion en manejo de recetas y medicamentos","Dificultad para conservar y entregar la receta fisica","Capacitacion insuficiente en farmacologia","Empatia del personal"] }},
    {{ name:"Personas Beneficiarias", icon:"fa-users", color:"#a57f2c",
       barriers:["Desconfianza","Cambio de domicilio sin notificacion","Fallecimiento","Baja adherencia al tratamiento por efectos secundarios o confusion","Desconocimiento informativo del programa o de sus beneficios","Falta de acompanamiento familiar para tramites"] }},
    {{ name:"BIRMEX", icon:"fa-industry", color:"#1e5b4f",
       barriers:["Errores en la conformacion de paquetes individualizados","Problematicas de Abasto con Proveeduria","Dificultad para identificar medicamentos faltantes","Retrasos en el envio desde almacenes centrales","Falta de seguimiento a contratos"] }},
    {{ name:"Secretaria del Bienestar", icon:"fa-building-columns", color:"#0369a1",
       barriers:["Falta de sistemas de Informacion","Falta de personal de Captura","No existe un sistema digital integral para seguimiento","Imposibilidad de consultar recetas surtidas en tiempo real","Riesgo de duplicidad o perdida de informacion","Errores en el registro manual de recetas surtidas"] }},
    {{ name:"Secretaria de Salud", icon:"fa-hospital", color:"#6b21a8",
       barriers:["Error en la prescripcion","Falta de personal de enfermeria","Falta de informacion","Falta de Recurso Humano Capacitado y Especializado"] }},
    {{ name:"IMSS Bienestar", icon:"fa-hand-holding-medical", color:"#db2777",
       barriers:["Falta de sincronizacion entre demanda y surtimiento","Demoras logisticas por rutas mal planificadas","Falta de personal operativo para distribucion","Problemas de coordinacion entre almacenes y tiendas del bienestar","Demora del transporte","Falta de sistema de Vinculacion","Ausencia de protocolos compartidos entre dependencias","Falta de alineacion entre Secretaria de Salud, Bienestar y Birmex","Procesos fragmentados sin responsables claros"] }}
];

const dimensiones = [
    {{ title:'Completitud', subtitle:'Nivel de Surtimiento', icon:'fa-chart-pie', color:'#9b2247', desc:'Porcentaje de recetas surtidas completas vs. parciales o no surtidas. Nos dira que tanto del problema es falta de insumos.', metric:'% recetas completas' }},
    {{ title:'Oportunidad', subtitle:'Tiempos Logisticos', icon:'fa-clock', color:'#a57f2c', desc:'Dias/horas transcurridos desde la emision de la receta hasta la entrega al beneficiario.', metric:'Dias promedio' }},
    {{ title:'Exactitud', subtitle:'Calidad del Proceso', icon:'fa-check-double', color:'#1e5b4f', desc:'Concordancia entre lo que dice la receta, lo que se armo en el paquete y lo que se entrego (medicamento, dosis, cantidad).', metric:'% concordancia' }},
    {{ title:'Trazabilidad', subtitle:'Visibilidad', icon:'fa-eye', color:'#0369a1', desc:'Capacidad de ubicar el estado de un pedido en tiempo real sin cadenas telefonicas.', metric:'Nivel de visibilidad' }}
];

const fases = [
    {{ num:1, title:'Capa 1: Diagnostico Cuantitativo', icon:'fa-chart-bar', color:'#9b2247', tiempo:'2-3 semanas', desc:'Medir la frecuencia de fallas y ubicar cuellos de botella exactos (recetas emitidas vs. surtidas).', tasks:['Cedulas de revision de casos','Auditoria documental de recetas reales','Encuestas cortas al personal','Medicion de las 4 dimensiones'] }},
    {{ num:2, title:'Capa 2: Profundizacion Cualitativa', icon:'fa-comments', color:'#1e5b4f', tiempo:'1-2 semanas', desc:'Entender el por que de las fallas metricas y evaluar la experiencia de usuarios y personal operativo.', tasks:['Mini-encuestas a beneficiarios','Entrevistas con personal de farmacia','Evaluacion de empatia y carga administrativa','Analisis de experiencia del usuario'] }},
    {{ num:3, title:'Capa 3: Taller de Priorizacion', icon:'fa-users-cog', color:'#a57f2c', tiempo:'1 semana', desc:'Convertir los hallazgos en mejoras de abastecimiento y procesos con actores clave.', tasks:['Taller con DGCOSEM, DGPLADES y operacion','Pareto de causas principales','Matriz Impacto/Esfuerzo','Definicion de plan de accion'] }}
];

const instrumentos = [
    {{ title:'Encuesta a Personal CxC', icon:'fa-people-carry-box', color:'#9b2247', desc:'Evalua claridad de indicaciones, problemas de registro y tiempos tipicos del personal de Casa por Casa.', capa:'Capa 1' }},
    {{ title:'Encuesta a Farmacia/Operador', icon:'fa-store', color:'#1e5b4f', desc:'Identifica volumen de faltantes, discrepancias y coordinacion interinstitucional en el punto de surtimiento.', capa:'Capa 1' }},
    {{ title:'Cedula de Auditoria de Recetas', icon:'fa-file-medical', color:'#a57f2c', desc:'Matriz para evaluar 30-50 recetas por unidad. Documenta folio, estatus (completo/parcial/nulo), exactitud y motivo de falla.', capa:'Capa 1', principal:true }},
    {{ title:'Mini-encuesta a Beneficiarios', icon:'fa-user-check', color:'#0369a1', desc:'Enfocada en la experiencia humana, contactabilidad y recepcion efectiva del medicamento.', capa:'Capa 2' }}
];

// ===== RENDER =====
function renderFlow() {{
    const c = document.getElementById('flowContainer');
    c.innerHTML = flowSteps.map((s,i) => `
        <div class="flow-node glass rounded-xl p-5 text-center" onclick="showFlowDetail(${{s.id}})" data-id="${{s.id}}">
            <div class="w-14 h-14 rounded-full mx-auto mb-3 flex items-center justify-center text-white text-xl shadow-lg" style="background:${{s.color}}">
                <i class="fas ${{s.icon}}"></i>
            </div>
            <div class="text-xs text-gray-400 mb-1">Paso ${{i+1}}</div>
            <h4 class="font-semibold text-sm text-gray-800">${{s.title}}</h4>
            <div class="flex justify-center gap-1 mt-2 flex-wrap">${{s.actors.map(a=>`<span class="text-[10px] bg-gray-100 text-gray-500 rounded-full px-2 py-0.5">${{a}}</span>`).join('')}}</div>
            ${{i < flowSteps.length-1 ? '<div class="hidden lg:block absolute -right-3 top-1/2 transform -translate-y-1/2 text-gray-300"><i class=\\"fas fa-chevron-right\\"></i></div>' : ''}}
        </div>
    `).join('');
}}

function showFlowDetail(id) {{
    const s = flowSteps.find(x=>x.id===id);
    document.querySelectorAll('.flow-node').forEach(n=>n.classList.remove('ring-2','ring-[#9b2247]'));
    document.querySelector(`.flow-node[data-id="${{id}}"]`).classList.add('ring-2','ring-[#9b2247]');
    const d = document.getElementById('flowDetail');
    d.classList.remove('hidden');
    document.getElementById('flowDetailTitle').innerHTML = `<i class="fas ${{s.icon}} mr-2"></i>${{s.title}}`;
    document.getElementById('flowDetailDesc').textContent = s.desc;
}}

function renderBarreras() {{
    // Filters
    const f = document.getElementById('actorFilters');
    f.innerHTML = `<button class="tab-btn active px-4 py-2 rounded-full text-sm bg-gray-100 hover:bg-gray-200" onclick="filterActor('all',this)">Todos</button>` +
        actors.map(a=>`<button class="tab-btn px-4 py-2 rounded-full text-sm bg-gray-100 hover:bg-gray-200" onclick="filterActor('${{a.name}}',this)"><i class="fas ${{a.icon}} mr-1" style="color:${{a.color}}"></i>${{a.name}}</button>`).join('');
    renderBarreraCards('all');
}}

function renderBarreraCards(filter) {{
    const g = document.getElementById('barrerasGrid');
    const filtered = filter === 'all' ? actors : actors.filter(a=>a.name===filter);
    g.innerHTML = filtered.map(a=>`
        <div class="barrier-card glass rounded-2xl p-6 fade-up" data-actor="${{a.name}}">
            <div class="flex items-center gap-3 mb-4">
                <div class="actor-icon" style="background:${{a.color}}"><i class="fas ${{a.icon}}"></i></div>
                <div><h3 class="font-bold text-gray-800">${{a.name}}</h3><span class="text-xs text-gray-500">${{a.barriers.length}} barreras</span></div>
            </div>
            <div class="space-y-2">
                ${{a.barriers.map(b=>`<div class="flex items-start gap-2 text-sm text-gray-600 cedula-field rounded-lg p-2"><i class="fas fa-exclamation-circle text-xs mt-1" style="color:${{a.color}}"></i><span>${{b}}</span></div>`).join('')}}
            </div>
        </div>
    `).join('');
}}

function filterActor(name, btn) {{
    document.querySelectorAll('#actorFilters .tab-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    renderBarreraCards(name);
}}

function renderDimensiones() {{
    document.getElementById('dimensionesGrid').innerHTML = dimensiones.map(d=>`
        <div class="glass rounded-2xl p-5 hover:shadow-lg transition border-t-4" style="border-color:${{d.color}}">
            <div class="w-12 h-12 rounded-xl flex items-center justify-center text-white mb-3 shadow-md" style="background:${{d.color}}"><i class="fas ${{d.icon}} text-lg"></i></div>
            <h4 class="font-bold text-gray-800 mb-1">${{d.title}}</h4>
            <span class="text-xs font-medium px-2 py-0.5 rounded-full mb-3 inline-block" style="background:${{d.color}}15;color:${{d.color}}">${{d.subtitle}}</span>
            <p class="text-gray-500 text-sm mb-3">${{d.desc}}</p>
            <div class="bg-gray-50 rounded-lg p-2 text-center"><span class="text-xs text-gray-400">Indicador:</span><br><span class="text-sm font-semibold" style="color:${{d.color}}">${{d.metric}}</span></div>
        </div>
    `).join('');
}}

function renderMetodologia() {{
    document.getElementById('fasesGrid').innerHTML = fases.map(f=>`
        <div class="methodology-card glass rounded-2xl p-6">
            <div class="flex items-center gap-3 mb-2">
                <div class="w-10 h-10 rounded-full flex items-center justify-center text-white font-bold" style="background:${{f.color}}">${{f.num}}</div>
                <div><h3 class="font-bold text-gray-800 text-sm">${{f.title}}</h3></div>
            </div>
            <span class="inline-block text-xs bg-gray-100 text-gray-500 rounded-full px-3 py-1 mb-3"><i class="fas fa-clock mr-1"></i>${{f.tiempo}}</span>
            <p class="text-gray-600 text-sm mb-4">${{f.desc}}</p>
            <ul class="space-y-2">${{f.tasks.map(t=>`<li class="text-sm text-gray-500 flex items-center gap-2"><i class="fas fa-chevron-right text-xs" style="color:${{f.color}}"></i>${{t}}</li>`).join('')}}</ul>
        </div>
    `).join('');
    document.getElementById('instrumentosGrid').innerHTML = instrumentos.map(inst=>`
        <div class="glass rounded-xl p-5 hover:shadow-lg transition ${{inst.principal ? 'ring-2 ring-[#a57f2c] ring-offset-2' : ''}}">
            ${{inst.principal ? '<div class="absolute -top-2 -right-2 bg-[#a57f2c] text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow">PRINCIPAL</div>' : ''}}
            <div class="relative">
            <div class="w-12 h-12 rounded-lg flex items-center justify-center text-white mb-3" style="background:${{inst.color}}"><i class="fas ${{inst.icon}} text-lg"></i></div>
            <span class="text-[10px] font-medium px-2 py-0.5 rounded-full" style="background:${{inst.color}}15;color:${{inst.color}}">${{inst.capa}}</span>
            <h4 class="font-semibold text-gray-800 mb-2 mt-2">${{inst.title}}</h4>
            <p class="text-gray-500 text-sm">${{inst.desc}}</p>
            </div>
        </div>
    `).join('');
}}

function renderCedulaOptions() {{
    const sel = document.getElementById('cedulaActor');
    sel.innerHTML = actors.map(a=>`<option value="${{a.name}}">${{a.name}}</option>`).join('');
    sel.addEventListener('change', updateBarreraCheckboxes);
    updateBarreraCheckboxes();
}}

function updateBarreraCheckboxes() {{
    const name = document.getElementById('cedulaActor').value;
    const actor = actors.find(a=>a.name===name);
    const c = document.getElementById('barreraCheckboxes');
    c.innerHTML = `<label class="block font-semibold text-sm mb-2 text-gray-700">Barreras a Incluir</label>` +
        actor.barriers.map((b,i)=>`<label class="flex items-start gap-2 text-sm text-gray-600 p-1 cedula-field rounded cursor-pointer"><input type="checkbox" checked class="mt-1 accent-[#9b2247]" value="${{i}}"><span>${{b}}</span></label>`).join('');
}}

function generateCedula() {{
    const actorName = document.getElementById('cedulaActor').value;
    const tipo = document.getElementById('cedulaTipo').value;
    const actor = actors.find(a=>a.name===actorName);
    const checked = [...document.querySelectorAll('#barreraCheckboxes input:checked')].map(c=>parseInt(c.value));
    const selectedBarriers = checked.map(i=>actor.barriers[i]);
    const tipoLabels = {{encuesta:'Encuesta a Personal CxC',farmacia:'Encuesta a Farmacia/Operador',auditoria:'Cedula de Auditoria de Recetas',beneficiario:'Mini-encuesta a Beneficiarios'}};
    const preview = document.getElementById('cedulaPreview');

    let questions = '';
    if (tipo === 'encuesta') {{
        questions = selectedBarriers.map((b,i)=>`
            <div class="border-b pb-3 mb-3">
                <p class="font-medium text-sm text-gray-800 mb-2">${{i+1}}. En su experiencia, ¿con que frecuencia se presenta: <em>"${{b}}"</em>?</p>
                <div class="flex gap-4 text-xs text-gray-500">
                    <label class="flex items-center gap-1"><input type="radio" name="q${{i}}" disabled> Nunca</label>
                    <label class="flex items-center gap-1"><input type="radio" name="q${{i}}" disabled> A veces</label>
                    <label class="flex items-center gap-1"><input type="radio" name="q${{i}}" disabled> Frecuente</label>
                    <label class="flex items-center gap-1"><input type="radio" name="q${{i}}" disabled> Siempre</label>
                </div>
            </div>`).join('');
    }} else if (tipo === 'farmacia') {{
        questions = `<div class="border-b pb-3 mb-3"><p class="font-medium text-sm text-gray-800 mb-2">1. Volumen promedio de recetas recibidas por semana:</p><div class="border border-gray-300 rounded-lg p-2 text-sm text-gray-400 h-8"></div></div>
        <div class="border-b pb-3 mb-3"><p class="font-medium text-sm text-gray-800 mb-2">2. Porcentaje estimado de recetas con faltantes:</p><div class="flex gap-4 text-xs text-gray-500"><label class="flex items-center gap-1"><input type="radio" disabled> 0-10%</label><label class="flex items-center gap-1"><input type="radio" disabled> 11-25%</label><label class="flex items-center gap-1"><input type="radio" disabled> 26-50%</label><label class="flex items-center gap-1"><input type="radio" disabled> >50%</label></div></div>
        <div class="border-b pb-3 mb-3"><p class="font-medium text-sm text-gray-800 mb-2">3. Principales medicamentos faltantes (listar):</p><div class="border border-dashed border-gray-300 rounded-lg p-3 text-xs text-gray-400 min-h-[60px]"></div></div>
        <div class="border-b pb-3 mb-3"><p class="font-medium text-sm text-gray-800 mb-2">4. Nivel de coordinacion con almacen central:</p><div class="flex gap-4 text-xs text-gray-500"><label class="flex items-center gap-1"><input type="radio" disabled> Deficiente</label><label class="flex items-center gap-1"><input type="radio" disabled> Regular</label><label class="flex items-center gap-1"><input type="radio" disabled> Bueno</label><label class="flex items-center gap-1"><input type="radio" disabled> Excelente</label></div></div>
        ` + selectedBarriers.map((b,i)=>`<div class="border-b pb-3 mb-3"><p class="font-medium text-sm text-gray-800 mb-2">${{i+5}}. ¿Ha identificado: <em>"${{b}}"</em>?</p><div class="flex gap-4 text-xs text-gray-500"><label class="flex items-center gap-1"><input type="radio" disabled> Si</label><label class="flex items-center gap-1"><input type="radio" disabled> No</label><label class="flex items-center gap-1"><input type="radio" disabled> Parcialmente</label></div></div>`).join('');
    }} else if (tipo === 'auditoria') {{
        questions = `<div class="mb-4 p-3 bg-[#a57f2c]/10 rounded-lg text-sm text-[#a57f2c]"><i class="fas fa-star mr-1"></i><strong>Instrumento Principal.</strong> Evaluar 30-50 recetas por unidad.</div>
        <div class="overflow-x-auto"><table class="w-full text-xs border"><thead><tr class="bg-gray-50"><th class="border p-2">No.</th><th class="border p-2">Folio Receta</th><th class="border p-2">Estatus</th><th class="border p-2">Medicamento Correcto</th><th class="border p-2">Dosis Correcta</th><th class="border p-2">Cantidad Correcta</th><th class="border p-2">Motivo Falla</th></tr></thead><tbody>` +
        [1,2,3,4,5].map(n=>`<tr><td class="border p-2 text-center text-gray-400">${{n}}</td><td class="border p-2"><span class="text-gray-300">EDM-DSB__-CS__-________-___</span></td><td class="border p-2"><span class="text-gray-300">Completo / Parcial / Nulo</span></td><td class="border p-2 text-center"><span class="text-gray-300">Si / No</span></td><td class="border p-2 text-center"><span class="text-gray-300">Si / No</span></td><td class="border p-2 text-center"><span class="text-gray-300">Si / No</span></td><td class="border p-2"><span class="text-gray-300">________________</span></td></tr>`).join('') +
        `<tr><td colspan="7" class="border p-2 text-center text-gray-400">... (continuar hasta 30-50 recetas)</td></tr></tbody></table></div>`;
    }} else {{
        questions = `<div class="border-b pb-3 mb-3"><p class="font-medium text-sm text-gray-800 mb-2">1. ¿Recibio todos los medicamentos indicados en su receta?</p><div class="flex gap-4 text-xs text-gray-500"><label class="flex items-center gap-1"><input type="radio" disabled> Si, todos</label><label class="flex items-center gap-1"><input type="radio" disabled> Solo algunos</label><label class="flex items-center gap-1"><input type="radio" disabled> Ninguno</label></div></div>
        <div class="border-b pb-3 mb-3"><p class="font-medium text-sm text-gray-800 mb-2">2. ¿Le explicaron como tomar sus medicamentos?</p><div class="flex gap-4 text-xs text-gray-500"><label class="flex items-center gap-1"><input type="radio" disabled> Si, claramente</label><label class="flex items-center gap-1"><input type="radio" disabled> Si, pero no entendi</label><label class="flex items-center gap-1"><input type="radio" disabled> No</label></div></div>
        <div class="border-b pb-3 mb-3"><p class="font-medium text-sm text-gray-800 mb-2">3. ¿Cuanto tiempo paso desde que le dieron la receta hasta recibir el medicamento?</p><div class="flex gap-4 text-xs text-gray-500"><label class="flex items-center gap-1"><input type="radio" disabled> Mismo dia</label><label class="flex items-center gap-1"><input type="radio" disabled> 1-3 dias</label><label class="flex items-center gap-1"><input type="radio" disabled> 4-7 dias</label><label class="flex items-center gap-1"><input type="radio" disabled> >1 semana</label></div></div>
        <div class="border-b pb-3 mb-3"><p class="font-medium text-sm text-gray-800 mb-2">4. ¿Como califica el trato del personal que le entrego el medicamento?</p><div class="flex gap-4 text-xs text-gray-500"><label class="flex items-center gap-1"><input type="radio" disabled> Excelente</label><label class="flex items-center gap-1"><input type="radio" disabled> Bueno</label><label class="flex items-center gap-1"><input type="radio" disabled> Regular</label><label class="flex items-center gap-1"><input type="radio" disabled> Malo</label></div></div>`;
    }}

    preview.innerHTML = `
        <div class="border-b-4 border-[#9b2247] pb-4 mb-6">
            <div class="flex justify-between items-start">
                <div><h3 class="font-patria text-xl font-bold text-[#9b2247]">Cedula de Evaluacion</h3>
                <p class="text-sm text-gray-500">Programa Salud Casa por Casa &mdash; CeCoSaBi</p></div>
                <span class="text-xs bg-[#9b2247]/10 text-[#9b2247] px-3 py-1 rounded-full font-medium">${{tipoLabels[tipo]}}</span>
            </div>
        </div>
        <div class="grid grid-cols-2 gap-4 mb-6 text-sm">
            <div><span class="text-gray-500">Actor:</span> <strong>${{actorName}}</strong></div>
            <div><span class="text-gray-500">Fecha:</span> ____/____/________</div>
            <div><span class="text-gray-500">Aplicador:</span> ________________________</div>
            <div><span class="text-gray-500">Folio:</span> <span class="font-mono text-xs text-[#9b2247]">EDM-DSB__-CS__-________-___</span></div>
        </div>
        <h4 class="font-semibold text-sm text-gray-700 mb-4 border-b pb-2"><i class="fas fa-list mr-2 text-[#9b2247]"></i>${{tipo === 'auditoria' ? 'Matriz de Auditoria' : 'Preguntas / Items'}}</h4>
        ${{questions}}
        <div class="mt-6 pt-4 border-t">
            <p class="text-sm font-medium text-gray-700 mb-2">Observaciones generales:</p>
            <div class="border border-dashed border-gray-300 rounded-lg p-4 min-h-[80px] text-xs text-gray-400">Espacio para observaciones</div>
        </div>
        <div class="mt-4 text-right text-xs text-gray-400">Firma del aplicador: ________________________</div>
    `;
}}

async function exportPDF() {{
    const el = document.getElementById('cedulaPreview');
    if (el.querySelector('.text-gray-400.py-20')) {{ alert('Primero genera una cedula'); return; }}
    const canvas = await html2canvas(el, {{ scale: 2, useCORS: true }});
    const {{ jsPDF }} = window.jspdf;
    const pdf = new jsPDF('p','mm','a4');
    const w = pdf.internal.pageSize.getWidth();
    const h = (canvas.height * w) / canvas.width;
    pdf.addImage(canvas.toDataURL('image/png'), 'PNG', 0, 0, w, h);
    pdf.save('cedula_casaxcasa.pdf');
}}

function renderNextSteps() {{
    const steps = [
        {{ icon:'fa-vial', title:'Prueba Piloto', desc:'Aplicar la cedula de auditoria a 100 recetas para generar el primer Tablero de Control (Pareto de causas y tiempos de entrega).', color:'#9b2247' }},
        {{ icon:'fa-layer-group', title:'Despliegue Capa 1+2', desc:'Ejecutar diagnostico cuantitativo (2-3 sem.) seguido de profundizacion cualitativa (1-2 sem.) en campo.', color:'#1e5b4f' }},
        {{ icon:'fa-users-cog', title:'Taller de Priorizacion', desc:'Reunion con DGCOSEM, DGPLADES y operacion para Pareto de causas y Matriz Impacto/Esfuerzo.', color:'#a57f2c' }}
    ];
    document.getElementById('nextSteps').innerHTML = steps.map(s=>`
        <div class="bg-gray-50 rounded-xl p-5 hover:shadow-md transition">
            <div class="w-10 h-10 rounded-lg flex items-center justify-center text-white mb-3" style="background:${{s.color}}"><i class="fas ${{s.icon}}"></i></div>
            <h4 class="font-semibold text-gray-800 mb-2">${{s.title}}</h4>
            <p class="text-gray-500 text-sm">${{s.desc}}</p>
        </div>
    `).join('');
}}

function renderGantt() {{
    const weeks = ['S1','S2','S3','S4','S5','S6','S7','S8'];
    const weekLabels = ['Sem 1','Sem 2','Sem 3','Sem 4','Sem 5','Sem 6','Sem 7','Sem 8'];
    const tasks = [
        {{ name:'Piloto: 100 recetas auditadas', phase:'Capa 1: Diagnostico Cuantitativo', start:0, duration:1, color:'#611232' }},
        {{ name:'Diseno/ajuste de instrumentos', phase:'Capa 1: Diagnostico Cuantitativo', start:0, duration:1, color:'#9b2247' }},
        {{ name:'Aplicacion cedulas auditoria', phase:'Capa 1: Diagnostico Cuantitativo', start:1, duration:2, color:'#9b2247' }},
        {{ name:'Encuestas a personal CxC', phase:'Capa 1: Diagnostico Cuantitativo', start:1, duration:2, color:'#b83560' }},
        {{ name:'Encuestas a farmacia/operador', phase:'Capa 1: Diagnostico Cuantitativo', start:2, duration:1, color:'#b83560' }},
        {{ name:'Mini-encuestas beneficiarios', phase:'Capa 2: Profundizacion Cualitativa', start:3, duration:2, color:'#1e5b4f' }},
        {{ name:'Entrevistas farmacia/distribuidores', phase:'Capa 2: Profundizacion Cualitativa', start:3, duration:2, color:'#267a6b' }},
        {{ name:'Tabulacion y analisis', phase:'Capa 2: Profundizacion Cualitativa', start:4, duration:1, color:'#267a6b' }},
        {{ name:'Taller priorizacion DGCOSEM/DGPLADES', phase:'Capa 3: Taller de Priorizacion', start:5, duration:1, color:'#a57f2c' }},
        {{ name:'Pareto + Matriz Impacto/Esfuerzo', phase:'Capa 3: Taller de Priorizacion', start:5, duration:1, color:'#a57f2c' }},
        {{ name:'Plan de accion y Tablero de Control', phase:'Capa 3: Taller de Priorizacion', start:6, duration:2, color:'#c49a3a' }}
    ];
    const g = document.getElementById('ganttChart');
    let html = `<div class="overflow-x-auto"><table class="w-full min-w-[700px] text-sm"><thead><tr>
        <th class="text-left py-3 px-4 font-semibold text-gray-700 w-56 border-b">Actividad</th>`;
    weekLabels.forEach(m => {{ html += `<th class="text-center py-3 px-2 font-medium text-gray-500 border-b w-20">${{m}}</th>`; }});
    html += `</tr></thead><tbody>`;
    let lastPhase = '';
    tasks.forEach(t => {{
        if (t.phase !== lastPhase) {{
            html += `<tr><td colspan="${{weekLabels.length+1}}" class="pt-4 pb-2 px-4 font-bold text-sm" style="color:${{t.color}}"><i class="fas fa-folder-open mr-2"></i>${{t.phase}}</td></tr>`;
            lastPhase = t.phase;
        }}
        html += `<tr class="hover:bg-gray-50 transition"><td class="py-2 px-4 text-gray-600 border-b border-gray-100">${{t.name}}</td>`;
        for (let i = 0; i < weekLabels.length; i++) {{
            if (i === t.start) {{
                html += `<td colspan="${{t.duration}}" class="py-2 px-1 border-b border-gray-100"><div class="gantt-bar h-7 flex items-center justify-center text-white text-xs font-medium shadow-sm" style="background:${{t.color}}">${{t.duration > 1 ? t.duration + ' sem' : '1 sem'}}</div></td>`;
                i += t.duration - 1;
            }} else {{
                html += `<td class="py-2 px-1 border-b border-gray-100"><div class="h-7 border-l border-dashed border-gray-200"></div></td>`;
            }}
        }}
        html += `</tr>`;
    }});
    html += `</tbody></table></div>`;
    html += `<div class="flex gap-6 mt-6 justify-center flex-wrap">`;
    [['#9b2247','Capa 1: Diagnostico'],['#1e5b4f','Capa 2: Cualitativa'],['#a57f2c','Capa 3: Priorizacion']].forEach(([c,l]) => {{
        html += `<div class="flex items-center gap-2 text-sm"><div class="w-4 h-4 rounded" style="background:${{c}}"></div><span class="text-gray-600">${{l}}</span></div>`;
    }});
    html += `</div>`;
    g.innerHTML = html;
}}

// ===== INIT =====
document.addEventListener('DOMContentLoaded', () => {{
    renderFlow();
    renderDimensiones();
    renderBarreras();
    renderMetodologia();
    renderCedulaOptions();
    renderNextSteps();
    renderGantt();
    // Active tab highlight on scroll
    const sections = ['ruta','marco','barreras','metodologia','cedula','resumen'];
    const observer = new IntersectionObserver(entries => {{
        entries.forEach(e => {{
            if (e.isIntersecting) {{
                document.querySelectorAll('#section-nav .tab-btn').forEach(t=>t.classList.remove('active'));
                const link = document.querySelector(`#section-nav a[href="#${{e.target.id}}"]`);
                if (link) link.classList.add('active');
            }}
        }});
    }}, {{ threshold: 0.3 }});
    sections.forEach(id => {{ const el = document.getElementById(id); if(el) observer.observe(el); }});
}});
</script>
</body>
</html>'''

out_path = os.path.join(DIR, 'casaxcasa-barreras.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Done! File size: {{len(html):,}} chars')
print(f'Written to: {{out_path}}')
