
from ursina import *
from random import randint
app = Ursina()

snake = Entity(model = 'circle' , color = color.orange , scale = 0.4 , z =- 1 , collider = 'box')
ground = Entity(model = 'cube' , color = color.rgb(255,255,0) , rotation=(90 , 0 , 0) , scale = (5 , 2 , 5) , z = 3 )
apple = Entity(model = 'circle' , color = color.red , scale = 0.4 , position = (1 , -1 , -1) , collider = 'mesh')
body = [Entity(model = 'circle' , scale = 0.2 , color = color.orange) for i in range(14)]

camera.orthographic = True
camera.fov = 10

dx = dy = 0

def update():
  info = snake.intersects()

  if info.hit:
    apple.x = randint(  -camera.fov  , camera.fov) 
    apple.y = randint(  -camera.fov  , camera.fov )

    new = Entity(model = 'circle' , z = -1 , scale = 0.2 , color = color.orange)
    body.append(new)

  for i in range(len(body) -1 , 0 , -1):
    pos = body[i - 1].position
    body[i].position = pos

  body[0].x = snake.x
  body[0].y = snake.y

  snake.x += time.dt * dx
  snake.y += time.dt * dy

def input(key):
  global dx , dy

  if key == 'q':
    quit()

  if key == '6':
    camera.rotation_z -= 1
  
  if key == '4':
    camera.rotation_z +=1

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