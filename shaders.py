import math

from Mathlib import Tmatrix


def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["viewMatrix"]

    # Convertir el vértice a una matriz columna 4x1 agregando un valor de 1
    vt = [[vertex[0]], [vertex[1]], [vertex[2]], [1]]
    # Realizar la multiplicación de la matriz del modelo con el vértice
    vt = Tmatrix(vpMatrix, Tmatrix(projectionMatrix, Tmatrix(viewMatrix, Tmatrix(modelMatrix, vt))))
    # Convertir la matriz resultado de nuevo a un vértice (lista)
    vt = [vt[0][0],vt[1][0],vt[2][0]]
    return vt




#toonshader
def toonshader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    # Calculate the intensity of the color (brightness)
    intensity = (color[0] + color[1] + color[2]) / 3.0

    # Define the toon shading levels (adjust as needed)
    levels = 4

    # Calculate the new color value based on toon shading levels
    if intensity > 0.9:
        color = (1, 0, 1)  # High intensity, use white color for cuerpo
    elif intensity > 0.7:
        color = (1, 0.2, 0.8)  # Medium-high intensity, use white color for cuerpo
    elif intensity > 0.5:
        color = (0.3, 0.4, 0.6)  # Medium intensity, use orange color for camisa
    elif intensity > 0.3:
        color = (0.2, 0.6, 0.3)
    else:
        color = (0.1, 0.8, 0.2)

    return color


def grayScaleShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    # Calculate the intensity of the color (brightness)
    intensity = (color[0] + color[1] + color[2]) / 3.0

    # Calculate new color components based on brightness
    new_red = intensity
    new_green = intensity
    new_blue = intensity

    # Return the new color
    return (new_red, new_green, new_blue)

#invertion color shader
def invertionColorShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    # Calculate the intensity of the color (brightness)
    intensity = (color[0] + color[1] + color[2]) / 3.0

    # Calculate new color components based on brightness
    new_red = 1.0 - color[0]
    new_green = 1.0 - color[1]
    new_blue = 1.0 - color[2]

    # Return the new color
    return (new_red, new_green, new_blue)

def passThroughShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    return color

def fireShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    u = texCoords[0] % 1
    v = texCoords[1] % 1

    if texture is not None:
        color = texture.getColor(u, v)
    else:
        color = (1, 1, 1)

    intensity = (u + v) * 0.5

    new_red = min(1.0, color[0] + intensity * 0.5)
    new_green = max(0.0, color[1] - intensity * 0.2)
    new_blue = max(0.0, color[2] - intensity * 0.5)

    return (new_red, new_green, new_blue)
def flyingZubatShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    shadow_intensity = texCoords[1]
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)
    new_red = max(0.0, color[0] - shadow_intensity)
    new_green = max(0.0, color[1] - shadow_intensity * 0.5)
    new_blue = max(0.0, color[2] - shadow_intensity)
    return (new_red, new_green, new_blue)

def electricShader(texCoords, texture, time):
    u = texCoords[0] % 1
    v = texCoords[1] % 1

    # Color azul brillante para el efecto de electricidad
    electric_color = (0.2, 0.4, 1.0)

    # Ajustar la frecuencia y amplitud del efecto eléctrico
    frequency = 10.0  # Frecuencia del parpadeo
    amplitude = 2.6  # Amplitud del brillo

    # Calcular el factor eléctrico basado en el tiempo
    electric_factor = (math.sin(time * frequency) + 1) * 0.5

    # Mezclar el color base con el color eléctrico brillante y aplicar brillo
    new_red = min(1.0, (1 - electric_factor) * texture.getColor(u, v)[0] + electric_factor * electric_color[0] * amplitude)
    new_green = min(1.0, (1 - electric_factor) * texture.getColor(u, v)[1] + electric_factor * electric_color[1] * amplitude)
    new_blue = min(1.0, (1 - electric_factor) * texture.getColor(u, v)[2] + electric_factor * electric_color[2] * amplitude)

    return (new_red, new_green, new_blue)

def shinyNeonShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    # Calcular la intensidad del color (brillo)
    intensity = (color[0] + color[1] + color[2]) / 3.0

    # Cambiar el color de gris opaco a celeste claro en partes brillantes
    if intensity > 0.6:
        shine_color = (0.5, 0.85, 1.0)  # Celeste claro para el efecto neon
        color = (shine_color[0], shine_color[1], shine_color[2])

    return color



