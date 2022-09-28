from ursina import *
from random import randint

window_width = 800
window_height = 600

app = Ursina()

window.size=(window_width,window_height)
window.make_editor_gui()

window._icon = 'Game_icon.png'
print(window.size)
snakebody = 1
collected_apples = 0
sea = Entity(model = 'cube' , color = color.rgb(0,0,255) , rotation=(90 , 0 , 0) , scale = (300 , 2 , 300) , z = 3 )
snake = Entity(model = 'circle' , color = color.orange , scale = 0.4 , z =- 1 , collider = 'box')
ground = Entity(model = 'cube' , color = color.rgb(0,255,0) , rotation=(90 , 0 , 0) , scale = (5 , 2 , 5) , z = 3 )
apple = Entity(model = 'circle' , color = color.red , scale = 0.4 , position = (1 , -1 , -1) , collider = 'mesh')
body = [Entity(model = 'circle' , scale = 0.2 , color = color.orange) for i in range(snakebody)]

camera.orthographic = True
camera.fov = 10

dx = dy = 0
snake_speed = time.dt * dy
def update():
  global collected_apples

  info = snake.intersects()

  if info.hit and snake_speed == time.dt * dy :
    collected_apples += 1
    
    apple.x = randint(  -ground.scale_x - 2 , ground.scale_x - 2) 
    apple.y = randint(  -ground.scale_x - 2 , ground.scale_x - 2)

    new = Entity(model = 'circle' , z = -1 , scale = 0.2 , color = color.orange)
    body.append(new)

    print('apples : ' , collected_apples)
    print(snake_speed)

  for i in range(len(body) -1 , 0 , -1):
    pos = body[i - 1].position
    body[i].position = pos

  body[0].x = snake.x
  body[0].y = snake.y

  snake.x += time.dt * dx
  snake.y += time.dt * dy

def input(key):
  global dx , dy , snake_speed

  if key == 'q':
    quit()
  
  if held_keys['-']:
    camera.fov += 1 
  
  if held_keys['+']:
    camera.fov -= 1

  if held_keys['6']:
    camera.rotation_z -= 1
  
  if held_keys['4']:
    camera.rotation_z += 1

  for x , y , z in zip(['d' , 'a'] , [2 , -2] , [270 , 90]):
    if key == x:
      snake.rotation_z = z
      dx = y
      dy = 0

  for x , y , z in zip(['w' , 's'] , [2 , -2] , [180 , 0]):
    if key == x:
      snake.rotation_z = z
      dy = y
      dx = 0

app.run()