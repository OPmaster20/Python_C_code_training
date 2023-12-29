import random
from math import sin,cos,pi,log
from tkinter import *
ca_w = 640
ca_h = 480
ca_ce_x = ca_w / 2
ca_ce_y = ca_h / 2
image = 11
h_c = "#ff4323"
def heart_f(t,shrink_ratio: float = image):
    x = 16 * (sin(t) ** 3)
    y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))
    x *= shrink_ratio
    y *=shrink_ratio
    x += ca_ce_x
    y +=ca_ce_y
    return int(x),int(y)
def scatter_inside(x,y,beta=0.15):
    ratio_x = - beta * log(random.random())
    ratio_y = - beta * log(random.random())
    dx = ratio_x * (x - ca_ce_x)
    dy = ratio_y * (y - ca_ce_y)
    return x - dx,y - dy

def shrink(x,y,ratio):
    force = -1 / (((x - ca_ce_x)  ** 2 + (y - ca_ce_y) ** 2)  ** 0.6)
    dx = ratio * force * (x - ca_ce_x)
    dy = ratio * force * (y - ca_ce_y)
    return x - dx,y - dy
def curve(p):
    return 2 * (2 * sin(4 * p)) / (2 * pi)
class hea:
    def __init__(self,generate_frame = 20):
        self._point = set()
        self._edge_point = set()
        self._center_point = set()
        self.all_point = {}
        self.build(2000)

        self.random_halo = 1000
        self.generate_frame = generate_frame
        for frame in range(generate_frame):
            self.calc(frame)
    def build(self,number):
        for _ in range(number):
            t = random.uniform(0,2 * pi)
            x,y = heart_f(t)
            self._point.add((x,y))
        for _x,_y in list(self._point):
            for _ in range(3):
                x,y = scatter_inside(_x,_y,0.05)
                self._edge_point.add((x,y))
        point_list = list(self._point)
        for _ in range(4000):
            x,y = random.choice(point_list)
            x,y = scatter_inside(x,y,0.17)
            self._center_point.add((x,y))
    
    @staticmethod
    def cal(x,y,ratio):
        force = 1 / (((x - ca_ce_x)  ** 2 + (y - ca_ce_y) ** 2) ** 0.520)
        dx = ratio * force * (x - ca_ce_x) + random.randint(-1,1)
        dy = ratio * force * (y - ca_ce_y) + random.randint(-1,1)
        return x - dx,y - dy
    def calc(self,generate_frame):
        ratio = 10 * curve(generate_frame / 10 * pi)
        halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))
        all_point = []
        hea_point = set()
        for _ in range(halo_number):
            t = random.uniform(0,2 * pi)
            x,y = heart_f(t,shrink_ratio = 11.6)
            x,y =  shrink(x,y,halo_radius)
            if (x,y) not in hea_point:
                hea_point.add((x,y))
                x += random.randint(-14,14)
                y += random.randint(-14,14)
                size = random.choice((1,2,2))
                all_point.append((x,y,size))
        for x,y in self._point:
            x,y = self.cal(x,y,ratio)
            size = random.randint(1,3)
            all_point.append((x,y,size))
        for x,y in self._edge_point:
            x,y = self.cal(x,y,ratio)
            size =random.randint(1,2)
            all_point.append((x,y,size))
        for x,y in self._center_point:
            x,y = self.cal(x,y,ratio)
            size =random.randint(1,2)
            all_point.append((x,y,size))
        self.all_point[generate_frame] = all_point
    def render(self,render_canvas,render_frame):
        for x,y,size in self.all_point[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x,y,x + size, y + size,width = 0,fill = h_c)
def draw(main: Tk, render_canvas: Canvas,render_heart: hea,render_frame = 0):
    render_canvas.delete('all')
    render_heart.render(render_canvas,render_frame)
    main.after(160,draw,main,render_canvas,render_heart,render_frame + 1)

if __name__ == '__main__':
    root = Tk()
    root.title("To you")
    canvas = Canvas(root, bg='black', height=ca_h, width=ca_w)
    canvas.pack()
    heart = hea()  
    draw(root, canvas, heart)  
    root.mainloop()



