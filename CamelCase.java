// Complete the solution so that the function will break up camel casing, using a space between words.

// Example
// "camelCasing"  =>  "camel Casing"
// "identifier"   =>  "identifier"
// ""             =>  ""

class Solution {
  public static String camelCase(String input) {
    
        String newStr = input.replaceAll("\\d+", "").replaceAll("(.)([A-Z])", "$1 $2");
        return newStr.toString();
    
  }
}