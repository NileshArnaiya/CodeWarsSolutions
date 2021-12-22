public class Square {    
    public static boolean isSquare(int n) {     
        if(n<0){
          return false;
        }
      int sqrt = (int)Math.sqrt(n);
         if(n == sqrt * sqrt){
             return true;
         }
          return false;
     
    }
}