class star { 


  int xPos, yPos, starSize; 


  float flickerRate, light; 


  boolean rise; 


  star(){ 


    flickerRate = random(2,5);  


    starSize = int(random(2,5)); 


    xPos = int(random(0,1500 - starSize)); 


    yPos = int(random(0,700 - starSize)); 


    light = random(10,245); 


    rise = true; 


  } 


  void display(){ 


    if(light >= 245){ 


      rise = false; 


    } 


    if(light <= 10){ 


      flickerRate = random(2,5); 


      starSize = int(random(2,5)); 


      rise = true; 


      xPos = int(random(0,1500 - starSize)); 


      yPos = int(random(0,700 - starSize)); 


    } 


    if(rise == true){ 


      light += flickerRate; 


    } 


    if(rise == false){ 


      light -= flickerRate; 


    } 


    fill(light); 


    rect(xPos, yPos,starSize,starSize); 


  } 


} 
