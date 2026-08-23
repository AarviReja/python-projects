# Game essentials
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pygame.display.set_caption("Tower of Hanoi")
start_time = start_time = int(pygame.time.get_ticks()/1000)
font20 = pygame.font.Font("items_used/Oswald-VariableFont_wght.ttf", 20)
font30 = pygame.font.Font("items_used/Oswald-VariableFont_wght.ttf", 30)
font40 = pygame.font.Font("items_used/Oswald-VariableFont_wght.ttf", 40)

# Ring Class
class Ring:
    def __init__(self, x, y, ring_number):
        self.width = 50 + ring_number*10
        self.rect = pygame.Rect(x, y, self.width, 25)
        self.rect.center = (x, y)
        self.ring_number = ring_number

    def render(self, screen):
        pygame.draw.rect(screen, "white", self.rect)

        text = font20.render(str(self.ring_number), True, "black")

        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def width(self):
        return self.width

    def number(self):
        return self.ring_number
    
# Peg Class
class Peg:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def render(self, screen):
        pygame.draw.rect(screen, "blue", self.rect)

    def middle_x(self):
        return self.rect.x + self.rect.width // 2

# Ring up or down arrow class
class Arrow:
    def __init__(self, side_length, middle_x, middle_y, direction):
        self.side_length = side_length
        self.middle_x = middle_x
        self.middle_y = middle_y
        self.direction = direction

        top_left_x = middle_x - (1/2) * side_length
        top_left_y = middle_y - (1/2) * side_length

        self.rect = pygame.Rect(top_left_x, top_left_y, side_length, side_length)

    def render(self, screen):
        x1 = self.middle_x - (1/2) * self.side_length
        x2 = self.middle_x + (1/2) * self.side_length
        def draw_arrow():
            pygame.draw.polygon(screen, "sky blue", [(x1, y1), (x2, y1), (self.middle_x, y3)])
        if self.direction == "up":
            y1 = self.middle_y + (1/2) * self.side_length
            y3 = self.middle_y - (1/2) * self.side_length
            draw_arrow()
        elif self.direction == "down":
            y1 = self.middle_y - (1/2) * self.side_length
            y3 = self.middle_y + (1/2) * self.side_length
            draw_arrow()

# Pegs
pegs_list = []
touching_rings_lists = []
for i in range(3):
    peg = Peg((300 + 200*i), 100, 25, 300)
    pegs_list.append(peg)
for i in range(3):
    touching_rings = []
    touching_rings_lists.append(touching_rings)

def pick_up_ring(index):
    global active_ring, start_peg

    touching_rings_lists[index].clear()
    for ring in rings:
        if ring.rect.colliderect(pegs_list[index].rect):
            touching_rings_lists[index].append(ring)
    if touching_rings_lists[index]:
        active_ring = touching_rings_lists[index][-1]
        start_peg = index
        touching_rings_lists[index].remove(active_ring)

def put_down_ring(index):
    global active_ring, end_peg
    if pegs_list[index].rect.collidepoint(event.pos):
        touching_rings_lists[index].clear()

        if not touching_rings_lists[index] or active_ring.ring_number < touching_rings_lists[index][-1].ring_number:
            for ring in rings:
                if ring.rect.colliderect(pegs_list[index].rect) and ring != active_ring:
                    touching_rings_lists[index].append(ring)

            # Makes sure that the ring is not placed on top of a smaller ring
            if not touching_rings_lists[index] or active_ring.number() < touching_rings_lists[index][-1].number():
                active_ring.rect.center = (pegs_list[index].middle_x(), 375 - len(touching_rings_lists[index])*26)
                active_ring = None
                end_peg = index

# Rings
active_ring = None
number_of_rings = 5
ring_number = number_of_rings
rings = []
for i in range(number_of_rings):
    width = 50 + ring_number*10
    ring = Ring(pegs_list[0].middle_x(), 375 - i*26, ring_number)
    ring_number -= 1
    rings.append(ring)

