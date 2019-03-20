import visit_writer, struct

NX=72
NY=72
NZ=72


npts=NX*NY*NZ


#print type(xcoord_data)
#print len(xcoord_data)

#coords_format = "'"+`npts`+"f"+"'"
#print x_format
#debug later want to replace the hardcoded 373248f with coords_format

#for a rectilinear grid is the xcoord file alll the xcoords or is it xyz, xyz... of the x axis

xcoord_file = open("/Users/adb/Documents/Collaborations/HortonWendel/Visualization.DD/DDevil.xcoord.050.dat", "rb")
xcoord_data = xcoord_file.read() 
x_grid = struct.unpack('>72f',xcoord_data[0:4*72])


ycoord_file = open("/Users/adb/Documents/Collaborations/HortonWendel/Visualization.DD/DDevil.ycoord.050.dat", "rb")
ycoord_data = ycoord_file.read() 
y_grid = struct.unpack('>72f',ycoord_data[0:4*72])


zcoord_file = open("/Users/adb/Documents/Collaborations/HortonWendel/Visualization.DD/DDevil.zcoord.050.dat", "rb")
zcoord_data = zcoord_file.read()
#print len(zcoord_data)
z_grid = struct.unpack('>72f',zcoord_data[0:4*72])


#xyz_grid = list(chain.from_iterable(izip(x_grid,y_grid,z_grid)))


p_file = open("/Users/adb/Documents/Collaborations/HortonWendel/Visualization.DD/DDevil.pressu.050.dat", "rb") 
p_data = p_file.read() 

#print len(p_data)
p = struct.unpack('>373248f',p_data[0:4*373248])




bx_file = open("/Users/adb/Documents/Collaborations/HortonWendel/Visualization.DD/DDevil.veloc1.050.dat", "rb") 
bx_data = bx_file.read() 
bx = struct.unpack('>373248f',bx_data[0:4*npts])

by_file = open("/Users/adb/Documents/Collaborations/HortonWendel/Visualization.DD/DDevil.veloc2.050.dat", "rb") 
by_data = by_file.read() 
by = struct.unpack('>373248f',by_data[0:4*npts])

bz_file = open("/Users/adb/Documents/Collaborations/HortonWendel/Visualization.DD/DDevil.veloc3.050.dat", "rb") 
bz_data = bz_file.read() 
bz = struct.unpack('>373248f',bz_data[0:4*npts])

b_vec = [y for x in map(None,bx,by,bz) for y in x if y is not None]





			
# Pass data to visit_writer to write a binary VTK file.
dims = (NX, NY, NZ)
vars = (("bvec", 3, 1, b_vec), ("pressure", 1, 1, p))
visit_writer.WriteRectilinearMesh("DD_50_lRGE.vtk", 0, x_grid,y_grid,z_grid, vars)
			
			
			
			

#read in data from external file x Run565sm90.xcoord
# y Run565sm90.ycoord
# z Run565sm90.zcoord
