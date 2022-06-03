import os
import mouse as mouse
import pygame
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("600x280")
root.title("Startbildschirm")
photo = PhotoImage(file="C:/Users/walte/OneDrive/Desktop/bloons/assets/startscreen.png")
panel1 = Label(root, image=photo)
panel1.grid(row=0, column=0)
exit_button = Button(root, text="Spiel starten", command=root.destroy)
exit_button.grid(row=1, column=0)
mainloop()


class Sound:
    def __init__(self, path):
        self.path = path
        pygame.init()
        self.sound = pygame.mixer.music.load(self.path)
        pygame.mixer.music.set_volume(.1)

    def play_sound(self):
        pygame.mixer.music.play(1, 0.0)


class BaloonSetting:
    def __init__(self, image: str, hp: float, speed: float) -> None:
        self.image = image
        self.hp = hp
        self.speed = speed


class TowerSetting:
    def __init__(self, image: str, price: int, range: int, damage: int, fire_rate: int) -> None:
        self.image = image
        self.price = price
        self.range = range
        self.damage = damage
        self.fire_rate = fire_rate


class Settings:
    _window_width = 1000
    _window_height = 720

    @staticmethod
    def get_window_size():
        return Settings._window_width, Settings._window_height

    _window_caption = "Bloons Clone"
    _window_fps = 60
    _window_delta_time = 1.0 / _window_fps

    _working_directory = os.path.dirname(os.path.realpath(__file__))
    _assets_directory = os.path.join(_working_directory, "assets")
    _baloons_directory = os.path.join(_assets_directory, "baloons")
    _tower_directory = os.path.join(_assets_directory, "towers")

    _path = [
        (170, 0),
        (170, 210),
        (200, 210),
        (335, 210),
        (335, 125),
        (360, 100),
        (400, 100),
        (600, 100),
        (600, 250),
        (400, 250),
        (400, 500),
        (100, 500),
        (100, 650),
        (570, 650),
        (570, 400),
        (1000, 400),
    ]

    _spot_size = 50
    _map_spots = [
        (0, 0), (50, 0), (100, 0), (200, 0), (250, 0), (300, 0), (350, 0), (400, 0), (450, 0), (500, 0), (550, 0), (600, 0), (650, 0), (700, 0), (750, 0), (800, 0), (850, 0), (900, 0), (950, 0),
        (0, 50), (50, 50), (100, 50), (200, 50), (250, 50), (300, 50), (350, 50), (400, 50), (450, 50), (500, 50), (550, 50), (600, 50), (650, 50), (700, 50), (750, 50), (800, 50), (850, 50), (900, 50), (950, 50),
        (0, 100), (50, 100), (100, 100), (200, 100), (250, 100), (650, 100), (700, 100), (750, 100), (800, 100), (850, 100), (900, 100), (950, 100),
        (0, 150), (50, 150), (100, 150), (200, 150), (250, 150), (350, 150), (400, 150), (450, 150), (500, 150), (550, 150), (600, 150), (650, 150), (700, 150), (750, 150), (800, 150), (850, 150), (900, 150), (950, 150),
        (0, 200), (50, 200), (100, 200), (400, 200), (450, 200), (500, 200), (550, 200), (600, 200), (650, 200), (700, 200), (750, 200), (800, 200), (850, 200), (900, 200), (950, 200),
        (0, 250), (50, 250), (100, 250), (150, 250), (200, 250), (250, 250), (300, 250), (350, 250), (400, 250), (450, 250), (500, 250), (550, 250), (600, 250), (650, 250), (700, 250), (750, 250), (800, 250), (850, 250), (900, 250), (950, 250),
        (0, 300), (50, 300), (100, 300), (150, 300), (200, 300), (250, 300), (300, 300), (350, 300), (400, 300), (450, 300), (500, 300), (550, 300), (600, 300), (650, 300), (700, 300), (750, 300), (800, 300), (850, 300), (900, 300), (950, 300),
        (0, 350), (50, 350), (100, 350), (150, 350), (200, 350), (250, 350), (300, 350), (350, 350), (400, 350), (450, 350), (500, 350), (550, 350), (600, 350), (650, 350), (700, 350), (750, 350), (800, 350), (850, 350), (900, 350), (950, 350),
        (0, 400), (50, 400), (100, 400), (150, 400), (200, 400), (250, 400), (300, 400), (350, 400), (400, 400), (450, 400), (500, 400), (550, 400), (600, 400), (650, 400), (700, 400), (750, 400), (800, 400), (850, 400), (900, 400), (950, 400),
        (0, 450), (50, 450), (100, 450), (150, 450), (200, 450), (250, 450), (300, 450), (350, 450), (400, 450), (450, 450), (500, 450), (550, 450), (600, 450), (650, 450), (700, 450), (750, 450), (800, 450), (850, 450), (900, 450), (950, 450),
        (0, 500), (50, 500), (100, 500), (150, 500), (200, 500), (250, 500), (300, 500), (350, 500), (400, 500), (450, 500), (500, 500), (550, 500), (600, 500), (650, 500), (700, 500), (750, 500), (800, 500), (850, 500), (900, 500), (950, 500),
        (0, 550), (50, 550), (100, 550), (150, 550), (200, 550), (250, 550), (300, 550), (350, 550), (400, 550), (450, 550), (500, 550), (550, 550), (600, 550), (650, 550), (700, 550), (750, 550), (800, 550), (850, 550), (900, 550), (950, 550),
        (0, 600), (50, 600), (100, 600), (150, 600), (200, 600), (250, 600), (300, 600), (350, 600), (400, 600), (450, 600), (500, 600), (550, 600), (600, 600), (650, 600), (700, 600), (750, 600), (800, 600), (850, 600), (900, 600), (950, 600),
        (0, 650), (50, 650), (100, 650), (150, 650), (200, 650), (250, 650), (300, 650), (350, 650), (400, 650), (450, 650), (500, 650), (550, 650), (600, 650), (650, 650), (700, 650), (750, 650), (800, 650), (850, 650), (900, 650), (950, 650)
    ]

    _baloons = [
        BaloonSetting(os.path.join(_baloons_directory, "baloon_1.png"), 1, 1),
        BaloonSetting(os.path.join(_baloons_directory, "baloon_2.png"), 2, 1),
        BaloonSetting(os.path.join(_baloons_directory, "baloon_3.png"), 4, 1),
    ]

    _towers = [
        TowerSetting(os.path.join(_tower_directory, "tower_1.png"), 15, 100, 1, 1000),
        TowerSetting(os.path.join(_tower_directory, "tower_2.png"), 25, 150, 2, 500),
        TowerSetting(os.path.join(_tower_directory, "tower_3.png"), 35, 200, 3, 300),
        TowerSetting(os.path.join(_tower_directory, "tower_4.png"), 45, 250, 4, 200)
    ]

    _bullet_speed = 5


