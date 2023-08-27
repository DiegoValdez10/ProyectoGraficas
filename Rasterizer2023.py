from gl import Renderer
import shaders
import time
# El tama�o del FrameBuffer
width = 1200
height = 1420

# Se crea el renderizador
rend = Renderer(width, height)
rend.glBackgroundTexture("textures/bg.bmp")
rend.glClearBackground()
# Le damos los shaders que se utilizar�s
rend.vertexShader = shaders.vertexShader

rend.fragmentShader = shaders.flyingZubatShader
rend.glLoadModel(filename = "obj/zubat.obj",
                 textureName = "textures/zubat.bmp",
                 translate = (width/6.5, height/3, 0),
                 rotate = (15, 0, 0),
                 scale = (30, 30, 30))
rend.glRender()



rend.fragmentShader = shaders.fireShader
rend.glLoadModel(filename = "obj/charizard.obj",
                    textureName = "textures/chari.bmp",
                    translate = (width/4.9, height/8, 0),
                    rotate = (50, 5, 5),
                    scale = (50,50,50))
rend.glRender()

rend.fragmentShader = shaders.electricShader
current_time = time.time()
rend.glLoadModel(filename = "obj/pikachu.obj",
                    textureName = "textures/pikachu1.bmp",
                    translate = (width/7.5, height/20, 0),
                    rotate = (0, 140, 0),
                    scale = (4,4,4))
current_time = time.time()
rend.glRender(time=current_time)

rend.fragmentShader = shaders.shinyNeonShader
rend.glLoadModel(filename = "obj/UmbreonHighPoly.obj",
                    textureName = "textures/umbreon.bmp",
                    translate = (width/4.5, height/10, 0),
                    rotate = (70, 190, 10),
                    scale = (50,50,50))

rend.glRender()

# Se crea el FrameBuffer con la escena renderizada
rend.glFinish("output.bmp")