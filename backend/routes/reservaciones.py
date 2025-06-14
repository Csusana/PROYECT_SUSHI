from flask import Blueprint, jsonify, request
from db import get_connection

reservaciones_bp = Blueprint("reservaciones", __name__)

CAPACIDAD_HANA = 100


@reservaciones_bp.route("/guardar", methods=["POST"])
def guardar_reservacion():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    data = request.get_json()

    if (
        "nombre_completo" not in data
        or "fecha" not in data
        or "hora" not in data
        or "cant_personas" not in data
    ):
        return (
            jsonify(
                {
                    "error": "Debe enviar un JSON en el body con los campos: 'nombre_completo', 'fecha', 'hora' y 'cant_personas'."
                }
            ),
            400,
        )

    nombre_completo = data["nombre_completo"]
    fecha = data["fecha"]
    hora = data["hora"]
    cant_personas = data["cant_personas"]

    if type(nombre_completo) != str or type(fecha) != str or type(hora) != str:
        return (
            jsonify(
                {
                    "error": "Los campos 'nombre_completo', 'fecha' y 'hora' en el body de la petición deben ser strings."
                }
            ),
            400,
        )
    elif type(cant_personas) != int:
        return (
            jsonify(
                {
                    "error": "El campo 'cant_personas' en el body de la petición debe ser un número entero."
                }
            ),
            400,
        )
    elif nombre_completo == "" or fecha == "" or hora == "":
        return (
            jsonify(
                {
                    "error": "Los campos 'nombre_completo', 'fecha' y 'hora' en el body de la petición no deben ser vacíos."
                }
            ),
            400,
        )
    elif cant_personas <= 0:
        return (
            jsonify(
                {
                    "error": "El campo 'cant_personas' en el body de la petición debe ser un número mayor a cero."
                }
            ),
            400,
        )

    cursor.execute(
        """
        SELECT 1 FROM reservaciones 
        WHERE nombre_completo = %s AND fecha = %s AND hora = %s AND cant_personas = %s
        LIMIT 1
        """,
        (nombre_completo, fecha, hora, cant_personas),
    )
    repetido = cursor.fetchone()
    if repetido:
        return (
            jsonify({"error": "Ya existe una reservación con los mismos datos."}),
            409,
        )

    cursor.execute(
        """
        INSERT INTO reservaciones (nombre_completo, fecha, hora, cant_personas)
        VALUES (%s, %s, %s, %s)
        """,
        (nombre_completo, fecha, hora, cant_personas),
    )

    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"success": "Reservación guardada correctamente."}), 201


@reservaciones_bp.route("/disponibilidad")
def chequear_disponibilidad():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    data = request.get_json()

    if "fecha" not in data or "hora" not in data or "cant. personas" not in data:
        return (
            jsonify(
                {
                    "error": "El JSON envíado debe contener 'fecha', 'hora' y 'cant. personas'."
                }
            ),
            400,
        )

    fecha = data["fecha"]
    hora = data["hora"]
    cant_personas = data["cant. personas"]

    if type(cant_personas) != int:
        return (
            jsonify(
                {
                    "error": "El campo 'cant. personas' del JSON envíado debe ser un entero."
                }
            ),
            400,
        )

    cursor.execute(
        """
        SELECT SUM(cant_personas)
        FROM reservaciones
        WHERE fecha = %s AND hora = %s
        """,
        (fecha, hora),
    )

    capacidad_ocupada = cursor.fetchone()
    cursor.close()
    conn.close()

    if capacidad_ocupada + cant_personas > CAPACIDAD_HANA:
        return jsonify({"success": "No se puede realizar la reservación."}), 200
    return jsonify({"success": "Se puede realizar la reservación."}), 200
