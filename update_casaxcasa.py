import sys

html_path = r"c:\Users\Lenovo\OneDrive\Escritorio\APPs\Feria de la Salud\casaxcasa-barreras.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update navigation
nav_old = """    <nav id="section-nav" class="sticky top-[72px] z-40 bg-white/95 backdrop-blur-md shadow-sm no-print">
        <div class="container mx-auto px-4 flex gap-1 overflow-x-auto py-2 text-sm">
            <a href="#ruta" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i
                    class="fas fa-route mr-1"></i>Ruta Critica</a>
            <a href="#marco" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i
                    class="fas fa-bullseye mr-1"></i>Marco Operativo</a>
            <a href="#barreras" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i
                    class="fas fa-exclamation-triangle mr-1"></i>Barreras</a>
            <a href="#metodologia" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i
                    class="fas fa-flask mr-1"></i>Metodologia</a>
            <a href="#cedula" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i
                    class="fas fa-clipboard-list mr-1"></i>Cedulas</a>
            <a href="#resumen" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i
                    class="fas fa-chart-pie mr-1"></i>Proximos Pasos</a>
        </div>
    </nav>"""

nav_new = """    <nav id="section-nav" class="sticky top-[72px] z-40 bg-white/95 backdrop-blur-md shadow-sm no-print">
        <div class="container mx-auto px-4 flex gap-1 overflow-x-auto py-2 text-sm">
            <a href="#ruta" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-route mr-1"></i>Ruta Critica</a>
            <a href="#marco" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-bullseye mr-1"></i>Marco Operativo</a>
            <a href="#variables" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-list-ul mr-1"></i>Variables</a>
            <a href="#indicadores" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-chart-line mr-1"></i>Indicadores</a>
            <a href="#causas" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-sitemap mr-1"></i>Taxonomía</a>
            <a href="#barreras" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-exclamation-triangle mr-1"></i>Barreras</a>
            <a href="#metodologia" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-flask mr-1"></i>Metodologia</a>
            <a href="#cedula" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-clipboard-list mr-1"></i>Cedulas</a>
            <a href="#productos" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-box-open mr-1"></i>Productos</a>
            <a href="#resumen" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-chart-pie mr-1"></i>Proximos Pasos</a>
        </div>
    </nav>"""
if nav_old not in content: print("Missing nav")
content = content.replace(nav_old, nav_new)

# 2. Marco Operativo (after dimensionesGrid)
marco_old = """            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" id="dimensionesGrid"></div>
        </div>
    </section>"""

marco_new = """            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="dimensionesGrid"></div>

            <!-- Cascada de Provisión -->
            <h3 class="font-bold text-xl text-[#161a1d] mt-12 mb-4"><i class="fas fa-stream text-[#0369a1] mr-2"></i>Cascada de Provisión Farmacéutica</h3>
            <div class="glass rounded-2xl p-6 mb-8">
                <div class="flex flex-col space-y-2" id="cascadaContainer"></div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Categorías -->
                <div>
                    <h3 class="font-bold text-xl text-[#161a1d] mb-4"><i class="fas fa-tags text-[#6b21a8] mr-2"></i>Categorías de Surtimiento</h3>
                    <div class="glass rounded-2xl p-6" id="categoriasContainer"></div>
                </div>
                <!-- Tiempos -->
                <div>
                    <h3 class="font-bold text-xl text-[#161a1d] mb-4"><i class="fas fa-hourglass-half text-[#ea580c] mr-2"></i>Tiempos de Surtimiento</h3>
                    <div class="glass rounded-2xl p-6" id="tiemposContainer"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION: VARIABLES -->
    <section id="variables" class="bg-gradient-to-b from-gray-50 to-white py-12">
        <div class="container mx-auto px-4">
            <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-4"><i class="fas fa-list-ul text-[#9b2247] mr-2"></i>Marco Analítico y Variables</h2>
            <p class="text-gray-600 mb-8 max-w-3xl">Clasificación de variables para analizar el <strong>No surtimiento de recetas</strong>.</p>
            <div class="glass rounded-2xl p-6 overflow-x-auto mb-8">
                <h3 class="font-bold text-lg text-gray-800 mb-4 border-b pb-2">Variables Independientes y de Control</h3>
                <div id="variablesContainer"></div>
            </div>
        </div>
    </section>

    <!-- SECTION: INDICADORES -->
    <section id="indicadores" class="bg-gradient-to-b from-white to-gray-50 py-12">
        <div class="container mx-auto px-4">
            <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-4"><i class="fas fa-chart-line text-[#1e5b4f] mr-2"></i>Sistema de Indicadores Ampliado</h2>
            <p class="text-gray-600 mb-8 max-w-3xl">Indicadores de cobertura, oportunidad, calidad/estructura y satisfacción.</p>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6" id="indicadoresContainer"></div>
        </div>
    </section>

    <!-- SECTION: TAXONOMIA -->
    <section id="causas" class="bg-white py-12">
        <div class="container mx-auto px-4">
            <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-4"><i class="fas fa-sitemap text-[#a57f2c] mr-2"></i>Taxonomía de Causas de No Surtimiento</h2>
            <p class="text-gray-600 mb-8 max-w-3xl">Clasificación de las diferentes causas que limitan o impiden el surtimiento completo y oportuno.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" id="taxonomiaContainer"></div>
        </div>
    </section>"""
