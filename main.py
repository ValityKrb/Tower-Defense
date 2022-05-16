import os
import mouse as mouse
import pygame
from tkinter import *
from tkinter.ttk import *


# Tkinter Startscreen
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
    _window_width = 1275
    _window_height = 904

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
        (500, 0),
        (500, 65),
        (155, 65),
        (155, 535),
        (665, 535),
        (665, 270),
        (510, 270),
        (510, 430),
        (325, 430),
        (325, 175),
        (840, 175),
        (840, 635),
        (515, 635),
        (515, 720)
    ]

    _spot_size = 50
    _map_spots = [
        (527, 41),
        (474, 94),
        (420, 95)
    ]

    _baloons = [
        BaloonSetting(os.path.join(_baloons_directory, "baloon_1.png"), 1, 1),
        BaloonSetting(os.path.join(_baloons_directory, "baloon_2.png"), 2, 2),
        BaloonSetting(os.path.join(_baloons_directory, "baloon_3.png"), 4, 2),
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
            os.path.join(Settings._assets_directory, "background.jpg")
        )
        self.image = pygame.transform.scale(self.image, (1000, 720))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))


class Overlay(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(Settings._assets_directory, "overlay.png")
        )
        self.image = pygame.transform.scale(self.image, Settings.get_window_size())

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


class Coinsbar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        coins_icon = pygame.image.load(os.path.join(Settings._assets_directory, "coins.png"))
        coins_icon = pygame.transform.scale(coins_icon, (50, 50))
        self.image = coins_icon
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings._window_width // 2
        self.rect.centery = 720 + (Settings._window_height - 720) // 2
        self.coins = 0

        self.coins_text = pygame.font.SysFont("comicsansms", 30)
        self.coins_text_surface = self.coins_text.render(f"{self.coins}", True, (255, 255, 255))
        self.coins_text_rect = self.coins_text_surface.get_rect()
        self.coins_text_rect.x = self.rect.x + self.rect.width + 10
        self.coins_text_rect.centery = 720 + (Settings._window_height - 720) // 2

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
        self.rect.centerx = Settings._window_width // 3
        self.rect.centery = 720 + (Settings._window_height - 720) // 2

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
        self.overlay = Overlay()
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
        self.overlay.update()
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

        self.overlay.draw(self.screen)
        self.healthbar.draw(self.screen)
        self.coinsbar.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
