/* setup function extracts data from file and grabs unique values */

/*************** GLOBAL VARIABLES **********************************/
ArrayList<String> toolList;
ArrayList<Integer> countList;
ArrayList<String> actionList;
ArrayList<ArrayList<Integer>> actioncountList;
PFont f;
ArrayList<String> toolLog;
ArrayList<Integer> studentLog;
ArrayList<Integer> sidList;
ArrayList<Integer> dayspassedList;
//ArrayList<ArrayList<String>> timelineData;

/******************************************************************/


/*---------- START SETUP FUNCTION ----------------------------------*/
void setup() {

  size(2300, 800, P3D);
  noStroke();

  toolList = new ArrayList<String>();
  countList = new ArrayList<Integer>();
  actioncountList = new ArrayList<ArrayList<Integer>>();
  actionList = new ArrayList<String>();
  toolLog = new ArrayList<String>();
  studentLog = new ArrayList<Integer>();
  sidList = new ArrayList<Integer>();
  dayspassedList = new ArrayList<Integer>();
  //timelineData = new ArrayList<ArrayList<String>>();


  importTextFile();

  f = createFont("Helvetica", 15);
  //noLoop();
}
/*---------- END SETUP FUNCTION ------------------------------------*/


/*---------- START IMPORTTEXTFILE FUNCTION ------------------------*/

