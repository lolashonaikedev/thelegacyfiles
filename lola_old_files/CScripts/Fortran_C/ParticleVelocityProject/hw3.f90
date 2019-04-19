
xypair function updatePosition(vel,par)
type::xypair
 real*8::x,y,z
end type
type(xypair)::answer(:)

real*8::posx,posy,posz
posx=par%x+vel(par%x,par%y,par%z)%x
posy=par%y+vel(par%x,par%y,par%z)%y
posz=par%z+vel(par%x,par%y,par%z)%z
par%x=floor(posx)
par%y=floor(posy)
par%z=floor(posz)
answer%x=par%x
answer%y=par%y
answer%z=par%z
updatePosition=answer
return 
end

program arguments
  implicit none
  type::xypair
   real*8::x,y,z
  end type
  integer::num_arguments,i,j,k,num_ts,num_particles
  real*8 ::posx, posy,posz
  type(xypair),allocatable::par(:)
  type(xypair),allocatable::vel(:,:,:)
  character(200)::buffer,outfile_basename,vel_file,part_file
  num_arguments = NARGS()
  
  if (num_arguments > 1) THEN
   CALL GETARG(1,buffer)
   CALL GETARG(2,outfile_basename)
   CALL GETARG(3,vel_file)
   CALL GETARG(4,part_file)  
   read(buffer,*)num_ts
   open(1000,file=part_file)
   open(2000,file=vel_file)
   outfile_basename="results"
  else
    open(1000,file='particles.dat')
    open(2000,file='velocity.dat')
    num_ts=50
    outfile_basename="results"
   
  end if
  read(1000,*)num_particles
  allocate(par(num_particles))
  allocate(vel(0:num_particles,0:num_particles,0:num_particles))
  do i=1,num_particles
   read(1000,*)par(i)
  end do
  do i=0,num_particles
      read(2000,*),vel(i,:,:)
  end do
  do j=0,num_ts
  do i=0,num_particles
    par(i)= updatePosition(vel,par(i))
  end do
  end do
end program
