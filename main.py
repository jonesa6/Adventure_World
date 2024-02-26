@namespace
class SpriteKind:
    fire = SpriteKind.create()
    stop1 = SpriteKind.create()
    stop2 = SpriteKind.create()
    stop3 = SpriteKind.create()
    stop4 = SpriteKind.create()
    stop5 = SpriteKind.create()
    stop6 = SpriteKind.create()
    NPC = SpriteKind.create()
    stop7 = SpriteKind.create()
    stop8 = SpriteKind.create()
    stop9 = SpriteKind.create()
    Bat = SpriteKind.create()
    guide_for_bats_and_yeti = SpriteKind.create()
    water_dragon = SpriteKind.create()
    Attack = SpriteKind.create()
    dragon_feeding = SpriteKind.create()
    tamable_dragons = SpriteKind.create()
    Yeti = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    mySprite.say_text("Ohh bats!! AHHHH!!", 2000, True)
sprites.on_overlap(SpriteKind.player, SpriteKind.Bat, on_on_overlap)

def on_overlap_tile(sprite2, location):
    global dragon_spawning
    tiles.place_on_tile(mySprite, tiles.get_tile_location(6, mySprite.y))
    tiles.set_current_tilemap(tilemap("""
        level7
    """))
    dragon_spawning = True
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(mySprite4)
    sprites.destroy(mySprite5)
    sprites.destroy(mySprite6)
    sprites.destroy(mySprite7)
    sprites.destroy(mySprite8)
    sprites.destroy(mySprite9)
    sprites.destroy(mySprite10)
    sprites.destroy(mySprite11)
    sprites.destroy(mySprite12)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile38
    """),
    on_overlap_tile)

def on_player3_button_b_pressed():
    mySprite.set_kind(SpriteKind.player)
controller.player3.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player3_button_b_pressed)

def on_on_overlap2(sprite3, otherSprite2):
    mySprite15.follow(mySprite)
sprites.on_overlap(SpriteKind.dragon_feeding,
    SpriteKind.tamable_dragons,
    on_on_overlap2)

def on_overlap_tile2(sprite4, location2):
    global mySprite17, mySprite14, inside_mud_home
    for index in range(10):
        mySprite17 = sprites.create(img("""
                . . f f f . . . . . . . . f f f 
                            . f f c c . . . . . . f c c c c 
                            f f c c . . . . . . f c c c c . 
                            f c f c . . . . . . f c c c c . 
                            f f f c c . c c . f c c c c c . 
                            f f c 3 c c 3 c c f c c c c c . 
                            f f c 3 c c 3 c c f c c c c c . 
                            . c c c c c c c c c c c c c . . 
                            . c 1 c c c 1 c c c c c c . . . 
                            c c c c c c c c c c c c . . . . 
                            c c c c c c c c c c c f . . . . 
                            f c 1 f f f 1 c c c c f c . . . 
                            f c c c c c c c c c c f c c . . 
                            . f c c c c c c c c c f . . . . 
                            . . f c c c c c c c f . . . . . 
                            . . . f f f f f f f . . . . . .
            """),
            SpriteKind.Bat)
        tiles.place_on_tile(mySprite17,
            tiles.get_tile_location(randint(5, 20), randint(5, 20)))
        animation.run_image_animation(mySprite17,
            [img("""
                    . . f f f . . . . . . . . f f f 
                                . f f c c . . . . . . f c c c c 
                                f f c c . . . . . . f c c c c . 
                                f c f c . . . . . . f c c c c . 
                                f f f c c . c c . f c c c c c . 
                                f f c 3 c c 3 c c f c c c c c . 
                                f f c 3 c c 3 c c f c c c c c . 
                                . c c c c c c c c c c c c c . . 
                                . c 1 c c c 1 c c c c c c . . . 
                                c c c c c c c c c c c c . . . . 
                                c c c c c c c c c c c f . . . . 
                                f c 1 f f f 1 c c c c f c . . . 
                                f c c c c c c c c c c f c c . . 
                                . f c c c c c c c c c f . . . . 
                                . . f c c c c c c c f . . . . . 
                                . . . f f f f f f f . . . . . .
                """),
                img("""
                    . . f f f . . . . . . . . . . . 
                                f f f c c . . . . . . . . f f f 
                                f f c c . . c c . . . f c c c c 
                                f f c 3 c c 3 c c f f c c c c . 
                                f f c 3 c c 3 c c f c c c c c . 
                                . c c c c c c c c f c c c c c . 
                                . c c c c c c c c c c c c c c . 
                                c c 1 c c c 1 c c c c c c c c . 
                                c c c c c c c c c c c c c c . . 
                                f c c c c c c c c c c f c . . . 
                                f c 1 f f f 1 c c c c f c c . . 
                                . f c c c c c c c c c f . . . . 
                                . . f c c c c c c c f . . . . . 
                                . . . f f f f f f f . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . c c . . c c . . . . . . . . 
                                . . c 3 c c 3 c c c . . . . . . 
                                . c c 3 c c 3 c c c c . . . . . 
                                . c c c c c c c c c f f . . . . 
                                c c c c c c c c c c f f . . . . 
                                c c 1 c c c 1 c c c f f f . . . 
                                c c c c c c c c c f f f f . . . 
                                f c c c c c c c c c c c c . . . 
                                f c 1 f f f 1 c f c c c c . . . 
                                . f c c c c c c f c c c c . . . 
                                c c f c c c c c c c c c c . . . 
                                c c c f f f f f f c c c c c . . 
                                . c c c . . . . . . c c c c c . 
                                . . c c c . . . . . . . c c c c 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . f f f . . . . . . . . f f f . 
                                f f c . . . . . . . f c c c c . 
                                f c c . . . . . . f c c c c . . 
                                c f . . . . . . . f c c c c . . 
                                c f f . . . . . f f c c c c . . 
                                f f f c c . c c f c c c c c . . 
                                f f f c c c c c f c c c c c . . 
                                . f c 3 c c 3 c c c c c c . . . 
                                . c c 3 c c 3 c c c c c c . . . 
                                c c c c c c c c c c c c . . . . 
                                c c 1 c c c 1 c c c c f c . . . 
                                f c c c c c c c c c c f c c . . 
                                f c c c c c c c c c c f . . . . 
                                . f 1 f f f 1 c c c c f . . . . 
                                . . f c c c c c c c f . . . . . 
                                . . . f f f f f f f . . . . . .
                """)],
            100,
            True)
        mySprite14 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.guide_for_bats_and_yeti)
        mySprite17.follow(mySprite14)
    inside_mud_home = True
    tiles.set_current_tilemap(tilemap("""
        level4
    """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(12, 12))
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(mySprite4)
    sprites.destroy(mySprite5)
    sprites.destroy(mySprite6)
    sprites.destroy(mySprite7)
    sprites.destroy(mySprite8)
    sprites.destroy(mySprite9)
    sprites.destroy(mySprite10)
    sprites.destroy(mySprite11)
    sprites.destroy(mySprite12)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile6
    """),
    on_overlap_tile2)

def on_on_overlap3(sprite5, otherSprite3):
    mySprite3.say_text("Hi traveler! Have you heard of the mythological Clear Lakes Water Dragon?",
        2000,
        True)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC, on_on_overlap3)

def on_player2_button_b_pressed():
    if inventory_open:
        switch_between_toolbar_and_inventory()
    else:
        toolbar.set_number(ToolbarNumberAttribute.SELECTED_INDEX,
            toolbar.get_number(ToolbarNumberAttribute.SELECTED_INDEX) + 1)
        if toolbar.get_number(ToolbarNumberAttribute.SELECTED_INDEX) + 1 > toolbar.get_number(ToolbarNumberAttribute.MAX_ITEMS):
            toolbar.set_number(ToolbarNumberAttribute.SELECTED_INDEX, 0)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_player4_button_b_pressed():
    global xy_viewing
    xy_viewing = False
controller.player4.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player4_button_b_pressed)

def on_overlap_tile3(sprite6, location3):
    global mySprite16
    tiles.set_current_tilemap(tilemap("""
        level14
    """))
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(mySprite4)
    sprites.destroy(mySprite5)
    sprites.destroy(mySprite6)
    sprites.destroy(mySprite7)
    sprites.destroy(mySprite8)
    sprites.destroy(mySprite9)
    sprites.destroy(mySprite10)
    sprites.destroy(mySprite11)
    sprites.destroy(mySprite12)
    mySprite16 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.fire)
    tiles.place_on_tile(mySprite16, tiles.get_tile_location(126, 126))
    mySprite16.start_effect(effects.fire)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile45
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite7, location4):
    global mySprite16
    tiles.set_current_tilemap(tilemap("""
        level14
    """))
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(mySprite4)
    sprites.destroy(mySprite5)
    sprites.destroy(mySprite6)
    sprites.destroy(mySprite7)
    sprites.destroy(mySprite8)
    sprites.destroy(mySprite9)
    sprites.destroy(mySprite10)
    sprites.destroy(mySprite11)
    sprites.destroy(mySprite12)
    mySprite16 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.fire)
    tiles.place_on_tile(mySprite16, tiles.get_tile_location(126, 126))
    mySprite16.start_effect(effects.fire)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile63
    """),
    on_overlap_tile4)

def on_on_overlap4(sprite8, otherSprite4):
    mySprite3.follow(mySprite4, 10)
sprites.on_overlap(SpriteKind.NPC, SpriteKind.stop2, on_on_overlap4)

def on_overlap_tile5(sprite9, location5):
    global mySprite16
    tiles.set_current_tilemap(tilemap("""
        level14
    """))
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(mySprite4)
    sprites.destroy(mySprite5)
    sprites.destroy(mySprite6)
    sprites.destroy(mySprite7)
    sprites.destroy(mySprite8)
    sprites.destroy(mySprite9)
    sprites.destroy(mySprite10)
    sprites.destroy(mySprite11)
    sprites.destroy(mySprite12)
    mySprite16 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.fire)
    tiles.place_on_tile(mySprite16, tiles.get_tile_location(126, 126))
    mySprite16.start_effect(effects.fire)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile46
    """),
    on_overlap_tile5)

