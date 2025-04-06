# 🐦 Flappy Bird Python Game 🎮

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Made with Pygame](https://img.shields.io/badge/Made%20with-Pygame-green.svg)](https://www.pygame.org/)

## 📝 Description

A fun and addictive Flappy Bird clone built with Python and Pygame! Navigate your bird through pipes by timing your jumps perfectly. How high can you score?

![Flappy Bird Game](https://raw.githubusercontent.com/pygame/pygame/main/docs/reST/_static/pygame_logo.svg)

## ✨ Features

- 🏠 **Attractive Home Screen** - Start your game journey with a clean, intuitive interface
- 🎯 **Simple One-Button Controls** - Easy to learn, difficult to master!
- 🌈 **Colorful Graphics** - Custom bird and pipe sprites with a beautiful background
- 🏆 **Score Tracking** - Keep track of your high scores
- 🔄 **Game Over Screen** - With options to restart or return to home
- 🎵 **Smooth Gameplay** - Optimized performance with 60 FPS

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- Pygame library

### Steps

1. Clone this repository or download the ZIP file
2. Install the required dependencies:

```bash
pip install pygame
```

3. Navigate to the game directory
4. Run the game:

```bash
python flappy_bird.py
```

## 🎮 How to Play

1. **Start the Game**: Press SPACE on the home screen to begin
2. **Control the Bird**: Press SPACE to make the bird flap and gain height
3. **Navigate**: Guide the bird through the gaps between pipes
4. **Score Points**: Each pipe you successfully pass earns you 1 point
5. **Game Over**: If you hit a pipe or the ground, the game ends
6. **Restart**: Press R to play again or H to return to the home screen

## 🎛️ Controls

- **SPACE** - Make the bird jump/flap
- **R** - Restart the game after Game Over
- **H** - Return to home screen after Game Over

## 🧩 Game Mechanics

- The bird constantly falls due to gravity
- Pressing SPACE gives the bird upward velocity
- Pipes generate randomly with varying heights
- Collision with pipes or the screen boundaries ends the game
- Each successfully passed pipe increases your score

## 📁 Project Structure

```
Python Flappy Bird Game/
├── flappy_bird.py    # Main game code
├── bird.png          # Bird sprite image
├── background.png    # Background image
├── pillar.png        # Pipe/pillar image
└── README.md         # Game documentation
```

## 🛠️ Technical Details

- **Game Engine**: Pygame
- **Screen Size**: 400x600 pixels
- **Frame Rate**: 60 FPS
- **Physics**: Simple gravity and velocity system
- **Collision Detection**: Rectangle-based collision system

## 🎨 Customization

You can easily customize the game by modifying these constants in the code:

- `SCREEN_WIDTH` and `SCREEN_HEIGHT` - Change the game window size
- `GRAVITY` - Adjust how quickly the bird falls
- `BIRD_JUMP` - Change the jump strength
- `PIPE_GAP` - Make the gaps between pipes larger or smaller
- `PIPE_FREQUENCY` - Adjust how often new pipes appear

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📜 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## 🙏 Acknowledgements

- Original Flappy Bird game by Dong Nguyen
- Pygame community for the excellent game development library
- All the contributors who have helped improve this game

---

⭐ **Enjoy the game and happy flapping!** ⭐