void importTextFile() {

  /*======= READ DATA FILE ====================================*/
  String[] strLines = loadStrings("AlienLogData.csv");
  int totData = strLines.length-1;
  int[] arrSid = new int[totData];          //student id
  //int[] arrCid = new int[totData];          //class period id
  int[] arrMonth = new int[strLines.length];        //month
  int[] arrDay = new int[strLines.length];          //day
  //int[] arrHour = new int[strLines.length];         //hour
  //int[] arrMinute = new int[strLines.length];       //minute
  String[] arrTool = new String[totData];   //tool-represents software functions
  String[] arrAction = new String[totData]; //action-represents student enering/leaving/sub-functions
  String[] arrStamp = new String[totData];  //full timestamp for each entry as a string entry
  String[] TSID = new String[totData];
  IntList tesid = new IntList(totData);
  StringList stringAction = new StringList(totData);
  StringList stringTool = new StringList(totData);
   for (int i=1; i<strLines.length; i++) 
  {
   String[] tokens = split(strLines[i], ',');
   String tsid = tokens[0];
   String tool = tokens[1];
   TSID[i-1] = tsid;
   stringAction.append("open");
   stringTool.append(tool);
  }
 
  int count;
  count = 1;
  for (int i=0; i<TSID.length; i++) 
  {
   if (i < TSID.length-1){
     if (TSID[i+1].equals(TSID[i])){
       tesid.append(count);
       append(arrSid,count);
     }
     else{
       count +=1;
       tesid.append(count);
        append(arrSid, count);
     }
   }
   else{
    tesid.append(count);
    append(arrSid, count);
  }
  }
 
  
  //print(tesid.get(5));

  for (int i=1; i<strLines.length; i++) 
  {

    String[] arrTokens = split(strLines[i], ','); 
    //int sid = tesid.get(i);
    //int cid = int(arrTokens[2]);
    String tool = arrTokens[1];
    String action = arrTokens[1];

    String[] arrTime1 = split(arrTokens[2], '/');
    String[] arrTime2 = split(arrTime1[2], ' ');
    String[] arrTime3 = split(arrTime2[1], ':');
    arrStamp[i-1] = arrTokens[2];       //takes in the entire timestamp as a string
    arrMonth[i-1] = int(arrTime1[0]);   // month of timestamp as int
    arrDay[i-1] = int(arrTime1[1]);     // day of timestamp as int
    //arrHour[i-1] = int(arrTime3[0]);    // hour of timestamp as int
    //arrMinute[i-1] = int(arrTime3[1]);  // minute of timestamp as int

    //arrSid[i-1] = sid;
    //arrCid[i-1] = cid;
    arrTool[i-1] = tool;
    arrAction[i-1] = action;
  }

  //print(arrStamp.length);
  /*======== MAKE ARRAY OF DAYS PASSED SINCE START OF PROJECT ============*/
  int daycount = 0;
  for (int i=0;i<arrDay.length; i++) {
    if (i==0) {dayspassedList.add(i,daycount++);}
    if (i>0) { 
      if (arrDay[i-1] != arrDay[i]) {
        dayspassedList.add(i, daycount++);
      }
      else { dayspassedList.add(i, daycount);}
    }
  }
    

  /*========EXTRACT UNIQUE VALUES FROM DATA FILE================ */
  int[] arrUnSid = new int[totData];          // unique student ids in datafile
  int[] arrUnCid = new int[totData];          // unique class ids in datafile
  String[] arrUnTool = new String[totData];   // unique tool names in datafile
  String[] arrUnAction = new String[totData]; // unique action names in datafile
  int i, j, k;
  int ctest = 0;


  /************************ Extract unique values of TOOLS *****************************/
  arrUnTool = stringTool.getUnique();
  int totalk = arrUnTool.length;
  print(totalk);
  print(arrUnTool);
  
  /*----------- Count how many times a particular tool is logged --------------- */
  int[] arrUnToolCount = new int[totalk];     // counts how many times a unique tool is logged
  String[] arrUnToolNew = new String[totalk]; // copies values of unique tool names to a variable of the correct size

  for (i=0; i<totalk; i++) 
  {
    arrUnToolCount[i] = 0;
    arrUnToolNew[i] = arrUnTool[i];
  }

  for (i=0; i<totalk; i++)
  {
    for (j=0; j<arrTool.length; j++) 
    {
      if (arrUnTool[i].equals(arrTool[j]))
      {
        arrUnToolCount[i]++;
      }
    }
  }

  /*-------------- Copy unique tool count variable to gloal array list --------------*/
  for (i=0; i<arrUnToolNew.length; i++) {
    toolList.add(i, arrUnToolNew[i]);
    countList.add(i, arrUnToolCount[i]);
  }

  /*=========*/

  /**************************  Extract unique values of ACTIONS  ******************************/
  arrUnAction = stringAction.getUnique();
  int totalaction = arrUnAction.length;

  int [][] arrActionperTool = new int[arrUnToolNew.length][totalaction];   // the rows are the unique values of tools, in the same order 
  // as in the array arrUnToolNew. the cols are the unique values of actions,
  // in the same order as the variable arrUnAction.


  /*----------------- Count how many times an action is logged per tool------------------------ */
  for (i=0; i<arrUnToolNew.length; i++) {
    for (j=0; j<arrTool.length-1; j++) {
      if (arrTool[j].equals(arrUnToolNew[i])) {
        for (k=0; k<totalaction; k++) {
          if (arrAction[j].equals(arrUnAction[k])) {
            arrActionperTool[i][k]++;
          }
        }
      }
    }
  }

  /*-------------- Copy unique tool names and respective counts to gloal array list --------------*/
  for (i=0; i<arrUnToolNew.length; i++) {
    actioncountList.add(new ArrayList<Integer>());
    for (j=0; j<totalaction; j++) {
      actioncountList.get(i).add(j, arrActionperTool[i][j]);
    }
  }
  for (j=0; j<totalaction; j++) {
    actionList.add(j, arrUnAction[j]);
  }


  /******************************** Extract unique values of SID *************************************/
  for (i=0,k=-1,j=i+1;j<arrSid.length-1;j++)
  {
    if (k==-1) {
      k++;
      arrUnSid[k] = tesid.get(i);
      //print(4);
    }
    for (int n=0; n<arrUnSid.length; n++)
    {
      if (tesid.get(j) == arrUnSid[n]) {  
        ctest = 1;
        break;
      }
      else {
        ctest = 0;
      }
    }
    if (ctest ==  1) {
      continue;
    } 
    k++;
    arrUnSid[k]=tesid.get(j);      // if they are not equal then b[k++] is equal to the repeating value
    i=j;                          // assign i==j to start from the end of the repeating elemnet 
}
  
  int totalSid = k+1;               //total unique values- don't delete this or put anything before it!

  /*-------------- Copy unique SID values to global array list ---------------------------------------*/
  for (j=0; j<totalSid; j++) {
    sidList.add(j, arrUnSid[j]);
  }


  /*-------------- Copy tools log to gloal array list --------------*/
  for (j=0; j<arrTool.length; j++) {
    toolLog.add(j, stringTool.get(j));
  }  

  /*-------------- Copy student ID log to gloal array list --------------*/
  for (j=0; j<arrSid.length; j++) {
    studentLog.add(j, tesid.get(j));
  }  
  
print(arrUnSid);
}