def on_a_pressed():
    if inventory_open:
        if toolbar_selected:
            if toolbar.get_items()[toolbar.get_number(ToolbarNumberAttribute.SELECTED_INDEX)] and len(inventory.get_items()) < inventory.get_number(InventoryNumberAttribute.MAX_ITEMS):
                inventory.get_items().append(toolbar.get_items().remove_at(toolbar.get_number(ToolbarNumberAttribute.SELECTED_INDEX)))
        else:
            if inventory.get_items()[inventory.get_number(InventoryNumberAttribute.SELECTED_INDEX)] and len(toolbar.get_items()) < toolbar.get_number(ToolbarNumberAttribute.MAX_ITEMS):
                toolbar.get_items().append(inventory.get_items().remove_at(inventory.get_number(InventoryNumberAttribute.SELECTED_INDEX)))
        switch_between_toolbar_and_inventory()
    else:
        if toolbar.get_items()[toolbar.get_number(ToolbarNumberAttribute.SELECTED_INDEX)]:
            mySprite.set_kind(SpriteKind.dragon_feeding)
            
            def on_after():
                mySprite.set_kind(SpriteKind.player)
            timer.after(5000, on_after)
            
    toolbar.update()
    inventory.update()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_player2_button_a_pressed():
    global inventory_open, toolbar_selected
    inventory_open = not (inventory_open)
    inventory.set_number(InventoryNumberAttribute.SELECTED_INDEX,
        inventory.get_number(InventoryNumberAttribute.SELECTED_INDEX))
    inventory.set_flag(SpriteFlag.INVISIBLE, not (inventory_open))
    if not (inventory_open):
        inventory.set_number(InventoryNumberAttribute.SELECTED_INDEX, -1)
        toolbar.set_number(ToolbarNumberAttribute.SELECTED_INDEX, 0)
        toolbar_selected = True
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player2_button_down_pressed():
    if inventory_open:
        if not (toolbar_selected):
            inventory.set_number(InventoryNumberAttribute.SELECTED_INDEX,
                min(inventory.get_number(InventoryNumberAttribute.SELECTED_INDEX) + 8,
                    len(inventory.get_items()) - 1))
controller.player2.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player2_button_down_pressed)

def on_overlap_tile6(sprite10, location6):
    global Water_Dragon, boss_fight_not_active, statusbar2
    statusbar.value += -3
    if boss_fight_not_active:
        Water_Dragon = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . f f f f f 
                            . . . . . . . . . f f a a a 9 f 
                            . . . . . . . . f f a a a f f . 
                            . . . . . . . . f 9 a a f . . . 
                            . . . . . . . . f 9 9 9 f . . . 
                            . . . f f f f f f 9 9 9 f f . . 
                            . . f 9 a a a a 9 f f 9 9 9 f . 
                            . f a a a a a a a a f 9 9 9 f f 
                            f 9 a a a a a a a a 9 f 9 9 9 f 
                            f a f 9 9 9 9 f a a a f 9 9 9 f 
                            f a f f 9 9 f f a a a f 9 9 9 f 
                            f a 5 d 9 9 d 5 a a a f 9 9 9 f 
                            . a a a f f a a a 6 f 9 9 f f . 
                            . f f f f f f f f f f f f . . .
            """),
            SpriteKind.water_dragon)
        Water_Dragon.set_position(mySprite.x, mySprite.y)
        boss_fight_not_active = False
        Water_Dragon.follow(mySprite, 10)
        statusbar2 = statusbars.create(20, 4, StatusBarKind.enemy_health)
        statusbar2.max = 500
        statusbar2.value = 500
        statusbar2.attach_to_sprite(Water_Dragon)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile25
    """),
    on_overlap_tile6)

def on_overlap_tile7(sprite11, location7):
    global dragon_spawning
    tiles.place_on_tile(mySprite, tiles.get_tile_location(5, mySprite.y))
    tiles.set_current_tilemap(tilemap("""
        level7
    """))
    dragon_spawning = True
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(mySprite4)
    sprites.destroy(mySprite5)
    sprites.destroy(mySprite6)
    sprites.destroy(mySprite7)
    sprites.destroy(mySprite8)
    sprites.destroy(mySprite9)
    sprites.destroy(mySprite10)
    sprites.destroy(mySprite11)
    sprites.destroy(mySprite12)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile42
    """),
    on_overlap_tile7)

def switch_between_toolbar_and_inventory():
    global toolbar_selected
    toolbar_selected = not (toolbar_selected)
    if toolbar_selected:
        inventory.set_number(InventoryNumberAttribute.SELECTED_INDEX, -1)
        toolbar.set_number(ToolbarNumberAttribute.SELECTED_INDEX, 0)
    else:
        toolbar.set_number(ToolbarNumberAttribute.SELECTED_INDEX, -1)
        inventory.set_number(InventoryNumberAttribute.SELECTED_INDEX, 0)

def on_overlap_tile8(sprite12, location8):
    global dragon_spawning
    tiles.place_on_tile(mySprite, tiles.get_tile_location(5, mySprite.y))
    tiles.set_current_tilemap(tilemap("""
        level7
    """))
    dragon_spawning = True
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(mySprite4)
    sprites.destroy(mySprite5)
    sprites.destroy(mySprite6)
    sprites.destroy(mySprite7)
    sprites.destroy(mySprite8)
    sprites.destroy(mySprite9)
    sprites.destroy(mySprite10)
    sprites.destroy(mySprite11)
    sprites.destroy(mySprite12)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile39
    """),
    on_overlap_tile8)

def on_on_zero(status):
    sprites.destroy(Water_Dragon)
    statusbar.max += 60
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def on_player2_button_up_pressed():
    if inventory_open:
        if not (toolbar_selected):
            inventory.set_number(InventoryNumberAttribute.SELECTED_INDEX,
                max(inventory.get_number(InventoryNumberAttribute.SELECTED_INDEX) - 8,
                    0))
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def on_on_zero2(status2):
    game.reset()
statusbars.on_zero(StatusBarKind.health, on_on_zero2)

