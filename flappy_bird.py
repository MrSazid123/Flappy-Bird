import pygame
import sys
import random
import os

# Initialize pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.25
BIRD_JUMP = -5
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds
FPS = 60

# Game States
HOME_SCREEN = 0
GAME_PLAYING = 1
GAME_OVER = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
GREEN = (0, 128, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

# Load images
BIRD_IMG = pygame.image.load(os.path.join('bird.png'))
BIRD_IMG = pygame.transform.scale(BIRD_IMG, (30, 30))
BACKGROUND_IMG = pygame.image.load(os.path.join('background.png'))
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT))
PIPE_IMG = pygame.image.load(os.path.join('pillar.png'))
# We'll scale the pipe image when drawing to match the pipe dimensions

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.width = 30
        self.height = 30
        self.image = BIRD_IMG
    
    def jump(self):
        self.velocity = BIRD_JUMP
    
    def update(self):
        # Apply gravity
        self.velocity += GRAVITY
        self.y += self.velocity
        
        # Keep bird on screen
        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.velocity = 0
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
    
    def get_mask(self):
        # For collision detection
        return pygame.Rect(self.x, self.y, self.width, self.height)

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, 300)
        self.width = 50
        self.passed = False
        self.speed = 3
        self.image = PIPE_IMG
    
    def update(self):
        self.x -= self.speed
    
    def draw(self):
        # Scale pipe image to match dimensions
        top_pipe = pygame.transform.scale(self.image, (self.width, self.height))
        bottom_pipe = pygame.transform.scale(self.image, (self.width, SCREEN_HEIGHT - self.height - PIPE_GAP))
        
        # Draw top pipe (flipped)
        screen.blit(pygame.transform.flip(top_pipe, False, True), (self.x, 0))
        # Draw bottom pipe
        screen.blit(bottom_pipe, (self.x, self.height + PIPE_GAP))
    
    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_pipe = pygame.Rect(self.x, 0, self.width, self.height)
        bottom_pipe = pygame.Rect(self.x, self.height + PIPE_GAP, 
                                 self.width, SCREEN_HEIGHT - self.height - PIPE_GAP)
        
        return bird_mask.colliderect(top_pipe) or bird_mask.colliderect(bottom_pipe)

# Game class
class Game:
    def __init__(self):
        self.reset_game()
        self.font = pygame.font.SysFont(None, 36)
        self.title_font = pygame.font.SysFont(None, 72)
        self.game_state = HOME_SCREEN
    
    def reset_game(self):
        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.last_pipe = pygame.time.get_ticks()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if self.game_state == HOME_SCREEN:
                    if event.key == pygame.K_SPACE:
                        self.game_state = GAME_PLAYING
                elif self.game_state == GAME_PLAYING:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()
                elif self.game_state == GAME_OVER:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        self.game_state = GAME_PLAYING
                    elif event.key == pygame.K_h:
                        self.reset_game()
                        self.game_state = HOME_SCREEN
    
    def update(self):
        if self.game_state == GAME_PLAYING:
            self.bird.update()
            
            # Generate new pipes
            current_time = pygame.time.get_ticks()
            if current_time - self.last_pipe > PIPE_FREQUENCY:
                self.pipes.append(Pipe())
                self.last_pipe = current_time
            
            # Update pipes and check for score
            for pipe in self.pipes:
                pipe.update()
                
                # Check if bird passed the pipe
                if not pipe.passed and pipe.x < self.bird.x:
                    pipe.passed = True
                    self.score += 1
                
                # Check for collision
                if pipe.collide(self.bird):
                    self.game_state = GAME_OVER
            
            # Remove pipes that are off screen
            self.pipes = [pipe for pipe in self.pipes if pipe.x > -pipe.width]
            
            # Check if bird hits the ground or ceiling
            if self.bird.y >= SCREEN_HEIGHT - self.bird.height or self.bird.y <= 0:
                self.game_state = GAME_OVER
    
    def draw(self):
        # Draw background for all states
        screen.blit(BACKGROUND_IMG, (0, 0))
        
        if self.game_state == HOME_SCREEN:
            # Draw home screen
            title_text = self.title_font.render('FLAPPY BIRD', True, BLACK)
            start_text = self.font.render('Press SPACE to Start', True, BLACK)
            bird_img = pygame.transform.scale(BIRD_IMG, (60, 60))
            
            # Center the title and instructions
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
            start_rect = start_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            bird_rect = bird_img.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//1.5))
            
            # Draw elements with a slight animation for the bird
            screen.blit(title_text, title_rect)
            screen.blit(start_text, start_rect)
            screen.blit(bird_img, bird_rect)
            
        elif self.game_state == GAME_PLAYING or self.game_state == GAME_OVER:
            # Draw pipes
            for pipe in self.pipes:
                pipe.draw()
            
            # Draw bird
            self.bird.draw()
            
            # Draw score
            score_text = self.font.render(f'Score: {self.score}', True, BLACK)
            screen.blit(score_text, (10, 10))
            
            # Draw game over screen
            if self.game_state == GAME_OVER:
                # Semi-transparent overlay
                overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 128))  # Black with alpha
                screen.blit(overlay, (0, 0))
                
                # Game over text
                game_over_text = self.title_font.render('GAME OVER', True, WHITE)
                score_text = self.font.render(f'Final Score: {self.score}', True, WHITE)
                restart_text = self.font.render('Press R to Restart', True, WHITE)
                home_text = self.font.render('Press H for Home Screen', True, WHITE)
                
                # Position text
                game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//3))
                score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//1.5))
                home_rect = home_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//1.3))
                
                # Draw text
                screen.blit(game_over_text, game_over_rect)
                screen.blit(score_text, score_rect)
                screen.blit(restart_text, restart_rect)
                screen.blit(home_text, home_rect)
        
        pygame.display.update()

# Main function
def main():
    game = Game()
    
    # Game loop
    while True:
        game.handle_events()
        game.update()
        game.draw()
        clock.tick(FPS)

if __name__ == "__main__":
    main()