import sys

html_path = r"c:\Users\Lenovo\OneDrive\Escritorio\APPs\Feria de la Salud\casaxcasa-barreras.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

nav_item = """            <a href="#productos" class="tab-btn px-4 py-2 rounded-lg whitespace-nowrap hover:bg-gray-50"><i class="fas fa-box-open mr-1"></i>Productos</a>\n"""
content = content.replace(nav_item, "")

section_html = """    <!-- SECTION 5: PRODUCTOS ESPERADOS -->
    <section id="productos" class="bg-gradient-to-b from-gray-50 to-white py-12">
        <div class="container mx-auto px-4">
            <h2 class="section-title font-patria text-2xl md:text-3xl font-bold text-[#161a1d] mb-8"><i class="fas fa-box-open text-[#6b21a8] mr-2"></i>Productos Esperados</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="productosContainer"></div>
        </div>
    </section>\n\n"""
content = content.replace(section_html, "")

js_const = """        const productosList = [
            "Diagnóstico de brechas en cascada", "Reporte de bases administrativas",
            "Informe instrumentos cuantitativos", "Informe cualitativo (entrevistas)",
            "Dashboard de indicadores para monitoreo", "Recomendaciones técnicas accionables", "Protocolo de trazabilidad digital"
        ];\n\n"""
content = content.replace(js_const, "")

js_render = """            // Productos
            document.getElementById('productosContainer').innerHTML = productosList.map((p, i) => `
                <div class="glass p-5 rounded-2xl flex items-center gap-4 hover:transform hover:-translate-y-1 transition duration-300 fade-up" style="animation-delay: ${i*0.1}s">
                    <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-[#6b21a8] to-[#4c1d95] text-white flex items-center justify-center font-bold text-lg shadow-lg flex-shrink-0"><i class="fas fa-check"></i></div>
                    <div class="text-sm font-semibold text-gray-800">${p}</div>
                </div>
            `).join('');\n"""
content = content.replace(js_render, "")

nav_sections_old = """const sections = ['ruta', 'marco', 'variables', 'indicadores', 'causas', 'barreras', 'metodologia', 'cedula', 'productos', 'resumen'];"""
nav_sections_new = """const sections = ['ruta', 'marco', 'variables', 'indicadores', 'causas', 'barreras', 'metodologia', 'cedula', 'resumen'];"""
content = content.replace(nav_sections_old, nav_sections_new)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Removed Productos Esperados")