def fill_inventory_with_food():
    global allitems
    allitems = [Inventory.create_item("Dragon Berries",
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . 7 . . . . 
                        . . . . . 7 . . . . 7 7 7 . . . 
                        . . . . 7 7 7 . . 2 2 7 . . . . 
                        . . . 2 2 7 . . . 2 2 . . . . . 
                        . . . 2 2 . . . . . . . . . . . 
                        . . . . . . . . 7 . . . . . . . 
                        . . . . . . . 7 7 7 . . . . . . 
                        . . . . . . 2 2 7 . . . . . . . 
                        . . . . . . 2 2 . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)),
        Inventory.create_item("Dragon Dust",
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . 5 5 5 . . . . . . 
                        . . . . . . 5 5 5 5 . . . . . . 
                        . . . . . 5 5 5 5 5 5 . . . . . 
                        . . . . . 5 5 5 5 1 5 5 5 . . . 
                        . . . 5 5 5 1 5 5 5 5 5 5 5 . . 
                        . . . 5 5 5 5 5 5 5 5 5 1 5 . . 
                        . 5 5 5 1 5 5 5 5 5 1 5 5 5 5 . 
                        . 5 5 5 5 5 5 5 5 5 5 5 5 5 5 . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)),
        Inventory.create_item("Dragon Potion",
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . 9 9 9 9 9 9 9 9 . . . . 
                        . . . . . 9 9 9 9 9 9 . . . . . 
                        . . . . . 9 9 9 9 9 9 . . . . . 
                        . . . . . 9 7 7 7 7 9 . . . . . 
                        . . . . . 9 7 7 7 7 9 . . . . . 
                        . . . . . 9 7 7 7 7 9 . . . . . 
                        . . . . 9 9 7 7 7 7 9 9 . . . . 
                        . . . . 9 7 7 7 7 7 7 9 . . . . 
                        . . . . 9 7 7 7 7 7 7 9 . . . . 
                        . . . . 9 7 7 7 7 7 7 9 . . . . 
                        . . . . 9 9 9 9 9 9 9 9 . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)),
        Inventory.create_item("Magic Dragon Leaf",
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . 7 7 7 7 7 . . 
                        . . . . . . 6 6 7 6 6 6 6 6 7 . 
                        . . . . 7 6 7 7 7 7 7 7 6 6 6 . 
                        . . . 7 6 6 6 6 7 7 6 7 7 7 7 . 
                        . . 7 6 7 7 7 7 6 7 7 7 7 7 6 . 
                        . 7 6 7 . . . 6 7 7 6 6 6 6 7 . 
                        . 7 7 . . . . . 6 7 7 7 7 7 7 . 
                        . . . . . . . . . 6 6 7 7 7 7 . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)),
        Inventory.create_item("Magic Dragon Flower",
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . 2 . 2 . 2 . . . . . . 
                        . . . . . 2 2 2 2 2 . . . . . . 
                        . . . . . 2 2 2 2 c . . . . . . 
                        . . . . . 2 2 2 c c . . . . . . 
                        . . . . . . 2 c c . . . . . . . 
                        . . . . . . . 7 . . 7 7 . . . . 
                        . . . . . . . 7 . 7 7 . . . . . 
                        . . . . . . . 7 . 7 7 . . . . . 
                        . . . . . . . 7 7 7 6 . . . . . 
                        . . . . . . . 7 7 6 . . . . . . 
                        . . . . . . . 7 7 6 . . . . . . 
                        . . . . . . . 6 6 . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """))]
    for index2 in range(randint(39, 39)):
        inventory.get_items().append(allitems._pick_random())

def on_overlap_tile9(sprite13, location9):
    global inside_mud_home, mySprite2, mySprite3, mySprite4, mySprite5, mySprite6, mySprite7, mySprite8, mySprite9, mySprite10, mySprite11, mySprite12
    inside_mud_home = False
    sprites.destroy(mySprite14)
    for index3 in range(10):
        sprites.destroy(mySprite17)
    tiles.set_current_tilemap(tilemap("""
        level1
    """))
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.fire)
    tiles.place_on_tile(mySprite2, tiles.get_tile_location(30, 15))
    mySprite2.start_effect(effects.fire)
    mySprite3 = sprites.create(img("""
            . . . . . . f f f f . . . . . . 
                    . . . . f f f 6 6 f f f . . . . 
                    . . . f f f 6 6 6 6 f f f . . . 
                    . . f f f e e e e e e f f f . . 
                    . . f f e 6 6 6 6 6 6 e e f . . 
                    . . f e 6 f f f f f f 6 e f . . 
                    . . f f f f e e e e f f f f . . 
                    . f f e f 8 f 4 4 f 8 f e f f . 
                    . f e e 4 1 f d d f 1 4 e e f . 
                    . . f e e d d d d d d e e f . . 
                    . . . f e e 4 4 4 4 e e f . . . 
                    . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                    . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        SpriteKind.NPC)
    tiles.place_on_tile(mySprite3, tiles.get_tile_location(6, 8))
    mySprite4 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop1)
    tiles.place_on_tile(mySprite4, tiles.get_tile_location(6, 8))
    mySprite5 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop2)
    tiles.place_on_tile(mySprite5, tiles.get_tile_location(6, 18))
    mySprite6 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop3)
    tiles.place_on_tile(mySprite6, tiles.get_tile_location(31, 18))
    mySprite7 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop4)
    tiles.place_on_tile(mySprite7, tiles.get_tile_location(31, 35))
    mySprite8 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop5)
    tiles.place_on_tile(mySprite8, tiles.get_tile_location(19, 35))
    mySprite9 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop6)
    tiles.place_on_tile(mySprite9, tiles.get_tile_location(19, 32))
    mySprite10 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop7)
    tiles.place_on_tile(mySprite10, tiles.get_tile_location(31, 27))
    mySprite11 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop8)
    tiles.place_on_tile(mySprite11, tiles.get_tile_location(41, 27))
    mySprite12 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop9)
    tiles.place_on_tile(mySprite12, tiles.get_tile_location(41, 23))
    characterAnimations.loop_frames(mySprite3,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 d 4 4 d 8 f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 d 4 4 d 8 f e f f . 
                        . f e e 4 1 d d d d 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 f 4 4 f 8 f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 f 4 4 f 8 f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """)],
        100,
        characterAnimations.rule(Predicate.NOT_MOVING))
    characterAnimations.loop_frames(mySprite3,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 6 6 f f f f f . . 
                        . . f f e 6 e 6 6 e 6 e f f . . 
                        . . f e 6 f 6 f f 6 f 6 e f . . 
                        . . f f f 6 6 e e 6 6 f f f . . 
                        . f f e f 6 f e e f 6 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . . f f f f 6 6 f f f f . . . . 
                        . f f e 6 e 6 6 e 6 e f f . . . 
                        . f e 6 f 6 f f f 6 f e f . . . 
                        . f f f 6 f e e 6 6 f f f . . . 
                        . f e 6 f f e e 6 f e e f . . . 
                        f f e f f e e e f e e e f f . . 
                        f f e e e e e e e e e e f d f . 
                        . . f e e e e e e e e f f b f . 
                        . . e f f f f f f f f 4 f b f . 
                        . . 4 f 6 6 6 6 6 e d d f c f . 
                        . . e f f f f f f e e 4 f f . . 
                        . . . f f f . . . . . . . . . .
            """),
            img("""
                . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . f f f f f 6 6 f f f f f . . . 
                        . f f e 6 e 6 6 e 6 e f f . . . 
                        . f e 6 f 6 f f 6 f 6 e f . . . 
                        . f f f 6 6 e e 6 6 f f f . . . 
                        f f e f 6 f e e f 6 f e f f . . 
                        f e e f f e e e e f e e e f . . 
                        . f e e e e e e e e e e f . . . 
                        . . f e e e e e e e e f . . . . 
                        . e 4 f f f f f f f f 4 e . . . 
                        . 4 d f 6 6 6 6 6 6 f d 4 . . . 
                        . 4 4 f 4 4 4 4 4 4 f 4 4 . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . f f . . f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . . f f f f 6 6 f f f f . . . . 
                        . f f e 6 e 6 6 e 6 e f f . . . 
                        . f e f 6 f f f 6 f 6 e f . . . 
                        . f f f 6 6 e e f 6 f f f . . . 
                        . f e e f 6 e e f f 6 e f . . . 
                        . f e e e f e e e f f e f f . . 
                        . f e e e e e e e e e e f f . . 
                        . f f e e e e e e e e f . . . . 
                        . f 4 f f f f f f f f e . . . . 
                        . f d d e 6 6 6 6 6 f 4 . . . . 
                        . f 4 e e f f f f f f e . . . . 
                        . . . . . . . . f f f . . . . .
            """)],
        100,
        characterAnimations.rule(Predicate.MOVING_UP))
    characterAnimations.loop_frames(mySprite3,
        [img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 6 f e e e e f f . . . . 
                        . . f 6 6 6 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 6 6 6 6 e e f f f f . . . 
                        . f 6 e f f f f 6 6 6 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 d 8 e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 6 6 6 e d d 4 . . . . . 
                        . . . f 6 6 6 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 6 f e e e e f f . . . . 
                        . . f 6 6 6 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 6 6 6 6 e e f f f f . . . 
                        . f 6 e f f f f 6 6 6 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 d 8 e 4 4 e f f . . 
                        . . f e d d d 1 4 d 4 e e f . . 
                        . . . f d d d e e e e e f . . . 
                        . . . f e 4 e d d 4 f . . . . . 
                        . . . f 6 6 e d d e f . . . . . 
                        . . f f 5 5 f e e f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """),
            img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 6 f e e e e f f . . . . 
                        . . f 6 6 6 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 6 6 6 6 e e f f f f . . . 
                        . f 6 e f f f f 6 6 6 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f 8 e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 6 6 6 e d d 4 . . . . . 
                        . . . f 6 6 6 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 6 f e e e e f f . . . . 
                        . . f 6 6 6 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 6 6 6 6 e e f f f f . . . 
                        . f 6 e f f f f 6 6 6 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f 8 e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e d d 4 . . . . 
                        . . . f 6 6 6 6 e d d e . . . . 
                        . . f f 5 5 4 4 f e e f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """)],
        100,
        characterAnimations.rule(Predicate.MOVING_LEFT))
    characterAnimations.loop_frames(mySprite3,
        [img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 6 f . . . 
                        . . . f f e e e e f 6 6 6 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 6 6 6 6 e f . 
                        . . . f e 6 6 6 f f f f e 6 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e 8 d 4 4 e e f . 
                        . . f e e 4 d 4 1 d d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 6 6 6 f . . . 
                        . . . . . e d d e 6 6 6 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 6 f . . . 
                        . . . f f e e e e f 6 6 6 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 6 6 6 6 e f . 
                        . . . f e 6 6 6 f f f f e 6 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e 8 f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e e e d d d f . . . 
                        . . . . . f 4 d d e 4 e f . . . 
                        . . . . . f e d d e 6 6 f . . . 
                        . . . . f f f e e f 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 6 f . . . 
                        . . . f f e e e e f 6 6 6 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 6 6 6 6 e f . 
                        . . . f e 6 6 6 f f f f e 6 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e 8 f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 6 6 6 f . . . 
                        . . . . . e d d e 6 6 6 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 6 f . . . 
                        . . . f f e e e e f 6 6 6 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 6 6 6 6 e f . 
                        . . . f e 6 6 6 f f f f e 6 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e 8 f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . 4 d d e 4 4 4 e f . . . 
                        . . . . e d d e 6 6 6 6 f . . . 
                        . . . . f e e f 4 4 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """)],
        100,
        characterAnimations.rule(Predicate.MOVING_RIGHT))
    characterAnimations.loop_frames(mySprite3,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 d 4 4 d 8 f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . f f e 6 f f f f f f 6 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f 8 d 4 4 d 8 f e f . . 
                        . . f e 4 1 d d d d 1 4 e f . . 
                        . . . f e 4 d d d d 4 e f e . . 
                        . . f e f 6 6 6 6 e d d 4 e . . 
                        . . e 4 f 6 6 6 6 e d d e . . . 
                        . . . . f 4 4 5 5 f e e . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 f 4 4 f 8 f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f e e 6 6 6 6 6 6 e f f . . 
                        . f f e 6 f f f f f f 6 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f 8 f 4 4 f 8 f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . e f e 4 d d d d 4 e f . . . 
                        . . e 4 d d e 6 6 6 6 f e f . . 
                        . . . e d d e 6 6 6 6 f 4 e . . 
                        . . . . e e f 5 5 4 4 f . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        100,
        characterAnimations.rule(Predicate.MOVING_DOWN))
    mySprite3.follow(mySprite5, 10)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile16
    """),
    on_overlap_tile9)