/*---------- END IMPORTTEXTFILE FUNCTION -----------------------------------------------------------*/
/*------------------------------------------------------------------------------------------------*/


/*------------------------------------------------------------------------------------------------*/
/*---------------------- START DRAW FUNCTION -----------------------------------------------------------*/

/* At some point, move to PShapes to speed up drawing. Otherwise your sketch may be REALLY slow*/
void draw() {

  background(250);
  //background(255,255,255);
  lights();

  /*========= Extract unique tools, actions, and respective counts from arraylists ============*/
  String arrUnTool[] = new String[toolList.size()];
  Integer arrUnToolCount[] = new Integer[countList.size()];
  String arrUnAction[] = new String[actionList.size()];
  Integer arrActionperTool[][] = new Integer[toolList.size()][actionList.size()];
  String arrTool[] = new String[toolLog.size()];
  Integer arrSid[] = new Integer[studentLog.size()];
  Integer arrUnSid[] = new Integer[sidList.size()];
  Integer arrDaysPassed[] = new Integer[dayspassedList.size()];
  String arrUnDecisions[] = new String[arrUnSid.length];
 
  arrUnTool = toolList.toArray(arrUnTool);
  arrUnToolCount = countList.toArray(arrUnToolCount);
  arrUnAction = actionList.toArray(arrUnAction);
  arrTool = toolLog.toArray(arrTool);
  arrSid = studentLog.toArray(arrSid);
  arrUnSid = sidList.toArray(arrUnSid);
  arrDaysPassed = dayspassedList.toArray(arrDaysPassed);

  //... find max values of arrUnSid (unique sid array) ...//
  int maxSid = arrUnSid[0];
  for (int i=1; i<arrUnSid.length; i++) {
    if (maxSid < arrUnSid[i]) 
    {
      maxSid = arrUnSid[i];
    }
  }
  //println(maxSid);
  //println(arrSid.length);
  print(maxSid);
  
  for (int i=0; i<toolList.size(); i++) {
    ArrayList<Integer> temp = actioncountList.get(i);
    for (int j=0; j<actionList.size(); j++) {
      arrActionperTool[i][j] = temp.get(j);
      // println(temp.get(j));
    }
  }


  float reldist = width/arrUnTool.length;
  int rect_width = 100;
  int rect_height = 55;
  int rect_x, rect_y;
  float startx, starty, endx, endy;


  // Make color wheel
  color[] colorOptions = new color[arrUnTool.length];
  colorOptions[0] = #91C772;
  colorOptions[1] = #BCC772;
  colorOptions[2] = #758B43;
  colorOptions[3] = #C7A872;
  colorOptions[4] = #C77291;
  colorOptions[5] = #C772BC;
  colorOptions[6] = #A872C7;
  colorOptions[7] = #7E72C7;
  colorOptions[8] = #7291C7;
  colorOptions[9] = #72BCC7;
 // colorOptions[10] = #72C7A8;
 // colorOptions[11] = #72C77E;
 // colorOptions[12] = #438B59;
  
  /**************************************************/

  int cnt = -1;
  float vspace = float(height)/float(arrUnTool.length);
  float tool_heights[] = new float[arrUnTool.length];
  print(arrUnTool.length);
  // start drawing, first setup the axes
  int toolcntr = 0;
  for (int i=0; i<arrUnTool.length; i++) {

    // draw Tool Text lines in order of first appearance
    //String tool = arrUnTool[i];
    //fill(colorOptions[i]);
    fill(0);
    textFont(f, 18);
    PVector pos1 = new PVector(0,0);

    pos1.x = 50;     // sets spacing for x-axis between decisions
    pos1.y = height*0.8 - (toolcntr+1)*(vspace*0.7);  //sets spacing for y-axis between tools
    tool_heights[i] = pos1.y;
    toolcntr++;

    // draws the axes
    text(arrUnTool[i], 50.0, tool_heights[i]); //text,x,y,width,height
    if (i==0) {
      text("Chronological Order of Unique Decisions", width/2, tool_heights[0]+45);
    }
    noFill();
    stroke(0);
    strokeWeight(0.86);
    line(50, pos1.y+2, 0, width-50, pos1.y+2, 0);
    //line(50, tool_heights[0]+50, width-50, tool_heights[0]+50);
    
  }

  // NOW plot the UNIQUE tools accessed by each student
  // make an array to count most used tools at each decision instant
  int min_decisions = 0;
  int max_decisions = 400;
  Integer arrMostUsedTools[][] = new Integer[max_decisions+1][arrUnTool.length];
  for (int m=0; m<max_decisions+1; m++) {  //initialize 2d array
    for (int n=0; n<arrUnTool.length; n++) {
      arrMostUsedTools[m][n] = 0;
    }
  }
  
  for (int i=0; i<arrUnSid.length; i++){
    ArrayList<Float> tmpheight = new ArrayList<Float>(); // for sid i, make a tmpheight vector so you can draw lines
    int count = -1;  // counts the number of decisions student i takes   
    for (int j=0; j<arrSid.length; j++) {
      if (arrSid[j].equals(arrUnSid[i])) {
        if (count<0) {
          for (int n=0; n<arrUnTool.length; n++) {
            if (arrTool[j].equals(arrUnTool[n])){
              count++;
              tmpheight.add(count,tool_heights[n]); } } }
        if (count>=0) {
          for (int n=0; n<arrUnTool.length; n++) {
            if (arrTool[j].equals(arrUnTool[n])) {
              if (tmpheight.get(count)!=tool_heights[n]){ // this line forces you to only grab unique clicks of tools
                                                         // (so if the same tool was clicked twice, it won't be recorded in tmpheight 
                count++;
                tmpheight.add(count,tool_heights[n]); } 
              } } }
      }
      //println(count);
    }
    arrUnDecisions[i] = Integer.toString(count);
    //println(count);
    
    // here, limiting the counting values weeds out students. so basically, now we plot students who only make 45-55 decisions or 85-100 decisions.   
    if ((count>max_decisions)||(count<min_decisions)) {   
      continue;
    }
    
    //println(i);
  
    // now make a plotData matrix to draw lines      
    float plotData[][] = new float[count+1][2];
    int start_dec = 0;
    int end_dec = 400; // what range of decisions to plot
    //for (int j=0; j<count+1; j++) {   
    for (int j=start_dec; j<end_dec; j++) {
      if (j>=count+1) {break;}
      plotData[j][0] = 8*(j-start_dec) + 200;   //first col is x-coord, this determines the distance between successive decisions on the plot 
      plotData[j][1] = tmpheight.get(j)+2;       //second col is y-coord
      for (int m=0; m<arrUnTool.length; m++){ //count how many times a tool is used for all students in the range of min_decisions<count<max_decisions
        if (tmpheight.get(j)==tool_heights[m]) {
          arrMostUsedTools[j][m] += 1;
        }
      }
    }
    noFill();
    stroke(50,50); //stroke(grayscale,opacity)
    strokeWeight(1.7);
    //for (int j=0; j<count+1; j++) {
    for (int j=start_dec; j<end_dec; j++) {
      if (j>=count) {break;}  
      if (j>end_dec-2) { break;}
      line(plotData[j][0], plotData[j][1], plotData[j+1][0], plotData[j+1][1]); //line(x1,y1, x2, y2)
    }
    
  } 
  
  // Now plot the Most Used Tools
  float plotMostUsedTools[][] = new float[max_decisions+1][3]; //x-axis, y-axis, opacity
  int max_value = 0;
  int max_index = 0;
  for (int m=0; m<max_decisions+1; m++) { // from rows 0 to max_decisions
    for (int n=0; n<arrUnTool.length; n++) {
      if (arrMostUsedTools[m][n] > max_value) {
        max_value = arrMostUsedTools[m][n];
        max_index = n;
      }
    }
    println(m);
    println(max_value);
    //println(max_index);
    plotMostUsedTools[m][0]=8*m + 200; 
    plotMostUsedTools[m][1]=tool_heights[max_index];
    plotMostUsedTools[m][2]=max_value*10; // play around with opacity of the most used line
    max_value = 0; //reset max_value
    max_index = 0; //reset index
  }
  for (int j=0; j<max_decisions+1; j++) { 
    if (j>max_decisions-2) { break;}
    stroke(#293FFC); //stroke(grayscale,opacity)
    strokeWeight(2.5);
    line(plotMostUsedTools[j][0], plotMostUsedTools[j][1], plotMostUsedTools[j+1][0], plotMostUsedTools[j+1][1]); //line(x1,y1, x2, y2)
  }
  
  // make x-axis label
  //int mm = 0 ;
  for (int j=0; j<max_decisions+1; j++) { 
    //mm = mm + 10;
    stroke(0);
    strokeWeight(1.0);
    line(plotMostUsedTools[j][0], tool_heights[0]-3, plotMostUsedTools[j][0], tool_heights[0]+3); //line(x1,y1, x2, y2)
    fill(0);
    textFont(f, 11);
    if (max_decisions>100) {
      if ((j==0)||(j==50)||(j==100)||(j==150)||(j==200)||(j==250)) {text(j, plotMostUsedTools[j][0], tool_heights[0]+15);}
    }
    else {
      text(j, plotMostUsedTools[j][0], tool_heights[0]+15); 
    }
  }
      
      
  
  // save the sketch as an image
  /* 1. */
  /*
  textFont(f,18);
  text("Decision History for Students Completing Task within 45-55 Unique Tool Clicks", width/2.5, 50);
  save("45-55decisions.jpg");
  */
  
  /* 2. */
  /*
  textFont(f,18);
  text("Decision History for Students Completing Task within 85-100 Unique Tool Clicks", width/2.5, 50);
  save("85-100decisions.jpg");
  */
  
  /* 3. */
  /*
  textFont(f,18);
  text("Decision History for Students Completing Task within 100 Unique Tool Clicks", width/2.5, 50);
  save("0-100decisions.jpg");
  */
  
  /* 4. */
  
  textFont(f,18);
  text("Decision History for All Students (Unique Tool Clicks)", width/2.5, 50);
  save("Alldecisions_v2.jpg");
  
  
  
  saveStrings("NumUnDecisions.txt", arrUnDecisions);
  String arrUnSidstring[] = new String[arrUnSid.length];
  for (int m = 0; m<arrUnSid.length; m++) {
    arrUnSidstring[m] = Integer.toString(arrUnSid[m]);
  }
  saveStrings("UniqueSids.txt", arrUnSidstring);
  
}
/*---------------------- END DRAW FUNCTION -----------------------------------------------------------*/
/*----------------------------------------------------------------------------------------------------*/


/*-------- START DRAW ARROW FUNCTION -----------------*/

void drawArrow(float cx, float cy, float len, float angle) {
  pushMatrix();
  translate(cx, cy);
  rotate(radians(angle));
  line(0, 0, len, 0);
  line(len, 0, len - 8, -8);
  line(len, 0, len - 8, 8);
  popMatrix();
  //noLoop();
}
/*-------- END DRAW ARROW FUNCTION -----------------*/

          










