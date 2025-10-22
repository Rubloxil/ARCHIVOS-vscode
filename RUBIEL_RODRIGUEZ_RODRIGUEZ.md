# Semana 01 - Introducción al Paradigma Orientado a Objetos

**Estudiante:** Rubiel Rodriguez Rodriguez  
**Ficha:** 3228970B  
**Dominio Asignado:** Taller de Carpintería "Madera y Arte"

---

## 📋 Contexto del Dominio

**Tipo de Negocio:** Taller de Carpintería y Ebanistería  
**Nombre Comercial:** Madera y Arte  
**Ubicación:** Bogotá, Localidad de Fontibón  
**Especialidad:** Muebles a medida, reparaciones, restauración de madera

### Descripción Breve
Madera y Arte es un taller de carpintería que fabrica muebles a medida, realiza reparaciones y restauración de muebles antiguos. Cuenta con 6 carpinteros especializados y produce aproximadamente 20 muebles mensuales.

---

## 🎯 Objetivos de la Semana 01

Al finalizar esta semana, deberás ser capaz de:

1. Identificar objetos del mundo real en el contexto de un taller de carpintería
2. Comprender las diferencias entre programación estructurada y POO
3. Reconocer los conceptos fundamentales: clase, objeto, atributo, método
4. Crear tu primera clase simple en Java aplicada al dominio

---

## 📝 Actividades Obligatorias

### Actividad 1: Identificación de Objetos (Ejercicio 01)

**Instrucciones:**
- Lee el material teórico de la semana sobre conceptos fundamentales de POO
- Identifica **5 objetos principales** que existen en un taller de carpintería
- Para cada objeto, describe:
  - ¿Qué es? (definición)
  - ¿Qué características tiene? (atributos)
  - ¿Qué puede hacer? (comportamientos/métodos)

**Ejemplo:**
```
Objeto: Orden de Trabajo
- ¿Qué es?: Un pedido de fabricación o reparación de un mueble
- Características: número de orden, cliente, tipo de mueble, dimensiones, madera, costo
- Comportamientos: registrar orden, asignar carpintero, calcular costo, actualizar estado
```

**Entregable:** Documento con la identificación de 5 objetos del dominio del taller de carpintería.

---

### Actividad 2: Comparación de Paradigmas (Ejercicio 02)

**Instrucciones:**
- Investiga las diferencias entre programación estructurada y POO
- Escribe un ejemplo conceptual de cómo se manejaría la información de una orden de trabajo en:
  1. **Programación estructurada** (usando variables sueltas y funciones)
  2. **Programación orientada a objetos** (usando una clase)

**Entregable:** Documento comparativo con ejemplos explicados.

---

### Actividad 3: Primera Clase Simple (Ejercicio 03)

**Instrucciones:**
Crea tu primera clase en Java llamada `WorkOrder` (Orden de Trabajo) con:
- **3 atributos** (ej: `orderNumber`, `furnitureType`, `price`)
- **1 constructor** que inicialice los atributos
- **1 método** que muestre la información de la orden

**Código de ejemplo:**

```java
public class WorkOrder {
    // Atributos
    String orderNumber;
    String furnitureType;
    double price;
    
    // Constructor
    public WorkOrder(String orderNumber, String furnitureType, double price) {
        this.orderNumber = orderNumber;
        this.furnitureType = furnitureType;
        this.price = price;
    }
    
    // Método para mostrar información
    public void showInfo() {
        System.out.println("Orden No.: " + orderNumber);
        System.out.println("Mueble: " + furnitureType);
        System.out.println("Precio: $" + price);
    }
}
```

**Instrucciones adicionales:**
1. Crea una clase `Main` con el método `main`
2. Instancia **3 objetos diferentes** de tipo `WorkOrder`
3. Llama al método `showInfo()` para cada objeto

**Entregable:** Archivo `WorkOrder.java` y `Main.java` funcionando correctamente.

---

### Actividad 4: Múltiples Objetos (Ejercicio 04)

**Instrucciones:**
Amplía el ejercicio anterior:
- Crea al menos **5 objetos** de tipo `WorkOrder` con datos diferentes
- Cada orden debe tener información coherente con un taller de carpintería
- Muestra la información de todas las órdenes

**Ejemplo de datos:**
- ORD-001, Mesa de Comedor, $850000
- ORD-002, Biblioteca, $1200000
- ORD-003, Cama King Size, $950000
- ORD-004, Escritorio Ejecutivo, $680000
- ORD-005, Closet a Medida, $1500000

**Entregable:** Código Java con 5 instancias de `WorkOrder` y su salida en consola.

---

## 🎓 Criterios de Evaluación

| Criterio | Peso | Descripción |
|----------|------|-------------|
| **Identificación de objetos** | 25% | Objetos identificados son relevantes al dominio del taller de carpintería |
| **Comprensión conceptual** | 25% | Demuestra entender diferencias entre paradigmas |
| **Implementación de clase** | 30% | Clase `WorkOrder` implementada correctamente con atributos, constructor y método |
| **Instanciación de objetos** | 20% | Crea múltiples objetos con datos coherentes |

---

## 📚 Recursos de Apoyo

### Material Teórico (Carpeta `1-teoria/`)
- `01-historia-evolucion-poo.md`
- `02-paradigmas-programacion.md`
- `03-conceptos-fundamentales-poo.md`
- `04-primer-programa-poo.md`

### Ejercicios Guiados (Carpeta `2-practica/`)
- `ejercicio-01-comparacion-paradigmas/`
- `ejercicio-02-primera-clase/`
- `ejercicio-03-multiples-objetos/`
- `ejercicio-04-modelado-mundo-real/`

### Glosario
Revisa el archivo `3-recursos/glosario.md` para términos clave de esta semana.

---

## 💡 Consejos

1. **No te compliques:** Esta semana es sobre conceptos básicos, no sobre código complejo
2. **Piensa en objetos reales:** Visualiza cómo funciona un taller de carpintería real
3. **Pregunta:** Si tienes dudas sobre el dominio o los conceptos, consulta con el instructor
4. **Compila y prueba:** Asegúrate de que tu código compile antes de entregar

---

## 📅 Fecha de Entrega

**Entrega:** Según calendario definido por el instructor  
**Formato:** Código fuente (.java) y documentos en formato Markdown o PDF

---

**Nota Importante:** Este es tu dominio personal para todo el bootcamp. Todas las actividades futuras seguirán en el contexto del taller de carpintería Madera y Arte. No compartas tu código directamente con otros estudiantes, ya que cada uno tiene un dominio diferente.
