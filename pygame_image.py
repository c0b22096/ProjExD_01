import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230418/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01-20230418/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img10 = pg.transform.rotozoom(kk_img, 10, 1.0)
    lst = [kk_img, kk_img10]
    dx = 0
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr = (tmr+1) % 2
        dx = (dx+1) % 1600

        screen.blit(bg_img, [-dx, 0])
        screen.blit(bg_img, [1600-dx, 0])

        screen.blit(lst[tmr], [300, 200])

        pg.display.update()
        clock.tick(100)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

    