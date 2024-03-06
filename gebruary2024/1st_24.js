


osc(12,0,[0,.5].smooth())
.mult(osc().rotate(1.5), .2)
.modulateScale(voronoi().modulate(noise(500),.4), .3)
.modulate(noise([.4,2].smooth()),.6)
.mult(solid(.1,.1,.2), [.5,1.2].smooth())
.out()
speed=.1
