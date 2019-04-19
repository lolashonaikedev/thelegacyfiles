

program arguments 
 use myModule
 implicit none
   type::xypair
   real*8::x,y,z
  end type
  integer::num_arguments,i,j,k,num_ts,num_particles,numDim
  real*8 ::posx, posy,posz
  type(xypair),allocatable::par(:)
  type(xypair),allocatable::vel(:,:,:)
  character(200)::buffer,outfile_basename,vel_file,part_file,stepStr
  num_arguments = NARGS()
  
  if (num_arguments > 1) THEN
   CALL GETARG(1,buffer)
   CALL GETARG(2,outfile_basename)
   CALL GETARG(3,vel_file)
   CALL GETARG(4,part_file)  
   read(buffer,*)num_ts
   open(1000,file=part_file)
   open(2000,file=vel_file)
  ! outfile_basename="results"
  else
    open(1000,file='particles.dat')
    open(2000,file='velocity.dat')
    num_ts=50
    outfile_basename="results"
   
  end if
  read(1000,*)num_particles
  numDim=num_particles -1
  allocate(par(num_particles))
  allocate(vel(0:numDim,0:numDim,0:numDim))
  do i=1,num_particles
   read(1000,*)par(i)
  end do
  do i=0,numDim
   do j=0,numDim
    read(2000,*),vel(j,i,:)
  end do
  end do
  do j=1,num_ts
    if (j+1 /10==0) then
   write(stepStr,'(I4)') j
   outfile_basename=outfile_basename//stepStr
   open(3000,file=outfile_basename)
  do i=1,num_particles
    par(i)= updatePosition(vel,par(i))
    write(3000,*),"t=",j,"p=",i,":(",par(i)%x,par%y,par(i)%z,")"
  end do
  end if
  end do
   

end program

