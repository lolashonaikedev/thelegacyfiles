try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

RenderView1 = GetRenderView()
Tube1 = GetActiveSource()
DataRepresentation5 = GetDisplayProperties(Tube1)
RenderView1.CameraViewUp = [0.5303820756110584, 0.8426282049287047, 0.09312659195490001]
RenderView1.CameraFocalPoint = [328.6856722804005, 552.9045781558367, 2083.1583421976225]
RenderView1.CameraClippingRange = [2786.6952480051514, 3524.7006631813465]
RenderView1.CameraPosition = [195.6528163168024, 526.1099747873246, 3083.2607710906573]

DataRepresentation5.ColorArrayName = ''

Render()