def on_overlap_tile10(sprite14, location10):
    global mySprite2, mySprite3, mySprite4, mySprite5, mySprite6, mySprite7, mySprite8, mySprite9, mySprite10, mySprite11, mySprite12
    for index4 in range(dragon_amount):
        sprites.destroy(mySprite15)
    sprites.destroy(mySprite16)
    tiles.set_current_tilemap(tilemap("""
        level1
    """))
    mySprite2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.fire)
    tiles.place_on_tile(mySprite2, tiles.get_tile_location(30, 15))
    mySprite2.start_effect(effects.fire)
    mySprite3 = sprites.create(img("""
            . . . . . . f f f f . . . . . . 
                    . . . . f f f 6 6 f f f . . . . 
                    . . . f f f 6 6 6 6 f f f . . . 
                    . . f f f e e e e e e f f f . . 
                    . . f f e 6 6 6 6 6 6 e e f . . 
                    . . f e 6 f f f f f f 6 e f . . 
                    . . f f f f e e e e f f f f . . 
                    . f f e f 8 f 4 4 f 8 f e f f . 
                    . f e e 4 1 f d d f 1 4 e e f . 
                    . . f e e d d d d d d e e f . . 
                    . . . f e e 4 4 4 4 e e f . . . 
                    . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                    . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        SpriteKind.NPC)
    tiles.place_on_tile(mySprite3, tiles.get_tile_location(6, 8))
    mySprite4 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop1)
    tiles.place_on_tile(mySprite4, tiles.get_tile_location(6, 8))
    mySprite5 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop2)
    tiles.place_on_tile(mySprite5, tiles.get_tile_location(6, 18))
    mySprite6 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop3)
    tiles.place_on_tile(mySprite6, tiles.get_tile_location(31, 18))
    mySprite7 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop4)
    tiles.place_on_tile(mySprite7, tiles.get_tile_location(31, 35))
    mySprite8 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop5)
    tiles.place_on_tile(mySprite8, tiles.get_tile_location(19, 35))
    mySprite9 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop6)
    tiles.place_on_tile(mySprite9, tiles.get_tile_location(19, 32))
    mySprite10 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop7)
    tiles.place_on_tile(mySprite10, tiles.get_tile_location(31, 27))
    mySprite11 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop8)
    tiles.place_on_tile(mySprite11, tiles.get_tile_location(41, 27))
    mySprite12 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.stop9)
    tiles.place_on_tile(mySprite12, tiles.get_tile_location(41, 23))
    characterAnimations.loop_frames(mySprite3,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 6 6 f f f f f . . 
                        . . f f e 6 e 6 6 e 6 e f f . . 
                        . . f e 6 f 6 f f 6 f 6 e f . . 
                        . . f f f 6 6 e e 6 6 f f f . . 
                        . f f e f 6 f e e f 6 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . . f f f f 6 6 f f f f . . . . 
                        . f f e 6 e 6 6 e 6 e f f . . . 
                        . f e 6 f 6 f f f 6 f e f . . . 
                        . f f f 6 f e e 6 6 f f f . . . 
                        . f e 6 f f e e 6 f e e f . . . 
                        f f e f f e e e f e e e f f . . 
                        f f e e e e e e e e e e f d f . 
                        . . f e e e e e e e e f f b f . 
                        . . e f f f f f f f f 4 f b f . 
                        . . 4 f 6 6 6 6 6 e d d f c f . 
                        . . e f f f f f f e e 4 f f . . 
                        . . . f f f . . . . . . . . . .
            """),
            img("""
                . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . f f f f f 6 6 f f f f f . . . 
                        . f f e 6 e 6 6 e 6 e f f . . . 
                        . f e 6 f 6 f f 6 f 6 e f . . . 
                        . f f f 6 6 e e 6 6 f f f . . . 
                        f f e f 6 f e e f 6 f e f f . . 
                        f e e f f e e e e f e e e f . . 
                        . f e e e e e e e e e e f . . . 
                        . . f e e e e e e e e f . . . . 
                        . e 4 f f f f f f f f 4 e . . . 
                        . 4 d f 6 6 6 6 6 6 f d 4 . . . 
                        . 4 4 f 4 4 4 4 4 4 f 4 4 . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . f f . . f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . . f f f f 6 6 f f f f . . . . 
                        . f f e 6 e 6 6 e 6 e f f . . . 
                        . f e f 6 f f f 6 f 6 e f . . . 
                        . f f f 6 6 e e f 6 f f f . . . 
                        . f e e f 6 e e f f 6 e f . . . 
                        . f e e e f e e e f f e f f . . 
                        . f e e e e e e e e e e f f . . 
                        . f f e e e e e e e e f . . . . 
                        . f 4 f f f f f f f f e . . . . 
                        . f d d e 6 6 6 6 6 f 4 . . . . 
                        . f 4 e e f f f f f f e . . . . 
                        . . . . . . . . f f f . . . . .
            """)],
        100,
        characterAnimations.rule(Predicate.MOVING_UP))
    characterAnimations.loop_frames(mySprite3,
        [img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 6 f e e e e f f . . . . 
                        . . f 6 6 6 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 6 6 6 6 e e f f f f . . . 
                        . f 6 e f f f f 6 6 6 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 d 8 e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 6 6 6 e d d 4 . . . . . 
                        . . . f 6 6 6 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 6 f e e e e f f . . . . 
                        . . f 6 6 6 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 6 6 6 6 e e f f f f . . . 
                        . f 6 e f f f f 6 6 6 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 d 8 e 4 4 e f f . . 
                        . . f e d d d 1 4 d 4 e e f . . 
                        . . . f d d d e e e e e f . . . 
                        . . . f e 4 e d d 4 f . . . . . 
                        . . . f 6 6 e d d e f . . . . . 
                        . . f f 5 5 f e e f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """),
            img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 6 f e e e e f f . . . . 
                        . . f 6 6 6 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 6 6 6 6 e e f f f f . . . 
                        . f 6 e f f f f 6 6 6 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f 8 e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 6 6 6 e d d 4 . . . . . 
                        . . . f 6 6 6 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 6 f e e e e f f . . . . 
                        . . f 6 6 6 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 6 6 6 6 e e f f f f . . . 
                        . f 6 e f f f f 6 6 6 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f 8 e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e d d 4 . . . . 
                        . . . f 6 6 6 6 e d d e . . . . 
                        . . f f 5 5 4 4 f e e f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """)],
        100,
        characterAnimations.rule(Predicate.MOVING_LEFT))
    characterAnimations.loop_frames(mySprite3,
        [img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 6 f . . . 
                        . . . f f e e e e f 6 6 6 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 6 6 6 6 e f . 
                        . . . f e 6 6 6 f f f f e 6 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e 8 d 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 6 6 6 f . . . 
                        . . . . . e d d e 6 6 6 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 6 f . . . 
                        . . . f f e e e e f 6 6 6 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 6 6 6 6 e f . 
                        . . . f e 6 6 6 f f f f e 6 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e 8 d 4 4 e e f . 
                        . . f e e 4 d 4 1 d d d e f . . 
                        . . . f e e e e e d d d f . . . 
                        . . . . . f 4 d d e 4 e f . . . 
                        . . . . . f e d d e 6 6 f . . . 
                        . . . . f f f e e f 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 6 f . . . 
                        . . . f f e e e e f 6 6 6 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 6 6 6 6 e f . 
                        . . . f e 6 6 6 f f f f e 6 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e 8 f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 6 6 6 f . . . 
                        . . . . . e d d e 6 6 6 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 6 f . . . 
                        . . . f f e e e e f 6 6 6 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 6 6 6 6 e f . 
                        . . . f e 6 6 6 f f f f e 6 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e 8 f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . 4 d d e 4 4 4 e f . . . 
                        . . . . e d d e 6 6 6 6 f . . . 
                        . . . . f e e f 4 4 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """)],
        100,
        characterAnimations.rule(Predicate.MOVING_RIGHT))
    characterAnimations.loop_frames(mySprite3,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 d 4 4 d 8 f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . f f e 6 f f f f f f 6 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f 8 d 4 4 d 8 f e f . . 
                        . . f e 4 1 d d d d 1 4 e f . . 
                        . . . f e 4 d d d d 4 e f e . . 
                        . . f e f 6 6 6 6 e d d 4 e . . 
                        . . e 4 f 6 6 6 6 e d d e . . . 
                        . . . . f 4 4 5 5 f e e . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 f 4 4 f 8 f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f e e 6 6 6 6 6 6 e f f . . 
                        . f f e 6 f f f f f f 6 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f 8 f 4 4 f 8 f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . e f e 4 d d d d 4 e f . . . 
                        . . e 4 d d e 6 6 6 6 f e f . . 
                        . . . e d d e 6 6 6 6 f 4 e . . 
                        . . . . e e f 5 5 4 4 f . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        100,
        characterAnimations.rule(Predicate.MOVING_DOWN))
    characterAnimations.loop_frames(mySprite3,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 d 4 4 d 8 f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 d 4 4 d 8 f e f f . 
                        . f e e 4 1 d d d d 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 f 4 4 f 8 f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 6 6 f f f . . . . 
                        . . . f f f 6 6 6 6 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 6 6 6 6 6 6 e e f . . 
                        . . f e 6 f f f f f f 6 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f 8 f 4 4 f 8 f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                        . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """)],
        100,
        characterAnimations.rule(Predicate.NOT_MOVING))
    mySprite3.follow(mySprite5, 10)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile49
    """),
    on_overlap_tile10)

def on_overlap_tile11(sprite15, location11):
    global dragon_spawning
    tiles.place_on_tile(mySprite, tiles.get_tile_location(5, mySprite.y))
    tiles.set_current_tilemap(tilemap("""
        level7
    """))
    dragon_spawning = True
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(mySprite4)
    sprites.destroy(mySprite5)
    sprites.destroy(mySprite6)
    sprites.destroy(mySprite7)
    sprites.destroy(mySprite8)
    sprites.destroy(mySprite9)
    sprites.destroy(mySprite10)
    sprites.destroy(mySprite11)
    sprites.destroy(mySprite12)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile40
    """),
    on_overlap_tile11)

def on_player2_button_right_pressed():
    if inventory_open:
        if toolbar_selected:
            toolbar.set_number(ToolbarNumberAttribute.SELECTED_INDEX,
                min(toolbar.get_number(ToolbarNumberAttribute.SELECTED_INDEX) + 1,
                    toolbar.get_number(ToolbarNumberAttribute.MAX_ITEMS) - 1))
        else:
            inventory.set_number(InventoryNumberAttribute.SELECTED_INDEX,
                min(inventory.get_number(InventoryNumberAttribute.SELECTED_INDEX) + 1,
                    len(inventory.get_items()) - 1))
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_right_pressed)