if marco_old not in content: print("Missing marco")
content = content.replace(marco_old, marco_new)

# 3. Metodologia: Instrumentos + Muestreo
meto_old = """        <h3 class="font-bold text-lg mb-6 text-gray-800"><i class="fas fa-tools text-[#9b2247] mr-2"></i>Instrumentos de
            Medicion. </h3>
        <p class="text-gray-500 text-sm mb-6">Pueden montarse en Google Forms y Excel para agilidad en campo.</p>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" id="instrumentosGrid"></div>
    </section>"""

meto_new = """        <h3 class="font-bold text-lg mb-6 text-gray-800"><i class="fas fa-tools text-[#9b2247] mr-2"></i>Instrumentos de Medicion. </h3>
        <p class="text-gray-500 text-sm mb-6">Pueden montarse en Google Forms y Excel para agilidad en campo.</p>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12" id="instrumentosGrid"></div>

        <h3 class="font-bold text-lg mb-6 text-gray-800 border-t pt-8"><i class="fas fa-users text-[#1e5b4f] mr-2"></i>Plan de Muestreo</h3>
        <div class="glass rounded-2xl p-6 overflow-x-auto">
            <table class="w-full text-sm text-left border-collapse">
                <thead class="bg-gray-50 text-gray-700">
                    <tr><th class="p-3 border-b border-gray-200">Componente</th><th class="p-3 border-b border-gray-200">Universo</th><th class="p-3 border-b border-gray-200">Tipo de muestreo</th></tr>
                </thead>
                <tbody class="text-gray-600">
                    <tr class="border-b border-gray-100 hover:bg-gray-50"><td class="p-3 font-semibold">Análisis administrativo (recetas)</td><td class="p-3">Todas las recetas emitidas</td><td class="p-3">Censo o probabilística estratificada</td></tr>
                    <tr class="border-b border-gray-100 hover:bg-gray-50"><td class="p-3 font-semibold">Instrumento a personal</td><td class="p-3">Todo el personal en farmacias / CxC</td><td class="p-3">Censo o aleatorio simple</td></tr>
                    <tr class="border-b border-gray-100 hover:bg-gray-50"><td class="p-3 font-semibold">Instrumento a usuarios</td><td class="p-3">Beneficiarios con receta</td><td class="p-3">Aleatorio estratificado</td></tr>
                    <tr class="hover:bg-gray-50"><td class="p-3 font-semibold">Cualitativo</td><td class="p-3">Submuestra usuarios/personal</td><td class="p-3">Intencional (15-30 entrevistas)</td></tr>
                </tbody>
            </table>
        </div>
    </section>"""
if meto_old not in content: print("Missing meto")
content = content.replace(meto_old, meto_new)

# 4. Resumen section (inject Productos Esperados before Proximos pasos)
resumen_old = """    <!-- SECTION 5: PROXIMOS PASOS -->
    <section id="resumen" class="container mx-auto px-4 py-12">"""

resumen_new = """    <!-- SECTION 5: PRODUCTOS ESPERADOS -->
    <section id="productos" class="bg-gradient-to-b from-gray-50 to-white py-12">
        <div class="container mx-auto px-4">
            <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-8"><i class="fas fa-box-open text-[#6b21a8] mr-2"></i>Productos Esperados</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="productosContainer"></div>
        </div>
    </section>

    <!-- SECTION 6: PROXIMOS PASOS -->
    <section id="resumen" class="container mx-auto px-4 py-12">"""
if resumen_old not in content: print("Missing resumen")
content = content.replace(resumen_old, resumen_new)

# 5. JS INJECTION
js_inj_old = """        // ===== RENDER =====
        function renderFlow() {"""

