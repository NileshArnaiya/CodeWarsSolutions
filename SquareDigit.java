// A square of squares
// You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

// However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

// Task
// Given an integral number, determine if it's a square number:

// In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

// The tests will always use some integral number, so don't worry about that in dynamic typed languages.

// Examples
// -1  =>  false
//  0  =>  true
//  3  =>  false
//  4  =>  true
// 25  =>  true
// 26  =>  false



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