class Timer:
    def __init__(self, duration, with_start=False) -> None:
        self.duration = duration
        self.next = pygame.time.get_ticks()

        if not with_start:
            self.next += self.duration

    def is_next_stop_reached(self) -> bool:
        """
        Return flag and reset timer when next iteration is reached
        """
        if pygame.time.get_ticks() >= self.next:
            self.next = pygame.time.get_ticks() + self.duration
            return True
        return False


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(Settings._assets_directory, "background.png")
        )
        self.image = pygame.transform.scale(self.image, (1000, 720))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))




class MapSpot(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.surface_image = pygame.Surface((Settings._spot_size, Settings._spot_size))
        self.surface_image.fill((0, 0, 0))
        self.surface_image.set_alpha(0)

        self.add_image = pygame.image.load(
            os.path.join(Settings._assets_directory, "empty_slot.png")
        )
        self.add_image = pygame.transform.scale(self.add_image, (Settings._spot_size, Settings._spot_size))

        self.image = self.surface_image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.tower = None
        self.hovered = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, *args, **kwargs):
        if kwargs.get('click', False) and self.hovered:
            if self.tower is not None:
                try:
                    if game.coins >= Settings._towers[self.tower.level].price:
                        game.coins -= Settings._towers[self.tower.level].price
                        self.tower.level += 1
                        self.tower.__init__(self.tower.rect.x, self.tower.rect.y, self, self.tower.level)

                    return
                except IndexError:
                    print("Tower is maxed out")

            if game.coins >= Settings._towers[0].price:
                game.coins -= Settings._towers[0].price
                self.tower = Tower(self.rect.x, self.rect.y, self, 1)

                game.towers.add(self.tower)
                self.image = self.surface_image if self.tower is not None else self.add_image
                return

        if self.tower is not None:
            self.tower.update()

        x_range = range(self.rect.x, self.rect.x + Settings._spot_size)
        y_range = range(self.rect.y, self.rect.y + Settings._spot_size)

        cursor_pos = pygame.mouse.get_pos()

        self.hovered = cursor_pos[0] in x_range and cursor_pos[1] in y_range

        if self.hovered:
            self.image = self.add_image
        else:
            self.image = self.surface_image