js_inj_new = """        // --- NUEVOS DATOS INTEGRADOS ---
        const dimensionesNuevas = [
            { title: 'Disponibilidad', subtitle: 'Inventario', icon: 'fa-box', color: '#6b21a8', desc: 'El medicamento prescrito se encuentra en el inventario de la farmacia.', metric: 'Sí/No' },
            { title: 'Completitud', subtitle: 'Nivel de Surtimiento', icon: 'fa-chart-pie', color: '#9b2247', desc: 'Porcentaje de recetas surtidas completas vs. parciales o nulas.', metric: '% claves surtidas' },
            { title: 'Oportunidad', subtitle: 'Tiempos Logísticos', icon: 'fa-clock', color: '#a57f2c', desc: 'Plazo desde emisión de la receta hasta entrega.', metric: 'Días promedio' },
            { title: 'Concordancia', subtitle: 'Exactitud', icon: 'fa-check-double', color: '#1e5b4f', desc: 'Surtido coincide con prescrito (clave, dosis, presentación).', metric: 'Sí/No' },
            { title: 'Aceptabilidad', subtitle: 'Usuario', icon: 'fa-user-check', color: '#ea580c', desc: 'El usuario recibe el medicamento y acepta su uso.', metric: 'Sí/No, rechazo' },
            { title: 'Trazabilidad', subtitle: 'Visibilidad', icon: 'fa-eye', color: '#0369a1', desc: 'Registro documental de cada paso del proceso.', metric: '% pasos' }
        ];

        const cascada = [
            "Emisión de la receta (consulta domiciliaria)", "Registro de la receta (sistema)", "Generación de pedido/requisición", 
            "Envío a la farmacia (logística)", "Recepción en farmacia y verificación", "Disponibilidad en inventario",
            "Conformación de paquete individualizado", "Surtimiento (entrega/envío)", "Recepción por el usuario", "Confirmación del surtimiento"
        ];

        const categoriasSurtimiento = [
            { cat: "Surtimiento Completo", desc: "100% de las claves prescritas entregadas." },
            { cat: "Surtimiento Parcial", desc: "≥1 clave surtida pero no la totalidad." },
            { cat: "No Surtimiento", desc: "Ninguna clave de la receta entregada." },
            { cat: "Surtimiento con Sustitución", desc: "Entrega de equivalente terapéutico (genérico)." }
        ];

        const tiemposSurtimiento = [
            { tipo: "Inmediato", rango: "Mismo día" },
            { tipo: "Oportuno", rango: "1-3 días hábiles" },
            { tipo: "Demorado", rango: "4-7 días hábiles" },
            { tipo: "Muy demorado", rango: "8-14 días hábiles" },
            { tipo: "Extemporáneo", rango: "> 14 días" },
            { tipo: "No surtido", rango: "Sin fecha de entrega" }
        ];

        const variablesInfo = [
            { var: "Desabasto en farmacia", tipo: "Independiente", fuente: "Registro administrativo" },
            { var: "Receta fuera de catálogo", tipo: "Independiente", fuente: "BD recetas vs catálogo" },
            { var: "Error en prescripción", tipo: "Independiente", fuente: "Revisión de recetas" },
            { var: "Capacitación de personal", tipo: "Independiente", fuente: "Instrumento cuantitativo" },
            { var: "Distancia usuario - farmacia", tipo: "Independiente", fuente: "Geo-referenciación" },
            { var: "Coordinación interinstitucional", tipo: "Independiente", fuente: "Instrumento personal" },
            { var: "Ubicación geográfica (farmacia)", tipo: "Control", fuente: "Urbano/Periurbano/Rural" },
            { var: "Volumen de recetas emitidas", tipo: "Control", fuente: "Carga de trabajo" },
            { var: "Número de claves por receta", tipo: "Control", fuente: "Complejidad surtimiento" }
        ];

        const indicadoresList = [
            { cat: "Cobertura", ind: "% de recetas surtidas", meta: "≥ 90%", color:"#9b2247" },
            { cat: "Cobertura", ind: "% de recetas no surtidas", meta: "≤ 5%", color:"#9b2247" },
            { cat: "Cobertura", ind: "% de recetas surtidas parcial", meta: "≤ 5%", color:"#9b2247" },
            { cat: "Cobertura", ind: "% de claves surtidas", meta: "≥ 95%", color:"#9b2247" },
            { cat: "Oportunidad", ind: "Tiempo promedio surtimiento", meta: "≤ 3 días", color:"#a57f2c" },
            { cat: "Oportunidad", ind: "% surtidas en ≤3 días", meta: "≥ 85%", color:"#a57f2c" },
            { cat: "Calidad", ind: "Tasa de quiebre de stock", meta: "≤ 5%", color:"#1e5b4f" },
            { cat: "Calidad", ind: "Tasa de error en prescripción", meta: "≤ 2%", color:"#1e5b4f" },
            { cat: "Satisfacción", ind: "Índice de satisfacción (1-5)", meta: "≥ 4.0", color:"#0369a1" },
            { cat: "Satisfacción", ind: "% usuarios reportan buen trato", meta: "≥ 90%", color:"#0369a1" }
        ];

        const taxonomiaList = [
            { grupo: "Causas Estructurales", color: "#6b21a8", icon: "fa-building", items: ["Medicamento fuera de catálogo", "Quiebre de stock", "Falla en cadena de abastecimiento", "Desalineación BIRMEX - Bienestar", "Insuficiencia de catálogo"] },
            { grupo: "Causas Operativas", color: "#ea580c", icon: "fa-cogs", items: ["Error en prescripción médica", "Receta no registrada", "Paquete incompleto", "Retraso logístico", "Falta de trazabilidad digital"] },
            { grupo: "Causas del Usuario", color: "#db2777", icon: "fa-users", items: ["No acudió a recoger", "Domicilio incorrecto / sin notificar", "Abandono del tratamiento", "Desconfianza hacia el programa", "Confusión en indicaciones"] },
            { grupo: "Causas Territoriales", color: "#0d9488", icon: "fa-map-marked-alt", items: ["Ubicación inaccesible", "Zonas mal delimitadas", "Factores climatológicos", "Inseguridad / amenazas"] }
        ];

        const productosList = [
            "Diagnóstico de brechas en cascada", "Reporte de bases administrativas",
            "Informe instrumentos cuantitativos", "Informe cualitativo (entrevistas)",
            "Dashboard de indicadores para monitoreo", "Recomendaciones técnicas accionables", "Protocolo de trazabilidad digital"
        ];

        // ===== RENDER =====
        function renderFlow() {"""
