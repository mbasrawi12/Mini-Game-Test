transform half_size:
    zoom 0.5

transform chest_transform:
    zoom 0.5
    anchor (0.5,0.5)
    align (0.5,0.7)
    subpixel True
    on hover:
        easin 1.0 zoom 0.51
    on idle:
        easin 1.0 zoom 0.5

transform chest_unlock_anim:
    zoom 0.5
    alpha 0.0
    parallel:
        easin 3.0 zoom 0.7
    parallel:
        easin 2.0 alpha 1.0

screen chest_puzzle:
    image "background.png" at half_size
    if not chest_unlocked:
        image "chest-closed-idle.png" align (0.5,0.7) at half_size
    else:
        image "chest-opened.png" align (0.5,0.7)

screen scene_1:
    image "background.png" at half_size
    imagebutton auto "chest-closed-%s.png" action [Hide("scene_1"), Show("chest_puzzle")] at chest_transform

label start:
    $chest_unlocked = False
    $chest_unlocked_tries = 2
    call screen scene_1
    start
