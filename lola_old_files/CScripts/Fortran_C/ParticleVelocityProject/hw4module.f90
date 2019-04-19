module myModule
contains
   type(xypair) function updatePosition(vel,par)
     real*8::posx,posy,posz
     type(xypair)::vel(0:,0:,0:),par,answer
     answer%x=par%x+vel(floor(par%x),floor(par%y),floor(par%z))%x
     answer%y=par%y+vel(floor(par%x),floor(par%y),floor(par%z))%y
     answer%z=par%z+vel(floor(par%x),floor(par%y),floor(par%z))%z
     updatePosition=answer
   end function

end module