def on_overlap_tile12(sprite16, location12):
    global mySprite16
    tiles.set_current_tilemap(tilemap("""
        level14
    """))
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(mySprite4)
    sprites.destroy(mySprite5)
    sprites.destroy(mySprite6)
    sprites.destroy(mySprite7)
    sprites.destroy(mySprite8)
    sprites.destroy(mySprite9)
    sprites.destroy(mySprite10)
    sprites.destroy(mySprite11)
    sprites.destroy(mySprite12)
    mySprite16 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.fire)
    tiles.place_on_tile(mySprite16, tiles.get_tile_location(126, 126))
    mySprite16.start_effect(effects.fire)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile44
    """),
    on_overlap_tile12)

def on_on_overlap5(sprite17, otherSprite5):
    statusbar.value += -15
sprites.on_overlap(SpriteKind.water_dragon, SpriteKind.player, on_on_overlap5)

def on_overlap_tile13(sprite18, location13):
    global mySprite16
    tiles.set_current_tilemap(tilemap("""
        level14
    """))
    sprites.destroy(mySprite2)
    sprites.destroy(mySprite3)
    sprites.destroy(mySprite4)
    sprites.destroy(mySprite5)
    sprites.destroy(mySprite6)
    sprites.destroy(mySprite7)
    sprites.destroy(mySprite8)
    sprites.destroy(mySprite9)
    sprites.destroy(mySprite10)
    sprites.destroy(mySprite11)
    sprites.destroy(mySprite12)
    mySprite16 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.fire)
    tiles.place_on_tile(mySprite16, tiles.get_tile_location(126, 126))
    mySprite16.start_effect(effects.fire)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile47
    """),
    on_overlap_tile13)

