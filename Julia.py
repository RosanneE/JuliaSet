import sys
#import and init pygame                                                                                                                                                                                   
import pygame
import time
import random

pygame.init()

#create the screen                                                                                                                                                                                        
window = pygame.display.set_mode((600, 600))

#draw a line - see http://www.pygame.org/docs/ref/draw.html for more                                                                                                                                      

def Julia(i,j):
    i = (i/150.0) - 2.0
    j = (j/150.0) - 2.0    
    newi = i 
    newj = j 
    
    for x in range (1,20):
        newi = i**2 - j**2 + 1
        newj = 2 * i * j
        i = newi
        j = newj
        if newi**2 + newj**2 > 200:
            return x
    return 20


  

                                                                                                                       
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit(0)
        
   for i in range (0,600):
        for j in range (0,600):
            jul = Julia(i,j)
            if Julia(i,j) > 20:
                pygame.draw.rect(window, (jul * 10, 2, 2), (i, j, 1, 1), 1)
                #print i, j
            else:
                pygame.draw.rect(window, (jul * 10, 2, 133), (i, j, 1, 1), 1)
                #print i, j

   #window.fill((0,0,0))
   pygame.display.flip()

   #ALL YOUR STUFF GOES HERE                                                                                                                                                                              
'''
    iadju = 150.0
    jadju = 300.0
    iscale = 150.0
    jscale = 300.0
    i = (i - iadju) /  iscale
    j = (j - jadju) / jscale
'''
  

   #END STUFF                                                                                                                                                                                             
   