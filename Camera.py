class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

    def apply_field(self, obj):
        obj.rect.x += self.x
        obj.rect.y += self.y

    def apply_player(self, obj):
        obj.sprite.rect.x += self.x
        obj.sprite.rect.y += self.y

    def update(self, target, width, height):
        self.x = -(target.sprite.rect.x + target.sprite.rect.w // 2 - width // 2)
        self.y = -(target.sprite.rect.y + target.sprite.rect.h // 2 - height // 2)
