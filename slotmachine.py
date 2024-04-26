import pygame
import random
import sys
import time  # Import tambahan untuk delay

# Inisialisasi Pygame
pygame.init()

# Set ukuran layar
screen = pygame.display.set_mode((900, 700))

# Judul dan Icon
pygame.display.set_caption("JUDIIIIIIIIIII")
icon = pygame.image.load('image/slot_machine.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('image/casino_background.jpg')

# Gambar untuk slot
slot_images = [
    pygame.transform.scale(pygame.image.load('image/lemon.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('image/apple.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('image/banana.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('image/cherry.png'), (80, 80)),
    pygame.transform.scale(pygame.image.load('image/seven.png'), (80, 80)) 
]

# Frame Mesin Slot
slot_frame = pygame.image.load('image/slot_frame.png')

# Font untuk teks
font = pygame.font.Font('freesansbold.ttf', 32)

# Fungsi untuk menampilkan teks
def show_text(text, x, y):
    render = font.render(text, True, (255, 255, 255))
    screen.blit(render, (x, y))

# Fungsi untuk menggambar slot
def draw_slots(slot1, slot2, slot3):
    screen.blit(slot_frame, (200, 200))  # Posisi frame mesin slot
    screen.blit(slot_images[slot1], (320, 330))
    screen.blit(slot_images[slot2], (430, 330))
    screen.blit(slot_images[slot3], (540, 330))

# Fungsi untuk animasi spin
def spin_animation():
    for _ in range(10):  # Jumlah pengulangan animasi
        slot1 = random.randint(0, 4)
        slot2 = random.randint(0, 4)
        slot3 = random.randint(0, 4)
        screen.blit(background, (0, 0))  # Bersihkan layar sebelum menggambar
        draw_slots(slot1, slot2, slot3)
        pygame.display.update()
        time.sleep(0.1)  # Delay antar update

# Main loop
running = True
slot1, slot2, slot3 = 0, 0, 0
while running:
    screen.blit(background, (0, 0))  # Tampilkan background
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                spin_animation()  # Panggil fungsi animasi
                # Randomize slots untuk hasil akhir
                slot1 = random.randint(0, 4)
                slot2 = random.randint(0, 4)
                slot3 = random.randint(0, 4)
    
    draw_slots(slot1, slot2, slot3)
    show_text("Press SPACE to spin", 300, 50)
    
    pygame.display.update()

pygame.quit()
sys.exit()