def on_overlap_tile14(sprite19, location14):
    global mySprite17, mySprite14, inside_ice_home
    for index5 in range(10):
        mySprite17 = sprites.create(img("""
                . . . . f f f f . . . . 
                            . . f f 9 9 9 9 f f . . 
                            . f f 9 9 9 9 9 9 f f . 
                            f f f f 1 9 9 9 f f f f 
                            f f f 1 1 1 9 9 f f f f 
                            f f f 1 1 1 1 9 9 f f f 
                            f 1 9 1 1 1 1 1 1 9 1 f 
                            f 1 1 f f 1 1 f f 1 1 f 
                            f 9 1 9 9 9 9 9 9 1 9 f 
                            . f 9 9 9 f f 9 9 9 f . 
                            . f f 9 9 9 9 9 9 f f . 
                            9 1 f 6 9 9 9 9 6 f 1 9 
                            1 6 f 9 9 9 9 9 9 f 6 1 
                            1 1 f 6 6 6 6 6 6 f 1 1 
                            . . . f f f f f f . . . 
                            . . . f f . . f f . . .
            """),
            SpriteKind.Yeti)
        tiles.place_on_tile(mySprite17,
            tiles.get_tile_location(randint(5, 20), randint(5, 20)))
        animation.run_image_animation(mySprite17,
            [img("""
                    . . . . f f f f . . . . 
                                . . f f 9 9 9 9 f f . . 
                                . f f 9 9 9 9 9 9 f f . 
                                f f f f 1 9 9 9 f f f f 
                                f f f 1 1 1 9 9 f f f f 
                                f f f 1 1 1 1 9 9 f f f 
                                f 1 9 1 1 1 1 1 1 9 1 f 
                                f 1 1 f f 1 1 f f 1 1 f 
                                f 9 1 9 9 9 9 9 9 1 9 f 
                                . f 9 9 9 f f 9 9 9 f . 
                                . f f 9 9 9 9 9 9 f f . 
                                9 1 f 6 9 9 9 9 6 f 1 9 
                                1 6 f 9 9 9 9 9 9 f 6 1 
                                1 1 f 6 6 6 6 6 6 f 1 1 
                                . . . f f f f f f . . . 
                                . . . f f . . f f . . .
                """),
                img("""
                    . . . . . . . . . . . . 
                                . . . f f f f f f . . . 
                                . f f f 9 9 9 9 f f f . 
                                f f f 9 9 9 9 9 9 f f f 
                                f f f f 1 9 9 9 f f f f 
                                f f f 1 1 1 9 9 f f f f 
                                f f f 1 1 1 1 9 9 f f f 
                                f 1 9 1 1 1 1 1 1 9 1 f 
                                f 1 1 f f 1 1 f f 1 1 f 
                                f 9 1 9 9 9 9 9 9 1 9 f 
                                . f 9 9 9 f f 9 1 9 f 6 
                                f f f 9 9 9 9 9 6 6 1 6 
                                6 1 f 6 9 9 9 1 6 6 1 . 
                                . . f 6 6 6 6 f 1 1 . . 
                                . . f f f f f f f . . . 
                                . . f f f . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . 
                                . . . f f f f f f . . . 
                                . f f f 9 9 9 9 f f f . 
                                f f f 9 9 9 9 9 9 f f f 
                                f f f f 9 9 9 1 f f f f 
                                f f f f 9 9 1 1 1 f f f 
                                f f f 9 9 1 1 1 1 f f f 
                                f 1 9 1 1 1 1 1 1 9 1 f 
                                f 1 1 f f 1 1 f f 1 1 f 
                                f 9 1 9 9 9 9 9 9 1 9 f 
                                6 f 9 1 9 f f 9 9 9 f . 
                                6 1 6 6 9 9 9 9 9 f f f 
                                . 1 6 6 1 9 9 9 6 f 1 6 
                                . . 1 1 f 6 6 6 6 f . . 
                                . . . f f f f f f f . . 
                                . . . . . . . f f f . .
                """)],
            100,
            True)
        mySprite14 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.guide_for_bats_and_yeti)
        mySprite17.follow(mySprite14)
    inside_ice_home = True
    tiles.set_current_tilemap(tilemap("""
        level4
    """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(12, 12))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile57
    """),
    on_overlap_tile14)

def on_on_overlap6(sprite20, otherSprite6):
    statusbar2.value += -15
sprites.on_overlap(SpriteKind.water_dragon, SpriteKind.Attack, on_on_overlap6)

def on_overlap_tile15(sprite21, location15):
    toolbar.get_items().remove_at(toolbar.get_number(ToolbarNumberAttribute.SELECTED_INDEX))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile15)

def on_player4_button_a_pressed():
    global xy_viewing
    xy_viewing = True
controller.player4.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player4_button_a_pressed)

def on_player2_button_left_pressed():
    if inventory_open:
        if toolbar_selected:
            toolbar.set_number(ToolbarNumberAttribute.SELECTED_INDEX,
                max(toolbar.get_number(ToolbarNumberAttribute.SELECTED_INDEX) - 1,
                    0))
        else:
            inventory.set_number(InventoryNumberAttribute.SELECTED_INDEX,
                max(inventory.get_number(InventoryNumberAttribute.SELECTED_INDEX) - 1,
                    0))
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_left_pressed)

def create_toolbar_and_inventory():
    global toolbar, inventory, inventory_open, toolbar_selected
    toolbar = Inventory.create_toolbar([], 4)
    toolbar.left = 4
    toolbar.bottom = scene.screen_height() - 9
    toolbar.z = 100
    toolbar.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    inventory = Inventory.create_inventory([], 39)
    inventory.set_number(InventoryNumberAttribute.SELECTED_INDEX, -1)
    inventory.set_color(InventoryColorAttribute.INVENTORY_BACKGROUND, 0)
    inventory.set_text("Dragon Aid Pouch")
    inventory.left = 4
    inventory.top = 4
    inventory.z = 100
    inventory.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, True)
    inventory_open = False
    inventory.set_flag(SpriteFlag.INVISIBLE, not (inventory_open))
    toolbar_selected = True

def on_player3_button_a_pressed():
    if True:
        mySprite.set_kind(SpriteKind.Attack)
    else:
        mySprite.set_kind(SpriteKind.player)
controller.player3.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player3_button_a_pressed)

def on_on_overlap7(sprite22, otherSprite7):
    mySprite.say_text("A tamable dragon!", 2000, True)
sprites.on_overlap(SpriteKind.player,
    SpriteKind.tamable_dragons,
    on_on_overlap7)

def on_on_overlap8(sprite23, otherSprite8):
    mySprite.say_text("Yeti! I must escape!", 2000, True)
sprites.on_overlap(SpriteKind.player, SpriteKind.Yeti, on_on_overlap8)

inside_ice_home = False
allitems: List[Inventory.Item] = []
statusbar2: StatusBarSprite = None
Water_Dragon: Sprite = None
inventory: Inventory.Inventory = None
toolbar_selected = False
mySprite16: Sprite = None
toolbar: Inventory.Toolbar = None
inventory_open = False
inside_mud_home = False
mySprite14: Sprite = None
mySprite17: Sprite = None
mySprite15: Sprite = None
mySprite12: Sprite = None
mySprite11: Sprite = None
mySprite10: Sprite = None
mySprite9: Sprite = None
mySprite8: Sprite = None
mySprite7: Sprite = None
mySprite6: Sprite = None
mySprite5: Sprite = None
mySprite4: Sprite = None
mySprite3: Sprite = None
statusbar: StatusBarSprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
boss_fight_not_active = False
dragon_spawning = False
dragon_amount = 0
xy_viewing = False
xy_viewing = False
dragon_amount = 0
music.play(music.create_song(hex("""
        0078000408060400001c00010a006400f401640000040000000000000000000000000005000004060000000400011d07001c00020a006400f4016400000400000000000000000000000000000000030e0100000400012704000800012708000c0001270c001000012410001400012714001800012918001c0001241c002000012720002400012a24002800012728002c00012430003400012434003800012538003c0001273c004000012944004800012448004c0001274c005000012a54005800012758005c0001275c006000012760006400012764006800012468006c0001276c007000012a70007400012474007800012778007c00012a7c008000012780008400012784008800012788008c0001248c009000012790009400012a94009800012798009c0001249c00a0000127a000a4000127a400a8000127a800ac000124ac00b0000127b000b400012ab400b8000127b800bc000124bc00c000012708001c000e050046006603320000040a002d00000064001400013200020100020e0100000400012704000800012708000c0001270c001000012410001400012714001800012918001c0001241c002000012720002400012a24002800012728002c00012430003400012434003800012538003c0001273c004000012944004800012448004c0001274c005000012a54005800012758005c0001275c006000012760006400012764006800012468006c0001276c007000012a70007400012474007800012778007c00012a7c008000012780008400012784008800012788008c0001248c009000012790009400012a94009800012798009c0001249c00a0000127a000a4000127a400a8000127a800ac000124ac00b0000127b000b400012ab400b8000127b800bc000124bc00c000012709010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8001d010000010001080400050001080800090001080c000d000206081000110001081400150001091800190001061c001d00010820002100010a2400250001082800290001062c002d0001063000310001063400350001073800390001083c003d000109400041000206084400450001064800490001084c004d00010a5400550001085800590002080b5c005d0001086000610001086400650001066800690001086c006d00010a70007100010674007500010878007900010a7c007d0001088000810001088400850001088800890001068c008d00010890009100010a9400950001089800990001069c009d000108a000a1000108a400a5000108a800a9000106ac00ad000108b000b100010ab400b5000108b800b9000106bc00bd000108
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
dragon_spawning = False
list2 = [img("""
        ........................
            ........bbb.............
            .......b333bb...........
            ......b333333b..........
            ......33f13333b.........
            .....f33f13333b.........
            .....333333333b.........
            .....3b3333333b.........
            ......bb33331b..........
            .......333333...........
            ......333333............
            .....333331b............
            .....3133331b...........
            .....31133331b..........
            .....33113333331b.......
            ......33333333331b......
            .......33331333331b.....
            ........33311333331b....
            ..........3333333333....
            ..............333333....
            ..........333..33333....
            .........b1333..333.....
            ..........b1333333......
            ........................
    """),
    img("""
        ........................
            .......666..............
            ......677766............
            .....67777776...........
            .....77f177776..........
            ....f77f177776..........
            ....7777777776..........
            ....7677777776..........
            .....66777716...........
            ......777777............
            .......7777.............
            .....777716.............
            .....7177716............
            .....71177716...........
            .....77117777716........
            ......77777177716.......
            ........7771177716......
            ..........777777776.....
            .............777777.....
            ..............77777.....
            ..........777..7777.....
            .........61777.777......
            ..........6177777.......
            ........................
    """),
    img("""
        ........................
            .......555..............
            ......544455............
            .....54444445...........
            .....44f144445..........
            ....f44f144445..........
            ....4444444445..........
            ....4544444445..........
            .....55444415...........
            ......444444............
            .....444444.............
            ....4444415.............
            ....41444415............
            ....411444415...........
            ....441144444415........
            .....444444444415.......
            ......444414444415......
            .......444114444415.....
            .........4444444444.....
            .............444444.....
            .........444..44444.....
            ........51444..444......
            .........51444444.......
            ........................
    """)]
game.set_dialog_frame(img("""
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
        4 9 9 9 9 9 9 9 9 9 9 9 9 9 4 
        4 9 7 7 7 7 7 7 7 7 7 7 7 9 4 
        4 9 7 5 5 5 5 5 5 5 5 5 7 9 4 
        4 9 7 5 8 8 8 8 8 8 8 5 7 9 4 
        4 9 7 5 8 1 1 1 1 1 8 5 7 9 4 
        4 9 7 5 8 1 1 1 1 1 8 5 7 9 4 
        4 9 7 5 8 1 1 1 1 1 8 5 7 9 4 
        4 9 7 5 8 1 1 1 1 1 8 5 7 9 4 
        4 9 7 5 8 1 1 1 1 1 8 5 7 9 4 
        4 9 7 5 8 8 8 8 8 8 8 5 7 9 4 
        4 9 7 5 5 5 5 5 5 5 5 5 7 9 4 
        4 9 7 7 7 7 7 7 7 7 7 7 7 9 4 
        4 9 9 9 9 9 9 9 9 9 9 9 9 9 4 
        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
"""))
game.set_dialog_cursor(img("""
    ................................
        ................................
        222...3.4.4.55.6....7..8.8.9..aa
        2.2...3.4.4.5..666.777.8.8.99.a.
        222.333.4.4.55.6.6..7..8.8.9..aa
        2.2.3.3.4.4.5..6.6..7..8.8.9..a.
        2.2.333..4..55.6.6..7..888.9..aa
        ................................
        .....b.b.b.ccc.d..e....f........
        .....b.b.b.c.c.dd.e....f........
        .....b.b.b.c.c.d..e..fff........
        .....b.b.b.c.c.d..e..f.f........
        .....bbbbb.ccc.d..ee.fff........
        ................................
        ................................
        ................................
"""))
game.show_long_text("Welcome to Adventure World. Explore caves and find mythical creatures. Dragons exist outside of your home map! Use the arrows to move up and down, as well as side to side. The teleportation squares are found in the middle of maps that are not your home map, using them will bring you back to your home map. ",
    DialogLayout.BOTTOM)
game.show_long_text("Traveler we have gifted you a Dragon Aid Pouch containing items to help you tame small dragons! To use the pouch, go onto Blue Player mode and press A. Next press B and enter to toggle between inventory and hotbar. Use the arrows to navigate the inventory. Now switch to Red Player, press A to select an item. Finally, switch to Blue Player mode and press A to close the inventory.",
    DialogLayout.BOTTOM)
game.show_long_text("In order to move to a different biome, step on the edge of any map! You will be teleported to another map. Pay attention to the colors at the edge of the map, they tell you which biome you will be tramsported to! ",
    DialogLayout.BOTTOM)
game.show_long_text("If you encounter a mythical creature, go onto Yellow Player mode and press A to attack! If you are lost, you are in luck! Go onto Green Player mode, press A to view your x,y coordinates and press B to turn them off. ",
    DialogLayout.BOTTOM)
boss_fight_not_active = True
tiles.set_current_tilemap(tilemap("""
    level1
"""))
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
mySprite.set_position(scene.screen_width() / 2, scene.screen_height() / 2)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
mySprite2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.fire)
tiles.place_on_tile(mySprite2, tiles.get_tile_location(30, 15))
mySprite2.start_effect(effects.fire)
statusbar = statusbars.create(20, 4, StatusBarKind.health)
statusbar.max = 300
statusbar.value = 300
statusbar.attach_to_sprite(mySprite)
characterAnimations.loop_frames(mySprite,
    [img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . . f e 2 f f f f f f 2 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b d 4 4 d b f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . . f e 2 f f f f f f 2 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b d 4 4 d b f e f f . 
                . f e e 4 1 d d d d 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . . f e 2 f f f f f f 2 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b f 4 4 f b f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . . f e 2 f f f f f f 2 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b f 4 4 f b f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """)],
    100,
    characterAnimations.rule(Predicate.NOT_MOVING))
characterAnimations.loop_frames(mySprite,
    [img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f e e e e f f . . . . 
                . . . f e e e f f e e e f . . . 
                . . f f f f f 2 2 f f f f f . . 
                . . f f e 2 e 2 2 e 2 e f f . . 
                . . f e 2 f 2 f f 2 f 2 e f . . 
                . . f f f 2 2 e e 2 2 f f f . . 
                . f f e f 2 f e e f 2 f e f f . 
                . f e e f f e e e e f e e e f . 
                . . f e e e e e e e e e e f . . 
                . . . f e e e e e e e e f . . . 
                . . e 4 f f f f f f f f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . f f f f . . . . . . . 
                . . . f f e e e e f f . . . . . 
                . . f e e e f f e e e f . . . . 
                . . f f f f 2 2 f f f f . . . . 
                . f f e 2 e 2 2 e 2 e f f . . . 
                . f e 2 f 2 f f f 2 f e f . . . 
                . f f f 2 f e e 2 2 f f f . . . 
                . f e 2 f f e e 2 f e e f . . . 
                f f e f f e e e f e e e f f . . 
                f f e e e e e e e e e e f d f . 
                . . f e e e e e e e e f f b f . 
                . . e f f f f f f f f 4 f b f . 
                . . 4 f 2 2 2 2 2 e d d f c f . 
                . . e f f f f f f e e 4 f f . . 
                . . . f f f . . . . . . . . . .
        """),
        img("""
            . . . . . f f f f . . . . . . . 
                . . . f f e e e e f f . . . . . 
                . . f e e e f f e e e f . . . . 
                . f f f f f 2 2 f f f f f . . . 
                . f f e 2 e 2 2 e 2 e f f . . . 
                . f e 2 f 2 f f 2 f 2 e f . . . 
                . f f f 2 2 e e 2 2 f f f . . . 
                f f e f 2 f e e f 2 f e f f . . 
                f e e f f e e e e f e e e f . . 
                . f e e e e e e e e e e f . . . 
                . . f e e e e e e e e f . . . . 
                . e 4 f f f f f f f f 4 e . . . 
                . 4 d f 2 2 2 2 2 2 f d 4 . . . 
                . 4 4 f 4 4 4 4 4 4 f 4 4 . . . 
                . . . . f f f f f f . . . . . . 
                . . . . f f . . f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . f f f f . . . . . . . 
                . . . f f e e e e f f . . . . . 
                . . f e e e f f e e e f . . . . 
                . . f f f f 2 2 f f f f . . . . 
                . f f e 2 e 2 2 e 2 e f f . . . 
                . f e f 2 f f f 2 f 2 e f . . . 
                . f f f 2 2 e e f 2 f f f . . . 
                . f e e f 2 e e f f 2 e f . . . 
                . f e e e f e e e f f e f f . . 
                . f e e e e e e e e e e f f . . 
                . f f e e e e e e e e f . . . . 
                . f 4 f f f f f f f f e . . . . 
                . f d d e 2 2 2 2 2 f 4 . . . . 
                . f 4 e e f f f f f f e . . . . 
                . . . . . . . . f f f . . . . .
        """)],
    100,
    characterAnimations.rule(Predicate.MOVING_UP))
