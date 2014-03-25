#!/usr/bin/env python2.7-32

'''
Created on Mar 10, 2013

@author: dstu
'''

import site
import os

site.addsitedir(os.getcwd())

import Game as G
import Const as C

fontsize = 14
# font = u'couriernew'
font = None

def main():
    x = 100
    y = 50
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    os.environ['SDL_VIDEODRIVER'] = 'x11'
# x11, dga, fbcon, directfb, ggi, vgl, svgalib, aalib    

    print '-=' + C.TITLE + '=-'
    
    game = G.Game(fontsize = fontsize, font = font, debug = False)
    
    game.play()

if __name__ == '__main__':
    main()
