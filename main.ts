namespace SpriteKind {
    export const fire = SpriteKind.create()
    export const stop1 = SpriteKind.create()
    export const stop2 = SpriteKind.create()
    export const stop3 = SpriteKind.create()
    export const stop4 = SpriteKind.create()
    export const stop5 = SpriteKind.create()
    export const stop6 = SpriteKind.create()
    export const Catya = SpriteKind.create()
    export const stop7 = SpriteKind.create()
    export const stop8 = SpriteKind.create()
    export const stop9 = SpriteKind.create()
    export const Bat = SpriteKind.create()
    export const guide_for_bats_and_yeti = SpriteKind.create()
    export const water_dragon = SpriteKind.create()
    export const Attack = SpriteKind.create()
    export const dragon_feeding = SpriteKind.create()
    export const tamable_dragons = SpriteKind.create()
    export const Yeti = SpriteKind.create()
    export const goblin = SpriteKind.create()
    export const Harpie = SpriteKind.create()
    export const ask_npc_for_story = SpriteKind.create()
    export const wait = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Bat, function (sprite, otherSprite) {
    mySprite.sayText("Ohh bats!! AHHHH!!", 2000, true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile72`, function (sprite, location) {
    mySprite.setKind(SpriteKind.wait)
    timer.after(1000, function () {
        mySprite.setKind(SpriteKind.Player)
    })
    timer.after(500, function () {
        tileUtil.replaceAllTiles(assets.tile`myTile65`, assets.tile`myTile77`)
        tileUtil.replaceAllTiles(assets.tile`myTile72`, assets.tile`myTile73`)
        timer.after(500, function () {
            tileUtil.replaceAllTiles(assets.tile`myTile70`, assets.tile`myTile67`)
        })
        tileUtil.replaceAllTiles(assets.tile`myTile71`, assets.tile`myTile74`)
        timer.after(500, function () {
            tileUtil.replaceAllTiles(assets.tile`myTile75`, assets.tile`myTile76`)
        })
        tileUtil.setWalls(assets.tile`myTile67`, true)
        tileUtil.setWalls(assets.tile`myTile76`, true)
        timer.after(500, function () {
            tileUtil.replaceAllTiles(assets.tile`myTile77`, assets.tile`myTile69`)
        })
    })
})
controller.player3.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    mySprite.setKind(SpriteKind.Player)
})
controller.player2.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    if (inventory_open) {
        switch_between_toolbar_and_inventory()
    } else {
        toolbar.set_number(ToolbarNumberAttribute.SelectedIndex, toolbar.get_number(ToolbarNumberAttribute.SelectedIndex) + 1)
        if (toolbar.get_number(ToolbarNumberAttribute.SelectedIndex) + 1 > toolbar.get_number(ToolbarNumberAttribute.MaxItems)) {
            toolbar.set_number(ToolbarNumberAttribute.SelectedIndex, 0)
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile44`, function (sprite16, location12) {
    tiles.setCurrentTilemap(tilemap`level14`)
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
    mySprite16 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.fire)
    tiles.placeOnTile(mySprite16, tiles.getTileLocation(126, 126))
    mySprite16.startEffect(effects.fire)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile6`, function (sprite4, location2) {
    for (let index = 0; index < 10; index++) {
        mySprite17 = sprites.create(img`
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
            `, SpriteKind.Bat)
        tiles.placeOnTile(mySprite17, tiles.getTileLocation(randint(5, 20), randint(5, 20)))
        animation.runImageAnimation(
        mySprite17,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        true
        )
        mySprite14 = sprites.create(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, SpriteKind.guide_for_bats_and_yeti)
        mySprite17.follow(mySprite14)
    }
    tiles.setCurrentTilemap(tilemap`level24`)
    inside_mud_home = true
    tiles.placeOnTile(mySprite, tiles.getTileLocation(12, 12))
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
})
controller.player4.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function () {
    xy_viewing = false
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.tamable_dragons, function (sprite22, otherSprite7) {
    mySprite.sayText("A tamable dragon!", 2000, true)
})
statusbars.onZero(StatusBarKind.Health, function (status2) {
    game.reset()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile42`, function (sprite11, location7) {
    tiles.placeOnTile(mySprite, tiles.getTileLocation(5, mySprite.y))
    tiles.setCurrentTilemap(tilemap`level7`)
    dragon_spawning = true
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
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (inventory_open) {
        if (toolbar_selected) {
            if (toolbar.get_items()[toolbar.get_number(ToolbarNumberAttribute.SelectedIndex)] && inventory.get_items().length < inventory.get_number(InventoryNumberAttribute.MaxItems)) {
                inventory.get_items().push(toolbar.get_items().removeAt(toolbar.get_number(ToolbarNumberAttribute.SelectedIndex)))
            }
        } else if (inventory.get_items()[inventory.get_number(InventoryNumberAttribute.SelectedIndex)] && toolbar.get_items().length < toolbar.get_number(ToolbarNumberAttribute.MaxItems)) {
            toolbar.get_items().push(inventory.get_items().removeAt(inventory.get_number(InventoryNumberAttribute.SelectedIndex)))
        }
        switch_between_toolbar_and_inventory()
    } else if (toolbar.get_items()[toolbar.get_number(ToolbarNumberAttribute.SelectedIndex)]) {
        mySprite.setKind(SpriteKind.dragon_feeding)
        timer.after(5000, function () {
            mySprite.setKind(SpriteKind.Player)
        })
    }
    toolbar.update()
    inventory.update()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile46`, function (sprite9, location5) {
    tiles.setCurrentTilemap(tilemap`level14`)
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
    mySprite16 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.fire)
    tiles.placeOnTile(mySprite16, tiles.getTileLocation(126, 126))
    mySprite16.startEffect(effects.fire)
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    inventory_open = !(inventory_open)
    inventory.set_number(InventoryNumberAttribute.SelectedIndex, inventory.get_number(InventoryNumberAttribute.SelectedIndex))
    inventory.setFlag(SpriteFlag.Invisible, !(inventory_open))
    if (!(inventory_open)) {
        inventory.set_number(InventoryNumberAttribute.SelectedIndex, -1)
        toolbar.set_number(ToolbarNumberAttribute.SelectedIndex, 0)
        toolbar_selected = true
    }
})
controller.player2.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Pressed, function () {
    if (inventory_open) {
        if (!(toolbar_selected)) {
            inventory.set_number(InventoryNumberAttribute.SelectedIndex, Math.min(inventory.get_number(InventoryNumberAttribute.SelectedIndex) + 8, inventory.get_items().length - 1))
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile73`, function (sprite, location) {
    mySprite.setKind(SpriteKind.wait)
    timer.after(1000, function () {
        mySprite.setKind(SpriteKind.Player)
    })
    timer.after(500, function () {
        tileUtil.replaceAllTiles(assets.tile`myTile73`, assets.tile`myTile72`)
        tileUtil.replaceAllTiles(assets.tile`myTile69`, assets.tile`myTile77`)
        timer.after(500, function () {
            tileUtil.replaceAllTiles(assets.tile`myTile67`, assets.tile`myTile70`)
        })
        tileUtil.replaceAllTiles(assets.tile`myTile74`, assets.tile`myTile71`)
        timer.after(500, function () {
            tileUtil.replaceAllTiles(assets.tile`myTile76`, assets.tile`myTile75`)
        })
        tileUtil.setWalls(assets.tile`myTile75`, false)
        tileUtil.setWalls(assets.tile`myTile70`, true)
        timer.after(500, function () {
            tileUtil.replaceAllTiles(assets.tile`myTile77`, assets.tile`myTile65`)
        })
    })
})
controller.player4.onButtonEvent(ControllerButton.Down, ControllerButtonEvent.Pressed, function () {
    mySprite.setKind(SpriteKind.ask_npc_for_story)
    timer.after(5000, function () {
        mySprite.setKind(SpriteKind.Player)
    })
})
sprites.onOverlap(SpriteKind.ask_npc_for_story, SpriteKind.Catya, function (sprite, otherSprite) {
    game.setDialogTextColor(6)
    game.setDialogCursor(img`
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        ................................
        .......666.666..6..6.6.666......
        .......6.....6.666.6.6...6......
        .......6...666..6..666.666......
        .......6...6.6..6....6.6.6......
        .......666.666..6..666.666......
        ................................
        ...............ffff.............
        .............fff66fff...........
        ............fff6666fff..........
        ...........fffeeeeeefff.........
        ...........ffe666666eef.........
        ...........fe6ffffff6ef.........
        ...........ffffeeeeffff.........
        ..........ffef8f44f8feff........
        ..........fee41fddf14eef........
        ...........feeddddddeef.........
        ............fee4444eef..........
        ...........e4f666666f4e.........
        ...........4df666666fd4.........
        ...........44f445544f44.........
        ..............ffffff............
        ..............ff..ff............
        ................................
        `)
    game.showLongText("Oh so you want to hear my story. When I was just a kid, I had the most fun kitty. One day, my kitty disappeared and I was never able to find it. I wished upon a star to bring us back together. But my wish was too strong! The star fused me with my kitty. ", DialogLayout.Bottom)
})
function switch_between_toolbar_and_inventory () {
    toolbar_selected = !(toolbar_selected)
    if (toolbar_selected) {
        inventory.set_number(InventoryNumberAttribute.SelectedIndex, -1)
        toolbar.set_number(ToolbarNumberAttribute.SelectedIndex, 0)
    } else {
        toolbar.set_number(ToolbarNumberAttribute.SelectedIndex, -1)
        inventory.set_number(InventoryNumberAttribute.SelectedIndex, 0)
    }
}
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    sprites.destroy(Water_Dragon)
    statusbar.max += 60
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile40`, function (sprite15, location11) {
    tiles.placeOnTile(mySprite, tiles.getTileLocation(5, mySprite.y))
    tiles.setCurrentTilemap(tilemap`level7`)
    dragon_spawning = true
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
})
sprites.onOverlap(SpriteKind.water_dragon, SpriteKind.Attack, function (sprite20, otherSprite6) {
    statusbar2.value += -15
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Catya, function (sprite5, otherSprite3) {
    mySprite3.sayText("Hi traveler! Have you heard of the mythological Clear Lakes Water Dragon?", 2000, true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile38`, function (sprite2, location) {
    tiles.placeOnTile(mySprite, tiles.getTileLocation(6, mySprite.y))
    tiles.setCurrentTilemap(tilemap`level7`)
    dragon_spawning = true
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
})
controller.player2.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Pressed, function () {
    if (inventory_open) {
        if (!(toolbar_selected)) {
            inventory.set_number(InventoryNumberAttribute.SelectedIndex, Math.max(inventory.get_number(InventoryNumberAttribute.SelectedIndex) - 8, 0))
        }
    }
})
function fill_inventory_with_food () {
    allitems = [
    Inventory.create_item("Dragon Berries", img`
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
        `),
    Inventory.create_item("Dragon Dust", img`
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
        `),
    Inventory.create_item("Dragon Potion", img`
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
        `),
    Inventory.create_item("Magic Dragon Leaf", img`
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
        `),
    Inventory.create_item("Magic Dragon Flower", img`
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
        `)
    ]
    for (let index = 0; index < randint(39, 39); index++) {
        inventory.get_items().push(allitems._pickRandom())
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile45`, function (sprite6, location3) {
    tiles.setCurrentTilemap(tilemap`level14`)
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
    mySprite16 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.fire)
    tiles.placeOnTile(mySprite16, tiles.getTileLocation(126, 126))
    mySprite16.startEffect(effects.fire)
})
controller.player2.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function () {
    if (inventory_open) {
        if (toolbar_selected) {
            toolbar.set_number(ToolbarNumberAttribute.SelectedIndex, Math.min(toolbar.get_number(ToolbarNumberAttribute.SelectedIndex) + 1, toolbar.get_number(ToolbarNumberAttribute.MaxItems) - 1))
        } else {
            inventory.set_number(InventoryNumberAttribute.SelectedIndex, Math.min(inventory.get_number(InventoryNumberAttribute.SelectedIndex) + 1, inventory.get_items().length - 1))
        }
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Yeti, function (sprite23, otherSprite8) {
    mySprite.sayText("Yeti! I must escape!", 2000, true)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile47`, function (sprite18, location13) {
    tiles.setCurrentTilemap(tilemap`level14`)
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
    mySprite16 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.fire)
    tiles.placeOnTile(mySprite16, tiles.getTileLocation(126, 126))
    mySprite16.startEffect(effects.fire)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile39`, function (sprite12, location8) {
    tiles.placeOnTile(mySprite, tiles.getTileLocation(5, mySprite.y))
    tiles.setCurrentTilemap(tilemap`level7`)
    dragon_spawning = true
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
})
sprites.onOverlap(SpriteKind.dragon_feeding, SpriteKind.tamable_dragons, function (sprite3, otherSprite2) {
    mySprite15.follow(mySprite)
})
controller.player4.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    xy_viewing = true
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile49`, function (sprite14, location10) {
    for (let index = 0; index < dragon_amount; index++) {
        sprites.destroy(mySprite15)
        sprite_count += -1
    }
    sprites.destroy(mySprite16)
    tiles.setCurrentTilemap(tilemap`level1`)
    mySprite2 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.fire)
    tiles.placeOnTile(mySprite2, tiles.getTileLocation(30, 15))
    mySprite2.startEffect(effects.fire)
    mySprite3 = sprites.create(img`
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
        `, SpriteKind.Catya)
    tiles.placeOnTile(mySprite3, tiles.getTileLocation(6, 8))
    mySprite4 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop1)
    tiles.placeOnTile(mySprite4, tiles.getTileLocation(6, 8))
    mySprite5 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop2)
    tiles.placeOnTile(mySprite5, tiles.getTileLocation(6, 18))
    mySprite6 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop3)
    tiles.placeOnTile(mySprite6, tiles.getTileLocation(31, 18))
    mySprite7 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop4)
    tiles.placeOnTile(mySprite7, tiles.getTileLocation(31, 35))
    mySprite8 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop5)
    tiles.placeOnTile(mySprite8, tiles.getTileLocation(19, 35))
    mySprite9 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop6)
    tiles.placeOnTile(mySprite9, tiles.getTileLocation(19, 32))
    mySprite10 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop7)
    tiles.placeOnTile(mySprite10, tiles.getTileLocation(31, 27))
    mySprite11 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop8)
    tiles.placeOnTile(mySprite11, tiles.getTileLocation(41, 27))
    mySprite12 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop9)
    tiles.placeOnTile(mySprite12, tiles.getTileLocation(41, 23))
    characterAnimations.loopFrames(
    mySprite3,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    characterAnimations.rule(Predicate.MovingUp)
    )
    characterAnimations.loopFrames(
    mySprite3,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    characterAnimations.rule(Predicate.MovingLeft)
    )
    characterAnimations.loopFrames(
    mySprite3,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    characterAnimations.rule(Predicate.MovingRight)
    )
    characterAnimations.loopFrames(
    mySprite3,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    characterAnimations.rule(Predicate.MovingDown)
    )
    characterAnimations.loopFrames(
    mySprite3,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    characterAnimations.rule(Predicate.NotMoving)
    )
    mySprite3.follow(mySprite5, 10)
    sprite_count += 10
})
controller.player2.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function () {
    if (inventory_open) {
        if (toolbar_selected) {
            toolbar.set_number(ToolbarNumberAttribute.SelectedIndex, Math.max(toolbar.get_number(ToolbarNumberAttribute.SelectedIndex) - 1, 0))
        } else {
            inventory.set_number(InventoryNumberAttribute.SelectedIndex, Math.max(inventory.get_number(InventoryNumberAttribute.SelectedIndex) - 1, 0))
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile25`, function (sprite10, location6) {
    statusbar.value += -3
    if (boss_fight_not_active) {
        Water_Dragon = sprites.create(img`
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
            `, SpriteKind.water_dragon)
        Water_Dragon.setPosition(mySprite.x, mySprite.y)
        boss_fight_not_active = false
        Water_Dragon.follow(mySprite, 10)
        statusbar2 = statusbars.create(20, 4, StatusBarKind.EnemyHealth)
        statusbar2.max = 500
        statusbar2.value = 500
        statusbar2.attachToSprite(Water_Dragon)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile57`, function (sprite19, location14) {
    for (let index = 0; index < 10; index++) {
        mySprite17 = sprites.create(img`
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
            `, SpriteKind.Yeti)
        tiles.placeOnTile(mySprite17, tiles.getTileLocation(randint(5, 20), randint(5, 20)))
        animation.runImageAnimation(
        mySprite17,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        true
        )
        mySprite14 = sprites.create(img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            `, SpriteKind.guide_for_bats_and_yeti)
        mySprite17.follow(mySprite14)
    }
    inside_ice_home = true
    tiles.setCurrentTilemap(tilemap`level4`)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(12, 12))
})
function create_toolbar_and_inventory () {
    toolbar = Inventory.create_toolbar([], 4)
    toolbar.left = 4
    toolbar.bottom = scene.screenHeight() - 9
    toolbar.z = 100
    toolbar.setFlag(SpriteFlag.RelativeToCamera, true)
    inventory = Inventory.create_inventory([], 39)
    inventory.set_number(InventoryNumberAttribute.SelectedIndex, -1)
    inventory.set_color(InventoryColorAttribute.InventoryBackground, 0)
    inventory.set_text("Dragon Aid Pouch")
    inventory.left = 4
    inventory.top = 4
    inventory.z = 100
    inventory.setFlag(SpriteFlag.RelativeToCamera, true)
    inventory_open = false
    inventory.setFlag(SpriteFlag.Invisible, !(inventory_open))
    toolbar_selected = true
}
controller.player3.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function () {
    if (true) {
        mySprite.setKind(SpriteKind.Attack)
    } else {
        mySprite.setKind(SpriteKind.Player)
    }
})
sprites.onOverlap(SpriteKind.water_dragon, SpriteKind.Player, function (sprite17, otherSprite5) {
    statusbar.value += -15
})
sprites.onOverlap(SpriteKind.Catya, SpriteKind.stop2, function (sprite8, otherSprite4) {
    mySprite3.follow(mySprite4, 10)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile63`, function (sprite7, location4) {
    tiles.setCurrentTilemap(tilemap`level14`)
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
    mySprite16 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.fire)
    tiles.placeOnTile(mySprite16, tiles.getTileLocation(126, 126))
    mySprite16.startEffect(effects.fire)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile16`, function (sprite13, location9) {
    inside_mud_home = false
    sprites.destroy(mySprite14)
    for (let index = 0; index < 10; index++) {
        sprites.destroy(mySprite17)
    }
    sprite_count += -10
    tiles.setCurrentTilemap(tilemap`level1`)
    mySprite2 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.fire)
    tiles.placeOnTile(mySprite2, tiles.getTileLocation(30, 15))
    mySprite2.startEffect(effects.fire)
    mySprite3 = sprites.create(img`
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
        `, SpriteKind.Catya)
    tiles.placeOnTile(mySprite3, tiles.getTileLocation(6, 8))
    mySprite4 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop1)
    tiles.placeOnTile(mySprite4, tiles.getTileLocation(6, 8))
    mySprite5 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop2)
    tiles.placeOnTile(mySprite5, tiles.getTileLocation(6, 18))
    mySprite6 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop3)
    tiles.placeOnTile(mySprite6, tiles.getTileLocation(31, 18))
    mySprite7 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop4)
    tiles.placeOnTile(mySprite7, tiles.getTileLocation(31, 35))
    mySprite8 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop5)
    tiles.placeOnTile(mySprite8, tiles.getTileLocation(19, 35))
    mySprite9 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop6)
    tiles.placeOnTile(mySprite9, tiles.getTileLocation(19, 32))
    mySprite10 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop7)
    tiles.placeOnTile(mySprite10, tiles.getTileLocation(31, 27))
    mySprite11 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop8)
    tiles.placeOnTile(mySprite11, tiles.getTileLocation(41, 27))
    mySprite12 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.stop9)
    tiles.placeOnTile(mySprite12, tiles.getTileLocation(41, 23))
    characterAnimations.loopFrames(
    mySprite3,
    [img`
        ......ffff......
        ....fff66fff....
        ...fff6666fff...
        ..fffeeeeeefff..
        ..ffe666666eef..
        ..fe6ffffff6ef..
        ..ffffeeeeffff..
        .ffef8d44d8feff.
        .fee41fddf14eef.
        ..feeddddddeef..
        ...fee4444eef...
        ..e4f666666f4e..
        ..4df666666fd4..
        ..44f445544f44..
        .....ffffff.....
        .....ff..ff.....
        ................
        .....ff..ff.....
        .....ffffff.....
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ....fffffffff...
        ...fffffffffff..
        ..fffffffffffff.
        ..fffffffffffff.
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ....fffffffff...
        .....fffffff....
        `,img`
        ......ffff......
        ....fff66fff....
        ...fff6666fff...
        ..fffeeeeeefff..
        ..ffe666666eef..
        ..fe6ffffff6ef..
        ..ffffeeeeffff..
        .ffef8d44d8feff.
        .fee41dddd14eef.
        ..feeddddddeef..
        ...fee4444eef...
        ..e4f666666f4e..
        ..4df666666fd4..
        ..44f445544f44..
        .....ffffff.....
        .....ff..ff.....
        ................
        .....ff..ff.....
        .....ffffff.....
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ....fffffffff...
        ...fffffffffff..
        ..fffffffffffff.
        ..fffffffffffff.
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ....fffffffff...
        .....fffffff....
        `,img`
        ......ffff......
        ....fff66fff....
        ...fff6666fff...
        ..fffeeeeeefff..
        ..ffe666666eef..
        ..fe6ffffff6ef..
        ..ffffeeeeffff..
        .ffef8f44f8feff.
        .fee41fddf14eef.
        ..feeddddddeef..
        ...fee4444eef...
        ..e4f666666f4e..
        ..4df666666fd4..
        ..44f445544f44..
        .....ffffff.....
        .....ff..ff.....
        ................
        .....ff..ff.....
        .....ffffff.....
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ....fffffffff...
        ...fffffffffff..
        ..fffffffffffff.
        ..fffffffffffff.
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ....fffffffff...
        .....fffffff....
        `,img`
        ......ffff......
        ....fff66fff....
        ...fff6666fff...
        ..fffeeeeeefff..
        ..ffe666666eef..
        ..fe6ffffff6ef..
        ..ffffeeeeffff..
        .ffef8f44f8feff.
        .fee41fddf14eef.
        ..feeddddddeef..
        ...fee4444eef...
        ..e4f666666f4e..
        ..4df666666fd4..
        ..44f445544f44..
        .....ffffff.....
        .....ff..ff.....
        ................
        .....ff..ff.....
        .....ffffff.....
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ....fffffffff...
        ...fffffffffff..
        ..fffffffffffff.
        ..fffffffffffff.
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ...fffffffffff..
        ....fffffffff...
        .....fffffff....
        `],
    100,
    characterAnimations.rule(Predicate.NotMoving)
    )
    characterAnimations.loopFrames(
    mySprite3,
    [img`
        ......ffff......
        ....ffeeeeff....
        ...feeeffeeef...
        ..fffff66fffff..
        ..ffe6e66e6eff..
        ..fe6f6ff6f6ef..
        ..fff66ee66fff..
        .ffef6feef6feff.
        .feeffeeeefeeef.
        ..feeeeeeeeeef..
        ...feeeeeeeef...
        ..e4ffffffff4e..
        ..4df666666fd4..
        ..44f444444f44..
        .....ffffff.....
        .....ff..ff.....
        ................
        .....ff..ff.....
        .....ffffff.....
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ...ffffffffff...
        ..ffffffffffff..
        .ffffffffffffff.
        .ffffffffffffff.
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ...ffffffffff...
        ....ffffffff....
        `,img`
        ......ffff......
        ....ffeeeeff....
        ...feeeffeeef...
        ..fffff66fffff..
        ..ffe6e66e6eff..
        ..fe6f6ff6f6ef..
        ..fff66ee66fff..
        .ffef6feef6feff.
        .feeffeeeefeeef.
        ..feeeeeeeeeef..
        ...feeeeeeee4e..
        ..e4ffffffffd4..
        ..4df666666f44..
        ..44f444444f....
        .....ffffff.....
        .....ff.........
        ................
        .....ff.........
        .....ffffff.....
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ...ffffffffff...
        ..ffffffffffff..
        .ffffffffffffff.
        .ffffffffffffff.
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ...ffffffffff...
        ....ffffffff....
        `,img`
        ......ffff......
        ....ffeeeeff....
        ...feeeffeeef...
        ..fffff66fffff..
        ..ffe6e66e6eff..
        ..fe6f6ff6f6ef..
        ..fff66ee66fff..
        .ffef6feef6feff.
        .feeffeeeefeeef.
        ..feeeeeeeeeef..
        ..e4eeeeeeeef...
        ..4dffffffff4e..
        ..44f666666fd4..
        ....f444444f44..
        .....ffffff.....
        .........ff.....
        ................
        .........ff.....
        .....ffffff.....
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ...ffffffffff...
        ..ffffffffffff..
        .ffffffffffffff.
        .ffffffffffffff.
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ...ffffffffff...
        ....ffffffff....
        `,img`
        ......ffff......
        ....ffeeeeff....
        ...feeeffeeef...
        ..fffff66fffff..
        ..ffe6e66e6eff..
        ..fe6f6ff6f6ef..
        ..fff66ee66fff..
        .ffef6feef6feff.
        .feeffeeeefeeef.
        ..feeeeeeeeeef..
        ...feeeeeeeef...
        ..e4ffffffff4e..
        ..4df666666fd4..
        ..44f444444f44..
        .....ffffff.....
        .....ff..ff.....
        ................
        .....ff..ff.....
        .....ffffff.....
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ...ffffffffff...
        ..ffffffffffff..
        .ffffffffffffff.
        .ffffffffffffff.
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ..ffffffffffff..
        ...ffffffffff...
        ....ffffffff....
        `],
    100,
    characterAnimations.rule(Predicate.MovingUp)
    )
    characterAnimations.loopFrames(
    mySprite3,
    [img`
        ....ffffff......
        ...f6feeeeff....
        ..f666feeeeff...
        ..feeeeffeeef...
        .fe6666eeffff...
        .f6effff666ef...
        .fffeeefffffff..
        .fee44d8e44eff..
        ..feddf14d4eef..
        ...fdddd4eeef...
        ...fe444eeff....
        ...f666edd4.....
        ...f666edde.....
        ...f554feef.....
        ....ffffff......
        ......fff.......
        ................
        ......fff.......
        ....ffffff......
        ...ffffffff.....
        ...ffffffff.....
        ...ffffffff.....
        ...fffffffff....
        ...ffffffffff...
        ..ffffffffffff..
        .fffffffffffff..
        .fffffffffffff..
        .ffffffffffff...
        .ffffffffffff...
        ..fffffffffff...
        ..fffffffffff...
        ...fffffffff....
        `,img`
        ................
        ....ffffff......
        ...f6feeeeff....
        ..f666feeeeff...
        ..feeeeffeeef...
        .fe6666eeffff...
        .f6effff666ef...
        .fffeeefffffff..
        .fee44d8e44eff..
        ..feddd14d4eef..
        ...fdddeeeeef...
        ...fe4edd4f.....
        ...f66eddef.....
        ..ff55feefff....
        ..ffffffffff....
        ...fff...ff.....
        ................
        ...fff...ff.....
        ..ffffffffff....
        ..ffffffffff....
        ...ffffffff.....
        ...ffffffff.....
        ...ffffffffff...
        ..ffffffffffff..
        .fffffffffffff..
        .fffffffffffff..
        .ffffffffffff...
        .ffffffffffff...
        ..fffffffffff...
        ..fffffffffff...
        ...fffffffff....
        ....ffffff......
        `,img`
        ....ffffff......
        ...f6feeeeff....
        ..f666feeeeff...
        ..feeeeffeeef...
        .fe6666eeffff...
        .f6effff666ef...
        .fffeeefffffff..
        .fee44f8e44eff..
        ..feddf14d4eef..
        ...fdddd4eeef...
        ...fe444eeff....
        ...f666edd4.....
        ...f666edde.....
        ...f554feef.....
        ....ffffff......
        ......fff.......
        ................
        ......fff.......
        ....ffffff......
        ...ffffffff.....
        ...ffffffff.....
        ...ffffffff.....
        ...fffffffff....
        ...ffffffffff...
        ..ffffffffffff..
        .fffffffffffff..
        .fffffffffffff..
        .ffffffffffff...
        .ffffffffffff...
        ..fffffffffff...
        ..fffffffffff...
        ...fffffffff....
        `,img`
        ................
        ....ffffff......
        ...f6feeeeff....
        ..f666feeeeff...
        ..feeeeffeeef...
        .fe6666eeffff...
        .f6effff666ef...
        .fffeeefffffff..
        .fee44f8e44eff..
        ..feddf14d4eef..
        ...fdddd4eeef...
        ...fe444edd4....
        ...f6666edde....
        ..ff5544feef....
        ..ffffffffff....
        ...fff...ff.....
        ................
        ...fff...ff.....
        ..ffffffffff....
        ..ffffffffff....
        ...fffffffff....
        ...fffffffff....
        ...fffffffff....
        ..fffffffffff...
        .fffffffffffff..
        .fffffffffffff..
        .fffffffffffff..
        .ffffffffffff...
        ..fffffffffff...
        ..fffffffffff...
        ...ffffffffff...
        ....ffffffff....
        `],
    100,
    characterAnimations.rule(Predicate.MovingLeft)
    )
    characterAnimations.loopFrames(
    mySprite3,
    [img`
        ......ffffff....
        ....ffeeeef6f...
        ...ffeeeef666f..
        ...feeeffeeeef..
        ...ffffee6666ef.
        ...fe666ffffe6f.
        ..fffffffeeefff.
        ..ffe44e8d44eef.
        ..fee4d41dddef..
        ...feee4ddddf...
        ....ffee444ef...
        .....4dde666f...
        .....edde666f...
        .....feef455f...
        ......ffffff....
        .......fff......
        ................
        .......fff......
        ......ffffff....
        ......fffffff...
        ......fffffff...
        .....ffffffff...
        ....fffffffff...
        ...ffffffffff...
        ...fffffffffff..
        ...ffffffffffff.
        ....fffffffffff.
        ....fffffffffff.
        ....fffffffffff.
        ....ffffffffff..
        .....fffffffff..
        .......ffffff...
        `,img`
        ................
        ......ffffff....
        ....ffeeeef6f...
        ...ffeeeef666f..
        ...feeeffeeeef..
        ...ffffee6666ef.
        ...fe666ffffe6f.
        ..fffffffeeefff.
        ..ffe44e8f44eef.
        ..fee4d41fddef..
        ...feeeeedddf...
        .....f4dde4ef...
        .....fedde66f...
        ....fffeef55ff..
        ....ffffffffff..
        .....ff...fff...
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        `,img`
        ......ffffff....
        ....ffeeeef6f...
        ...ffeeeef666f..
        ...feeeffeeeef..
        ...ffffee6666ef.
        ...fe666ffffe6f.
        ..fffffffeeefff.
        ..ffe44e8f44eef.
        ..fee4d41fddef..
        ...feee4ddddf...
        ....ffee444ef...
        .....4dde666f...
        .....edde666f...
        .....feef455f...
        ......ffffff....
        .......fff......
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        `,img`
        ................
        ......ffffff....
        ....ffeeeef6f...
        ...ffeeeef666f..
        ...feeeffeeeef..
        ...ffffee6666ef.
        ...fe666ffffe6f.
        ..fffffffeeefff.
        ..ffe44e8f44eef.
        ..fee4d41fddef..
        ...feee4ddddf...
        ....4dde444ef...
        ....edde6666f...
        ....feef4455ff..
        ....ffffffffff..
        .....ff...fff...
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        ................
        `],
    100,
    characterAnimations.rule(Predicate.MovingRight)
    )
    characterAnimations.loopFrames(
    mySprite3,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    100,
    characterAnimations.rule(Predicate.MovingDown)
    )
    mySprite3.follow(mySprite5, 10)
    sprite_count += 10
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile2`, function (sprite21, location15) {
    toolbar.get_items().removeAt(toolbar.get_number(ToolbarNumberAttribute.SelectedIndex))
})
let harpie_amount = 0
let mySprite18: Sprite = null
let goblin_amount = 0
let mySprite13: Sprite = null
let inside_ice_home = false
let mySprite15: Sprite = null
let allitems: Inventory.Item[] = []
let statusbar2: StatusBarSprite = null
let Water_Dragon: Sprite = null
let inventory: Inventory.Inventory = null
let toolbar_selected = false
let inside_mud_home = false
let mySprite14: Sprite = null
let mySprite17: Sprite = null
let mySprite16: Sprite = null
let toolbar: Inventory.Toolbar = null
let inventory_open = false
let mySprite12: Sprite = null
let mySprite11: Sprite = null
let mySprite10: Sprite = null
let mySprite9: Sprite = null
let mySprite8: Sprite = null
let mySprite7: Sprite = null
let mySprite6: Sprite = null
let mySprite5: Sprite = null
let mySprite4: Sprite = null
let mySprite3: Sprite = null
let statusbar: StatusBarSprite = null
let mySprite2: Sprite = null
let mySprite: Sprite = null
let boss_fight_not_active = false
let dragon_spawning = false
let dragon_amount = 0
let xy_viewing = false
xy_viewing = false
dragon_amount = 0
dragon_spawning = false
let list2 = [img`
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
    ..........ffffffff......
    .........fffff..fff.....
    ..........fff..fffff....
    ..............ffffff....
    ..........ffffffffff....
    ........ffffffffffff....
    .......ffffffffffff.....
    ......ffffffffffff......
    .....ffffffffffff.......
    .....fffffffff..........
    .....ffffffff...........
    .....fffffff............
    ......ffffff............
    .......ffffff...........
    ......ffffffff..........
    .....ffffffffff.........
    .....ffffffffff.........
    .....ffffffffff.........
    `, img`
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
    ...........ffffff.......
    ..........ffff.fff......
    .........ffff..ffff.....
    ..............fffff.....
    .............ffffff.....
    ..........fffffffff.....
    ........ffffffffff......
    ......fffffffffff.......
    .....fffffffffff........
    .....ffffffff...........
    .....fffffff............
    .....ffffff.............
    .......ffff.............
    ......ffffff............
    .....ffffffff...........
    ....fffffffff...........
    ....fffffffff...........
    .....ffffffff...........
    `, img`
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
    ..........fffffff.......
    .........ffff..fff......
    ........ffff..fffff.....
    .........ff..ffffff.....
    ............fffffff.....
    .........ffffffffff.....
    .........fffffffff......
    .........ffffffff.......
    ........ffffffff........
    ......fffffff...........
    .....fffffff............
    ....fffffff.............
    ....fffffff.............
    ....ffffffff............
    ....fffffffff...........
    .....fffffffff..........
    ......ffffffff..........
    .......fffffff..........
    `]
game.setDialogFrame(img`
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
    4 9 9 9 9 9 9 9 9 9 9 9 9 9 4 
    4 9 7 7 7 7 7 7 7 7 7 7 7 9 4 
    4 9 7 5 5 5 5 5 5 5 5 5 7 9 4 
    4 9 7 5 1 1 1 1 1 1 1 5 7 9 4 
    4 9 7 5 1 1 1 1 1 1 1 5 7 9 4 
    4 9 7 5 1 1 1 1 1 1 1 5 7 9 4 
    4 9 7 5 1 1 1 1 1 1 1 5 7 9 4 
    4 9 7 5 1 1 1 1 1 1 1 5 7 9 4 
    4 9 7 5 1 1 1 1 1 1 1 5 7 9 4 
    4 9 7 5 1 1 1 1 1 1 1 5 7 9 4 
    4 9 7 5 5 5 5 5 5 5 5 5 7 9 4 
    4 9 7 7 7 7 7 7 7 7 7 7 7 9 4 
    4 9 9 9 9 9 9 9 9 9 9 9 9 9 4 
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 
    `)
game.setDialogCursor(img`
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
    `)
game.showLongText("Welcome to Adventure World. Explore caves and find mythical creatures. Dragons exist outside of your home map! Use the arrows to move up and down, as well as side to side. The teleportation squares are found in the middle of maps that are not your home map, using them will bring you back to your home map. ", DialogLayout.Bottom)
game.showLongText("Traveler we have gifted you a Dragon Aid Pouch containing items to help you tame small dragons! To use the pouch, go onto Blue Player mode and press A. Next press B and enter to toggle between inventory and hotbar. Use the arrows to navigate the inventory. Now switch to Red Player, press A to select an item. Finally, switch to Blue Player mode and press A to close the inventory.", DialogLayout.Bottom)
game.showLongText("In order to move to a different biome, step on the edge of any map! You will be teleported to another map. Pay attention to the colors at the edge of the map, they tell you which biome you will be tramsported to! ", DialogLayout.Bottom)
game.showLongText("If you encounter a mythical creature, go onto Yellow Player mode and press A to attack! If you are lost, you are in luck! Go onto Green Player mode, press A to view your x,y coordinates and press B to turn them off. ", DialogLayout.Bottom)
boss_fight_not_active = true
tiles.setCurrentTilemap(tilemap`level1`)
mySprite = sprites.create(img`
    ......ffff......
    ....fff22fff....
    ...fff2222fff...
    ..fffeeeeeefff..
    ..ffe222222eef..
    ..fe2ffffff2ef..
    ..ffffeeeeffff..
    .ffefbf44fbfeff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f222222f4e..
    ..4df222222fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    ................
    `, SpriteKind.Player)
mySprite.setPosition(scene.screenWidth() / 2, scene.screenHeight() / 2)
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
mySprite2 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.fire)
tiles.placeOnTile(mySprite2, tiles.getTileLocation(30, 15))
mySprite2.startEffect(effects.fire)
statusbar = statusbars.create(20, 4, StatusBarKind.Health)
statusbar.max = 300
statusbar.value = 300
statusbar.attachToSprite(mySprite)
characterAnimations.loopFrames(
mySprite,
[img`
    ......ffff......
    ....fff22fff....
    ...fff2222fff...
    ..fffeeeeeefff..
    ..ffe222222eef..
    ..fe2ffffff2ef..
    ..ffffeeeeffff..
    .ffefbd44dbfeff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f222222f4e..
    ..4df222222fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..fffffffffff...
    .fffffffffffff..
    fffffffffffffff.
    fffffffffffffff.
    fffffffffffffff.
    .fffffffffffff..
    ..fffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    `,img`
    ......ffff......
    ....fff22fff....
    ...fff2222fff...
    ..fffeeeeeefff..
    ..ffe222222eef..
    ..fe2ffffff2ef..
    ..ffffeeeeffff..
    .ffefbd44dbfeff.
    .fee41dddd14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f222222f4e..
    ..4df222222fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..fffffffffff...
    .fffffffffffff..
    fffffffffffffff.
    fffffffffffffff.
    fffffffffffffff.
    .fffffffffffff..
    ..fffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    `,img`
    ......ffff......
    ....fff22fff....
    ...fff2222fff...
    ..fffeeeeeefff..
    ..ffe222222eef..
    ..fe2ffffff2ef..
    ..ffffeeeeffff..
    .ffefbf44fbfeff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f222222f4e..
    ..4df222222fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..fffffffffff...
    .fffffffffffff..
    fffffffffffffff.
    fffffffffffffff.
    fffffffffffffff.
    .fffffffffffff..
    ..fffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    `,img`
    ......ffff......
    ....fff22fff....
    ...fff2222fff...
    ..fffeeeeeefff..
    ..ffe222222eef..
    ..fe2ffffff2ef..
    ..ffffeeeeffff..
    .ffefbf44fbfeff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f222222f4e..
    ..4df222222fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..fffffffffff...
    .fffffffffffff..
    fffffffffffffff.
    fffffffffffffff.
    fffffffffffffff.
    .fffffffffffff..
    ..fffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    `],
100,
characterAnimations.rule(Predicate.NotMoving)
)
characterAnimations.loopFrames(
mySprite,
[img`
    .....ffff.......
    ...ffeeeeff.....
    ..feeeffeeef....
    .fffff22fffff...
    .ffe2e22e2eff...
    .fe2f2ff2f2ef...
    .fff22ee22fff...
    ffef2feef2feff..
    feeffeeeefeeef..
    .feeeeeeeeeef...
    ..feeeeeeeef....
    .e4ffffffff4e...
    .4df222222fd4...
    .44f444444f44...
    ....ffffff......
    ....ff..ff......
    ................
    ....ff..........
    ....ff..ff......
    ....ffffff......
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    ...ffffffff.....
    ..ffffffffff....
    .ffffffffffff...
    ffffffffffffff..
    ffffffffffffff..
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    `,img`
    .......ffff.....
    .....ffeeeeff...
    ....feeeffeeef..
    ...fffff22fffff.
    ...ffe2e22e2eff.
    ...fe2f2ff2f2ef.
    ...fff22ee22fff.
    ..ffef2feef2feff
    ..feeffeeeefeeef
    ...feeeeeeeeeef.
    ....feeeeeeee4e.
    ...e4ffffffffd4.
    ...4df222222f44.
    ...44f444444f...
    ......ffffff....
    ......ff........
    ................
    ......ff........
    ......ff........
    ......ffffff....
    ...ffffffffffff.
    ...ffffffffffff.
    ...ffffffffffff.
    .....ffffffff...
    ....ffffffffff..
    ...ffffffffffff.
    ..ffffffffffffff
    ..ffffffffffffff
    ...ffffffffffff.
    ...ffffffffffff.
    ...ffffffffffff.
    ...ffffffffffff.
    `,img`
    ......ffff......
    ....ffeeeeff....
    ...feeeffeeef...
    ..fffff22fffff..
    ..ffe2e22e2eff..
    ..fe2f2ff2f2ef..
    ..fff22ee22fff..
    .ffef2feef2feff.
    .feeffeeeefeeef.
    ..feeeeeeeeeef..
    ..e4eeeeeeeef...
    ..4dffffffff4e..
    ..44f222222fd4..
    ....f444444f44..
    .....ffffff.....
    .........ff.....
    ................
    .....ff.........
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ....ffffffff....
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    `,img`
    ......ffff......
    ....ffeeeeff....
    ...feeeffeeef...
    ..fffff22fffff..
    ..ffe2e22e2eff..
    ..fe2f2ff2f2ef..
    ..fff22ee22fff..
    .ffef2feef2feff.
    .feeffeeeefeeef.
    ..feeeeeeeeeef..
    ...feeeeeeee4e..
    ..e4ffffffffd4..
    ..4df222222f44..
    ..44f444444f....
    .....ffffff.....
    .....ff.........
    ................
    .....ff.........
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ....ffffffff....
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    `],
100,
characterAnimations.rule(Predicate.MovingUp)
)
characterAnimations.loopFrames(
mySprite,
[img`
    ....ffffff......
    ...f2feeeeff....
    ..f222feeeeff...
    ..feeeeffeeef...
    .fe2222eeffff...
    .f2effff222ef...
    .fffeeefffffff..
    .fee44dbe44eff..
    ..feddf14d4eef..
    ...fdddd4eeef...
    ...fe444eeff....
    ...f222edd4.....
    ...f222edde.....
    ...f554feef.....
    ....ffffff......
    ....f.fff.......
    ................
    ......fff.......
    ....ffffff......
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ..ffffffffff....
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    ..ffffffffffff..
    ..ffffffffffff..
    ...fffffffff....
    `,img`
    ....ffffff......
    ...f2feeeeff....
    ..f222feeeeff...
    ..feeeeffeeef...
    .fe2222eeffff...
    .f2effff222ef...
    .fffeeefffffff..
    .fee44dbe44eff..
    ..feddd14d4eef..
    ...fdddd4eeef...
    ...fe444ddff....
    ...f222edd4.....
    ...f222eeee.....
    ...f554feef.....
    ....ffffff......
    ....fff..f......
    ................
    ....fff.........
    ....ffffff......
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ..ffffffffff....
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    ..ffffffffffff..
    ..ffffffffffff..
    ...fffffffff....
    `,img`
    ....ffffff......
    ...f2feeeeff....
    ..f222feeeeff...
    ..feeeeffeeef...
    .fe2222eeffff...
    .f2effff222ef...
    .fffeeefffffff..
    .fee44fbe44eff..
    ..feddf14d4eef..
    ...fdddd4eeef...
    ...fe444eeff....
    ...f222edd4.....
    ...f222edde.....
    ...f554feef.....
    ....ffffff......
    ......fff.......
    ................
    ......fff.......
    ....ffffff......
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ..ffffffffff....
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    ..ffffffffffff..
    ..ffffffffffff..
    ...fffffffff....
    `,img`
    ....ffffff......
    ...f2feeeeff....
    ..f222feeeeff...
    ..feeeeffeeef...
    .fe2222eeffff...
    .f2effff222ef...
    .fffeeefffffff..
    .fee44fbe44eff..
    ..feddf14d4eef..
    ...fdddd4eeef...
    ...fe444ddff....
    ...f222edd4.....
    ...f222eeee.....
    ...f554feef.....
    ....ffffff......
    ....fff..f......
    ................
    ....fff.........
    ....ffffff......
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ..ffffffffff....
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    ..ffffffffffff..
    ..ffffffffffff..
    ...fffffffff....
    `],
100,
characterAnimations.rule(Predicate.MovingLeft)
)
characterAnimations.loopFrames(
mySprite,
[img`
    ......ffffff....
    ....ffeeeef2f...
    ...ffeeeef222f..
    ...feeeffeeeef..
    ...ffffee2222ef.
    ...fe222ffffe2f.
    ..fffffffeeefff.
    ..ffe44ebd44eef.
    ..fee4d41fddef..
    ...feee4ddddf...
    ....ffee444ef...
    .....4dde222f...
    .....edde222f...
    .....feef455f...
    ......ffffff....
    .......fff......
    ................
    .......fff......
    ......ffffff....
    .....ffffffff...
    .....ffffffff...
    .....ffffffff...
    ....fffffffff...
    ...ffffffffff...
    ..ffffffffffff..
    ..fffffffffffff.
    ..fffffffffffff.
    ...ffffffffffff.
    ...ffffffffffff.
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    `,img`
    ......ffffff....
    ....ffeeeef2f...
    ...ffeeeef222f..
    ...feeeffeeeef..
    ...ffffee2222ef.
    ...fe222ffffe2f.
    ..fffffffeeefff.
    ..ffe44ebd44eef.
    ..fee4d41dddef..
    ...feee4ddddf...
    ....ffdd444ef...
    .....4dde222f...
    .....eeee222f...
    .....feef455f...
    ......ffffff....
    .........fff....
    ................
    .........fff....
    ......ffffff....
    .....ffffffff...
    .....ffffffff...
    .....ffffffff...
    ....fffffffff...
    ...ffffffffff...
    ..ffffffffffff..
    ..fffffffffffff.
    ..fffffffffffff.
    ...ffffffffffff.
    ...ffffffffffff.
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    `,img`
    ......ffffff....
    ....ffeeeef2f...
    ...ffeeeef222f..
    ...feeeffeeeef..
    ...ffffee2222ef.
    ...fe222ffffe2f.
    ..fffffffeeefff.
    ..ffe44ebf44eef.
    ..fee4d41fddef..
    ...feee4ddddf...
    ....ffee444ef...
    .....4dde222f...
    .....edde222f...
    .....feef455f...
    ......ffffff....
    .......fff......
    ................
    .......fff......
    ......ffffff....
    .....ffffffff...
    .....ffffffff...
    .....ffffffff...
    ....fffffffff...
    ...ffffffffff...
    ..ffffffffffff..
    ..fffffffffffff.
    ..fffffffffffff.
    ...ffffffffffff.
    ...ffffffffffff.
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    `,img`
    ......ffffff....
    ....ffeeeef2f...
    ...ffeeeef222f..
    ...feeeffeeeef..
    ...ffffee2222ef.
    ...fe222ffffe2f.
    ..fffffffeeefff.
    ..ffe44ebf44eef.
    ..fee4d41fddef..
    ...feee4ddddf...
    ....ffdd444ef...
    .....4dde222f...
    .....eeee222f...
    .....feef455f...
    ......ffffff....
    .........fff....
    ................
    .........fff....
    ......ffffff....
    .....ffffffff...
    .....ffffffff...
    .....ffffffff...
    ....fffffffff...
    ...ffffffffff...
    ..ffffffffffff..
    ..fffffffffffff.
    ..fffffffffffff.
    ...ffffffffffff.
    ...ffffffffffff.
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    `],
100,
characterAnimations.rule(Predicate.MovingRight)
)
characterAnimations.loopFrames(
mySprite,
[img`
    ......ffff......
    ....fff22fff....
    ...fff2222fff...
    ..fffeeeeeefff..
    ..ffe222222eef..
    ..fe2ffffff2ef..
    ..ffffeeeeffff..
    .ffefbf44fbfeff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f222222f4e..
    ..4df222222fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    `,img`
    .....ffff.......
    ...fff22fff.....
    ..fff2222fff....
    .fffeeeeeefff...
    .ffe222222eef...
    .fe2ffffff2ef...
    .ffffeeeeffff...
    ffefbd44dbfeff..
    fee41fddf14eef..
    .feeddddddeef...
    ..fee4444ee4e...
    .e4f222222fd4...
    .4df222222f44...
    .44f445544f.....
    ....ffffff......
    ....ff..ff......
    ................
    ....ff..ff......
    ....ffffff......
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    ..ffffffffff....
    .ffffffffffff...
    ffffffffffffff..
    ffffffffffffff..
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    .ffffffffffff...
    ..ffffffffff....
    `,img`
    ......ffff......
    ....fff22fff....
    ...fff2222fff...
    ..fffeeeeeefff..
    ..ffe222222eef..
    ..fe2ffffff2ef..
    ..ffffeeeeffff..
    .ffefbf44fbfeff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ..e4ee4444eef...
    ..4df222222f4e..
    ..44f222222fd4..
    ....f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    `,img`
    ......ffff......
    ....fff22fff....
    ...fff2222fff...
    ..fffeeeeeefff..
    ..ffe222222eef..
    ..fe2ffffff2ef..
    ..ffffeeeeffff..
    .ffefbf44fbfeff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444ee4e..
    ..e4f222222fd4..
    ..4df222222f44..
    ..44f445544f....
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    `],
100,
characterAnimations.rule(Predicate.MovingDown)
)
mySprite3 = sprites.create(img`
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
    `, SpriteKind.Catya)
tiles.placeOnTile(mySprite3, tiles.getTileLocation(6, 8))
mySprite4 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.stop1)
tiles.placeOnTile(mySprite4, tiles.getTileLocation(6, 8))
mySprite5 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.stop2)
tiles.placeOnTile(mySprite5, tiles.getTileLocation(6, 18))
mySprite6 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.stop3)
tiles.placeOnTile(mySprite6, tiles.getTileLocation(31, 18))
mySprite7 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.stop4)
tiles.placeOnTile(mySprite7, tiles.getTileLocation(31, 35))
mySprite8 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.stop5)
tiles.placeOnTile(mySprite8, tiles.getTileLocation(19, 35))
mySprite9 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.stop6)
tiles.placeOnTile(mySprite9, tiles.getTileLocation(19, 32))
mySprite10 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.stop7)
tiles.placeOnTile(mySprite10, tiles.getTileLocation(31, 27))
mySprite11 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.stop8)
tiles.placeOnTile(mySprite11, tiles.getTileLocation(41, 27))
mySprite12 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.stop9)
tiles.placeOnTile(mySprite12, tiles.getTileLocation(41, 23))
create_toolbar_and_inventory()
fill_inventory_with_food()
characterAnimations.loopFrames(
mySprite3,
[img`
    ......ffff......
    ....ffeeeeff....
    ...feeeffeeef...
    ..fffff66fffff..
    ..ffe6e66e6eff..
    ..fe6f6ff6f6ef..
    ..fff66ee66fff..
    .ffef6feef6feff.
    .feeffeeeefeeef.
    ..feeeeeeeeeef..
    ...feeeeeeeef...
    ..e4ffffffff4e..
    ..4df666666fd4..
    ..44f444444f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ....ffffffff....
    `,img`
    ......ffff......
    ....ffeeeeff....
    ...feeeffeeef...
    ..fffff66fffff..
    ..ffe6e66e6eff..
    ..fe6f6ff6f6ef..
    ..fff66ee66fff..
    .ffef6feef6feff.
    .feeffeeeefeeef.
    ..feeeeeeeeeef..
    ...feeeeeeee4e..
    ..e4ffffffffd4..
    ..4df666666f44..
    ..44f444444f....
    .....ffffff.....
    .....ff.........
    ................
    .....ff.........
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ....ffffffff....
    `,img`
    ......ffff......
    ....ffeeeeff....
    ...feeeffeeef...
    ..fffff66fffff..
    ..ffe6e66e6eff..
    ..fe6f6ff6f6ef..
    ..fff66ee66fff..
    .ffef6feef6feff.
    .feeffeeeefeeef.
    ..feeeeeeeeeef..
    ..e4eeeeeeeef...
    ..4dffffffff4e..
    ..44f666666fd4..
    ....f444444f44..
    .....ffffff.....
    .........ff.....
    ................
    .........ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ....ffffffff....
    `,img`
    ......ffff......
    ....ffeeeeff....
    ...feeeffeeef...
    ..fffff66fffff..
    ..ffe6e66e6eff..
    ..fe6f6ff6f6ef..
    ..fff66ee66fff..
    .ffef6feef6feff.
    .feeffeeeefeeef.
    ..feeeeeeeeeef..
    ...feeeeeeeef...
    ..e4ffffffff4e..
    ..4df666666fd4..
    ..44f444444f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ....ffffffff....
    `],
100,
characterAnimations.rule(Predicate.MovingUp)
)
characterAnimations.loopFrames(
mySprite3,
[img`
    ....ffffff......
    ...f6feeeeff....
    ..f666feeeeff...
    ..feeeeffeeef...
    .fe6666eeffff...
    .f6effff666ef...
    .fffeeefffffff..
    .fee44d8e44eff..
    ..feddf14d4eef..
    ...fdddd4eeef...
    ...fe444eeff....
    ...f666edd4.....
    ...f666edde.....
    ...f554feef.....
    ....ffffff......
    ......fff.......
    ................
    ......fff.......
    ....ffffff......
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ...fffffffff....
    ...ffffffffff...
    ..ffffffffffff..
    .fffffffffffff..
    .fffffffffffff..
    .ffffffffffff...
    .ffffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    ...fffffffff....
    `,img`
    ................
    ....ffffff......
    ...f6feeeeff....
    ..f666feeeeff...
    ..feeeeffeeef...
    .fe6666eeffff...
    .f6effff666ef...
    .fffeeefffffff..
    .fee44d8e44eff..
    ..feddd14d4eef..
    ...fdddeeeeef...
    ...fe4edd4f.....
    ...f66eddef.....
    ..ff55feefff....
    ..ffffffffff....
    ...fff...ff.....
    ................
    ...fff...ff.....
    ..ffffffffff....
    ..ffffffffff....
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffffff...
    ..ffffffffffff..
    .fffffffffffff..
    .fffffffffffff..
    .ffffffffffff...
    .ffffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    ...fffffffff....
    ....ffffff......
    `,img`
    ....ffffff......
    ...f6feeeeff....
    ..f666feeeeff...
    ..feeeeffeeef...
    .fe6666eeffff...
    .f6effff666ef...
    .fffeeefffffff..
    .fee44f8e44eff..
    ..feddf14d4eef..
    ...fdddd4eeef...
    ...fe444eeff....
    ...f666edd4.....
    ...f666edde.....
    ...f554feef.....
    ....ffffff......
    ......fff.......
    ................
    ......fff.......
    ....ffffff......
    ...ffffffff.....
    ...ffffffff.....
    ...ffffffff.....
    ...fffffffff....
    ...ffffffffff...
    ..ffffffffffff..
    .fffffffffffff..
    .fffffffffffff..
    .ffffffffffff...
    .ffffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    ...fffffffff....
    `,img`
    ................
    ....ffffff......
    ...f6feeeeff....
    ..f666feeeeff...
    ..feeeeffeeef...
    .fe6666eeffff...
    .f6effff666ef...
    .fffeeefffffff..
    .fee44f8e44eff..
    ..feddf14d4eef..
    ...fdddd4eeef...
    ...fe444edd4....
    ...f6666edde....
    ..ff5544feef....
    ..ffffffffff....
    ...fff...ff.....
    ................
    ...fff...ff.....
    ..ffffffffff....
    ..ffffffffff....
    ...fffffffff....
    ...fffffffff....
    ...fffffffff....
    ..fffffffffff...
    .fffffffffffff..
    .fffffffffffff..
    .fffffffffffff..
    .ffffffffffff...
    ..fffffffffff...
    ..fffffffffff...
    ...ffffffffff...
    ....ffffffff....
    `],
100,
characterAnimations.rule(Predicate.MovingLeft)
)
characterAnimations.loopFrames(
mySprite3,
[img`
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
    `,img`
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
    `,img`
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
    `,img`
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
    `],
100,
characterAnimations.rule(Predicate.MovingRight)
)
characterAnimations.loopFrames(
mySprite3,
[img`
    ......ffff......
    ....fff66fff....
    ...fff6666fff...
    ..fffeeeeeefff..
    ..ffe666666eef..
    ..fe6ffffff6ef..
    ..ffffeeeeffff..
    .ffef8d44d8feff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f666666f4e..
    ..4df666666fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ....ffffffff....
    `,img`
    ................
    ......ffff......
    ....fff66fff....
    ...fff6666fff...
    ..fffeeeeeefff..
    ..ffe666666eef..
    .ffe6ffffff6eff.
    .fffffeeeefffff.
    ..fef8d44d8fef..
    ..fe41dddd14ef..
    ...fe4dddd4efe..
    ..fef6666edd4e..
    ..e4f6666edde...
    ....f4455fee....
    .....ffffff.....
    .....ff.........
    ................
    .....ff.........
    .....ffffff.....
    ....ffffffff....
    ..fffffffffff...
    ..ffffffffffff..
    ...fffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ....ffffffff....
    ......ffff......
    `,img`
    ......ffff......
    ....fff66fff....
    ...fff6666fff...
    ..fffeeeeeefff..
    ..ffe666666eef..
    ..fe6ffffff6ef..
    ..ffffeeeeffff..
    .ffef8d44d8feff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444ee4e..
    ..e4f666666fd4..
    ..4df666666f44..
    ..44f445544f....
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ....ffffffff....
    `,img`
    ......ffff......
    ....fff66fff....
    ...fff6666fff...
    ..fffeeeeeefff..
    ..ffe666666eef..
    ..fe6ffffff6ef..
    ..ffffeeeeffff..
    .ffef8d44d8feff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ..e4ee4444eef...
    ..4df666666f4e..
    ..44f666666fd4..
    ....f445544f44..
    .....ffffff.....
    .........ff.....
    ................
    .........ff.....
    .....ffffff.....
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ..ffffffffffff..
    .ffffffffffffff.
    .ffffffffffffff.
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ..ffffffffffff..
    ...ffffffffff...
    ....ffffffff....
    `],
100,
characterAnimations.rule(Predicate.MovingDown)
)
characterAnimations.loopFrames(
mySprite3,
[img`
    ......ffff......
    ....fff66fff....
    ...fff6666fff...
    ..fffeeeeeefff..
    ..ffe666666eef..
    ..fe6ffffff6ef..
    ..ffffeeeeffff..
    .ffef8d44d8feff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f666666f4e..
    ..4df666666fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    ...fffffffffff..
    ..fffffffffffff.
    ..fffffffffffff.
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    .....fffffff....
    `,img`
    ......ffff......
    ....fff66fff....
    ...fff6666fff...
    ..fffeeeeeefff..
    ..ffe666666eef..
    ..fe6ffffff6ef..
    ..ffffeeeeffff..
    .ffef8d44d8feff.
    .fee41dddd14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f666666f4e..
    ..4df666666fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    ...fffffffffff..
    ..fffffffffffff.
    ..fffffffffffff.
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    .....fffffff....
    `,img`
    ......ffff......
    ....fff66fff....
    ...fff6666fff...
    ..fffeeeeeefff..
    ..ffe666666eef..
    ..fe6ffffff6ef..
    ..ffffeeeeffff..
    .ffef8f44f8feff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f666666f4e..
    ..4df666666fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    ...fffffffffff..
    ..fffffffffffff.
    ..fffffffffffff.
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    .....fffffff....
    `,img`
    ......ffff......
    ....fff66fff....
    ...fff6666fff...
    ..fffeeeeeefff..
    ..ffe666666eef..
    ..fe6ffffff6ef..
    ..ffffeeeeffff..
    .ffef8f44f8feff.
    .fee41fddf14eef.
    ..feeddddddeef..
    ...fee4444eef...
    ..e4f666666f4e..
    ..4df666666fd4..
    ..44f445544f44..
    .....ffffff.....
    .....ff..ff.....
    ................
    .....ff..ff.....
    .....ffffff.....
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    ...fffffffffff..
    ..fffffffffffff.
    ..fffffffffffff.
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ...fffffffffff..
    ....fffffffff...
    .....fffffff....
    `],
100,
characterAnimations.rule(Predicate.NotMoving)
)
mySprite3.follow(mySprite5, 10)
let sprite_count = 10
game.onUpdate(function () {
    let game_crash = 0
    if (game_crash) {
        game.showLongText("Adventure World is automatically restarting ", DialogLayout.Bottom)
        game.reset()
    }
})
game.onUpdate(function () {
    if (xy_viewing) {
        mySprite.sayText("X " + ("" + Math.round(mySprite.x)) + " Y" + ("" + Math.round(mySprite.y)))
    }
})
game.onUpdateInterval(50000, function () {
    let harpie_spawing = 0
    let goblin_spawning = 0
    if (dragon_spawning) {
        mySprite15 = sprites.create(list2._pickRandom(), SpriteKind.tamable_dragons)
        mySprite15.setPosition(randint(0, 255), randint(0, 255))
        dragon_amount += 1
    }
    if (goblin_spawning) {
        mySprite13 = sprites.create(img`
            ................
            ................
            ................
            .....66.66......
            ....f6666666....
            ...f667667666...
            ..f677777777ff..
            ..6617771777ff..
            ..6777777776fff.
            ..671ff1677ffff.
            ..67fffff766f...
            ..67fffff7f6f...
            ..67222226f7f...
            ...722222666f...
            ....77777ff6f...
            ....fffffffff...
            ....77766766....
            ...7766677766f..
            ...76f7777776f..
            ...76f7777776f..
            ..776f7777776f..
            ..666f7777666f..
            ..666f7777666f..
            ..ffff7777ffff..
            ....77777777f...
            ....77777777f...
            .....76fff76f...
            .....76fff76f...
            .....76fff76f...
            ..77776f7776f...
            ..fffffffffff...
            ..fffffffffff...
            `, SpriteKind.goblin)
        mySprite13.follow(mySprite)
        goblin_amount += 1
        tiles.placeOnTile(mySprite13, tiles.getTileLocation(randint(100, 10), randint(100, 10)))
    }
    if (harpie_spawing) {
        mySprite18 = sprites.create(img`
            ..................
            ..................
            ..................
            ...222.2222.222...
            ..22222222222222..
            ..2222b2222b2222..
            ..22224222242222..
            ...244222222442...
            ...222224422222...
            ...222244442222...
            ...222ef44fe222...
            ...2241fddf1422...
            ....22dddddd22....
            ......e4ee4e......
            .....e444444e.....
            ...2e44422e44e2...
            ...24442222e442...
            ..224442222e4422..
            .2224e222222e4222.
            .2224e222222e4222.
            .2224e222222e4222.
            .2224effffffe4222.
            .2224effffffe4222.
            .2224444ff4444222.
            .2224e4eff4e4e222.
            .22.ffff..ffff.22.
            .2..ffff..ffff..2.
            ...ffff..ffff.....
            ...fff...fff......
            ...ff....ff.......
            ..ff....ff........
            .ff....ff.........
            `, SpriteKind.Harpie)
        mySprite18.follow(mySprite)
        harpie_amount += 1
        tiles.placeOnTile(mySprite18, tiles.getTileLocation(randint(100, 10), randint(100, 10)))
    }
})
game.onUpdateInterval(100, function () {
    if (inside_mud_home) {
        mySprite14.setPosition(randint(0, 32), randint(0, 32))
    }
})
game.onUpdateInterval(100, function () {
    statusbar.value += 2
})