characterAnimations.loop_frames(mySprite,
    [img("""
            . . . . f f f f f f . . . . . . 
                . . . f 2 f e e e e f f . . . . 
                . . f 2 2 2 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 2 2 2 2 e e f f f f . . . 
                . f 2 e f f f f 2 2 2 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 d b e 4 4 e f f . . 
                . . f e d d f 1 4 d 4 e e f . . 
                . . . f d d d d 4 e e e f . . . 
                . . . f e 4 4 4 e e f f . . . . 
                . . . f 2 2 2 e d d 4 . . . . . 
                . . . f 2 2 2 e d d e . . . . . 
                . . . f 5 5 4 f e e f . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . . . . f f f . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . f 2 f e e e e f f . . . . 
                . . f 2 2 2 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 2 2 2 2 e e f f f f . . . 
                . f 2 e f f f f 2 2 2 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 d b e 4 4 e f f . . 
                . . f e d d d 1 4 d 4 e e f . . 
                . . . f d d d e e e e e f . . . 
                . . . f e 4 e d d 4 f . . . . . 
                . . . f 2 2 e d d e f . . . . . 
                . . f f 5 5 f e e f f f . . . . 
                . . f f f f f f f f f f . . . . 
                . . . f f f . . . f f . . . . .
        """),
        img("""
            . . . . f f f f f f . . . . . . 
                . . . f 2 f e e e e f f . . . . 
                . . f 2 2 2 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 2 2 2 2 e e f f f f . . . 
                . f 2 e f f f f 2 2 2 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 f b e 4 4 e f f . . 
                . . f e d d f 1 4 d 4 e e f . . 
                . . . f d d d d 4 e e e f . . . 
                . . . f e 4 4 4 e e f f . . . . 
                . . . f 2 2 2 e d d 4 . . . . . 
                . . . f 2 2 2 e d d e . . . . . 
                . . . f 5 5 4 f e e f . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . . . . f f f . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . f 2 f e e e e f f . . . . 
                . . f 2 2 2 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 2 2 2 2 e e f f f f . . . 
                . f 2 e f f f f 2 2 2 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 f b e 4 4 e f f . . 
                . . f e d d f 1 4 d 4 e e f . . 
                . . . f d d d d 4 e e e f . . . 
                . . . f e 4 4 4 e d d 4 . . . . 
                . . . f 2 2 2 2 e d d e . . . . 
                . . f f 5 5 4 4 f e e f . . . . 
                . . f f f f f f f f f f . . . . 
                . . . f f f . . . f f . . . . .
        """)],
    100,
    characterAnimations.rule(Predicate.MOVING_LEFT))
characterAnimations.loop_frames(mySprite,
    [img("""
            . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b d 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . f f e e 4 4 4 e f . . . 
                . . . . . 4 d d e 2 2 2 f . . . 
                . . . . . e d d e 2 2 2 f . . . 
                . . . . . f e e f 4 5 5 f . . . 
                . . . . . . f f f f f f . . . . 
                . . . . . . . f f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b d 4 4 e e f . 
                . . f e e 4 d 4 1 d d d e f . . 
                . . . f e e e e e d d d f . . . 
                . . . . . f 4 d d e 4 e f . . . 
                . . . . . f e d d e 2 2 f . . . 
                . . . . f f f e e f 5 5 f f . . 
                . . . . f f f f f f f f f f . . 
                . . . . . f f . . . f f f . . .
        """),
        img("""
            . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . f f e e 4 4 4 e f . . . 
                . . . . . 4 d d e 2 2 2 f . . . 
                . . . . . e d d e 2 2 2 f . . . 
                . . . . . f e e f 4 5 5 f . . . 
                . . . . . . f f f f f f . . . . 
                . . . . . . . f f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 2 f . . . 
                . . . f f e e e e f 2 2 2 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 2 2 2 2 e f . 
                . . . f e 2 2 2 f f f f e 2 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e b f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . 4 d d e 4 4 4 e f . . . 
                . . . . e d d e 2 2 2 2 f . . . 
                . . . . f e e f 4 4 5 5 f f . . 
                . . . . f f f f f f f f f f . . 
                . . . . . f f . . . f f f . . .
        """)],
    100,
    characterAnimations.rule(Predicate.MOVING_RIGHT))
characterAnimations.loop_frames(mySprite,
    [img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . . f e 2 f f f f f f 2 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b d 4 4 d b f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . f f e 2 f f f f f f 2 e f f . 
                . f f f f f e e e e f f f f f . 
                . . f e f b d 4 4 d b f e f . . 
                . . f e 4 1 d d d d 1 4 e f . . 
                . . . f e 4 d d d d 4 e f e . . 
                . . f e f 2 2 2 2 e d d 4 e . . 
                . . e 4 f 2 2 2 2 e d d e . . . 
                . . . . f 4 4 5 5 f e e . . . . 
                . . . . f f f f f f f . . . . . 
                . . . . f f f . . . . . . . . .
        """),
        img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . . f e 2 f f f f f f 2 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b f 4 4 f b f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f e e 2 2 2 2 2 2 e f f . . 
                . f f e 2 f f f f f f 2 e f f . 
                . f f f f f e e e e f f f f f . 
                . . f e f b f 4 4 f b f e f . . 
                . . f e 4 1 f d d f 1 4 e f . . 
                . . e f e 4 d d d d 4 e f . . . 
                . . e 4 d d e 2 2 2 2 f e f . . 
                . . . e d d e 2 2 2 2 f 4 e . . 
                . . . . e e f 5 5 4 4 f . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . . . . . . f f f . . . .
        """)],
    100,
    characterAnimations.rule(Predicate.MOVING_DOWN))
mySprite3 = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 6 6 f f f . . . . 
            . . . f f f 6 6 6 6 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 6 6 6 6 6 6 e e f . . 
            . . f e 6 f f f f f f 6 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f 8 f 4 4 f 8 f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 6 6 6 6 6 6 f 4 e . . 
            . . 4 d f 6 6 6 6 6 6 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.NPC)
