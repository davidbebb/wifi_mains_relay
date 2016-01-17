
# Tab length compensation a negative number will increase the gap between the tabs
#  a fudge factor that increases the gap along the finger joint when negative - it should be 1/4 of the gap you want

fudge=0.1

thickness=3

#
box_width=60
box_height=15
box_depth = 25

cutter='laser'

tab_length=5

centre = V(0,0)

module = camcam.add_plane(Plane('plane',cutter=cutter))

Lbottom=module.add_layer('bottom', material='perspex', thickness=thickness, z0=0, zoffset=-thickness-box_depth)
Lbottom=module.add_layer('top', material='perspex', thickness=thickness, z0=0, zoffset=-thickness-box_depth)
Lbottom=module.add_layer('back', material='perspex', thickness=thickness, z0=0, zoffset=-thickness-box_depth)
Lbottom=module.add_layer('side', material='perspex', thickness=thickness, z0=0, zoffset=-thickness-box_depth)

back_border=FingerJointBoxSide(
    centre,
    box_width,
    box_height,
    'in',
    corners={'left':'off',
            'top':'off',
            'right':'off',
            'bottom':'off'},
    sidemodes={},
    tab_length=tab_length,
    thickness=thickness,
    cutterrad=0,
    cutter=cutter,
    centred=True,
    fudge=fudge,
    auto=True
)

back=module.add_path(Part(name='back', border=back_border, layer='back'))
back.number=2


bottom_border = FingerJointBoxSide( centre,
                                    box_width,
                                    box_depth,
                                    'in',
                                    corners={   'left':'off',
                                                'top':'on',
                                                'right':'off',
                                                'bottom':'on'},
                                    sidemodes={},
                                    tab_length=tab_length,
                                    thickness={ 'left':thickness,
                                                'right':thickness,
                                                'bottom':thickness,
                                                'top':thickness},
                                    cutterrad=0,
                                    cutter=cutter,
                                    centred=True,
                                    fudge=fudge,
                                    auto=True
                                    )

top=module.add_path(Part(name='top', border=bottom_border,  layer='top'))

bottom=module.add_path(
    Part(name='bottom',
        border=bottom_border,
        layer='bottom'
    )
)


side = module.add_path(
    Part(name='side',
	    border = FingerJointBoxSide(
            centre,
            box_depth,
            box_height,
            'in',
            corners={'left':'on',
                     'top':'on',
                     'right':'on',
                     'bottom':'on'},
            sidemodes={},
            tab_length=tab_length,
            thickness ={'left':thickness,
                        'right':thickness,
                        'bottom':thickness,
                        'top':thickness},
            cutterrad=0,
            cutter=cutter,
            centred=True,
            fudge=fudge,
            auto=True
            ),
        layer='side'
        ),
	layers='side'
)

side.number=2
