// ok so my goal is to make a small program that selects a student and prints out some data
//depending on who u pick. it must have a ver # and warnings
//the categories are: clearance, MBTI/ennea, personal bio,
//and disposition. it has to be styled nicely and look cyberpunk-y. 

//vars
double version = 1.21;
string subject;


//intro
Console.WriteLine("Welcome to VITArchives.");
Console.WriteLine ("VERSION " + version);
Console.WriteLine("BOOTING PROGRAM");
Console.WriteLine("SUCCESS");

while (true)
{
Console.WriteLine("Please select a user, or type EXIT to quit.");
Console.WriteLine("VYNN");
Console.WriteLine("FELIX");
Console.WriteLine("NADIR");
Console.WriteLine("SAMAEL");
subject = Console.ReadLine();
subject = (subject ?? "").ToUpper();


    //data vynn
    if (subject == "VYNN") 
    {
        Console.WriteLine ("Loading user data.");
        Console.WriteLine ("Please wait...");
        Console.WriteLine ("Retrieved user data.");
        Console.WriteLine ("NAME: Avinash Vidyut");
        Console.WriteLine ("D.O.B. / AGE: 8/8 / 19");
        Console.WriteLine ("ETHNICITY: SOUTH ASIAN");
        Console.WriteLine ("MBTI: ENTP");
        Console.WriteLine ("DISPOSITION: Abrasive / Amiable");
        Console.WriteLine ("NOTES: None.");
        Console.WriteLine ("AUTHORIZATION LVL: 0");
        Console.WriteLine ("No clearance for advanced facilities.");
        Console.WriteLine ("Press Enter to return to menu.");
        Console.ReadLine();
    }
    //data felix
    else if (subject == "FELIX") 
    {
        Console.WriteLine ("Loading user data.");
        Console.WriteLine ("Please wait...");
        Console.WriteLine ("Retrieved user data.");
        Console.WriteLine ("NAME: Felix [Hajun] Angelos Cheon");
        Console.WriteLine ("D.O.B. / AGE: 10/10 / 20");
        Console.WriteLine ("ETHNICITY: Korean American");
        Console.WriteLine ("MBTI: ENTJ");
        Console.WriteLine ("DISPOSITION: Prideful, Calculating");
        Console.WriteLine ("NOTES: Current heir apparent to Cerasus Corp.");
        Console.WriteLine ("AUTHORIZATION LVL: 2");
        Console.WriteLine ("May access certain administrative datasets.");
        Console.WriteLine ("Press Enter to return to menu.");
        Console.ReadLine();
    }
    //data nadir
    else if (subject == "NADIR") 
    {
        Console.WriteLine ("Loading user data.");
        Console.WriteLine ("Please wait...");
        Console.WriteLine ("Retrieved user data.");
        Console.WriteLine ("NAME: Nadir Afolayan");
        Console.WriteLine ("D.O.B. / AGE: 9/18 / 19");
        Console.WriteLine ("ETHNICITY: West African");
        Console.WriteLine ("MBTI: INTJ");
        Console.WriteLine ("DISPOSITION: Analytical, Data Oriented ");
        Console.WriteLine ("NOTES: Incapable of collaboration despite intelligence.");
        Console.WriteLine ("AUTHORIZATION LVL: 1");
         Console.WriteLine ("May access advanced research equipment with supervision.");
         Console.WriteLine ("Press Enter to return to menu.");
         Console.ReadLine();
    }
    //data samael
    else if (subject == "SAMAEL") 
    {
        Console.WriteLine ("Loading user data.");
        Console.WriteLine ("Please wait...");
        Console.WriteLine ("Retrieved user data.");
        Console.WriteLine ("NAME: SAMAEL KRASNOFF");
        Console.WriteLine ("D.O.B. / AGE: 1/16 / 19");
        Console.WriteLine ("ETHNICITY: Russian American");
        Console.WriteLine ("MBTI: ISTJ");
        Console.WriteLine ("DISPOSITION: Precise, Blunt");
        Console.WriteLine ("WARNING: UNABLE TO ACCESS MORE INFORMATION.");
        Console.WriteLine ("WARNING: ELEVATION REQUIRED TO PROCEED.");
        Console.WriteLine ("Press Enter to return to menu.");
        Console.ReadLine();
    }
    //termination
    else if (subject == "EXIT"){
        Console.WriteLine ("TERMINATING...");
        Console.WriteLine ("PROGRAM STOPPED.");
        break;
    }
    //edge case
    else
    {   
       Console.WriteLine ("WARNING: NO DATA FOUND. PLEASE TRY AGAIN."); 
       Console.WriteLine ("Press Enter to return to menu.");
       Console.ReadLine();
    }
}