tiles.place_on_tile(mySprite3, tiles.get_tile_location(6, 8))
mySprite4 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.stop1)
tiles.place_on_tile(mySprite4, tiles.get_tile_location(6, 8))
mySprite5 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.stop2)
tiles.place_on_tile(mySprite5, tiles.get_tile_location(6, 18))
mySprite6 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.stop3)
tiles.place_on_tile(mySprite6, tiles.get_tile_location(31, 18))
mySprite7 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.stop4)
tiles.place_on_tile(mySprite7, tiles.get_tile_location(31, 35))
mySprite8 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.stop5)
tiles.place_on_tile(mySprite8, tiles.get_tile_location(19, 35))
mySprite9 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.stop6)
tiles.place_on_tile(mySprite9, tiles.get_tile_location(19, 32))
mySprite10 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.stop7)
tiles.place_on_tile(mySprite10, tiles.get_tile_location(31, 27))
mySprite11 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.stop8)
tiles.place_on_tile(mySprite11, tiles.get_tile_location(41, 27))
mySprite12 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.stop9)
tiles.place_on_tile(mySprite12, tiles.get_tile_location(41, 23))
create_toolbar_and_inventory()
fill_inventory_with_food()
characterAnimations.loop_frames(mySprite3,
    [img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f e e e e f f . . . . 
                . . . f e e e f f e e e f . . . 
                . . f f f f f 6 6 f f f f f . . 
                . . f f e 6 e 6 6 e 6 e f f . . 
                . . f e 6 f 6 f f 6 f 6 e f . . 
                . . f f f 6 6 e e 6 6 f f f . . 
                . f f e f 6 f e e f 6 f e f f . 
                . f e e f f e e e e f e e e f . 
                . . f e e e e e e e e e e f . . 
                . . . f e e e e e e e e f . . . 
                . . e 4 f f f f f f f f 4 e . . 
                . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . f f f f . . . . . . . 
                . . . f f e e e e f f . . . . . 
                . . f e e e f f e e e f . . . . 
                . . f f f f 6 6 f f f f . . . . 
                . f f e 6 e 6 6 e 6 e f f . . . 
                . f e 6 f 6 f f f 6 f e f . . . 
                . f f f 6 f e e 6 6 f f f . . . 
                . f e 6 f f e e 6 f e e f . . . 
                f f e f f e e e f e e e f f . . 
                f f e e e e e e e e e e f d f . 
                . . f e e e e e e e e f f b f . 
                . . e f f f f f f f f 4 f b f . 
                . . 4 f 6 6 6 6 6 e d d f c f . 
                . . e f f f f f f e e 4 f f . . 
                . . . f f f . . . . . . . . . .
        """),
        img("""
            . . . . . f f f f . . . . . . . 
                . . . f f e e e e f f . . . . . 
                . . f e e e f f e e e f . . . . 
                . f f f f f 6 6 f f f f f . . . 
                . f f e 6 e 6 6 e 6 e f f . . . 
                . f e 6 f 6 f f 6 f 6 e f . . . 
                . f f f 6 6 e e 6 6 f f f . . . 
                f f e f 6 f e e f 6 f e f f . . 
                f e e f f e e e e f e e e f . . 
                . f e e e e e e e e e e f . . . 
                . . f e e e e e e e e f . . . . 
                . e 4 f f f f f f f f 4 e . . . 
                . 4 d f 6 6 6 6 6 6 f d 4 . . . 
                . 4 4 f 4 4 4 4 4 4 f 4 4 . . . 
                . . . . f f f f f f . . . . . . 
                . . . . f f . . f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . f f f f . . . . . . . 
                . . . f f e e e e f f . . . . . 
                . . f e e e f f e e e f . . . . 
                . . f f f f 6 6 f f f f . . . . 
                . f f e 6 e 6 6 e 6 e f f . . . 
                . f e f 6 f f f 6 f 6 e f . . . 
                . f f f 6 6 e e f 6 f f f . . . 
                . f e e f 6 e e f f 6 e f . . . 
                . f e e e f e e e f f e f f . . 
                . f e e e e e e e e e e f f . . 
                . f f e e e e e e e e f . . . . 
                . f 4 f f f f f f f f e . . . . 
                . f d d e 6 6 6 6 6 f 4 . . . . 
                . f 4 e e f f f f f f e . . . . 
                . . . . . . . . f f f . . . . .
        """)],
    100,
    characterAnimations.rule(Predicate.MOVING_UP))
characterAnimations.loop_frames(mySprite3,
    [img("""
            . . . . f f f f f f . . . . . . 
                . . . f 6 f e e e e f f . . . . 
                . . f 6 6 6 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 6 6 6 6 e e f f f f . . . 
                . f 6 e f f f f 6 6 6 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 d 8 e 4 4 e f f . . 
                . . f e d d f 1 4 d 4 e e f . . 
                . . . f d d d d 4 e e e f . . . 
                . . . f e 4 4 4 e e f f . . . . 
                . . . f 6 6 6 e d d 4 . . . . . 
                . . . f 6 6 6 e d d e . . . . . 
                . . . f 5 5 4 f e e f . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . . . . f f f . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . f 6 f e e e e f f . . . . 
                . . f 6 6 6 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 6 6 6 6 e e f f f f . . . 
                . f 6 e f f f f 6 6 6 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 d 8 e 4 4 e f f . . 
                . . f e d d d 1 4 d 4 e e f . . 
                . . . f d d d e e e e e f . . . 
                . . . f e 4 e d d 4 f . . . . . 
                . . . f 6 6 e d d e f . . . . . 
                . . f f 5 5 f e e f f f . . . . 
                . . f f f f f f f f f f . . . . 
                . . . f f f . . . f f . . . . .
        """),
        img("""
            . . . . f f f f f f . . . . . . 
                . . . f 6 f e e e e f f . . . . 
                . . f 6 6 6 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 6 6 6 6 e e f f f f . . . 
                . f 6 e f f f f 6 6 6 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 f 8 e 4 4 e f f . . 
                . . f e d d f 1 4 d 4 e e f . . 
                . . . f d d d d 4 e e e f . . . 
                . . . f e 4 4 4 e e f f . . . . 
                . . . f 6 6 6 e d d 4 . . . . . 
                . . . f 6 6 6 e d d e . . . . . 
                . . . f 5 5 4 f e e f . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . . . . f f f . . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . f 6 f e e e e f f . . . . 
                . . f 6 6 6 f e e e e f f . . . 
                . . f e e e e f f e e e f . . . 
                . f e 6 6 6 6 e e f f f f . . . 
                . f 6 e f f f f 6 6 6 e f . . . 
                . f f f e e e f f f f f f f . . 
                . f e e 4 4 f 8 e 4 4 e f f . . 
                . . f e d d f 1 4 d 4 e e f . . 
                . . . f d d d d 4 e e e f . . . 
                . . . f e 4 4 4 e d d 4 . . . . 
                . . . f 6 6 6 6 e d d e . . . . 
                . . f f 5 5 4 4 f e e f . . . . 
                . . f f f f f f f f f f . . . . 
                . . . f f f . . . f f . . . . .
        """)],
    100,
    characterAnimations.rule(Predicate.MOVING_LEFT))
characterAnimations.loop_frames(mySprite3,
    [img("""
            . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 6 f . . . 
                . . . f f e e e e f 6 6 6 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 6 6 6 6 e f . 
                . . . f e 6 6 6 f f f f e 6 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e 8 d 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . f f e e 4 4 4 e f . . . 
                . . . . . 4 d d e 6 6 6 f . . . 
                . . . . . e d d e 6 6 6 f . . . 
                . . . . . f e e f 4 5 5 f . . . 
                . . . . . . f f f f f f . . . . 
                . . . . . . . f f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 6 f . . . 
                . . . f f e e e e f 6 6 6 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 6 6 6 6 e f . 
                . . . f e 6 6 6 f f f f e 6 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e 8 d 4 4 e e f . 
                . . f e e 4 d 4 1 d d d e f . . 
                . . . f e e e e e d d d f . . . 
                . . . . . f 4 d d e 4 e f . . . 
                . . . . . f e d d e 6 6 f . . . 
                . . . . f f f e e f 5 5 f f . . 
                . . . . f f f f f f f f f f . . 
                . . . . . f f . . . f f f . . .
        """),
        img("""
            . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 6 f . . . 
                . . . f f e e e e f 6 6 6 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 6 6 6 6 e f . 
                . . . f e 6 6 6 f f f f e 6 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e 8 f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . f f e e 4 4 4 e f . . . 
                . . . . . 4 d d e 6 6 6 f . . . 
                . . . . . e d d e 6 6 6 f . . . 
                . . . . . f e e f 4 5 5 f . . . 
                . . . . . . f f f f f f . . . . 
                . . . . . . . f f f . . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f . . . . 
                . . . . f f e e e e f 6 f . . . 
                . . . f f e e e e f 6 6 6 f . . 
                . . . f e e e f f e e e e f . . 
                . . . f f f f e e 6 6 6 6 e f . 
                . . . f e 6 6 6 f f f f e 6 f . 
                . . f f f f f f f e e e f f f . 
                . . f f e 4 4 e 8 f 4 4 e e f . 
                . . f e e 4 d 4 1 f d d e f . . 
                . . . f e e e 4 d d d d f . . . 
                . . . . 4 d d e 4 4 4 e f . . . 
                . . . . e d d e 6 6 6 6 f . . . 
                . . . . f e e f 4 4 5 5 f f . . 
                . . . . f f f f f f f f f f . . 
                . . . . . f f . . . f f f . . .
        """)],
    100,
    characterAnimations.rule(Predicate.MOVING_RIGHT))
characterAnimations.loop_frames(mySprite3,
    [img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 6 6 f f f . . . . 
                . . . f f f 6 6 6 6 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 6 6 6 6 6 6 e e f . . 
                . . f e 6 f f f f f f 6 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f 8 d 4 4 d 8 f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . f f f 6 6 f f f . . . . 
                . . . f f f 6 6 6 6 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 6 6 6 6 6 6 e e f . . 
                . f f e 6 f f f f f f 6 e f f . 
                . f f f f f e e e e f f f f f . 
                . . f e f 8 d 4 4 d 8 f e f . . 
                . . f e 4 1 d d d d 1 4 e f . . 
                . . . f e 4 d d d d 4 e f e . . 
                . . f e f 6 6 6 6 e d d 4 e . . 
                . . e 4 f 6 6 6 6 e d d e . . . 
                . . . . f 4 4 5 5 f e e . . . . 
                . . . . f f f f f f f . . . . . 
                . . . . f f f . . . . . . . . .
        """),
        img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 6 6 f f f . . . . 
                . . . f f f 6 6 6 6 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 6 6 6 6 6 6 e e f . . 
                . . f e 6 f f f f f f 6 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f 8 f 4 4 f 8 f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . . . . . . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . f f f 6 6 f f f . . . . 
                . . . f f f 6 6 6 6 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f e e 6 6 6 6 6 6 e f f . . 
                . f f e 6 f f f f f f 6 e f f . 
                . f f f f f e e e e f f f f f . 
                . . f e f 8 f 4 4 f 8 f e f . . 
                . . f e 4 1 f d d f 1 4 e f . . 
                . . e f e 4 d d d d 4 e f . . . 
                . . e 4 d d e 6 6 6 6 f e f . . 
                . . . e d d e 6 6 6 6 f 4 e . . 
                . . . . e e f 5 5 4 4 f . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . . . . . . f f f . . . .
        """)],
    100,
    characterAnimations.rule(Predicate.MOVING_DOWN))
characterAnimations.loop_frames(mySprite3,
    [img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 6 6 f f f . . . . 
                . . . f f f 6 6 6 6 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 6 6 6 6 6 6 e e f . . 
                . . f e 6 f f f f f f 6 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f 8 d 4 4 d 8 f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 6 6 f f f . . . . 
                . . . f f f 6 6 6 6 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 6 6 6 6 6 6 e e f . . 
                . . f e 6 f f f f f f 6 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f 8 d 4 4 d 8 f e f f . 
                . f e e 4 1 d d d d 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 6 6 f f f . . . . 
                . . . f f f 6 6 6 6 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 6 6 6 6 6 6 e e f . . 
                . . f e 6 f f f f f f 6 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f 8 f 4 4 f 8 f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 6 6 f f f . . . . 
                . . . f f f 6 6 6 6 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 6 6 6 6 6 6 e e f . . 
                . . f e 6 f f f f f f 6 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f 8 f 4 4 f 8 f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 6 6 6 6 6 6 f 4 e . . 
                . . 4 d f 6 6 6 6 6 6 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """)],
    100,
    characterAnimations.rule(Predicate.NOT_MOVING))
mySprite3.follow(mySprite5, 10)

def on_on_update():
    game_crash = 0
    if game_crash:
        game.show_long_text("Adventure World is automatically restarting ",
            DialogLayout.BOTTOM)
        game.reset()
game.on_update(on_on_update)

def on_on_update2():
    if xy_viewing:
        mySprite.say_text("X " + str(Math.round(mySprite.x)) + " Y" + str(Math.round(mySprite.y)))
game.on_update(on_on_update2)

def on_update_interval():
    global mySprite15, dragon_amount
    harpie_spawing = 0
    goblin_spawning = 0
    if dragon_spawning:
        mySprite15 = sprites.create(list2._pick_random(), SpriteKind.tamable_dragons)
        mySprite15.set_position(randint(0, 255), randint(0, 255))
        dragon_amount += 1
    if goblin_spawning:
        pass
    if harpie_spawing:
        pass
game.on_update_interval(50000, on_update_interval)

def on_update_interval2():
    if inside_mud_home:
        mySprite14.set_position(randint(0, 32), randint(0, 32))
game.on_update_interval(100, on_update_interval2)

def on_update_interval3():
    statusbar.value += 2
game.on_update_interval(100, on_update_interval3)