# Sidebar
sidebar = pygame.Rect(0, 0, 200, 400)

# Reset Buttons
reset_button = pygame.Rect(25, 50, 150, 50)
reset_button_text = font30.render("Reset Game", True, "white")

def reset():
    global moves, start_time, running, active_ring

    ring_number = number_of_rings
    running = True
    active_ring = None
    for i in range(3):
        touching_rings_lists[i].clear()
    rings.clear()
    moves = 0
    start_time = int(pygame.time.get_ticks()/1000)
    for i in range(number_of_rings):
        width = 50 + ring_number*10
        ring = Ring(pegs_list[0].middle_x(), 375 - i*26, ring_number)
        ring_number -= 1
        rings.append(ring)

# Arrow Buttons
up_arrow = Arrow(30, 100, 300, "up")
down_arrow = Arrow(30, 100, 350, "down")

# Number of moves
moves = 0
start_peg = None
end_peg = None
def display_moves():
    moves_text = font30.render(f"Moves: {moves}", True, "white")
    moves_rect = moves_text.get_rect(center=(100, 150))
    screen.blit(moves_text, moves_rect)

# Display Time
def display_time():
    current_time = int(pygame.time.get_ticks()/1000) -  start_time
    time_surface = font30.render(f"Time: {current_time}", True, "white")
    time_rect = time_surface.get_rect(center=(100, 225))
    screen.blit(time_surface, time_rect)

# When won
def win():
    win_surface = font40.render("You win! Click Reset to play again!", True, "purple")
    win_rect = win_surface.get_rect(center=(500, 25))
    screen.blit(win_surface, win_rect)

# Perfect amount of moves
def perfect():
    perf_surface = font40.render("Perfect amount of moves!", True, "pink")
    perf_rect = perf_surface.get_rect(center=(500, 75))
    screen.blit(perf_surface, perf_rect)


running = True
# Game Loop
while True:
    # Events Handling Loop
    for event in pygame.event.get():
        
        # When user clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                # Resetting
                if reset_button.collidepoint(event.pos):
                    # Resetting the game
                    reset()

                # Adding a ring
                if up_arrow.rect.collidepoint(event.pos):
                    if number_of_rings < 10:
                        number_of_rings += 1
                        reset()
                # Removing a ring
                elif down_arrow.rect.collidepoint(event.pos):
                    if number_of_rings > 2:
                        number_of_rings -= 1
                        reset()

                # Picking up a ring
                if active_ring == None and running:
                    for i in range(3):
                        if pegs_list[i].rect.collidepoint(event.pos):
                                pick_up_ring(i)

                # Placing a ring
                else:
                    if running:
                        for i in range(3):
                            if pegs_list[i].rect.collidepoint(event.pos):
                                put_down_ring(i)

        # Moving the ring with the mouse
        if event.type == pygame.MOUSEMOTION and running:
            if active_ring != None:
                active_ring.rect.center = (event.pos)

        # Quitting using the X button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if running:
        # Draw everything
        screen.fill("teal")
        for i in range(3):
            pegs_list[i].render(screen)

        for ring in rings:
            ring.render(screen)

        pygame.draw.rect(screen, "red", sidebar)

        up_arrow.render(screen)
        down_arrow.render(screen)

        pygame.draw.rect(screen, "black", reset_button)
        screen.blit(reset_button_text, reset_button_text.get_rect(center=reset_button.center))

        # Update the number of moves
        if start_peg != None and end_peg != None:
            if start_peg != end_peg:
                moves += 1
            start_peg = None
            end_peg = None
        display_moves()

        # Display the time
        display_time()

        # Detect when the user wins and if they have the perfect number of moves
        if number_of_rings == (len(touching_rings_lists[-1]))+1 and active_ring == None:
            running = False
            win()
            if moves == (2 ** number_of_rings) - 1:
                perfect()
            

        # Update the display and tick the clock
        pygame.display.update()
        clock.tick(60)