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

screen chest_puzzle:
    ##TIME STAMP: 8:39 find link in description

screen scene_1:
    image "background.png" at half_size
    imagebutton auto "chest-closed-%s.png" action [Hide("scene_1"), Show("chest_puzzle")] at chest_transform

label start:
    call screen scene_1
    start