class Baloon(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()

        try:
            __settings = Settings._baloons[level - 1]
        except:
            print(f"Baloon level {level} not found")
            __settings = Settings._baloons[0]

        self.image = pygame.image.load(__settings.image)
        self.image = pygame.transform.scale(self.image, (40, 50))
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2(Settings._path[0])
        self.rect.center = self.position
        self.initial_hp = __settings.hp
        self.hp = __settings.hp
        self.speed_multiplier = __settings.speed
        self.speed = pygame.Vector2(0, 0)

        self.path_index = 1
        self.path_item = Settings._path[self.path_index]

    def move(self):
        heading = self.path_item - self.position
        dist = heading.length()
        heading.normalize_ip()

        if dist < 2:
            self.path_index += 1

            if self.path_index >= len(Settings._path):
                game.hit(self.hp)
                self.kill()
                return
            self.path_item = Settings._path[self.path_index]
        else:
            self.speed = heading * self.speed_multiplier

        self.position += self.speed
        self.rect.center = self.position

    def update(self):
        self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Tower(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, spot: MapSpot, level: int):
        super().__init__()

        __settings = Settings._towers[level - 1]

        self.level = level
        self.image = pygame.image.load(__settings.image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.range = __settings.range
        self.damage = __settings.damage
        self.fire_rate = __settings.fire_rate
        self.fire_timer = Timer(self.fire_rate)
        self.target = None
        self.spot = spot
        sound = Sound("assets/sounds/buy.wav")
        sound.play_sound()

    def update(self, *args, **kwargs):
        if self.target is None:
            self.target = self.find_target()

        if self.target is not None:
            if self.fire_timer.is_next_stop_reached():
                self.fire()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def find_target(self):
        for baloon in game.baloons.sprites():
            if baloon.position.distance_to(self.rect.center) <= self.range:
                return baloon
        return None

    def fire(self):
        if self.target is not None:
            self.target.hp -= self.damage
            if self.target.hp <= 0:
                game.coins += self.target.initial_hp
                self.target.kill()
                self.target = None
                sound = Sound("assets/sounds/pop1.wav")
                sound.play_sound()


class Coinsbar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        coins_icon = pygame.image.load(os.path.join(Settings._assets_directory, "coins.png"))
        coins_icon = pygame.transform.scale(coins_icon, (50, 50))
        self.image = coins_icon
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings._window_width // 1.24
        self.rect.centery = 79
        self.coins = 0

        self.coins_text = pygame.font.SysFont("comicsansms", 30)
        self.coins_text_surface = self.coins_text.render(f"{self.coins}", True, (255, 255, 255))
        self.coins_text_rect = self.coins_text_surface.get_rect()
        self.coins_text_rect.x = Settings._window_width // 1.2
        self.coins_text_rect.centery = 80

    def update(self):
        if game.coins != self.coins:
            self.coins = game.coins

            old_rect = self.coins_text_rect
            self.coins_text_surface = self.coins_text.render(f"{self.coins}", True, (255, 255, 255))
            self.coins_text_rect = self.coins_text_surface.get_rect()
            self.coins_text_rect.x = old_rect.x
            self.coins_text_rect.centery = old_rect.centery

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.coins_text_surface, self.coins_text_rect)


class Healthbar(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(Settings._assets_directory, "healthbar.png")
        )
        self.image = pygame.transform.scale(self.image, (150, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings._window_width // 1.1
        self.rect.centery = 25

        self.health_icon = pygame.image.load(
            os.path.join(Settings._assets_directory, 'heart.png')
        )
        self.health_icon = pygame.transform.scale(self.health_icon, (30, 30))
        self.health_icon_rect = self.health_icon.get_rect()
        self.health_icon_rect.centery = self.rect.centery
        self.health_icon_rect.x = self.rect.x - self.health_icon_rect.width - 10

        self.max_hp = 100
        self.hp = 100

        self.hp_bar_back = pygame.Surface((self.rect.width - 8, self.rect.height - 2))
        self.hp_bar = pygame.Surface(((self.rect.width - 8) / (self.max_hp / self.hp), self.rect.height - 2))
        self.hp_bar_back.fill((0, 0, 0))
        self.hp_bar.fill((255, 0, 0))
        self.hp_bar_rect = self.hp_bar.get_rect()
        self.hp_bar_rect.center = self.rect.center

    def draw(self, screen):
        screen.blit(self.hp_bar_back, self.hp_bar_rect)
        screen.blit(self.hp_bar, self.hp_bar_rect)
        screen.blit(self.image, self.rect)
        screen.blit(self.health_icon, self.health_icon_rect)

    def update(self, *args, **kwargs):
        if kwargs.get('hit', False):
            try:
                position = self.hp_bar_rect.topleft
                self.hp -= kwargs.get('damage', 1)
                self.hp_bar = pygame.transform.scale(self.hp_bar, (
                    (self.rect.width - 8) / (self.max_hp / self.hp), self.rect.height - 2
                ))
                self.hp_bar_rect = self.hp_bar.get_rect()
                self.hp_bar_rect.topleft = position
            except:
                game.running = False


class Game:
    def __init__(self):
        os.environ['SDL_VIDEO_WINDOW_CENTERED'] = '1'

        pygame.init()
        pygame.display.set_caption(Settings._window_caption)
        pygame.mouse.set_cursor(*pygame.cursors.diamond)

        self.screen = pygame.display.set_mode(Settings.get_window_size())
        self.clock = pygame.time.Clock()
        self.running = True
        self.background = Background()
        self.healthbar = Healthbar()
        self.coinsbar = Coinsbar()

        self.baloons = pygame.sprite.Group()

        self.map_spots = pygame.sprite.Group()
        for spot in Settings._map_spots:
            self.map_spots.add(MapSpot(*spot))

        self.towers = pygame.sprite.Group()

        self.baloon_count = 10
        self.baloon_spawned = 0
        self.baloon_level = 1

        self.coins = Settings._towers[0].price

        self.baloon_spawn_timer = Timer(750)
        self.baloon_timer_cooldown = None

    def run(self) -> None:
        while self.running:
            self.clock.tick(Settings._window_fps)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.map_spots.update(click=True)

    def hit(self, damage: int) -> None:
        self.healthbar.update(hit=True, damage=damage)

    def update(self):
        self.map_spots.update()
        self.towers.update()
        self.baloons.update()
        self.healthbar.update()
        self.coinsbar.update()

        # Trigger level pause
        if self.baloon_spawned >= self.baloon_count and not self.baloon_timer_cooldown:
            self.baloon_spawned = 0
            self.baloon_timer_cooldown = Timer(30 * 1000)

            self.baloon_count += 10
            if self.baloon_count > 50:
                self.baloon_count = 10
                self.baloon_level += 1

        # End level pause
        if self.baloon_timer_cooldown and self.baloon_timer_cooldown.is_next_stop_reached():
            self.baloon_timer_cooldown = None

        # Spawn baloons
        if not self.baloon_timer_cooldown:
            if self.baloon_spawn_timer.is_next_stop_reached():
                self.baloon_spawned += 1
                self.baloons.add(Baloon(self.baloon_level))

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.background.draw(self.screen)
        self.map_spots.draw(self.screen)
        self.towers.draw(self.screen)
        self.baloons.draw(self.screen)

        self.healthbar.draw(self.screen)
        self.coinsbar.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
