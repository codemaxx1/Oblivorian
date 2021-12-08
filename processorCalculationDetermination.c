// created by Nicholas Garrett

#include <math.h>
#include <stdio.h>

// define what pi is
#define pi1 3.141592653

// define the number of known processors
#define processorsN 7

int determine ()
{
    
    // 
    int calculatedValue;

    // array to store the valcues calculated by this processor for sin(10^10 * pi), sin(10^17 * pi), and sin(10^37 * pi)
    float sinPowerCalculation[3];

    // array to store the values of sinPowerCalculation, but truncated to 3 decimals
    float roundedSinPowerCalculation[3];

    // array of known values that would be returned for some processors
    float knownCalculations[processorsN][3] = {   {0.375, 0.423,  -0.837},    // "IPHONE 3G"
                                        {0.375, 0.424, -0.837},     // "AMD 32"
                                        {0.375, 0.424, 0.837},      // "AMD 64"
                                        {0.375, 0.423, -0.832},     // "ATOM"
                                        {0.375, 0.423, -0.832},     // "INTEL DC"
                                        {0.375, 0.423, -0.832},     // "MIPS 12000"
                                        {0.81, 0.62, -0.44}         // "dsPIC33"
                                                                        };
    // array of the names for processors
    char* knownNames[processorsN] =  {  "IPHONE 3G",
                                        "AMD 32",
                                        "AMD 64",
                                        "ATOM",
                                        "INTEL DC",
                                        "MIPS 12000",
                                        "dsPIC33"
                                            };

    // array of mathematical operations to perform
    char* mathOpps[3] =                {    "sin(10^10 * pi)",
                                            "sin(10^17 * pi)",
                                            "sin(10^37 * pi)"
                                            };

    // simple matrix to hold whether it is determiend your processor is of a certain type
    /*
        0 --> not of that type (false)     
        1 -- > of that type    (true)
    */
    int determinations[processorsN][3] = {0};
    
    // calculate the calculations this specific processor returns
    sinPowerCalculation[0] = sin(powf(10, 10) * pi1);   // sin(10^10 * pi), 
    sinPowerCalculation[1] = sin(powf(10, 17) * pi1);   // sin(10^17 * pi), 
    sinPowerCalculation[2] = sin(powf(10, 37) * pi1);   // sin(10^37 * pi)

    // truncate the calculations calculated by this specific processor 
    roundedSinPowerCalculation[0] = trunc(sinPowerCalculation[0]*1000)/1000;
    roundedSinPowerCalculation[1] = trunc(sinPowerCalculation[1]*1000)/1000;
    roundedSinPowerCalculation[2] = trunc(sinPowerCalculation[2]*1000)/1000;

    // determine if this processor matches any of the known returns linked to a specific processor
    for(int i = 0; i < processorsN; i++)
    {
        for( int j = 0; j < 3; j++)
        {
            // if the calculated return matches a known return
            if( knownCalculations[i][j] == roundedSinPowerCalculation[j])
            {
                determinations[i][j] = 1;

            }
            else    
                determinations[i][j] = 0;
        }
    }


    // tell the user what information was gained
    char* isIsN;
        for(int j = 0; j < 3; j++)
        {
            if(j == 0) printf("\nOn a low-accuracy calculation, calculating %s, it can be determined your processor:\n", mathOpps[j]);
            if(j == 1) printf("\nOn a moderate-accuracy calculation, calculating %s, it can be determined your processor:\n", mathOpps[j]);
            if(j == 2) printf("\nOn a higher-accuracy calculation, calculating %s, it can be determined your processor:\n", mathOpps[j]);
            for( int i = 0; i < processorsN; i++)
            {
               
                    if(determinations[i][j] == 1) isIsN = "Might be";
                    else isIsN = "Is NOT";
                    printf("%s a(n) %s\n", isIsN, knownNames[i]);
                
  
           
                   
            }
        }


    

    // print the calculated outputs
    printf("\nThe exact calculations made for pi = 3.141592653, by your processor were:\n");
    for(int j = 0; j < 3; j++)
    {
        printf("%s = %f \n", mathOpps[j],sinPowerCalculation[j]);
    }
    printf("\n");



                                        
}

int main(){determine();}

 