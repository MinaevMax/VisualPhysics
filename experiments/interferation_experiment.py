from vpython import *
from multiprocessing import Process

class InterferationExperiment(Process):

    def __init__(self, value):
        super(InterferationExperiment, self).__init__()

        self.value = value
        
    def on_return_button_press(r, self):
        self.canvas.delete()
        self.button.delete()

        self.is_run = False
        self.value.value = 0

    def run(self):
        self.canvas = canvas(width=965, height=600, background=color.white)

        # 2 шарика в начале
        ball_1_1 = sphere(pos=vector(5, 8, 0), radius=0.3, color=color.red, make_trail=True, retain=20)
        ball_1_2 = sphere(pos=vector(-5, 8, 0), radius=0.3, color=color.red, make_trail=True, retain=20)
        my = box(pos=vector(0, 0, -2), opacity=0.3, length=50, height=0.1, width=50, color=color.cyan)
        b1 = vector(5, 8, 0)
        b2 = vector(-5, 8, 0)
        # Списки колебаний(колец) для первого и вторго шарика
        ri1 = []
        ri2 = []
        ch = 0
        n = 0
        # Первые кольца по умолчания
        ri1.append(ring(pos=vector(5, 0, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red, visible=False))
        ri2.append(ring(pos=vector(-5, 0, 0), axis=vector(0, 1, 0), radius=0.5, thickness=0.1, color=color.red, visible=False))
        
        self.is_run = True

        self.button = button(text='Назад', bind=lambda: self.on_return_button_press(self))

        while True:
            # Выход
            if not self.is_run:
                break

            # Падение двух шариков
            while b1.y >= 0.1:
                rate(300)

                # Выход
                if not self.is_run:
                    break
                
                ball_1_1.pos = b1
                ball_1_2.pos = b2
                b1.y -= 0.008
                b2.y -= 0.008
            
            # Выход
            if not self.is_run:
                break

            ri1[0].visible = True
            ri2[0].visible = True

            # Начало колебаний
            while True:
                rate(400)

                # Выход
                if not self.is_run:
                    break

                for i in range(len(ri1)):
                    # Выход
                    if not self.is_run:
                        break

                    ri1[i].radius += 0.008
                    ri2[i].radius += 0.008

                # Выход
                if not self.is_run:
                    break

                ch += 0.008
                # Добовление колец при первом прохождении
                if ch > 5 and len(ri1) <= 3:
                    ch = 0
                    ri1.append(ring(pos=vector(5, 0, 0), axis=vector(0, 1, 0),
                    radius=0.5, thickness=0.1, color=color.red))
                    ri2.append(ring(pos=vector(-5, 0, 0), axis=vector(0, 1, 0),
                    radius=0.5, thickness=0.1, color=color.red))
                # при достижении 4х колец новые перестают добовляться и просто меняется значение радиуса крайнего кольца
                elif ch > 5 and len(ri1) > 3:
                    ch = 0
                    ri1[n].radius = 0.5
                    ri2[n].radius = 0.5
                    if n + 1 < len(ri1):
                        n += 1
                    else:
                        n = 0