if js_inj_old not in content: print("Missing js inj")
content = content.replace(js_inj_old, js_inj_new)

# 6. Change renderDimensiones references
render_dim_old = """        function renderDimensiones() {
            document.getElementById('dimensionesGrid').innerHTML = dimensiones.map(d => `"""
render_dim_new = """        function renderDimensiones() {
            document.getElementById('dimensionesGrid').innerHTML = dimensionesNuevas.map(d => `"""
if render_dim_old not in content: print("Missing render dim")
content = content.replace(render_dim_old, render_dim_new)

# 7. Add new render functions to init
init_old = """        // ===== INIT =====
        document.addEventListener('DOMContentLoaded', () => {
            renderFlow();
            renderDimensiones();
            renderBarreras();
            renderMetodologia();
            renderCedulaOptions();
            renderNextSteps();
            renderGantt();
            // Active tab highlight on scroll"""

init_new = """        function renderNuevasSecciones() {
            // Cascada
            document.getElementById('cascadaContainer').innerHTML = cascada.map((c, i) => `
                <div class="flex items-center text-sm fade-up" style="animation-delay: ${i*0.05}s"><div class="w-6 h-6 rounded-full bg-[#0369a1] text-white flex items-center justify-center text-xs font-bold mr-3 flex-shrink-0">${i+1}</div>
                <div class="text-gray-700 bg-white border border-gray-100 rounded-lg shadow-sm w-full p-3 flex justify-between items-center hover:border-[#0369a1] transition"><span class="font-medium">${c}</span>${i < cascada.length - 1 ? '<i class="fas fa-arrow-down text-gray-300"></i>' : ''}</div></div>
            `).join('');

            // Categorias
            document.getElementById('categoriasContainer').innerHTML = categoriasSurtimiento.map(c => `
                <div class="border-l-4 border-[#6b21a8] pl-4 py-2 mb-3 bg-white shadow-sm rounded-r-lg hover:shadow-md transition"><span class="font-bold text-gray-800 block text-sm mb-1">${c.cat}</span><span class="text-xs text-gray-500">${c.desc}</span></div>
            `).join('');

            // Tiempos
            document.getElementById('tiemposContainer').innerHTML = tiemposSurtimiento.map(t => `
                <div class="flex justify-between items-center border-b border-gray-100 py-3 hover:bg-gray-50 transition px-2 rounded"><span class="font-medium text-gray-700 text-sm">${t.tipo}</span><span class="text-xs bg-[#ea580c]/10 text-[#ea580c] font-bold px-3 py-1 rounded-full">${t.rango}</span></div>
            `).join('');

            // Variables
            document.getElementById('variablesContainer').innerHTML = `<table class="w-full text-sm text-left border-collapse"><thead class="bg-gray-50 text-gray-700"><tr><th class="p-3 border-b font-bold">Variable</th><th class="p-3 border-b font-bold">Tipo</th><th class="p-3 border-b font-bold">Fuente / Justificación</th></tr></thead><tbody>` + 
                variablesInfo.map(v => `<tr class="border-b border-gray-50 hover:bg-gray-50 transition"><td class="p-3 text-gray-800 font-medium"><i class="fas fa-microscope text-gray-400 mr-2 text-xs"></i>${v.var}</td><td class="p-3 text-gray-500"><span class="text-[10px] font-bold uppercase tracking-wider bg-gray-100 px-2 py-1 rounded-full">${v.tipo}</span></td><td class="p-3 text-gray-500">${v.fuente}</td></tr>`).join('') + `</tbody></table>`;

            // Indicadores
            document.getElementById('indicadoresContainer').innerHTML = indicadoresList.map((i, idx) => `
                <div class="bg-white p-5 rounded-2xl shadow-sm border border-gray-100 flex items-center justify-between hover:shadow-md transition fade-up" style="animation-delay: ${idx*0.1}s">
                    <div class="flex items-center gap-4">
                        <div class="w-1.5 h-12 rounded-full" style="background:${i.color}"></div>
                        <div><span class="text-[10px] font-bold px-2 py-0.5 rounded-full mb-1 inline-block uppercase tracking-wider" style="background:${i.color}15; color:${i.color}">${i.cat}</span><div class="text-sm font-bold text-gray-800">${i.ind}</div></div>
                    </div>
                    <div class="text-right"><div class="text-xs text-gray-400 mb-1 font-medium">Meta</div><div class="font-bold text-lg" style="color:${i.color}">${i.meta}</div></div>
                </div>
            `).join('');

            // Taxonomia
            document.getElementById('taxonomiaContainer').innerHTML = taxonomiaList.map((t, idx) => `
                <div class="glass rounded-2xl p-6 border-t-4 hover:shadow-lg transition fade-up" style="border-color:${t.color}; animation-delay: ${idx*0.1}s">
                    <h4 class="font-bold text-gray-800 mb-4 text-lg"><i class="fas ${t.icon} mr-2" style="color:${t.color}"></i>${t.grupo}</h4>
                    <ul class="space-y-3">${t.items.map(item => `<li class="text-sm text-gray-600 flex items-start gap-2"><i class="fas fa-exclamation-triangle text-[10px] mt-1 opacity-50" style="color:${t.color}"></i><span>${item}</span></li>`).join('')}</ul>
                </div>
            `).join('');

            // Productos
            document.getElementById('productosContainer').innerHTML = productosList.map((p, i) => `
                <div class="glass p-5 rounded-2xl flex items-center gap-4 hover:transform hover:-translate-y-1 transition duration-300 fade-up" style="animation-delay: ${i*0.1}s">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-[#6b21a8] to-[#4c1d95] text-white flex items-center justify-center font-bold text-lg shadow-lg flex-shrink-0"><i class="fas fa-check"></i></div>
                    <div class="text-sm font-semibold text-gray-800">${p}</div>
                </div>
            `).join('');
        }

        // ===== INIT =====
        document.addEventListener('DOMContentLoaded', () => {
            renderFlow();
            renderDimensiones();
            renderBarreras();
            renderMetodologia();
            renderCedulaOptions();
            renderNextSteps();
            renderGantt();
            renderNuevasSecciones();
            // Active tab highlight on scroll"""
if init_old not in content: print("Missing init")
content = content.replace(init_old, init_new)

# 8. Add active nav sections
nav_sections_old = """const sections = ['ruta', 'marco', 'barreras', 'metodologia', 'cedula', 'resumen'];"""
nav_sections_new = """const sections = ['ruta', 'marco', 'variables', 'indicadores', 'causas', 'barreras', 'metodologia', 'cedula', 'productos', 'resumen'];"""
if nav_sections_old not in content: print("Missing nav sections")
content = content.replace(nav_sections_old, nav_sections_new)

# Write to file
with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
print("HTML Update Script Complete.")
