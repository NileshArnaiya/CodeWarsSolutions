// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

// Examples input/output:

// XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false

public class ExesAndOhs {
  
  public static boolean getXO (String str) {
    
    
            char smallo = 'o';
            char smallx = 'x';
            char bigO = 'O';
            char bigX = 'X';

            int countO = 0;
            int countX = 0;


            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == smallo || str.charAt(i) == bigO) {
                    countO++;
                }
                else if (str.charAt(i) == smallx || str.charAt(i) == bigX) {
                    countX++;
                }
            }
            if(countO == 0 && countX == 0){
                return true;
            }
            else if(countO == countX){
                return true;
            }
            else{
                return false;
            }
    
  
    
   }
}