import sys
#import and init pygame                                                                                                                                                                                   
import pygame
import time
import random

pygame.init()

#create the screen                                                                                                                                                                                        
window = pygame.display.set_mode((600, 600))

#draw a line - see http://www.pygame.org/docs/ref/draw.html for more                                                                                                                                      
CONSTANT = .285
#IMAGINARY = .1
def Julia(i,j):
    i = (i - 250.0) * .005
    j = (j - 250.0) * .005
    newi = i 
    newj = j 
    
    for x in range (1,100):
        newi = i**2 - j**2 + CONSTANT
        newj = 2 * i * j #+ IMAGINARY
        i = newi
        j = newj
        if newi**2 + newj**2 > 100:
            return x
    return 100


  

                                                                                                                       
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit(0)
        
   for i in range (0,600):
        for j in range (0,600):
            jul = Julia(i,j)
            if jul > 20:
               # print jul
                pygame.draw.rect(window, (100, 100, (255-int(jul*2.5))), (i, j, 1, 1), 1)
            else:
                #print jul
                pygame.draw.rect(window, ((255-int(jul*2.5)), 0, 250), (i, j, 1, 1), 1)
                

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
   