import sys
import re

with open('c:/Users/Lenovo/OneDrive/Escritorio/APPs/Feria de la Salud/dashboard-feria-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace header texts
content = content.replace('Victoria 1 (Echeverría) | 11 de Febrero 2026', 'Pajaritos, Victoria | 26 de Febrero 2026')
content = content.replace('Victoria 1 (Echeverría)', 'Pajaritos, Victoria')
content = content.replace('11 de Febrero 2026', '26 de Febrero 2026')
content = content.replace('Feria_Salud_11Feb2026_Victoria_Echeverria.csv', 'Feria_Salud_26Feb2026_Victoria_Pajaritos.csv')
content = content.replace('Feria_Salud_11Feb2026_Victoria_Echeverria.pdf', 'Feria_Salud_26Feb2026_Victoria_Pajaritos.pdf')
content = content.replace('Corredor DIF Victoria 1', 'Corredor DIF Pajaritos, Victoria')
content = content.replace('11 de Febrero de 2026', '26 de Febrero de 2026')
content = content.replace('~580', '~350')
content = content.replace('580),', '350),')

# Replace HTML section titles
content = content.replace('Salud Bucal', 'Estilo de Vida Saludable')
content = content.replace('Acciones preventivas de salud bucal', 'Evaluaciones e intervenciones')
content = content.replace('Detecciones IMSS', 'Detecciones Médicas')
content = content.replace('Pruebas rápidas y somatometría', 'Identificación de riesgos a la salud')
content = content.replace('Nutrición y Estilo de Vida', 'Asesoría y Salud Mental')
content = content.replace('Acciones de medicina preventiva y nutrición', 'Consultas, pláticas y consejería')

# The `programas` array starts at 'const programas = [' and ends at '];' before '// ============ CALCULATIONS ============'
old_programas_match = re.search(r'const programas = \[.*?\];', content, re.DOTALL)
if old_programas_match:
    new_programas = '''const programas = [
            {
                programa: "iBreast Exam y Exploración Clínica Mama",
                dependencia: "Sec. de Salud - Dir. Gral. de Enfermería",
                categoria: "Detección Cáncer",
                icon: "fa-ribbon",
                color: "#db2777",
                servicios: [
                    { nombre: "Exploración Clínica de mama", cantidad: 43 },
                    { nombre: "Tamizajes iBreast Exam", cantidad: 43 },
                    { nombre: "Orientación signos alarma CaMa", cantidad: 43 },
                    { nombre: "Orientación autoexploración", cantidad: 43 },
                    { nombre: "Referencia a mastografía", cantidad: 22 },
                    { nombre: "Referencia a Salud mental", cantidad: 2 }
                ]
            },
            {
                programa: "Medicina de Estilo de Vida Saludable",
                dependencia: "DSB 1 Victoria - CE Adolfo López Mateos",
                categoria: "Estilo de Vida",
                icon: "fa-apple-whole",
                color: "#16a34a",
                servicios: [
                    { nombre: "Tamizaje", cantidad: 117 },
                    { nombre: "Entrega de trípticos", cantidad: 117 },
                    { nombre: "Orientación Habitos saludables", cantidad: 117 },
                    { nombre: "Evaluación de IMC", cantidad: 117 },
                    { nombre: "Gestiones para Apoyo", cantidad: 3 }
                ]
            },
            {
                programa: "Detecciones",
                dependencia: "Secretaría de Salud - Distrito 1",
                categoria: "Detección",
                icon: "fa-vials",
                color: "#6b21a8",
                servicios: [
                    { nombre: "Detección Hipertensión Arterial", cantidad: 100 },
                    { nombre: "Detección Diabetes Mellitus", cantidad: 100 },
                    { nombre: "Detección Papanicolaou", cantidad: 3 },
                    { nombre: "Detección VPH", cantidad: 2 }
                ]
            },
            {
                programa: "Atención y Asesorías",
                dependencia: "Secretaría de Salud - Distrito 1",
                categoria: "Asesoría",
                icon: "fa-user-doctor",
                color: "#e11d48",
                servicios: [
                    { nombre: "Consulta médica", cantidad: 67 },
                    { nombre: "Consulta Salud Mental", cantidad: 9 },
                    { nombre: "Entrega de Información Salud Mental", cantidad: 20 },
                    { nombre: "Consejería Planificación Familiar", cantidad: 12 },
                    { nombre: "Consejería sobre violencia", cantidad: 12 },
                    { nombre: "Consejería Cáncer de la mujer", cantidad: 12 },
                    { nombre: "Entrega de Cartilla de Vacunación", cantidad: 10 }
                ]
            },
            {
                programa: "Vacunación Humana y Zoonosis",
                dependencia: "Secretaría de Salud - Barrio de Pajaritos",
                categoria: "Vacunación",
                icon: "fa-syringe",
                color: "#2563eb",
                servicios: [
                    { nombre: "Vacuna Influenza", cantidad: 33 },
                    { nombre: "Vacuna SR", cantidad: 32 },
                    { nombre: "Vacuna Neumococo", cantidad: 5 },
                    { nombre: "Vacuna Antitetánica", cantidad: 2 },
                    { nombre: "Vacunación Antirrábica Canina", cantidad: 25 }
                ]
            },
            {
                programa: "Padrón IMSS Bienestar",
                dependencia: "Servicios Públicos de Salud IMSS Bienestar",
                categoria: "Afiliación",
                icon: "fa-id-card",
                color: "#0369a1",
                servicios: [
                    { nombre: "Registros al IMSS Bienestar", cantidad: 40 }
                ]
            },
            {
                programa: "Farmacia",
                dependencia: "IMSS Bienestar",
                categoria: "Farmacia",
                icon: "fa-pills",
                color: "#0d9488",
                servicios: [
                    { nombre: "Receta Médica", cantidad: 107 },
                    { nombre: "Medicamento", cantidad: 286 }
                ]
            }
        ];'''
    content = content.replace(old_programas_match.group(0), new_programas)

# Animate persons approx
content = content.replace("animateCounter(document.getElementById('totalPersonas'), 580);", "animateCounter(document.getElementById('totalPersonas'), 350);")

# Replace Charts
content = content.replace('''labels: ['Exploración Mamaria', 'iBreast Exam', 'Signos CaMa', 'Autoexploración'],
                datasets: [{ data: [41, 41, 41, 41], backgroundColor: ['#db277790', '#f472b690', '#ec489990', '#f9a8d490'], borderColor: ['#db2777', '#f472b6', '#ec4899', '#f9a8d4'], borderWidth: 1, borderRadius: 4 }]''',
'''labels: ['Exploración', 'iBreast Exam', 'Signos CaMa', 'Autoexploración', 'Mastografía', 'Salud mental'],
                datasets: [{ data: [43, 43, 43, 43, 22, 2], backgroundColor: ['#db277790', '#f472b690', '#ec489990', '#f9a8d490', '#be185d90', '#e11d4890'], borderColor: ['#db2777', '#f472b6', '#ec4899', '#f9a8d4', '#be185d', '#e11d48'], borderWidth: 1, borderRadius: 4 }]''')

content = content.replace('''labels: ['SRP', 'Influenza', 'Neumococo 13', 'Hexavalente'],
                datasets: [{ data: [24, 7, 4, 2], backgroundColor: ['#2563eb88', '#3b82f688', '#60a5fa88', '#93c5fd88'], borderColor: ['#2563eb', '#3b82f6', '#60a5fa', '#93c5fd'], borderWidth: 2 }]''',
'''labels: ['Influenza', 'SR', 'Neumococo', 'Antitetánica', 'Zoonosis'],
                datasets: [{ data: [33, 32, 5, 2, 25], backgroundColor: ['#2563eb88', '#3b82f688', '#60a5fa88', '#93c5fd88', '#ea580c88'], borderColor: ['#2563eb', '#3b82f6', '#60a5fa', '#93c5fd', '#ea580c'], borderWidth: 2 }]''')

content = content.replace('''labels: ['Plática', 'Cepillos', 'Trípticos', 'Revisión', 'Consulta'],
                datasets: [{ data: [40, 63, 63, 40, 12], backgroundColor: '#0d948833', borderColor: '#0d9488', pointBackgroundColor: '#0d9488', borderWidth: 2 }]''',
'''labels: ['Tamizaje', 'Trípticos', 'Hábitos', 'IMC'],
                datasets: [{ data: [117, 117, 117, 117], backgroundColor: '#16a34a33', borderColor: '#16a34a', pointBackgroundColor: '#16a34a', borderWidth: 2 }]''')

content = content.replace('''labels: ['Somatometría', 'Glucosa', 'VIH', 'Hepatitis', 'Sífilis', 'Presión Arterial'],
                datasets: [{ data: [50, 50, 50, 50, 50, 50], backgroundColor: '#6b21a8aa', borderColor: '#6b21a8', borderWidth: 1, borderRadius: 4 }]''',
'''labels: ['HTA', 'Diabetes', 'Papanicolaou', 'VPH'],
                datasets: [{ data: [100, 100, 3, 2], backgroundColor: '#6b21a8aa', borderColor: '#6b21a8', borderWidth: 1, borderRadius: 4 }]''')

content = content.replace('''labels: ['Tamizajes', 'Eval. Nutricional', 'Hábitos Saludables', 'Trípticos', 'Canalización'],
                datasets: [{ data: [108, 108, 108, 108, 5], backgroundColor: ['#16a34aaa', '#22c55eaa', '#4ade80aa', '#86efacaa', '#bbf7d0aa'], borderColor: ['#16a34a', '#22c55e', '#4ade80', '#86efac', '#bbf7d0'], borderWidth: 1, borderRadius: 4 }]''',
'''labels: ['Consulta Mental', 'Info Mental', 'Prev. Violencia', 'Consejería PF', 'CaMa Mujer'],
                datasets: [{ data: [9, 20, 12, 12, 12], backgroundColor: ['#ea580caa', '#f97316aa', '#fb923caa', '#fdba74aa', '#ffedd5aa'], borderColor: ['#ea580c', '#f97316', '#fb923c', '#fdba74', '#ffedd5'], borderWidth: 1, borderRadius: 4 }]''')

with open('c:/Users/Lenovo/OneDrive/Escritorio/APPs/Feria de la Salud/dashboard-feria-2.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
