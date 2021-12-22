public class SquareDigit {

  public int squareDigits(int n) {
    /* Steps
    // 1. String to string array
    // 2. String array to Integer array used in Math.pow()
    // 3. Math.pow returns double so typecast to int and then convert that int to string to append to existing string. 
    // 4. Finally convert back to integer to return. */
    String finalNumber = ""; 
    // convert to string to split and store as string array
    String[] strArray = Integer.toString(n).split("");
    for(int i = 0; i < strArray.length; i++) {
      // Convert internal string array to int and apply math.pow which is also typecasted as int
      // finally String.valueof converts int to string. 
      finalNumber += String.valueOf((int)Math.pow(Integer.parseInt(strArray[i]),2));
    }

    // string converted and returned as integer. 
    return Integer.parseInt(finalNumber);
  }

}